from  fastapi import FastAPI

app=FastAPI()

@app.get("/")
def hello():
    return "hello there.. !"

@app.get("/greetings")
def hello():
    return "Good day buddy.. !"

