from fastapi import FastAPI

app=FastAPI()
items=[{"name":"shravan"},{"age":21}]
notes={
       1:{"title":"today's journal","content":"An overview of what i done today"},
    }

# health endpoint
@app.get("/health",status_code=200)
def health_check():
    return {"status":"running"}

# path parameter for listing the note title
@app.get("/notes/{id}")
def item(id:int):
    return notes[id]
