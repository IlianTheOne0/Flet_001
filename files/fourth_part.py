import flet as ft

from files.colors import color

# first row
advice_text = ft.Text(
    'Practice Advice',
    size=14,
    weight=ft.FontWeight.W_200,
    color=color['primary_color']
)

packages_text = ft.Text(
    'Approdable Packages',
    size=48,
    weight=ft.FontWeight.W_900,
    color=color['text_color']
)

problems_text = ft.Text(
    'Problems trying to resolve the conflict between\nthe two major realms of Classical physics: Newtonian mechanics',
    size=20,
    weight=ft.FontWeight.W_300,
    color=color['second_text_color']
)

# second row
carousel_image = ft.Image(
    'images/fourth_part/carousel.png',
    width=1050,
    height=526
)

# fourth_part
fourth_part = ft.Container(
    content=ft.Column(
        controls=[
            ft.Column(
                controls=[
                    advice_text,
                    packages_text,
                    problems_text
                ]
            ),
            carousel_image
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=50
    ),
    alignment=ft.alignment.center,
    padding=ft.Padding(top=200, right=0, left=0, bottom=0)
)