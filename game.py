from data import Data
from world import World
from user import Player
from reloadr import autoreload

HELP_TEXT = """
[COMMANDS]
> help -- see this screen
> look <object>? -- will print the area around you or if a name is provided, look at object
> take <thing>   -- will take the thing and put it in invatory
> goto <location>  -- will move you to that location
"""

@autoreload
class Game:
    def __init__(self):
        self.world = World()
        self.data = Data()
        self.data.load()

    def get_help(self, args):
        return HELP_TEXT

    async def do_look(self, channel, user, loc, rest):
        players_txt = ""
        for name in self.data.db["users"].keys():
            player = self.data.db["users"][name]

            if player.location != loc.title:
                continue
            if name == user: continue

            players_txt += f"\nYou see {name}"
        await channel.send(f"[{user}]: {players_txt}\n{loc}")

    async def interpret_command(self, command, channel, user):
        self.data.save()
        # Get the user
        player = None
        if user in self.data.db["users"].keys():
            player = self.data.db["users"][user]
        else:
            await channel.send(f"Welcome {user}! if you have any questions type `>help`")
            player = Player(user, user)
            self.data.db["users"][user] = player

        splits = command.split(' ')

        if len(splits) < 0: return

        fst = splits[0]
        if fst == ">":
            if len(splits) < 2:
                await channel.send(f"[{user}]: I don't understand...")
                return
            fst = splits[1]

        if len(fst) > 1 and fst.startswith(">"):
            fst = fst[1:]

        loc = self.world.theMap[player.location]

        if fst == "look":
            await self.do_look(channel, user, loc, splits[1:])

        if fst == "take":
            await channel.send(f"[{user}]: There is nothing to take idiot")

        if fst == "help":
            await channel.send(f"[{user}]:{self.get_help([])}")

        if fst == "ping":
            await channel.send(f"[{user}]: pong")

        if fst == "goto":
            if len(splits) == 1:
                await channel.send(f"[{user}]: where do I go?")
                return

            nxt = " ".join(splits[1:])

            found = False
            for path in loc.paths:
                if path == nxt:
                    found = True
            if not found:
                await channel.send(f"[{user}]: I cannot go there..")
                return
            else:
                await channel.send(f"[{user}]: 'You move to {nxt}'")
                player.location = nxt
