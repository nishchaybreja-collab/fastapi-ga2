from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

df = pd.read_csv("q-fastapi.csv")

@app.get("/api")
def get_students(class_: list[str] = Query(default=None, alias="class")):
    data = df.copy()

    if class_:
        data = data[data["class"].isin(class_)]

    return {
        "students": [
            {
                "studentId": int(row["studentId"]),
                "class": row["class"]
            }
            for _, row in data.iterrows()
        ]
    }