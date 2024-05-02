import reflex as rx
import datetime
import mago_oscuro91_web_rx.constants as constants
import mago_oscuro91_web_rx.styles.styles as styles
# from mago_oscuro91_web_rx.styles.colors import Colors


def author() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Hola, mi nombre es Jonathan B.V",
            size="5"
        ),
        rx.flex(
            rx.avatar(
                name="MagoOscuro91",
                size="7",
                src="/mago_toon_red_eyes.jpg",
                bg="",
                padding="2px",
                border="4px",
                border_color="#00CC00"
            ),
            rx.vstack(
                rx.text(
                    f"Soy estudiante de programación autodidacta desde hace casi {experience()} año."
                ),
                rx.text(
                    "En internet me conocen como ",
                    rx.link(
                        "@MagoOscuro91",
                        href=constants.MY_GITHUB,
                        # color=TextColor.ACCENT.value,
                        font_size="1em"
                    )   
                ),
                # author_buttons(),
                width="100%",
                align_items="start"
            ),
            align_items="start",
            spacing="4",
            flex_direction=["column", "column", "row", "row", "row"]
        ),
        style=styles.max_width_style,
        margin_bottom="30px"
    )


def author_buttons() -> rx.Component:
    return rx.box(
        button(
            "YouTube",
            constants.YOUTUBE_URL
        ),
        button(
            "Twitch",
            constants.TWITCH_URL
        ),
        button(
            "Discord",
            constants.DISCORD_URL
        ),
    )


def experience() -> int:
    return datetime.date.today().year - 2023
