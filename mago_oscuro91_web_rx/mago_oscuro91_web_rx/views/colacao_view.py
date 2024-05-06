import reflex as rx
from mago_oscuro91_web_rx.styles import styles
import mago_oscuro91_web_rx.constants as costants
from mago_oscuro91_web_rx.components import ant_components


def colacao_view() -> rx.Component:
    return rx.hstack(
        rx.spacer(),
        rx.vstack(
            rx.heading(
                "Si quieres apoyarme puedes invitarme a un colacao.",
                margin_y="10px"
            ),
            rx.vstack(
                rx.spacer(),
                rx.link(
                    rx.spacer(),
                    rx.vstack(
                        ant_components.coffee_icon(margin_left="75px"),
                        rx.text("Nesquik")
                    ),
                    rx.spacer(),
                    href=costants.COLACAO_DONAR,
                    align_items="center",
                    size="9"
                ),
                rx.spacer(),
                align_items="center",
                background_image="url('/nesquik.jpg')",
                background_size="cover",
                background_position="center",
                border_radius="15px 50px",
                border="5px solid #555",
                width="100%",
                height="30em"
            ),
            rx.link(
                rx.hstack(
                    ant_components.coffee_icon(),
                    rx.text(
                        "Pincha en este enlace para apoyarme con un colacao"
                    ),
                    ant_components.coffee_icon(),
                    margin_y="10px"
                ),
                href=costants.COLACAO_DONAR
            ),
            rx.heading(
                "ESCANEA EL CÓDIGO QR PARA UN NESQUIK"
            ),
            rx.image(
                src="/Código QR.png",
                alt="La imagen de mi QR para donativos",
                margin_y="15px"
            ),
            align_items="center",
            height="100%"
        ),
        rx.spacer(),
        margin_top="15px",
        style=styles.max_width_style_center
    )
