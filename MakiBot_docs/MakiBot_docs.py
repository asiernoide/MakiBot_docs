import pynecone as pc
import json

# Load commands from json file to a dictionary
commands = None

with open("commands.json", "r", encoding="utf-8") as f:
    commands = json.load(f)

# Throw an error if the commands file is empty
if commands is None:
    raise Exception("The commands file is empty!")

class State(pc.State):
    """The app state."""
    util_commands: list[dict[str, str]] = commands['Utilidades']
    ent_commands: list[dict[str, str]] = commands['Entretenimiento']
    nsfw_commands: list[dict[str, str]] = commands['NSFW']

def get_command(item):
    return pc.box(
        pc.text(
            item['name'],
            font_size="0.8em",
            as_="b",
        ),
        pc.text(
            item['description'],
            font_size="0.5em",
        ),
        width="100%",
    )

def index() -> pc.Component:
    return pc.vstack(
            pc.box(
                pc.center(
                    pc.heading(
                    "¡Bienvenido a la página de ayuda de MakiBot!",
                    color="white",
                    font_size="1.5em",
                    background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
                    background_clip="text",
                    ),
                ),
                pc.image(
                    src="/icon.png",
                    width="200px",
                    height="auto",
                ),
                # Change background to blurry image of drheader.jpg
                background_image="url('/drheader.jpg')",
                background_size="cover",
                background_position="center",
                width="100%",

                # Add a bit of padding to the left
                padding_left="2em",
                padding_right="2em",
                padding_top="1em",
            ),
            
            # Add different cards for each command category for the discord bot
            pc.responsive_grid(
                pc.vstack(
                    pc.heading(
                        "Utilidades",
                        font_size="1.1em",
                    ),
                    pc.text(
                        "Comandos para hacer tu vida un poco más fácil",
                        font_size="0.8em",
                        as_="em",
                    ),
                    pc.foreach(State.util_commands, get_command),
                    # Change bg property to #333333
                    background_color="#444444",
                    padding="1em",
                    shadow="lg",
                    border_radius="lg",
                ),
                pc.vstack(
                    pc.heading(
                        "Entretenimiento",
                        font_size="1.1em",
                    ),
                    pc.text(
                        "Comandos para pasar el rato",
                        font_size="0.8em",
                        as_="em",
                    ),
                    pc.foreach(State.ent_commands, get_command),
                    background_color="#444444",
                    padding="1em",
                    shadow="lg",
                    border_radius="lg",
                ),
                pc.vstack(
                    pc.heading(
                        "NSFW",
                        font_size="1.1em",
                    ),
                    pc.text(
                        "Comandos para los más atrevidos",
                        font_size="0.8em",
                        as_="em",
                    ),
                    pc.foreach(State.nsfw_commands, get_command),
                    background_color="#444444",
                    padding="1em",
                    shadow="lg",
                    border_radius="lg",
                ),
                columns=[1, 1, 3],
                spacing="5",
                padding_left="0.5em",
                padding_right="0.5em",
                color="white",
            ),
            pc.center(
                pc.vstack(
                    # Copyright disclaimer
                    pc.text(
                        "© 2023 Asier Gallego Roca. Todos los derechos reservados."
                    ),
                    pc.text(
                        "Esta página ha sido creada con el framework Pynecone."
                    ),
                    font_size="0.5em",
                    padding_bottom="0.5em",
                ),
                color="white",
            ),
            spacing="1.5em",
            font_size="2em",
            background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
        )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index, meta=[{"char_set": "UTF-8"}], title="Comandos de MakiBot", image="/iconbook.png", route="/")
app.compile()
