
from .database import classifieds_collection

def add_classified(data: dict):
    return classifieds_collection.insert_one(data)

def get_classifieds(location=None, language=None):
    query = {}
    if location:
        query["location"] = location
    if language:
        query["language"] = language
    return list(classifieds_collection.find(query))
