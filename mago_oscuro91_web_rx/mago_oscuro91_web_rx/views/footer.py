import reflex as rx
import mago_oscuro91_web_rx.styles.styles as styles
import mago_oscuro91_web_rx.constants as constants
from mago_oscuro91_web_rx.styles.styles import Size
# from mago_oscuro91_web_rx.styles.colors import Colors
from mago_oscuro91_web_rx.components import ant_components


def footer() -> rx.Component:
    return rx.hstack(
        rx.text(
            "MagicMP3, creado con ",
            ant_components.heart_icon(),
            " para la comunidad 2024",
            rx.link(
                rx.text(
                    "MagoOscuro91",
                    font_family="nuttynoisses"
                ),
                href=constants.MY_GITHUB,
                font_size="1.5em",
                margin_bottom=Size.ZERO.value
            ),
            align_items="start",
            spacing="2",
            padding_left="8px",
        ),
        rx.spacer(),
        ant_components.floatbutton(margin_right="15px",margin_bottom="50px"),
        padding_bottom=Size.DEFAULT.value,
        style=styles.max_width_style,
        padding_y="1em",
        height="134px",
        weight="100%",
        align_items="center"
    )
