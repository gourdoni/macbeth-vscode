import json
import pathlib
import jinja2


def generate_jsons():
    constants = {
        "background_4": "1B1C22",
        "background_3": "22232A",
        "background_2": "282A33",
        "background_1": "31333F",
        "foreground_1": "EEE4DD",
        "foreground_2": "D5C5B8",
        "foreground_3": "706A66",
        "red_1": "FFD9D6",
        "red_2": "FF8E85",
        "blue_1": "E3FAFF",
        "blue_2": "BCE7F1",
        "purple_1": "FFE2F2",
        "purple_2": "FFCCE8",
        "green_1": "F3F6F4",
        "green_2": "D7EADE",
        "yellow_1": "FFE5DA",
        "yellow_2": "FFD7BC",
    }
    configurations = {
        "purple": {"colour_1": "FFE2F2", "colour_2": "FFCCE8"},
        "blue": {"colour_1": "E3FAFF", "colour_2": "BCE7F1"},
        "green": {"colour_1": "F3F6F4", "colour_2": "D7EADE"},
    }
    directory = pathlib.Path(__file__).parent.resolve()
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(directory))
    base = env.get_template("macbeth.json.j2")
    for colour in configurations:
        rendered = base.render(constants | configurations[colour])
        output = pathlib.Path("macbeth_" + colour + ".json")
        with open(directory.parent / "themes" / output, "w+") as file:
            json.dump(json.loads(rendered), file, indent=4)


if __name__ == "__main__":
    generate_jsons()
