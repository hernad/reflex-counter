import reflex as rx


class HelloBase(rx.Component):
    # Use an absolute path starting with /public
    library = "/public/hello"

    # Define everything else as normal.
    tag = "Hello"

    user: rx.Var[str]
    on_change: rx.EventHandler


class Hello(HelloBase):
    @classmethod
    def create(cls, *children, **props) -> rx.Component:
        props.setdefault("align", "center")
        return rx.vstack(
            rx.heading(HelloState.count),
            # HelloBase(*children, **props),
            rx.button(HelloState.text, on_click=HelloState.change_text),
        )


class HelloState(rx.State):
    count: int = 100
    text: str = "Change me"

    @rx.event
    def set_count(self):
        # rx.console_log("set_count_hello_state")
        # print("set_count hello state", self.count)
        self.count = self.count + 1

    def set_text(self):
        print(self.text)

    @rx.event
    def change_text(self):
        if self.text == "Change Me!":
            self.text = "Changed!"
        else:
            self.text = "Change Me!"

        print("on_click clicked")
        print(self)
