import reflex as rx
import mago_oscuro91_web_rx.constants as costants
from mago_oscuro91_web_rx.styles import styles
from mago_oscuro91_web_rx.components import ant_components


def desarrollador_view3() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.text(
                'Mi nombre es Jonathan B.V. conocido como MagoOscuro91 en internet.\
                Empezó a estudiar de manera independiente hace 6 meses, después de 17 años que deje la E.S.O. para ponerme a trabajar en la obra.\
                6 meses después, partiendo de 0 y un inglés muy básico, tengo el placer de presentarme a este concurso de mouredev "hackaton reflex web 2024".\
                Con esta web de código abierto en la que ofrezco a la comunidad de desarrolladores una herramienta desarrollada por mí de código abierto que descarga \
                mediante una URL de YouTube, un clip mp3/mp4 o el video completo en formato mp3/mp4 pensando en los desarrolladores front-end que necesitan sonidos o clips.\
                Mi plan de estudio autodidacta gratis que a día de hoy sigo disciplinadamente.',
                padding_top="5px"
            ),
            rx.heading(
                "HISTORIA",
                size="8"
            ),
            rx.text(
                "Siempre he sido un gran fan de los videojuegos y la tecnología, tuve ordenador en casa desde los 9 años gracias\
                a mis padres y siempre tuve curiosidad de como funcionaban los juegos, mods, internet, sistemas operativos, etc…\
                En la pandemia me quede sin trabajo y me puse a aprender diseño 3d dándome cuenta de que aunque en la obra estaba bien, \
                lo mío era estar horas delante de una pantalla. Me lo pasaba muy bien cuando algo me salía bien después de horas, sentía\
                una sensación agradable al resolver problemas y avanzar, gane un poco de dinero con el 3D y era más feliz así.\
                Empecé a pensar cuál sería para mí el mejor teletrabajo y se cruzó conmigo la programación por primera vez.\
                Buscando contenido gratis en internet me crucé con profesores como ami, me gusta llamar como mouredev hola mundo (Nicolás) y midudev.\
                Después de 6 meses haciendo cursos gratuitos, escribiendo cada línea y comentando su explicación, he sido capaz de crear esta web con un\
                Framework nuevo como es Reflex y ayudar a la comunidad con un script Python sencillo."
            ),
            rx.heading(
                "MI ÚLTIMO TRABAJO",
                size="8"
            ),
            rx.text(
                "Al terminar el curso de 3 h Python web de mouredev en la que se desarrolla adeviento_web como trabajo final copie una web ya echa de una empresa\
                de mi pueblo para ver las posibilidades de Reflex y practicar lo aprendido."
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
                "No pongo el código por qué es propiedad intelectual (imagino) y yo lo hice de manera educativa."
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
