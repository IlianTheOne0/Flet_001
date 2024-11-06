import flet as ft
from flet import RoundedRectangleBorder

import time
import os

colors = {
    'dark': [
        '#4e505f', #operators_button_color
        '#4b5efc', #action_button_color
        '#2e2f38' #number_button_color
    ],

    'light': [
        '#d2d3da',  # operators_button_color
        '#4b5efc',  # action_button_color
        '#ffffff'  # number_button_color
    ]
}

button_size = 72
theme = 'dark'
text_color = ft.colors.WHITE
operators_bg = colors['dark'][0]
action_bg = colors['dark'][1]
numbers_bg = colors['dark'][2]

def start():
    ft.app(main, assets_dir='assets')

def main(page: ft.Page):
    ''' init '''
    page.window_width = 400
    page.window_height = 700
    page.window_resizable = False

    page.theme = ft.Theme(font_family='Open Sans')
    page.theme_mode = ft.ThemeMode.DARK

    ''' functions '''

    def theme_switcher(e):
        global text_color, operators_bg, action_bg, numbers_bg

        if e.data == 'true':
            page.theme_mode = ft.ThemeMode.LIGHT
            text_color = ft.colors.BLACK
            operators_bg = colors['light'][0]
            action_bg = colors['light'][1]
            numbers_bg = colors['light'][2]
        if e.data == 'false':
            page.theme_mode = ft.ThemeMode.DARK
            text_color = ft.colors.WHITE
            operators_bg = colors['dark'][0]
            action_bg = colors['dark'][1]
            numbers_bg = colors['dark'][2]

        print(operators_bg)

    def exit_from_app(e):
        os.system('taskkill /f /im flet.exe')

    def insert(user_value, action):
        if action == 'number':
            if len(output.value) != 13:
                output.value += user_value
        elif action == 'operator':
            pass

        page.update()


    ''' components '''
    # row 1
    clock = ft.Text('None')

    drawer = ft.NavigationDrawer (
        position=ft.NavigationDrawerPosition.END,
        controls= [
            ft.Column (
                alignment=ft.MainAxisAlignment.CENTER,
                controls= [
                    ft.Switch(
                        label='\tLight theme',
                        value='false',
                        on_change=theme_switcher
                    ),
                    ft.ElevatedButton(
                        text='\tExit',
                        icon='exit_to_app',
                        on_click=exit_from_app
                    )
                ]
            )
        ]
    )
    drawer_opener = ft.ElevatedButton (
        text='Settings',
        icon='settings',
        on_click=lambda e: page.open(drawer)
    )

    # row 2
    clear_button = ft.ElevatedButton(
        text='C',
        width=button_size,
        height=button_size,
        style=ft.ButtonStyle(
            shape=RoundedRectangleBorder(radius=15),
            bgcolor=operators_bg,
            color=text_color,
            text_style=ft.TextStyle(
                size=24
            )
        )
    )

    plus_or_minus_button = ft.ElevatedButton(
        content=ft.Image(src='dark/icons/plus_or_minus.png', width=18, height=18),
        width=button_size,
        height=button_size,
        style=ft.ButtonStyle(
            shape=RoundedRectangleBorder(radius=20),
            bgcolor=operators_bg,
            color=text_color,
            text_style=ft.TextStyle(
                size=18
            )
        )
    )

    percentage_button = ft.ElevatedButton(
        text='%',
        width=button_size,
        height=button_size,
        style=ft.ButtonStyle(
            shape=RoundedRectangleBorder(radius=20),
            bgcolor=operators_bg,
            color=text_color,
            text_style=ft.TextStyle(
                size=18
            )
        )
    )

    division_button = ft.ElevatedButton(
        content=ft.Image(src='both/icons/division.png', width=18, height=18),
        width=button_size,
        height=button_size,
        style=ft.ButtonStyle(
            shape=RoundedRectangleBorder(radius=20),
            bgcolor=action_bg,
            color=text_color,
            text_style=ft.TextStyle(
                size=18
            )
        ),
        on_click=lambda e: insert('/', 'operator')
    )

    # row 3
    seven_button = ft.ElevatedButton(
        text=7,
        width=button_size,
        height=button_size,
        style=ft.ButtonStyle(
            shape=RoundedRectangleBorder(radius=20),
            bgcolor=numbers_bg,
            color=text_color,
            text_style=ft.TextStyle(
                size=18
            )
        ),
        on_click=lambda e: insert('7', 'number')
    )

    eight_button = ft.ElevatedButton(
        text=8,
        width=button_size,
        height=button_size,
        style=ft.ButtonStyle(
            shape=RoundedRectangleBorder(radius=20),
            bgcolor=numbers_bg,
            color=text_color,
            text_style=ft.TextStyle(
                size=18
            )
        ),
        on_click=lambda e: insert('8', 'number')
    )

    nine_button = ft.ElevatedButton(
        text=9,
        width=button_size,
        height=button_size,
        style=ft.ButtonStyle(
            shape=RoundedRectangleBorder(radius=20),
            bgcolor=numbers_bg,
            color=text_color,
            text_style=ft.TextStyle(
                size=18
            )
        ),
        on_click=lambda e: insert('9', 'number')
    )

    multiplication_button = ft.ElevatedButton(
        content=ft.Image(src='both/icons/multiplication.png', width=128, height=128),
        width=button_size,
        height=button_size,
        style=ft.ButtonStyle(
            shape=RoundedRectangleBorder(radius=20),
            bgcolor=action_bg,
            color=text_color,
            text_style=ft.TextStyle(
                size=18
            )
        ),
        on_click=lambda e: insert('*', 'operator')
    )

    # row 4
    four_button = ft.ElevatedButton(
        text=4,
        width=button_size,
        height=button_size,
        style=ft.ButtonStyle(
            shape=RoundedRectangleBorder(radius=20),
            bgcolor=numbers_bg,
            color=text_color,
            text_style=ft.TextStyle(
                size=18
            )
        ),
        on_click=lambda e: insert('4', 'number')
    )

    five_button = ft.ElevatedButton(
        text=5,
        width=button_size,
        height=button_size,
        style=ft.ButtonStyle(
            shape=RoundedRectangleBorder(radius=20),
            bgcolor=numbers_bg,
            color=text_color,
            text_style=ft.TextStyle(
                size=18
            )
        ),
        on_click=lambda e: insert('5', 'number')
    )

    six_button = ft.ElevatedButton(
        text=6,
        width=button_size,
        height=button_size,
        style=ft.ButtonStyle(
            shape=RoundedRectangleBorder(radius=20),
            bgcolor=numbers_bg,
            color=text_color,
            text_style=ft.TextStyle(
                size=18
            )
        ),
        on_click=lambda e: insert('6', 'number')
    )

    minus_button = ft.ElevatedButton(
        text='-',
        width=button_size,
        height=button_size,
        style=ft.ButtonStyle(
            shape=RoundedRectangleBorder(radius=20),
            bgcolor=action_bg,
            color=text_color,
            text_style=ft.TextStyle(
                size=18
            )
        ),
        on_click=lambda e: insert('-', 'operator')
    )

    # row 5
    one_button = ft.ElevatedButton(
        text=1,
        width=button_size,
        height=button_size,
        style=ft.ButtonStyle(
            shape=RoundedRectangleBorder(radius=20),
            bgcolor=numbers_bg,
            color=text_color,
            text_style=ft.TextStyle(
                size=18
            )
        ),
        on_click=lambda e: insert('1', 'number')
    )

    two_button = ft.ElevatedButton(
        text=2,
        width=button_size,
        height=button_size,
        style=ft.ButtonStyle(
            shape=RoundedRectangleBorder(radius=20),
            bgcolor=numbers_bg,
            color=text_color,
            text_style=ft.TextStyle(
                size=18
            )
        ),
        on_click=lambda e: insert('2', 'number')
    )

    three_button = ft.ElevatedButton(
        text=3,
        width=button_size,
        height=button_size,
        style=ft.ButtonStyle(
            shape=RoundedRectangleBorder(radius=20),
            bgcolor=numbers_bg,
            color=text_color,
            text_style=ft.TextStyle(
                size=18
            )
        ),
        on_click=lambda e: insert('3', 'number')
    )

    plus_button = ft.ElevatedButton(
        text='+',
        width=button_size,
        height=button_size,
        style=ft.ButtonStyle(
            shape=RoundedRectangleBorder(radius=20),
            bgcolor=action_bg,
            color=text_color,
            text_style=ft.TextStyle(
                size=18
            )
        )
    )

    # row 6
    comma_button = ft.ElevatedButton(
        text=',',
        width=button_size,
        height=button_size,
        style=ft.ButtonStyle(
            shape=RoundedRectangleBorder(radius=20),
            bgcolor=numbers_bg,
            color=text_color,
            text_style=ft.TextStyle(
                size=18
            )
        )
    )

    zero_button = ft.ElevatedButton(
        text='0',
        width=button_size,
        height=button_size,
        style=ft.ButtonStyle(
            shape=RoundedRectangleBorder(radius=20),
            bgcolor=numbers_bg,
            color=text_color,
            text_style=ft.TextStyle(
                size=18
            )
        ),
        on_click=lambda e: insert('0', 'number')
    )

    delete_button = ft.ElevatedButton(
        content=ft.Image(src='dark/icons/delete.png', width=128, height=128),
        width=button_size,
        height=button_size,
        style=ft.ButtonStyle(
            shape=RoundedRectangleBorder(radius=20),
            bgcolor=numbers_bg,
            color=text_color,
            text_style=ft.TextStyle(
                size=18
            )
        )
    )

    equals_button = ft.ElevatedButton(
        text='=',
        width=button_size,
        height=button_size,
        style=ft.ButtonStyle(
            shape=RoundedRectangleBorder(radius=20),
            bgcolor=action_bg,
            color=text_color,
            text_style=ft.TextStyle(
                size=18
            )
        )
    )

    # output
    history = ft.TextField(
        value='',
        width=375,
        border_width=0,
        text_align=ft.TextAlign.CENTER,
        text_style=ft.TextStyle (
            color=ft.colors.GREY,
            size=24
        )
    )

    output = ft.TextField(
        value='',
        width=375,
        border_width=0,
        text_align=ft.TextAlign.CENTER,
        text_style=ft.TextStyle (
            color=text_color,
            size=48
        )
    )

    ''' rows'''
    first_row = [clock, drawer_opener]
    second_row = [clear_button, plus_or_minus_button, percentage_button, division_button]
    third_row = [seven_button, eight_button, nine_button, multiplication_button]
    fourth_row = [four_button, five_button, six_button, minus_button]
    fifth_row = [one_button, two_button, three_button, plus_button]
    sixth_row = [comma_button, zero_button, delete_button, equals_button]

    ''' add components to page '''
    page.add (
        ft.Row(controls=first_row, alignment=ft.MainAxisAlignment.SPACE_BETWEEN),

        ft.Row(controls=[history], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(controls=[output], alignment=ft.MainAxisAlignment.CENTER),

        ft.Row(controls=second_row, alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(controls=third_row, alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(controls=fourth_row, alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(controls=fifth_row, alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(controls=sixth_row, alignment=ft.MainAxisAlignment.CENTER)
    )

    ''' main loop '''
    while True:
        clock.value = time.strftime('%H:%M')
        page.update()
        time.sleep(1)

# division, multiplication, addition, subtraction, equals