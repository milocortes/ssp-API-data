from typing import List
from fastapi import APIRouter, Depends, HTTPException, Request, status
from database.connection import get_session, select
from models.tablas_ssp import *

## Definimos la ruta
ssp_router = APIRouter(
    tags=["ssp"]
)

### Definimos las funciones para agregar registros a las tablas
@ssp_router.post("/new/yf_agrc_bevs_and_spices_tonne_ha")
async def create_event(new_event : yf_agrc_bevs_and_spices_tonne_ha, session=Depends(get_session))->dict:
    session.add(new_event)
    session.commit()
    session.refresh(new_event)

    return {
        "message" : "Event created successfully"
    }

@ssp_router.post("/new/yf_agrc_cereals_tonne_ha")
async def create_event(new_event : yf_agrc_cereals_tonne_ha, session=Depends(get_session))->dict:
    session.add(new_event)
    session.commit()
    session.refresh(new_event)

    return {
        "message" : "Event created successfully"
    }




### Definimos las funciones para consultar TODOS los registros de las tablas
@ssp_router.get("/get_all/yf_agrc_bevs_and_spices_tonne_ha", response_model=List[yf_agrc_bevs_and_spices_tonne_ha])
async def retrieve_all_events(session=Depends(get_session))-> List[yf_agrc_bevs_and_spices_tonne_ha]:
    statement = select(yf_agrc_bevs_and_spices_tonne_ha)
    events = session.exec(statement).all()
    return events

@ssp_router.get("/get_all/yf_agrc_cereals_tonne_ha", response_model=List[yf_agrc_cereals_tonne_ha])
async def retrieve_all_events(session=Depends(get_session))-> List[yf_agrc_cereals_tonne_ha]:
    statement = select(yf_agrc_cereals_tonne_ha)
    events = session.exec(statement).all()
    return events



### Definimos las funciones para consultar los registros de las tablas de un pais
@ssp_router.get("/get_country/yf_agrc_bevs_and_spices_tonne_ha/{iso_code3}", response_model=List[yf_agrc_bevs_and_spices_tonne_ha])
async def retrieve_all_events(iso_code3 : str, session=Depends(get_session))-> List[yf_agrc_bevs_and_spices_tonne_ha]:
    statement = select(yf_agrc_bevs_and_spices_tonne_ha).where(yf_agrc_bevs_and_spices_tonne_ha.iso_code3 == iso_code3)
    events = session.exec(statement).all()
    return events

@ssp_router.get("/get_country/yf_agrc_cereals_tonne_ha/{iso_code3}", response_model=List[yf_agrc_cereals_tonne_ha])
async def retrieve_all_events(iso_code3 : str, session=Depends(get_session))-> List[yf_agrc_cereals_tonne_ha]:
    statement = select(yf_agrc_cereals_tonne_ha).where(yf_agrc_cereals_tonne_ha.iso_code3 == iso_code3)
    events = session.exec(statement).all()
    return events



## Actualiza registros
@ssp_router.put("/edit/yf_agrc_bevs_and_spices_tonne_ha/{iso_code3}/{year}", response_model=yf_agrc_bevs_and_spices_tonne_ha)
async def update_event(iso_code3 : str, year : int, new_data: SSPBase, session=Depends(get_session))->yf_agrc_bevs_and_spices_tonne_ha:

    statement = select(yf_agrc_bevs_and_spices_tonne_ha).where(yf_agrc_bevs_and_spices_tonne_ha.iso_code3 == iso_code3).where(yf_agrc_bevs_and_spices_tonne_ha.year == year)

    results = session.exec(statement)

    for i in results:
        id_consulta = i.id

    event = session.get(yf_agrc_bevs_and_spices_tonne_ha, id_consulta)
    if event:
        event_data = new_data.dict(exclude_unset=True)
        for key, value in event_data.items():
            setattr(event,key, value)
        session.add(event)
        session.commit()
        session.refresh(event)
        
        return event
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        details="Event with supplied ID does not exist"
    )

@ssp_router.put("/edit/yf_agrc_cereals_tonne_ha/{iso_code3}/{year}", response_model=yf_agrc_cereals_tonne_ha)
async def update_event(iso_code3 : str, year : int, new_data: SSPBase, session=Depends(get_session))->yf_agrc_cereals_tonne_ha:

    statement = select(yf_agrc_cereals_tonne_ha).where(yf_agrc_cereals_tonne_ha.iso_code3 == iso_code3).where(yf_agrc_cereals_tonne_ha.year == year)

    results = session.exec(statement)

    for i in results:
        id_consulta = i.id

    event = session.get(yf_agrc_cereals_tonne_ha, id_consulta)
    if event:
        event_data = new_data.dict(exclude_unset=True)
        for key, value in event_data.items():
            setattr(event,key, value)
        session.add(event)
        session.commit()
        session.refresh(event)
        
        return event
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        details="Event with supplied ID does not exist"
    )

