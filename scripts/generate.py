import json
import pathlib
import jinja2


def generate_jsons():
    configurations = {
        "purple": {"colour_1": "FFE2F2", "colour_2": "FFCCE8"},
        "blue": {"colour_1": "E3FAFF", "colour_2": "BCE7F1"},
        "green": {"colour_1": "F3F6F4", "colour_2": "D7EADE"},
    }
    directory = pathlib.Path(__file__).parent.resolve()
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(directory))
    base = env.get_template("macbeth.json.j2")
    for colour in configurations:
        rendered = base.render(configurations[colour])
        output = pathlib.Path("macbeth_" + colour + ".json")
        with open(directory.parent / "themes" / output, "w+") as file:
            json.dump(json.loads(rendered), file, indent=4)


if __name__ == "__main__":
    generate_jsons()
