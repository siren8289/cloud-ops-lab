from fastapi import FastAPI
from .database import connect


app = FastAPI()

# 1. GET/health 브라우저 요청
# 2. FastAPI 라우터
@app.get("/health")
def health(): # 3. 파이썬 함수 health()
    return {"status": "ok"} # 4. JSON 응답


# 1. GET/products 브라우저 요청
# 2. FastAPI 라우터
@app.get("/products")
def products(): # 3. 파이썬 함수 products()
    return [ # 4. Json응답
        {"id": 1, "name": "Keyboard"}
    ]


@app.get("/db-health")
def db_health():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT 1")
            value = cur.fetchone()[0]

    return {"database": value}
