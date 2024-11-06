# https://www.figma.com/community/file/1041082497681424521/responsive-calculator-app

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

        update_button_styles([plus_or_minus_button], operators_bg, text_color, 16)
        update_button_styles([delete_button], numbers_bg, text_color, 14.3)
        update_button_styles([clear_button], operators_bg, text_color, 18)
        update_button_styles([division_button, multiplication_button, minus_button, plus_button, equals_button], action_bg, ft.colors.WHITE if theme == 'dark' else ft.colors.BLACK, 18)
        update_button_styles([seven_button, eight_button, nine_button, four_button, five_button, six_button, one_button, two_button, three_button, comma_button, zero_button], numbers_bg, text_color, 18)
        page.update()

    def update_button_styles(buttons, bgcolor, text_color, font_size):
        for button in buttons:
            button.style = ft.ButtonStyle(
                shape=RoundedRectangleBorder(radius=15),
                bgcolor=bgcolor,
                color=text_color,
                text_style=ft.TextStyle(size=font_size)
            )
            button.update()

    def exit_from_app(e):
        os.system('taskkill /f /im flet.exe')

    def insert(user_value, action):
        if action == 'number':
            if output.value in ['/', '*', '+', '-']:
                history.value += output.value
                output.value = ''
            if len(output.value) != 13:
                output.value += user_value
        elif action == 'operator':
            history.value += output.value
            output.value = user_value
        elif action == 'equals':
            try:
                history.value += output.value
                output.value = round(eval(history.value), 6)
            except Exception as e:
                output.value = e
        elif action == 'clear':
            history.value = ''
            output.value = ''
        elif action == 'delete':
            output.value = output.value[:-1]
        elif action == 'minus':
            output.value = '(-' + output.value + ')'

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
        ),
        on_click=lambda e: insert(None, 'clear')
    )

    plus_or_minus_button = ft.ElevatedButton(
        text='+/-',
        width=button_size,
        height=button_size,
        style=ft.ButtonStyle(
            shape=RoundedRectangleBorder(radius=20),
            bgcolor=operators_bg,
            color=text_color,
            text_style=ft.TextStyle(
                size=16
            )
        ),
        on_click=lambda e: insert(None, 'minus')
    )

    empty = ft.Container(width=button_size, height=button_size)

    division_button = ft.ElevatedButton(
        text='/',
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
        text='*',
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
        ),
        on_click=lambda e: insert('+', 'operator')
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
        ),
        on_click=lambda e: insert('.', 'number')
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
        text='DEL',
        width=button_size,
        height=button_size,
        style=ft.ButtonStyle(
            shape=RoundedRectangleBorder(radius=20),
            bgcolor=numbers_bg,
            color=text_color,
            text_style=ft.TextStyle(
                size=14.3
            )
        ),
        on_click=lambda e: insert(None, 'delete')
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
        ),
        on_click=lambda e: insert(None, 'equals')
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
    second_row = [clear_button, plus_or_minus_button, empty, division_button]
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