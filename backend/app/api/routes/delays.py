from fastapi import APIRouter

router = APIRouter(prefix="/delay", tags=["delay"])

@router.get("/station/{station_id}")
def get_delay_for_station(station_id):
    pass