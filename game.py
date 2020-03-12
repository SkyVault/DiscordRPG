from data import Data
from world import World
from user import Player

class Game:
    def __init__(self):
        self.world = World()
        self.data = Data()
        self.data.load()

    async def interpret_command(self, command, channel, user):

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
            await channel.send(f"[{user}]: {loc}")

        if fst == "take":
            await channel.send(f"[{user}]: There is nothing to take idiot")
