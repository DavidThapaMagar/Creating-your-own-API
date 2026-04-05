from fastapi import FastAPI
from fastapi import Response

app = FastAPI()

@app.get("/")
def root():
    return{"message": "Hello World"}

@app.get('/csv')
def csv():
    csv_content = 'name,age,city\nDavid,20,ISU\nAlex,19,ISU'
    return Response(content=csv_content, media_type='text/plain')













