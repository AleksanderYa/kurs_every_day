import os

def getenv_boolean(name: str, default: bool=False) -> bool:
    value = os.getenv(name, default)
    if isinstance(value, str):
        return value.lower() == 'true'
    return value