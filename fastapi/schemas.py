from fastapi import Form, File, UploadFile
from pydantic import BaseModel

# inspiration from
# https://stackoverflow.com/a/60670614 via
# https://github.com/ianrufus/youtube/blob/main/fastapi-forms-file-upload/schemas.py


class FeaturesForm(BaseModel):
    """pydantic model to get the form input we want"""

    OverallQual: int
    FullBath: int
    GarageArea: int
    LotArea: int

    @classmethod
    def as_form(
        cls,
        OverallQual: int = Form(...),
        FullBath: int = Form(...),
        GarageArea: int = Form(...),
        LotArea: int = Form(...),
    ):
        return cls(
            OverallQual=OverallQual,
            FullBath=FullBath,
            GarageArea=GarageArea,
            LotArea=LotArea,
        )
