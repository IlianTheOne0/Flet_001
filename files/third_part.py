import flet as ft

from files.colors import color

# first column
woman_image = ft.Image(
    'images/third_part/woman.png',
    width=526,
    height=526
)

# Define the learn_more_button separately
learn_more_button = ft.ElevatedButton(
    content=ft.Text('Learn More', size=16),
    width=160,
    height=50,
    style=ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=5),
        side=ft.BorderSide(
            color=color['primary_color'],
            width=1
        ),
        color=color['primary_color'],
        bgcolor=ft.colors.WHITE,
        text_style=ft.TextStyle(
            size=16
        )
    ),
    on_click=lambda e: print('The "Learn more" button is pressed')
)

# second column
second_column = ft.Column(
    controls=[
        ft.Container(
            width=100,
            height=5,
            bgcolor=color['danger_color'],
        ),
        ft.Text(
            'Video in Live\nAction',
            size=48,
            weight=ft.FontWeight.W_900,
        ),
        ft.Text(
            'Problems trying to resolve the conflict between\nthe two major realms of Classical physics:\nNewtonian mechanics',
            size=16,
            weight=ft.FontWeight.W_300,
            color=color['second_text_color']
        ),
        ft.CupertinoButton(
            content=ft.Row (
                controls=[
                    ft.Text('Learn more', size=16),
                    ft.Image('images/third_part/arrow.png', width=16, height=16)
                ],
                spacing=10
            ),
            color=color['primary_color'],
            on_click=lambda e: print('The "Learn more" button is pressed')
        )
    ]
)

# third_part
third_part = ft.Container(
    content=ft.Row(
        controls=[
            woman_image,
            second_column
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.END,
        spacing=100
    ),
    padding=ft.Padding(top=200, right=0, left=0, bottom=0)
)