#!/usr/bin/python3
"""it Defines the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """it Represent a state.

    Attributes:
        name (str): The name of the state.
    """

    name = ""
