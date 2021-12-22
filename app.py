from entity.hello_world import HelloWorld
import sys


def app(name):
    hello_world = HelloWorld(name)
    hello_world.say_hello()


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        raise TypeError('missing required positional argument, Usage: python app.py Wentao')
    else:
        app(sys.argv[1])

