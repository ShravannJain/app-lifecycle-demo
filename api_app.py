from fastapi import FastAPI

app=FastAPI()
items=[{"name":"shravan"},{"age":21}]
@app.get("/items/")
def item():
    return items[0:2]