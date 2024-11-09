import flet as ft
from flet import RoundedRectangleBorder

from files.colors import color

# first part
welcome_text = ft.Text (
    'Welcome',
    size=14,
    weight=ft.FontWeight.W_200,
    color=color['primary_color']
)

opportunities_text = ft.Text (
    'Best Learning\nOpportunities',
    size=48,
    weight=ft.FontWeight.W_900,
    color=color['text_color']
)

goal_text = ft.Text (
    'Our goal is to make online\neducation work for everyone',
    size=20,
    weight=ft.FontWeight.W_300,
    color=color['second_text_color']
)

join_us_button = ft.ElevatedButton(
    content=ft.Text('Join us', size=16),
    width=120,
    height=50,
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
learn_more_button = ft.ElevatedButton(
    content=ft.Text('Learn More', size=16),
    width=160,
    height=50,
    style=ft.ButtonStyle(
        shape=RoundedRectangleBorder(radius=5),
        side=ft.BorderSide (
            color=color['primary_color'],
            width=1
        ),
        color=color['primary_color'],
        bgcolor=ft.colors.WHITE,
        text_style=ft.TextStyle (
            size=16
        )

    ),
    on_click=lambda e: print('The "Learn more" button is pressed')
)

# second part
woman_image = ft.Image(
    'images/header/container_fluid/woman.png',
    width=526,
    height=526
)

# container_fluid
container_fluid = ft.Container(
    content=ft.Row(
        controls=[
            ft.Column(
                controls=[
                    welcome_text,
                    opportunities_text,
                    goal_text,
                    ft.Row(
                        controls=[
                            join_us_button,
                            learn_more_button
                        ],
                        spacing=20
                    )
                ]
            ),
            ft.Column(
                controls=[woman_image]
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=100
    ),
    padding=ft.Padding(top=100, right=0, left=0, bottom=0)
)