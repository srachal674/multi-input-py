def greeting():
    input.button_is_pressed(Button.A)
    basic.show_string("Shannon")


def num():
    input.button_is_pressed(Button.B)
    basic.show_number(randint(1, 100))

do_something()