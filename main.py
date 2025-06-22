from fastapi import FastAPI
from api_routes import Play_route, actor_route, customers_route, tickets_route, directors_route, showtimes_route, authentication
from fastapi.security import  HTTPBearer

from api_routes.authentication import router

#from Oauth2 import get_current_user
#from JWTtoken import create_access_token
app = FastAPI(title= "SL Concert Association API")
auth_scheme = HTTPBearer()


app.include_router(authentication.router)
app.include_router(Play_route.router)
app.include_router(actor_route.actors_route)
app.include_router(customers_route.customer_route)
app.include_router(tickets_route.ticket_route)
app.include_router(showtimes_route.showtime_route)
app.include_router(directors_route.director_route)


@app.get("/")
def root():
    return {"message": " Welcome to Sierra Leone Concert API"}


