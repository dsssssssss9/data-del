input.onButtonPressed(Button.A, function () {
    ToLog = false
})
input.onButtonPressed(Button.AB, function () {
    ToLog = true
})
let ToLog = false
datalogger.setColumns(["Noise", "Temp"])
ToLog = false
loops.everyInterval(2000, function () {
    if (ToLog) {
        basic.showIcon(IconNames.Yes)
        datalogger.logData([datalogger.createCV("Noise", input.soundLevel()), datalogger.createCV("Temp", input.temperature())])
        basic.clearScreen()
    }
})
