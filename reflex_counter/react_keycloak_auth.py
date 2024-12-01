import reflex as rx


class KeycloakAuthProvider(rx.Component):
    library = "@react-keycloak/web"
    tag = "KeycloakOAuthProvider"

    client_id: rx.Var[str]


class KeycloakLogin(rx.Component):
    library = "@react-keycloak/web"
    tag = "KeycloakLogin"

    def get_event_triggers(self):
        return {"on_success": lambda data: [data]}

