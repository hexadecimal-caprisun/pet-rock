let angle2 = 0
let angle1 = 0
let angle = 0
while (true) {
    basic.showLeds(`
        . . . . .
                # # # # #
                . # . # .
                . # . # .
                . . # . .
    `)
    if (input.buttonIsPressed(Button.A)) {
        angle1 = randint(0, 360)
        angle2 = randint(0, 360)
        pins.servoWritePin(AnalogPin.P13, angle1)
        pins.servoWritePin(AnalogPin.P14, angle2)
        koi.koi_audio_play("say.wav")
    }
    
}
