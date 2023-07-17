from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.translate import router as translate_router
from app.routes.history import router as history_router



# Allows CORS middleware
# example: "http://localhost"
# * : all
origins = ["*"]

# Create FastAPI Instance
app = FastAPI(title="NMT-API",
              description="Backend API for NMT")


# Setting Middleware
# Tip : https://hides.kr/1107
# https://github.com/tiangolo/fastapi/issues/5071 깃헙 이슈에 따르면 해당 메소드의 경우 호출할 때 마다 미들웨어를 re-initialize하는 이슈가 있다고 한다.
# 따라서 Middleware클래스를 활용하여 넣어주는 방식으로 변경하는 게 좋다
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
async def root():
    return {"message": "Hello World"}

# Add translate router to FastAPI instance using 'include_router' method
# To access from outside
app.include_router(translate_router, prefix="/translate")
app.include_router(history_router, prefix="/history")
