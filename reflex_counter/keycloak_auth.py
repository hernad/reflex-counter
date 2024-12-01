import functools
import json
import os
import time

# https://python-keycloak.readthedocs.io/en/latest/modules/openid_client.html#configure-client-openid

#from google.auth.transport import requests
#from google.oauth2.id_token import verify_oauth2_token

from keycloak import KeycloakOpenID


CLIENT_SECRET = os.environ.get("KEYCLOAK_CLIENT_SECRET", "")

# Configure client
# For versions older than 18 /auth/ must be added at the end of the server_url.
keycloak_openid = KeycloakOpenID(server_url="http://keycloak.cloud.out.ba/",
                                 client_id="fastapi",
                                 realm_name="bringout",
                                 client_secret_key=CLIENT_SECRET)

import reflex as rx

from .react_keycloak_auth import KeycloakAuthProvider, KeycloakLogin
from .reflex_counter import app

class State(rx.State):
    id_token_json: str = rx.LocalStorage()

    def on_success(self, id_token: dict):
        self.id_token_json = json.dumps(id_token)

    @rx.cached_var
    def tokeninfo(self) -> dict[str, str]:
        try:
            token = keycloak_openid.token("user", "password", totp="012345")
            userinfo = keycloak_openid.userinfo(token['access_token'])
            token_info = keycloak_openid.introspect(token['access_token'])
            #return verify_oauth2_token(
            #    json.loads(self.id_token_json)["credential"],
            #    requests.Request(),
            #    CLIENT_ID,
            #)
        except Exception as exc:
            if self.id_token_json:
                print(f"Error verifying token: {exc}")
        return {}

    def logout(self):
        keycloak_openid.logout(token['refresh_token'])
        self.id_token_json = ""

    @rx.var
    def token_is_valid(self) -> bool:
        try:
            return bool(
                self.tokeninfo
                and int(self.tokeninfo.get("exp", 0)) > time.time()
            )
        except Exception:
            return False

    @rx.cached_var
    def protected_content(self) -> str:
        if self.token_is_valid:
            return f"This content can only be viewed by a logged in User. Nice to see you {self.tokeninfo['name']}"
        return "Not logged in."


def user_info(tokeninfo: dict) -> rx.Component:
    return rx.hstack(
        rx.avatar(
            name=tokeninfo["name"],
            src=tokeninfo["picture"],
            size="lg",
        ),
        rx.vstack(
            rx.heading(tokeninfo["name"], size="md"),
            rx.text(tokeninfo["email"]),
            align_items="flex-start",
        ),
        rx.button("Logout", on_click=State.logout),
        padding="10px",
    )


def login() -> rx.Component:
    return rx.vstack(
        KeycloakLogin.create(on_success=State.on_success),
    )


def require_keycloak_login(page) -> rx.Component:
    @functools.wraps(page)
    def _auth_wrapper() -> rx.Component:
        return KeycloakAuthProvider.create(
            rx.cond(
                State.is_hydrated,
                rx.cond(State.token_is_valid, page(), login()),
                rx.spinner(),
            ),
            client_id=CLIENT_ID,
        )
    return _auth_wrapper


def index():
    return rx.vstack(
        rx.heading("Keycloak auth", size="lg"),
        rx.link("Protected Page", href="/protected"),
    )


@rx.page(route="/protected")
@require_keycloak_login
def protected() -> rx.Component:
    return rx.vstack(
        user_info(State.tokeninfo),
        rx.text(State.protected_content),
        rx.link("Home", href="/"),
    )


app.add_page(index)
#app.compile()