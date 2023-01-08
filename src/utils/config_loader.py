from typing import Dict, Any
import yaml


def load_config(name: str) -> Dict[str, Any]:

    with open(f"conf/{name}.yml", "r") as stream:
        try:
            dictionary = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    return dictionary
