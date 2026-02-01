import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module.')
    sys.exit()

# Set up the constants:
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = '@'
EMPTY = ' '
WATER = '~'  # NEW: water tile for lake

INITIAL_TREE_DENSITY = 0.20
GROW_CHANCE = 0.01
FIRE_CHANCE = 0.01
PAUSE_LENGTH = 0.5


def main():
    forest = createNewForest()
    bext.clear()

    while True:
        displayForest(forest)

        nextForest = {'width': forest['width'],
                      'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):

                if (x, y) in nextForest:
                    continue

                # NEW: Water never changes
                if forest[(x, y)] == WATER:
                    nextForest[(x, y)] = WATER

                # Tree growth only on empty land
                elif ((forest[(x, y)] == EMPTY)
                      and (random.random() <= GROW_CHANCE)):
                    nextForest[(x, y)] = TREE

                # Lightning only affects trees
                elif ((forest[(x, y)] == TREE)
                      and (random.random() <= FIRE_CHANCE)):
                    nextForest[(x, y)] = FIRE

                # Fire behavior
                elif forest[(x, y)] == FIRE:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            # Fire spreads ONLY to trees (not water)
                            if forest.get((x + ix, y + iy)) == TREE:
                                nextForest[(x + ix, y + iy)] = FIRE

                    # Burned tree becomes empty
                    nextForest[(x, y)] = EMPTY

                else:
                    nextForest[(x, y)] = forest[(x, y)]

        forest = nextForest
        time.sleep(PAUSE_LENGTH)


def createNewForest():
    forest = {'width': WIDTH, 'height': HEIGHT}

    # Populate forest normally
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if random.random() <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE
            else:
                forest[(x, y)] = EMPTY

    # NEW: Create lake in the center
    lake_width = 12
    lake_height = 6
    start_x = (WIDTH // 2) - (lake_width // 2)
    start_y = (HEIGHT // 2) - (lake_height // 2)

    for x in range(start_x, start_x + lake_width):
        for y in range(start_y, start_y + lake_height):
            forest[(x, y)] = WATER

    return forest


def displayForest(forest):
    bext.goto(0, 0)

    for y in range(forest['height']):
        for x in range(forest['width']):
            if forest[(x, y)] == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif forest[(x, y)] == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            elif forest[(x, y)] == WATER:
                bext.fg('blue')  # NEW: blue lake
                print(WATER, end='')
            else:
                print(EMPTY, end='')
        print()

    bext.fg('reset')
    print(f'Grow chance: {GROW_CHANCE * 100}%  ', end='')
    print(f'Lightning chance: {FIRE_CHANCE * 100}%  ')
    print('Press Ctrl-C to quit.')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
