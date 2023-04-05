from microbit import *
import speech
angle2 = 0
angle1 = 0
angle = 0
while True:
    basic.show_leds("""
                . . . . .
                # # # # #
                . # . # .
                . # . # .
                . . # . .
    """)
    if input.button_is_pressed(Button.A):
        angle1 = randint(0, 360)
        angle2 = randint(0, 360)
        pins.servo_write_pin(AnalogPin.P13, angle1)
        pins.servo_write_pin(AnalogPin.P14, angle2)
        speech.say("Hello")
        basic.show_leds("""
                . . . . .
                # # # # #
                # . . . #
                . # # # .
                . . . . .
        """)