import reflex as rf
import json

# Load commands from json file to a dictionary
commands = None

with open("commands.json", "r", encoding="utf-8") as f:
    commands = json.load(f)

# Throw an error if the commands file is empty
if commands is None:
    raise Exception("The commands file is empty!")

class State(rf.State):
    """The app state."""
    util_commands: list[dict[str, str]] = commands['Utilidades']
    ent_commands: list[dict[str, str]] = commands['Entretenimiento']
    nsfw_commands: list[dict[str, str]] = commands['NSFW']

def get_command(item):
    return rf.box(
        rf.markdown(
            item['name'],
            as_="b",
            style={"fontSize": "0.8em", "lineHeight": "0.5em", "margin": "0", "padding": "0"}, # Adjust line height
            component_map={"code": lambda text: rf.code(text, color_scheme="ruby")}
        ),
        rf.markdown(
            item['description'],
            style={"fontSize": "0.5em", "lineHeight": "0.5em", "margin": "0", "padding": "0"}, # Adjust line height
            component_map={"code": lambda text: rf.code(text, color_scheme="ruby")}
        ),
        width="100%",
    )

def index() -> rf.Component:
    return rf.vstack(
            rf.box(
                rf.center(
                    rf.heading(
                    "¡Bienvenido a la página de ayuda de MakiBot!",
                    color="white",
                    font_size="1.5em",
                    line_height="1",
                    background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
                    background_clip="text",
                    ),
                ),
                rf.image(
                    src="/icon.png",
                    width="200px",
                    height="auto",
                ),
                # Change background to blurry image of drheader.jpg
                background_image="url('/drheader.jpg')",
                background_size="cover",
                background_position="center",
                width="100%",

                # Add a bit of padding to the sides
                padding_left="2em",
                padding_right="2em",
                padding_top="1em",
            ),
            
            # Add different cards for each command category for the discord bot
            rf.grid(
                rf.vstack(
                    rf.heading(
                        "Utilidades",
                        font_size="1.1em",
                    ),
                    rf.text(
                        "Comandos para hacer tu vida un poco más fácil",
                        font_size="0.8em",
                        as_="em",
                    ),
                    rf.foreach(State.util_commands, get_command),
                    background_color="#444444",
                    padding="1em",
                    box_shadow="8px 8px 6px 1px #333333",
                    border_radius="10px",
                ),
                rf.vstack(
                    rf.heading(
                        "Entretenimiento",
                        font_size="1.1em",
                    ),
                    rf.text(
                        "Comandos para pasar el rato",
                        font_size="0.8em",
                        as_="em",
                    ),
                    rf.foreach(State.ent_commands, get_command),
                    background_color="#444444",
                    padding="1em",
                    box_shadow="8px 8px 6px 1px #333333",
                    border_radius="10px",
                ),
                rf.vstack(
                    rf.heading(
                        "NSFW",
                        font_size="1.1em",
                    ),
                    rf.text(
                        "Comandos para los más atrevidos",
                        font_size="0.8em",
                        as_="em",
                    ),
                    rf.foreach(State.nsfw_commands, get_command),
                    background_color="#444444",
                    padding="1em",
                    box_shadow="8px 8px 6px 1px #333333",
                    border_radius="10px",
                ),
                grid_template_columns=[
                    "1fr"
                ],
                gap="2rem",
                padding_left="0.5em",
                padding_right="0.5em",
                color="white",
            ),
            rf.box(
                rf.center(
                    rf.vstack(
                        # Copyright disclaimer
                        rf.text(
                            "© 2023 Asier Gallego Roca. Todos los derechos reservados."
                        ),
                        rf.markdown(
                            "Esta página ha sido creada con el framework [Reflex](https://reflex.dev/)."
                        ),
                        font_size="0.5em",
                        padding_bottom="0.5em",
                        align="center"
                    ),
                    color="white",
                ),
                width="100%",
                padding="1em",
            ),
            gap="1em",
            font_size="2em",
            background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
            align="center"
        )



styles = {
    "global": {
        "rt-Text": {
            "margin": "0 !important",
            "padding": "0 !important",
        },
        "css-56tzch": {
            "margin": "0 !important",
            "padding": "0 !important",
        },
        "p": {
            "margin": "0 !important",
        }
    }
}

# Add state and page to the app.
app = rf.App(state=State, style=styles)
app.add_page(index, meta=[{"char_set": "UTF-8"}], title="Comandos de MakiBot", image="/iconbook.png", route="/")
app._compile()
