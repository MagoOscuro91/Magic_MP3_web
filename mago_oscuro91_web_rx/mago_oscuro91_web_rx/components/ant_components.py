import reflex as rx


class SpotifyIcon(rx.Component):
    library = "@ant-design/icons"
    tag = "SpotifyOutlined"


spotify_icon = SpotifyIcon.create


class GithubIcon(rx.Component):
    library = "@ant-design/icons"
    tag = "GithubOutlined"


github_icon = GithubIcon.create


class CoffeeIcon(rx.Component):
    library = "@ant-design/icons"
    tag = "CoffeeOutlined"


coffee_icon = CoffeeIcon.create


class HeartIcon(rx.Component):
    library = "@ant-design/icons"
    tag = "HeartOutlined"


heart_icon = HeartIcon.create


class DownloadIcon(rx.Component):
    library = "@ant-design/icons"
    tag = "DownloadOutlined"


download_icon = DownloadIcon.create


class PlayIcon(rx.Component):
    library = "@ant-design/icons"
    tag = "PlayCircleOutlined"


play_icon = PlayIcon.create


class CascosIcon(rx.Component):
    library = "@ant-design/icons"
    tag = "CustomerServiceOutlined"
    spin = True


cascos_icon = CascosIcon.create


class CasaIcon(rx.Component):
    library = "@ant-design/icons"
    tag = "HomeOutlined"


casa_icon = CasaIcon.create


class FacebookIcon(rx.Component):
    library = "@ant-design/icons"
    tag = "FacebookOutlined"


facebookicon = FacebookIcon.create


class CodeIcon(rx.Component):
    library = "@ant-design/icons"
    tag = "CodeOutlined"
    twoToneColor = "#fff"


codeicon = CodeIcon.create


class FloatButton(rx.Component):
    library = "antd"
    tag = "FloatButton.BackTop"
    shape = "square"
    icon = casa_icon()


floatbutton = FloatButton.create


# class CollapsedMenu(rx.Component):
#     library = "antd"
#     tag = "Button MenuProp"
#     theme = "dark"
#     items = [
#         "Herramienta",
#         "Plan de estudio",
#         "autor"
#     ]


# collapsed_menu = CollapsedMenu.create
