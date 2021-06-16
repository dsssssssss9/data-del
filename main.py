def on_button_pressed_a():
    global ToLog
    ToLog = False
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global ToLog
    ToLog = True
input.on_button_pressed(Button.AB, on_button_pressed_ab)

ToLog = False
datalogger.set_columns(["Noise", "Temp"])
ToLog = False
list2 = [[0, 1], [2, 3]]
text_list = [["00", "01"], ["10", "11"]]

def on_every_interval():
    if ToLog:
        basic.show_icon(IconNames.YES)
        datalogger.log_data([datalogger.create_cv("Noise", input.sound_level()),
                datalogger.create_cv("Temp", input.temperature())])
        basic.clear_screen()
loops.every_interval(2000, on_every_interval)
