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
            alt="La imagen de morfeo principal",
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
                "Creado con REFLEX! en 6 dias y un solo lenguaje de programacion PYTHON!",
                "Tanto la web como la app estan en version test, ten en cuenta esto por errores futuros\
                o actuales que ire corriguiendo y actualizando en el repositorio de GitHub.",
                "Faltas de ortografia, cambios de diseño, fuentes etc.",
                "Todos los assets/recursos se encuentran en internet pero pueden contener derechos de autor\
                utilizalos con responsabilidad y solo para uso personal/educativo.",
                "Tambien deves tener en cuenta mi nivel actual (Estudiante) y el tiempo de desarrollo para este proyecto (6 dias).",
                "En la siguiente actualización se corregiran las faltas de ortografia, propiedad hover, se ajustaran los textos y diseño de algun contenedor.\
                Tambien se añadira funcionalidad a la barra de busqueda y algun script .js"
            ),
            rx.heading(
                "HERRAMIENTA",
                size="8"
            ),
            rx.image(
                src="/herramienta_movil_index.png",
                alt="La foto pagina herramienta en vista movil",
                border_radius="15px 50px",
                border="5px solid #555"
            ),
            rx.text(
                'Primera pagina "HERRAMIENTA" donde podras descargar gratis una app de escritorio windows de codigo abierto, desarrollada por mi \
                que descarga mediante una URL de YouTube un archivo a tu escritorio mp3 mp4 de un punto a otro.',
                "Un dia creando una app de escritorio quise personalizar la parte frontend, buscando sonidos para mis botones\
                seme ocurrio la idea de desarrollar otra como ejercicio que me ayudara en este campo para mi comodidad y asi nacio MagicMp3."
            ),
            rx.heading(
                "PLAN DE ESTUDIO",
                size="8"
            ),
            rx.image(
                src="/plan_movil_index.png",
                alt="La foto pagina plan en vista movil",
                border_radius="15px 50px",
                border="5px solid #555"
            ),
            rx.text(
                'Segunda pagina "PLAN DE ESTUDIO" donde encontraras el plan de estudio que yo sigo de manera autodidacta, sin saber nada\
                de programación con contenido "Totalmente Gratuito".'
            ),
            rx.heading(
                "DESARROLLADOR",
                size="8"
            ),
            rx.image(
                src="/desarrollador_movil_index_2.png",
                alt="La foto pagina desarrollador en vista movil",
                border_radius="15px 50px",
                border="5px solid #555"
            ),
            rx.text(
                'Tercera pagina "DESARROLLADOR" donde me presento, cuento quien soy y un poco mi historia con la programacion.'
            ),
            rx.heading(
                "COLACAO",
                size="8"
            ),
            rx.image(
                src="/colacao_movil_index.png",
                alt="La foto pagina desarrollador en vista movil",
                border_radius="15px 50px",
                border="5px solid #555"
            ),
            rx.text(
                'Cuarta pagina "COLACAO" donde podras apoyarme invitandome a un colacao con una donacion via PayPal y un mensaje.'
            )
        ),
        padding_top="15px",
        style=styles.max_width_style
    )
