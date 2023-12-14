from fastapi import FastAPI

app = FastAPI()



@app.get("/items/{item_id}")
async def root(item_id:int):
    return {"message" : item_id}

@app.get("/aboutPage")
async def aboutpage():
    return {"message" : "hello world"}

@app.post("/blog")
async def created_blog():
    return {"data" : "blog is created"}