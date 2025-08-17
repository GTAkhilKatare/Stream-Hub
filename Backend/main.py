from fastapi import FastAPI

# Routers import
from .routers.authentication import login, register
from .routers.streams import all_streams, live_stream, search_stream
from .routers.users import channel, profile


app = FastAPI()

# Inclusion of routers
app.include_router(login.router)
app.include_router(register.router)
app.include_router(all_streams.router)
app.include_router(live_stream.router)
app.include_router(search_stream.router)
app.include_router(channel.router)
app.include_router(profile.router)