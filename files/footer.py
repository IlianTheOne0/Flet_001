import flet as ft

from files.colors import color

# row 1
# column 1
company_info = ft.Text(
    'Company Info',
    size=16,
    weight=ft.FontWeight.W_600,
    color=color['text_color']
)

about_us = ft.Text (
    'About Us',
    size=14,
    weight=ft.FontWeight.W_400,
    color=color['second_text_color']
)

carrier = ft.Text (
    'Carrier',
    size=14,
    weight=ft.FontWeight.W_400,
    color=color['second_text_color']
)

we_ahe_hiring = ft.Text (
    'We are hiring',
    size=14,
    weight=ft.FontWeight.W_400,
    color=color['second_text_color']
)

blog = ft.Text (
    'Blog',
    size=14,
    weight=ft.FontWeight.W_400,
    color=color['second_text_color']
)

# column 2
legal = ft.Text (
    'Legal',
    size=16,
    weight=ft.FontWeight.W_600,
    color=color['text_color']
)

# column 3
features = ft.Text (
    'Features',
    size=16,
    weight=ft.FontWeight.W_600,
    color=color['text_color']
)

business_marketing = ft.Text (
    'Business Marketing',
    size=14,
    weight=ft.FontWeight.W_400,
    color=color['second_text_color']
)

user_analytics = ft.Text (
    'User Analytics',
    size=14,
    weight=ft.FontWeight.W_400,
    color=color['second_text_color']
)

live_chat = ft.Text (
    'Live Chat',
    size=14,
    weight=ft.FontWeight.W_400,
    color=color['second_text_color']
)

unlimited_support = ft.Text (
    'Unlimited Support',
    size=14,
    weight=ft.FontWeight.W_400,
    color=color['second_text_color']
)

# column 4
resources = ft.Text (
    'Resources',
    size=16,
    weight=ft.FontWeight.W_600,
    color=color['text_color']
)

ios_android = ft.Text (
    'IOS & Android',
    size=14,
    weight=ft.FontWeight.W_400,
    color=color['second_text_color']
)

watch_a_demo = ft.Text (
    'Watch a Demo',
    size=14,
    weight=ft.FontWeight.W_400,
    color=color['second_text_color']
)

customers = ft.Text (
    'Customers',
    size=14,
    weight=ft.FontWeight.W_400,
    color=color['second_text_color']
)

api = ft.Text (
    'API',
    size=14,
    weight=ft.FontWeight.W_400,
    color=color['second_text_color']
)

# footer
footer = ft.Container(
    content=ft.Column (
        controls=[
            ft.Row(
                controls = [
                    ft.Column (
                        controls = [
                            company_info,
                            about_us,
                            carrier,
                            we_ahe_hiring,
                            blog
                        ]
                    ),
                    ft.Column (
                        controls = [
                            legal,
                            about_us,
                            carrier,
                            we_ahe_hiring,
                            blog
                        ]
                    ),
                    ft.Column (
                        controls = [
                            features,
                            business_marketing,
                            user_analytics,
                            live_chat,
                            unlimited_support
                        ]
                    ),
                    ft.Column (
                        controls = [
                            resources,
                            ios_android,
                            watch_a_demo,
                            customers,
                            api
                        ]
                    )
                ]
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=50
    ),
    alignment=ft.alignment.center,
    padding=ft.Padding(top=200, right=0, left=0, bottom=0)
)