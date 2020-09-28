def on_button_pressed_a():
    global numberOfPressesOnButtonA
    numberOfPressesOnButtonA += 1
    basic.show_string("" + str((numberOfPressesOnButtonA)))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global numberOfPressesOnButtonA
    numberOfPressesOnButtonA += -1
    basic.show_string("" + str((numberOfPressesOnButtonA)))
input.on_button_pressed(Button.B, on_button_pressed_b)

numberOfPressesOnButtonA = 0
numberOfPressesOnButtonA = 0

def on_forever():
    pass
basic.forever(on_forever)
