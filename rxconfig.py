import reflex as rx

config = rx.Config(
    app_name="reflex_counter",
    db_url="sqlite:////var/lib/reflexcounter/reflex-counter.db",
    api_url="https://reflex-counter-backend.bring-out-ba.uk",
    env=rx.Env.PROD,
)
