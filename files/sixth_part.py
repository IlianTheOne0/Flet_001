import flet as ft

from files.colors import color

# first row
newsletter_text = ft.Text(
    'Newsletter',
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
    color=color['second_text_color'],
    text_align=ft.TextAlign.CENTER
)

# second row
email_input = ft.Container(
    content=ft.Row(
        controls=[
            ft.TextField(
                label="Your Email",
                autofill_hints=[ft.AutofillHint.EMAIL],
                border_radius=ft.border_radius.all(15),
            ),
            ft.ElevatedButton(
                text="Subscribe",
                width=160,
                height=60,
                on_click=lambda e: print("Subscribed"),
                bgcolor=color['primary_color'],
                color=color['text_color']
            )
        ],
        spacing=25,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER
    ),
    border_radius=ft.border_radius.all(5),
    padding=ft.Padding(top=10, right=0, left=0, bottom=0)
)

# sixth part
sixth_part = ft.Container(
    content=ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.Column(
                        controls=[
                            newsletter_text,
                            courses_text,
                            problems_text
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            ),
            ft.Row(
                controls=[
                    email_input
                ],
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