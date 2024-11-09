import flet as ft

from .container_fluid import container_fluid
from .navbar import navbar
from ..colors import color

first_part = ft.Column(
    controls=[
        ft.Container (
            content=ft.Column (
                controls=[
                    navbar,
                    container_fluid
                ]
            ),
            bgcolor=color['background_color']
        )
    ]
)