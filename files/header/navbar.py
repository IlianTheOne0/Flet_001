import flet as ft
from flet import RoundedRectangleBorder

from files.colors import color

# header
brandname_text = ft.Text (
    'Brandname',
    size=24,
    weight=ft.FontWeight.W_900,
    color='#252B42'
)

home_button = ft.CupertinoButton (
    content=ft.Text (
        'Home',
        size=16
    ),
    color=color['second_text_color'],

    on_click=lambda e: print('The "Home" button is pressed')
)
product_button = ft.CupertinoButton (
    content=ft.Text (
        'Product',
        size=16
    ),
    color=color['second_text_color'],
    on_click=lambda e: print('The "Product" button is pressed')
)
pricing_button = ft.CupertinoButton (
    content=ft.Text (
        'Pricing',
        size=16
    ),
    color=color['second_text_color'],
    on_click=lambda e: print('The "Pricing" button is pressed')
)
contact_button = ft.CupertinoButton (
    content=ft.Text (
        'Contact',
        size=16
    ),
    color=color['second_text_color'],
    on_click=lambda e: print('The "Contact" button is pressed')
)

login_button = ft.CupertinoButton(
    content=ft.Text (
        'Login',
        size=16
    ),
    color=color['primary_color'],
    on_click=lambda e: print('The "Login" button is pressed')
)
join_us_button = ft.ElevatedButton(
    content=ft.Row (
        [
            ft.Text('JOIN US', size=16),
            ft.Image('images/header/navbar/arrow.png', width=16, height=16)
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=8
    ),
    style=ft.ButtonStyle(
        shape=RoundedRectangleBorder(radius=5),
        color=ft.colors.WHITE,
        bgcolor=color['primary_color'],
        text_style=ft.TextStyle (
            size=16
        )

    ),
    on_click=lambda e: print('The "Join us" button is pressed')
)

navbar = ft.Row (
    controls = [
        brandname_text,
        ft.Row (
            controls=[
                home_button, product_button, pricing_button, contact_button
            ],
            spacing=20
        ),
        ft.Row (
            controls=[
                login_button, join_us_button
            ],
            spacing=20
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER,
    spacing=100
)