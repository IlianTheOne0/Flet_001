import flet as ft

from files.colors import color

# first row
testimonials_text = ft.Text(
    'Testimonials',
    size=14,
    weight=ft.FontWeight.W_200,
    color=color['primary_color']
)

courses_text = ft.Text(
    'Watch our Courses',
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
# first column
woman = ft.Container (
    ft.Column (
        controls = [
            ft.Image('images/fifth_part/woman.png', width=128, height=128),
            ft.Text(
                'Slate helps you see how many more days\nyou need to work to reach your financial\ngoal for the month and year.',
                size=18,
                weight=ft.FontWeight.W_300,
                color=color['second_text_color'],
                text_align=ft.TextAlign.CENTER
            ),
            ft.Image('images/fifth_part/stars.png', width=320, height=60),
            ft.Text(
                'Regina Miles',
                size=18,
                weight=ft.FontWeight.W_600,
                text_align=ft.TextAlign.CENTER
            ),
            ft.Text(
                'Designer',
                size=16,
                weight=ft.FontWeight.W_300,
                text_align=ft.TextAlign.CENTER
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
)

man = ft.Container (
    ft.Column (
        controls = [
            ft.Image('images/fifth_part/man.png', width=128, height=128),
            ft.Text(
                'Slate helps you see how many more days\nyou need to work to reach your financial\ngoal for the month and year.',
                size=18,
                weight=ft.FontWeight.W_300,
                color=color['second_text_color'],
                text_align=ft.TextAlign.CENTER
            ),
            ft.Image('images/fifth_part/stars.png', width=320, height=60),
            ft.Text(
                'Regina Miles',
                size=18,
                weight=ft.FontWeight.W_600,
                text_align=ft.TextAlign.CENTER
            ),
            ft.Text(
                'Designer',
                size=16,
                weight=ft.FontWeight.W_300,
                text_align=ft.TextAlign.CENTER
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
)

# fifth_part
fifth_part = ft.Container(
    content=ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.Column(
                        controls=[
                            testimonials_text,
                            courses_text,
                            problems_text
                        ],
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            ),
            ft.Row(
                controls=[
                    woman,
                    man
                ],
                spacing=150,
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=50
    ),
    alignment=ft.alignment.center,
    padding=ft.Padding(top=200, right=0, left=0, bottom=0)
)