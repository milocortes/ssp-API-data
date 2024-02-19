from sqlmodel import SQLModel, Field
from typing import Optional, List

class SSPBase(SQLModel):
    iso_code3 : str 
    nation : str
    year : int
    value : float



class yf_agrc_bevs_and_spices_tonne_ha(SSPBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    class Config:
        schema_extra = {
            "example": {
                "iso_code3": "AFG",
                "nation": "Afghanistan",
                "year" : 2011,
                "value" : 0.0045000000000000005
            }
        }

class yf_agrc_cereals_tonne_ha(SSPBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    class Config:
        schema_extra = {
            "example": {
                "iso_code3": "AFG",
                "nation": "Afghanistan",
                "year" : 2011,
                "value" : 0.0045000000000000005
            }
        }



