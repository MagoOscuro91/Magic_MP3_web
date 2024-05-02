import reflex as rx
import mago_oscuro91_web_rx.constants as costants
from mago_oscuro91_web_rx.styles import styles
from mago_oscuro91_web_rx.components import ant_components


def desarrollador_view3() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.text(
                'Mi nombre es Jonathan B.V conocido como MagoOscuro91 en internet.\
                Empeze a estudiar de manera independiente hace 6 meses, despues de 17 años que deje la E.S.O para ponerme a trabajar en la obra.\
                6 meses despues partiendo de 0 y un ingles muy basico tengo el placer de presentarme a este concurso de mouredev "hackaton reflex web 2024".\
                Con esta web de codigo abierto en la que ofrezco a la comunidad de desarolladores una herramienta desarollada por mi de codigo abierto que descarga \
                mediante una url de youtube un clip mp3/mp4 o el video completo en formato mp3/mp4 pensando en los desarolladores frontend que necesitan sonidos o clips.\
                Mi plan de estudio autodidacta gratis que a dia de hoy sigo disciplinadamente.',
                padding_top="5px"
            ),
            rx.heading(
                "HISTORIA",
                size="8"
            ),
            rx.text(
                "Siempre e sido un gran fan de los videojuegos y la tecnologia, tube ordenador en casa desde los 9 años gracias\
                amis padres y siempre tube curiosidad de como funcionaban los juegos mods internet sistemas operativos etc..\
                En la pandemia me quede sin trabajo y me puse a aprender diseño 3d dandome cuenta que aunque en la obra estaba bien, \
                lo mio era estar horas delante de una pantalla. Me lo pasaba muy bien cuando algo me salia bien despues de horas, sentia\
                una sensacion agradable al resolver problemas y avanzar, gane un poco de dinero con el 3d y era mas feliz asi.\
                Empeze a pensar cual seria para mi el mejor teletrabajo y se cruzo conmigo la programacion por primera vez.\
                Buscando contenido gratis en internet me cruze con profesores como ami me gusta llamar como mouredev holamundo (nicolas) y midudev.\
                Despues de 6 meses haciendo cursos gratuitos escribiendo cada linea y comentando su explicacion e sido capaz de crear esta web con un\
                framework nuevo como es reflex y ayudar a la comunidad con un script python sencillo."
            ),
            rx.heading(
                "MI ULTIMO TRABAJO",
                size="8"
            ),
            rx.text(
                "Al terminar el curso de 3h python web de mouredev en la que se desarollar adeviento_web como trabajo final copie una web ya echa de una empresa\
                de mi pueblo para ver las posibilidades de reflex y practicar lo aprendido."
            ),
            rx.heading(
                "VIDEO",
                size="8"
            ),
            rx.video(
                url=costants.TRABAJO_REFLEX_3H_PARTE_1,
                width="100%",
                height="auto",
                margin_bottom="25px"
            ),
            rx.text(
                "No pongo el codigo por que es propiedad intelectual imagino y yo lo hice de manera educativa."
            )
        ),
        padding_bottom="15px",
        style=styles.max_width_style
    )


def desarrollador_view1() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.heading(
                "DESARROLLADOR",
                font_size="250%",
                size="8"
            )
        ),
        margin_top="25px",
        style=styles.max_width_style
    )


def desarrollador_view2() -> rx.Component:
    return rx.hstack(
        rx.spacer(),
        rx.hstack(
            rx.heading(
                "MagoOscuro91",
                size="8",
                font_family="nuttynoisses"
            )
        ),
        rx.spacer(),
        style=styles.max_width_style
    )
