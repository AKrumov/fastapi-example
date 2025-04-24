import uvicorn
from fastapi import FastAPI

from app.config import middlewares_cfg as middlewares, routers_cfg as routers, events_cfg as event
from app.config.settings_cfg import Settings

config = Settings().app
app = FastAPI(docs_url=f"{config['root_path']}/docs", lifespan=event.lifespan)

middlewares.configure(app)
routers.configure(app)

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=config['host'],
        port=config['port']
    )
