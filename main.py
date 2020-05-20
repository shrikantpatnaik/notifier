import pigpio
from RotaryDecoder import Decoder
from time import sleep

rotary = None


def init():
    global rotary
    pi = pigpio.pi()
    rotary = Decoder(pi, 23, 24, 25, encoder_change, switch_pressed)


def encoder_change(level):
    print(level)


def switch_pressed():
    print("switch pressed")


def main():
    '''
    The main routine.
    '''

    try:
        global rotary
        init()
        while True:

            # wait for an encoder click
            sleep(1)

    except KeyboardInterrupt:  # Ctrl-C to terminate the program
        if rotary != None:
            rotary.cancel()


if __name__ == '__main__':
    main()
