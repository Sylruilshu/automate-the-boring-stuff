import zombiedice, random


class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll()  # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults["brains"]

            if brains < 2:
                diceRollResults = zombiedice.roll()  # roll again
            else:
                break


class foo:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        while diceRollResults is not None:

            if random.randint(0, 1) == 0:
                diceRollResults = zombiedice.roll()
            else:
                break


class bar:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        brains = 0
        while diceRollResults is not None:
            brains = diceRollResults["brains"]

            if brains < 2:
                diceRollResults = zombiedice.roll()
            else:
                break


class baz:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        shotgun = 0
        while diceRollResults is not None:
            shotgun = diceRollResults["shotgun"]

            if shotgun < 2:
                diceRollResults = zombiedice.roll()
            else:
                break


class foobar:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        shotgun = 0
        while diceRollResults is not None:
            shotgun = diceRollResults["shotgun"]

            for i in range(4):
                diceRollResults = zombiedice.roll()

                if shotgun < 2:
                    continue
                else:
                    break
            break


class foobaz:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        shotgun = 0
        brains = 0
        while diceRollResults is not None:
            shotgun = diceRollResults["shotgun"]
            brains = diceRollResults["brains"]

            if shotgun < brains:
                diceRollResults = zombiedice.roll()
            else:
                break


zombies = (
    # zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    # zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    # zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Until 2 Shotguns', minShotguns=2),
    # zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Until 1 Shotgun', minShotguns=1),
    foo(name="Random Stop Bot"),
    bar(name="Double Brains Stop"),
    baz(name="Double Shotgun Stop"),
    foobar(name="One To Four"),
    foobaz(name="Shotguns Over Brains Stop"),
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
# zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)
