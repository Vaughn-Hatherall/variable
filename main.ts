input.onButtonPressed(Button.A, function () {
    numberOfPressesOnButtonA += 1
    basic.showString("" + (numberOfPressesOnButtonA))
})
input.onButtonPressed(Button.B, function () {
    numberOfPressesOnButtonA += -1
    basic.showString("" + (numberOfPressesOnButtonA))
})
let numberOfPressesOnButtonA = 0
numberOfPressesOnButtonA = 0
basic.forever(function () {
	
})
