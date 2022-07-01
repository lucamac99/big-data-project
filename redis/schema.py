from redis_om import HashModel
from config import redis_db

class RealEstate(HashModel):
    title: str
    textdata: str
    desktophidden2: str
    desktophidden4: str
    
    class Meta: 
        database: redis_db

        