import reflex as rx

import React from 'react';
import { KeycloakProvider, useKeycloak } from '@react-keycloak/web';
#
#const App = () => {
#    const { keycloak, initialized } = useKeycloak();
#
#    if (!initialized) {
#        return <div>Loading...</div>;
#    }
#
#    if (!keycloak.authenticated) {
#        return <div>Not authenticated</div>;
#    }
#
#    return (
#        <div>
#            <p>Welcome, {keycloak.tokenParsed.name}</p>
#            <button onClick={() => keycloak.logout()}>Logout</button>
#        </div>
#    );
#};
#
#const keycloakConfig = {
#    realm: 'your-realm',
#    url: 'your-keycloak-url',
#    clientId: 'your-client-id'
#};
#
#const WrappedApp = () => (
#    <KeycloakProvider keycloakConfig={keycloakConfig}>
#        <App />
#    </KeycloakProvider>
#);
#
#export default WrappedApp;


class KeycloakAuthProvider(rx.Component):
    library = "@react-keycloak/web"
    tag = "KeycloakOAuthProvider"

    client_id: rx.Var[str]


class KeycloakLogin(rx.Component):
    library = "@react-keycloak/web"
    tag = "KeycloakLogin"

    def get_event_triggers(self):
        return {"on_success": lambda data: [data]}

