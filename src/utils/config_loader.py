from multiprocessing.sharedctypes import Value
from typing import Dict, Any
import yaml


def load_config(name: str) -> Dict[str, Any]:

    with open(f"../conf/{name}.yml", "r") as stream:
        try:
            return yaml.load(stream, Loader=yaml.FullLoader)
        except yaml.YAMLError as exc:
            raise yaml.YAMLError(f"The config file {name} could not be loaded")
            print(exc)
