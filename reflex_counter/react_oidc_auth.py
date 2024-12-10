from typing import Dict

import reflex as rx
import reflex_chakra as rc
#from reflex.event import run_script
from reflex.vars.function import ArgsFunctionOperation, FunctionStringVar


# https://reflex.dev/docs/wrapping-react/guide/#local-components


class AuthProvider(rx.Component):
    library = "react-oidc-context"
    tag = "AuthProvider"
    authority: rx.Var[str]
    client_id: rx.Var[str]
    client_secret: rx.Var[str]
    scope: rx.Var[str]
    redirect_uri: rx.Var[str]
    
    _rename_props: dict[str, str] = {
        "clientId": "client_id",
        "clientSecret": "client_secret",
        "redirectUri": "redirect_uri"
    }




class AuthApp(rx.Component):    

    library = "react-oidc-context"
    tag = "AuthApp"

    def _get_imports(self) -> rx.utils.imports.ImportDict:
        return rx.utils.imports.merge_imports(
            #super()._get_imports(),
            {"react-oidc-context": {rx.utils.imports.ImportVar(tag="useAuth")}},
        )


    def add_custom_code(self) -> list[str]:
        return [
"""
function AuthApp()
{      
    const auth = useAuth();

    if (auth) {
        if (auth.isLoading) {
            return <div>Loading...</div>;
        }

        if (auth.error) {
            return <div>Oops... {auth.error.message}</div>;
        }

        if (auth.isAuthenticated) {
            return (
                <div>
                    Hello {auth.user?.profile.email}{" "}
                    <button onClick={() => void auth.removeUser()}>
                        Log out
                    </button>
                </div>
            );
        }
    }

    return <button onClick={() => void auth.signinRedirect()}>Log in</button>;
}
"""
        ]  
    
#    def _get_imports(self) -> rx.utils.imports.ImportDict:
#        return rx.utils.imports.merge_imports(
#            super()._get_imports(),
#            {"react-oidc-context": {rx.utils.imports.ImportVar(tag="useAuth")}},
#        )
#
#    def add_custom_code(self) -> list[str]:
#        return [ 
#            "const auth = useAuth();"
#        ]

    

#class ClickState(rx.State):
#    text = "Change Me!"
#
#    @rx.event
#    def change_text(self):
#        if self.text == "Change Me!":
#            self.text = "Changed!"
#        else:
#            self.text = "Change Me!"


# https://github.com/authts/react-oidc-context/blob/main/src/AuthContext.ts
# class AuthLogin(rx.Component):
#    library = "react-oidc-context"
#    tag = "useAuth"
#
#    # on_sucess: rx.EventHandler[lambda data: [data]]
#    signin_redirect: rx.Var
#
#    # is_loading: rx.Var[Dict[str, Union[float, str]]]
#    is_loading: rx.Var[bool]
#    is_authenticated: rx.Var[bool]
#    error: rx.Var[Dict[str, str]]
#
# https://github.com/orgs/reflex-dev/discussions/2621


#class AuthLoginButton(rc.Button):
    #@classmethod
    #def create(cls, **props):
    #    return super().create("Sign in with Keycloak 🚀", **props)

#    def _get_imports(self) -> rx.utils.imports.ImportDict:
#        return rx.utils.imports.merge_imports(
#            super()._get_imports(),
#            {"react-oidc-context": {rx.utils.imports.ImportVar(tag="useAuth")}},
#        )

#        def _get_hooks(self) -> str | None:
#            return """
#const login = () => useAuth().signinRedirect();
#"""



    #def _render(self):
    #    """Remove the onSuccess prop so that it doesn't try to render to the DOM."""
    #    tag = super()._render()
    #    # tag.remove_props("onSuccess")
    #    tag.add_props(on_click=FunctionStringVar("auth.signinRedirect()"))
    #    return tag

    # def get_event_triggers(self):
    #    return {"on_success": lambda data: [data]}


#auth_login = AuthLoginButton.create
