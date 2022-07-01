from fastapi import APIRouter
from schema import RealEstate

router = APIRouter()

@router.post("/realestate")
async def create(realestate: RealEstate):
    return realestate.save()

@router.get("/realestates")
async def all():
    return [format(pk) for pk in RealEstate.all_pks()]

def format(pk:str):
    realestate = RealEstate.get(pk)
    return {
        "id": realestate.pk,
        "title": realestate.title,
        "textdata": realestate.textdata,
        "desktophidden2": realestate.desktophidden2,
        "desktophidden4": realestate.desktophidden4
    }

@router.put("/realestate/{pk}")
async def update(pk: str, realestate: RealEstate):
    _realestate = RealEstate.get(pk)
    _realestate.title = realestate.title
    _realestate.textdata = realestate.textdata
    _realestate.desktophidden2 = realestate.desktophidden2
    _realestate.desktophidden4 = realestate.desktophidden4
    return _realestate.save()

@router.delete('/realestate/{pk}')
async def delete(pk: str):
    _realestate = RealEstate.get(pk)
    return _realestate.delete()