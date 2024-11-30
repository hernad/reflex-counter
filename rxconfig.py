import reflex as rx

config = rx.Config(
    app_name="reflex-counter",
    db_url="sqlite:///reflex-counter.db",
    api_url="https://reflex-counter-backend.bring-out-ba.uk",
    env=rx.Env.PROD,
)
