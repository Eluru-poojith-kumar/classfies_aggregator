
from fastapi import FastAPI, Query
from app.schemas import Classified, User
from app.crud import add_classified, get_classifieds
from app.recommender import recommend

app = FastAPI()

@app.post("/classifieds/")
def create_classified(item: Classified):
    result = add_classified(item.dict())
    return {"message": "Classified added", "id": str(result.inserted_id)}

@app.get("/classifieds/")
def fetch_classifieds(location: str = Query(None), language: str = Query(None)):
    data = get_classifieds(location, language)
    return {"results": data}

@app.post("/recommendations/")
def get_recommendations(user: User):
    all_ads = get_classifieds()
    recs = recommend(user.preferences, all_ads)
    return {"recommendations": recs}
