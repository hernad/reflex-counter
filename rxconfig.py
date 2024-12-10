import reflex as rx

config = rx.Config(
    app_name="reflex_counter",
    # db_url="sqlite:////var/lib/reflexcounter/reflex-counter.db",
    db_url="sqlite:///:memory",
    # api_url="https://reflex-counter-backend.bring-out-ba.uk",
    # env=rx.Env.PROD,
    env=rx.Env.DEV,
    bun_path="/run/current-system/sw/bin/bun",
)
