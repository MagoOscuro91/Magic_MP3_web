import reflex as rx
import mago_oscuro91_web_rx.constants as costants
from mago_oscuro91_web_rx.styles import styles
from mago_oscuro91_web_rx.components import ant_components
# from mago_oscuro91_web_rx.styles.colors import Colors


def index_view_image() -> rx.Component:
    return rx.vstack(
        rx.spacer(weidth="100%"),
        rx.image(
            src="/morfeo.png",
            alt="La imagen de Morfeo principal",
            weidth="100%",
            height="100%"
        ),
        rx.heading(
            "MAGIC WEB REFLEX",
            font_size="250%",
            margin_y="35px",
            size="8"
        ),
        rx.text(
            "Creado con REFLEX! En 6 días y un solo lenguaje de programación PYTHON!.",
            "Tanto la web como la app están en versión test y son de código abierto, ten en cuenta esto por errores actuales\
            que iré corrigiendo y actualizando en el repositorio de GitHub.",
            "Faltas de ortografía, fuentes, etc.",
            "Todos los assets/recursos se encuentran en internet, pero pueden contener derechos de autor\
            utilízalos con responsabilidad y solo para uso personal/educativo.",
            "También debes tener en cuenta mi nivel actual (Estudiante) y el tiempo de desarrollo para este proyecto (6 días) ",
            rx.link(
                'Código en GitHub aquí  ',
                ant_components.codeicon(),
                is_external=True,
                href=costants.PAGINA_REPO
            ),
            ".",
            margin_top="10px"
        ),
        rx.spacer(weidth="100%"),
        style=styles.max_width_style_center,
        margin_top="25px"
    )


def index_view_image_1() -> rx.Component:
    return rx.vstack(
        rx.spacer(weidth="100%"),
        rx.heading(
            "HERRAMIENTA",
            margin_top="5px",
            margin_bottom="15px",
            size="8"
        ),
        rx.image(
            src="/herramienta_movil.png",
            alt="La foto página herramienta en vista móvil",
            border_radius="15px 50px",
            border="5px solid #555"
        ),
        rx.link(
            ant_components.codeicon(padding_left="27.5px"),
            rx.text("Herramienta", size="1", margin_left="3px"),
            margin="0.3em",
            margin_top="10px",
            href="/herramienta"
        ),
        rx.text(
            'Primera página "HERRAMIENTA" donde podrás descargar gratis una app de escritorio Windows de código abierto, desarrollada por mí \
            que descarga mediante una URL de YouTube un archivo a tu escritorio mp3 mp4 de un punto a otro.',
            "Un día creando una app de escritorio quise personalizar la parte front-end, buscando sonidos para mis botones\
            seme ocurrió la idea de desarrollar otra como ejercicio que me ayudara en este campo para mi comodidad y así nació MagicMp3 ",
            rx.link(
                'Descarga desde GitHub aquí  ',
                ant_components.download_icon(),
                href=costants.GITHUB_DESCARGAR
            ),
            ".Para ver el código fuente ",
            rx.link(
                'Código en GitHub aquí  ',
                ant_components.codeicon(),
                is_external=True,
                href=costants.GITHUB_MAGICMP3
            ),
            ".",
            margin_top="10px"
        ),
        rx.heading(
            "PLAN DE ESTUDIO",
            margin_top="25px",
            margin_bottom="15px",
            size="8"
        ),
        rx.image(
            src="/plan_movil.png",
            alt="La foto página plan en vista móvil",
            border_radius="15px 50px",
            border="5px solid #555"
        ),
        rx.link(
            ant_components.codeicon(padding_left="31px"),
            rx.text("Plan de estudio", size="1"),
            margin="0.3em",
            margin_top="10px",
            href="/plan"
        ),
        rx.text(
            'Segunda página "PLAN DE ESTUDIO" donde encontraras el plan de estudio que yo sigo de manera autodidacta, sin saber nada\
            de programación con contenido "Totalmente Gratuito".',
            margin_top="10px"
        ),
        rx.heading(
            "DESARROLLADOR",
            margin_top="25px",
            margin_bottom="15px",
            size="8"
        ),
        rx.image(
            src="/desarrollador_movil.png",
            alt="La foto página desarrollador en vista móvil",
            border_radius="15px 50px",
            border="5px solid #555"
        ),
        rx.link(
            ant_components.codeicon(padding_left="27.5px"),
            rx.text("Desarollador", size="1", margin_left="3px"),
            margin="0.3em",
            margin_top="10px",
            href="/desarrollador"
        ),
        rx.text(
            'Tercera página "DESARROLLADOR" donde me presento, cuento quién soy y un poco mi historia con la programación.',
            margin_top="10px"
        ),
        rx.heading(
            "COLACAO",
            margin_top="25px",
            margin_bottom="15px",
            size="8"
        ),
        rx.image(
            src="/colacao_movil.png",
            alt="La foto página desarrollador en vista móvil",
            border_radius="15px 50px",
            border="5px solid #555"
        ),
        rx.link(
            ant_components.coffee_icon(padding_left="16px"),
            rx.text("Colacao", size="1", margin_left="3px"),
            margin="0.3em",
            margin_top="10px",
            href="/colacao"
        ),
        rx.text(
            'Cuarta página "COLACAO" donde podrás apoyarme invitándome a un colacao con una donación vía PayPal y un mensaje.',
            margin_top="10px"
        ),
        rx.spacer(weidth="100%"),
        style=styles.max_width_style_center,
        margin_top="15px"
    )
