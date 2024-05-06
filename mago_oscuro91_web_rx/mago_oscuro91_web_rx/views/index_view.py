import reflex as rx
import mago_oscuro91_web_rx.constants as costants
from mago_oscuro91_web_rx.styles import styles
from mago_oscuro91_web_rx.components import ant_components
from mago_oscuro91_web_rx.styles import styles


def index_view_image() -> rx.Component:
    return rx.hstack(
        rx.spacer(weidth="100%"),
        rx.image(
            src="/morfeo.png",
            alt="La imagen de Morfeo principal",
            weidth="100%",
            height="100%"
        ),
        rx.spacer(weidth="100%"),
        style=styles.max_width_style_center,
        margin_top="15px"
    )


def index_view() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.heading(
                "MAGIC WEB REFLEX",
                font_size="250%",
                size="8"
            ),
            rx.text(
                "Creado con REFLEX! En 6 días y un solo lenguaje de programación PYTHON!",
               "Tanto la web como la app están en versión test, ten en cuenta esto por errores futuros\
                O actuales que iré corrigiendo y actualizando en el repositorio de GitHub.",
                "Faltas de ortografía, cambios de diseño, fuentes, etc.",
                "Todos los assets/recursos se encuentran en internet, pero pueden contener derechos de autor\
                utilízalos con responsabilidad y solo para uso personal/educativo.",
                "También debes tener en cuenta mi nivel actual (Estudiante) y el tiempo de desarrollo para este proyecto (6 días).",
                "En la siguiente actualización se corregirán las faltas de ortografía, propiedad hover, se ajustarán los textos y diseño de algún contenedor.\
                También se añadirá funcionalidad a la barra de búsqueda y algún script .js"
            ),
            rx.heading(
                "HERRAMIENTA",
                size="8"
            ),
            rx.image(
                src="/herramienta_movil.png",
                alt="La foto página herramienta en vista móvil",
                border_radius="15px 50px",
                border="5px solid #555"
            ),
            rx.text(
                'Primera página "HERRAMIENTA" donde podrás descargar gratis una app de escritorio Windows de código abierto, desarrollada por mí \
                que descarga mediante una URL de YouTube un archivo a tu escritorio mp3 mp4 de un punto a otro.',
                "Un día creando una app de escritorio quise personalizar la parte front-end, buscando sonidos para mis botones\
                seme ocurrió la idea de desarrollar otra como ejercicio que me ayudara en este campo para mi comodidad y así nació MagicMp3."
            ),
            rx.heading(
                "PLAN DE ESTUDIO",
                size="8"
            ),
            rx.image(
                src="/plan_movil.png",
                alt="La foto página plan en vista móvil",
                border_radius="15px 50px",
                border="5px solid #555"
            ),
            rx.text(
                'Segunda página "PLAN DE ESTUDIO" donde encontraras el plan de estudio que yo sigo de manera autodidacta, sin saber nada\
                de programación con contenido "Totalmente Gratuito".'
            ),
            rx.heading(
                "DESARROLLADOR",
                size="8"
            ),
            rx.image(
                src="/desarrollador_movil.png",
                alt="La foto página desarrollador en vista móvil",
                border_radius="15px 50px",
                border="5px solid #555"
            ),
            rx.text(
                'Tercera página "DESARROLLADOR" donde me presento, cuento quién soy y un poco mi historia con la programación.'
            ),
            rx.heading(
                "COLACAO",
                size="8"
            ),
            rx.image(
                src="/colacao_movil.png",
                alt="La foto página desarrollador en vista móvil",
                border_radius="15px 50px",
                border="5px solid #555"
            ),
            rx.text(
                'Cuarta página "COLACAO" donde podrás apoyarme invitándome a un colacao con una donación vía PayPal y un mensaje.'
            )
        ),
        padding_top="15px",
        style=styles.max_width_style
    )
