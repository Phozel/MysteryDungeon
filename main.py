from View import View

def print_hi(name):
    print(f'You are playing: {name}')

def testView(size):
    view = View.View(size)
    view.showWindow()


if __name__ == '__main__':
    print_hi('Mystery Dungeon')
    size = 1080, 720
    testView(size)

