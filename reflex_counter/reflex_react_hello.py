import json
from typing import Dict

import reflex as rx
from reflex.event import input_event


class HelloBase(rx.Component):
    # Use an absolute path starting with /public
    library = "/public/hello"

    # Define everything else as normal.
    tag = "Hello"

    user: rx.Var[str]
    count1: rx.Var[int]
    # event handler ima dva arugmenta
    # https://reflex.dev/docs/events/event-arguments/

    on_success: rx.EventHandler[lambda arg1, arg2: [arg1, arg2]]


class Hello(HelloBase):
    @classmethod
    def create(cls, *children, **props) -> rx.Component:
        props.setdefault("align", "center")
        return rx.vstack(
            rx.heading(HelloState.count),
            HelloBase(*children, **props),
            rx.button(HelloState.text, on_click=HelloState.change_text),
        )


class HelloState(rx.State):
    count: int = 100
    text: str = "Change me"
    events: list[str] = []
    id_token_json: str = rx.LocalStorage()

    @rx.event
    def set_count(self):
        # rx.console_log("set_count_hello_state")
        print("set_count hello state", self.count)
        self.count = self.count + 1

    def on_success(self, id_token: dict, test_str: str):
        print("on_success:", "arg1:", id_token, "arg2:", test_str)
        self.id_token_json = json.dumps(id_token)
        print("id_token_json:", self.id_token_json)

    @rx.event
    def change_text(self):
        print("on_click clicked")
        if self.text == "Change Me!":
            self.text = "Changed!"
        else:
            self.text = "Change Me!"

        print(self)
