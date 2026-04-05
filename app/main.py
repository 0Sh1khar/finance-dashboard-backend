from fastapi import FastAPI
from app.database import Base, engine
from app.models.user import User
from app.models.financial_record import FinancialRecord
from app.routes.auth_routes import router as auth_router
from app.routes.record_routes import router as record_router
from app.routes.dashboard_routes import router as dashboard_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Finance Dashboard Backend",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(record_router)
app.include_router(dashboard_router)

@app.get("/")
def root():
    return {"message": "Finance Dashboard Backend Running"}