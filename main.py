def on_button_pressed_a():
    basic.show_string("Shannon")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_number(randint(1, 100))
input.on_button_pressed(Button.B, on_button_pressed_b)


