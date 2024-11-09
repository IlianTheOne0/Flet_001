import flet as ft

from files.colors import color

# first part
red_line_container = ft.Container(
    width=150,
    height=7,
    bgcolor=color['danger_color'],
)

packages_text = ft.Text(
    'Approdable Packages',
    size=48,
    weight=ft.FontWeight.W_900,
    color=color['text_color']
)

problems_text = ft.Text(
    'Problems trying to resolve the conflict between\nthe two major realms of Classical physics:\nNewtonian mechanics',
    size=20,
    weight=ft.FontWeight.W_300,
    color=color['second_text_color']
)

learn_more_button = ft.CupertinoButton(
    content=ft.Row(
        controls=[
            ft.Text('Learn more', size=16),
            ft.Image('images/second_part/arrow.png', width=16, height=16)
        ],
        spacing=10
    ),
    color=color['primary_color'],
    on_click=lambda e: print('The "Learn more" button is pressed')
)

# second part
# row 1
first_container = ft.Container(
    content=ft.Column(
        controls=[
            ft.Image('images/second_part/lamp.png', width=128, height=128),
            ft.Text(
                'Certified Teacher',
                size=24,
                weight=ft.FontWeight.W_900,
                color=color['text_color']
            ),
            ft.Container(
                width=100,
                height=5,
                bgcolor=color['danger_color'],
            ),
            ft.Text(
                'The gradual\naccumulation of\ninformation about',
                size=16,
                weight=ft.FontWeight.W_300,
                color=color['second_text_color']
            )
        ]
    )
)

# row 2
second_container = ft.Container(
    content=ft.Column(
        controls=[
            ft.Image('images/second_part/telescope.png', width=128, height=128),
            ft.Text(
                'Expert instruction',
                size=24,
                weight=ft.FontWeight.W_900,
                color=color['text_color']
            ),
            ft.Container(
                width=100,
                height=5,
                bgcolor=color['danger_color'],
            ),
            ft.Text(
                'The gradual\naccumulation of\ninformation about',
                size=16,
                weight=ft.FontWeight.W_300,
                color=color['second_text_color']
            )
        ]
    )
)

# second_part
second_part = ft.Container(
    content=ft.Row(
        controls=[
            ft.Column(
                controls=[
                    red_line_container,
                    packages_text,
                    problems_text,
                    learn_more_button
                ]
            ),
            ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            first_container,
                            second_container
                        ],
                        spacing=25
                    )
                ]
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.END,
        spacing=100
    ),
    padding=ft.Padding(top=200, right=0, left=0, bottom=0)
)