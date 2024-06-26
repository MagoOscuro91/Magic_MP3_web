import reflex as rx
from mago_oscuro91_web_rx.styles.colors import Colors
from mago_oscuro91_web_rx.components import ant_components
import mago_oscuro91_web_rx.constants as costants


def navbar(hola_neo) -> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.link(
                rx.hstack(
                    rx.text(
                        "MAGIC",
                        size="6",
                        font_family="matrix",
                        margin_left="10px",
                        align="right"
                    ),
                    ant_components.cascos_icon(),
                    padding_bottom="7px",
                    color="#00CC00"
                ),
                href="/",
                margin_y="12px",
                margin_left="2.5px",
                size="6"
            ),
            align="start"
        ),
        rx.spacer(),
        rx.box(
            rx.input(
                placeholder=hola_neo,
                size="3",
                radius="large",
                color_scheme="green",
                max_length="20",
                weidth="100%"
            ),
            padding_top="5px",
            margin_left="10px",
            weidth="100%"
        ),
        rx.spacer(),
        rx.link(
            ant_components.download_icon(
                margin_y="2.5px",
                margin_rigt="2.5px",
                padding_top="10px"
            ),
            href=costants.GITHUB_DESCARGAR,
            size="7"
        ),
        rx.link(
            ant_components.github_icon(
                margin_y="2.5px",
                margin_rigth="1.5px",
                padding_top="11px"
            ),
            href=costants.PAGINA_REPO,
            is_external=True,
            size="6"
        ),
        rx.link(
            rx.avatar(
                name="MagoOscuro91",
                size="3",
                src="/matrix_mp3_web.png",
                bg="",
                margin_y="5px",
                margin_right="6px",
                margin_left="1px",
                border="4px",
                border_color="#00CC00"
            ),
            is_external=True,
            href=costants.GITHUB_MAGICMP3
        ),
        bg=Colors.NEGRO_NAVBAR.value,
        position="sticky",
        z_index="999",
        top="0",
        height="50px",
        weight="100%"
    )
