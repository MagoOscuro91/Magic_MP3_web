import reflex as rx
import datetime
import mago_oscuro91_web_rx.constants as constants
import mago_oscuro91_web_rx.styles.styles as styles


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
                src="/mago_github.png",
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
                        href=constants.MI_YOUTUBE,
                        is_external=True,
                        font_size="1em"
                    )   
                ),
                width="100%",
                align_items="start"
            ),
            align_items="start",
            spacing="4",
            flex_direction=["column", "column", "row", "row", "row"]
        ),
        style=styles.max_width_style,
        margin_bottom="30px",
        margin_top="15px",
    )


def experience() -> int:
    return datetime.date.today().year - 2023
