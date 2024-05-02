import reflex as rx
from rxconfig import config
from mago_oscuro91_web_rx.pages import index
from mago_oscuro91_web_rx.pages import herramienta
from mago_oscuro91_web_rx.pages import plan
from mago_oscuro91_web_rx.pages import desarrollador
from mago_oscuro91_web_rx.pages import colacao


app = rx.App(
    stylesheets=[
        "/fonts/matrixfont.css",
        "/fonts/nuttynoissesfont.css",
        "/fonts/miltown_font.css",
        "/fonts/graffiti_font.css"
    ],
    style={
        "color": "#00CC00",
        rx.heading: {
            "font_family": "matrix"
        },
        rx.link: {
            "color": "#555"
        }
    },
    theme=rx.theme(
        appearance="dark"
    )
)





















"""Welcome to Reflex! This file outlines the steps to create a basic app."""


# docs_url = "https://reflex.dev/docs/getting-started/introduction/"
# filename = f"{config.app_name}/{config.app_name}.py"


# class State(rx.State):
#     """The app state."""


# def index() -> rx.Component:
#     return rx.center(
#         rx.theme_panel(),
#         rx.vstack(
#             rx.heading("Welcome to Reflex!", size="9"),
#             rx.text("Get started by editing ", rx.code(filename)),
#             rx.button(
#                 "Check out our docs!",
#                 on_click=lambda: rx.redirect(docs_url),
#                 size="4",
#             ),
#             rx.logo(),
#             align="center",
#             spacing="7",
#             font_size="2em",
#         ),
#         height="100vh",
#     )
