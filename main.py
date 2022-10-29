from fastapi import FastAPI
from gsi.app.ping.view import router as router_ping
from gsi.app.predict.view import router as router_predict

app = FastAPI()

app.include_router(router_ping)
app.include_router(router_predict)
