"""
main
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.route.translate import router as translate_router
from app.route.history import router as history_router


# Allows CORS middleware
# example: "http://localhost"
# * : all
origins = ["*"]

# Create FastAPI Instance
app = FastAPI(title="NMT-API",
              description="Backend API for NMT")


# Setting Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
async def root():
    """
    root (health check)
    """
    return {"message": "Hello World"}

# Add translate router to FastAPI instance using 'include_router' method
# To access from outside
app.include_router(translate_router, prefix="/translate")
app.include_router(history_router, prefix="/history")
