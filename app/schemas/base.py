from pydantic import BaseModel

class CustomBaseModel(BaseModel):
    def model_dump(self, mode="python", **kwargs):
        d = super().model_dump(mode=mode, **kwargs)
        d = {key: value for key, value in d.items() if value is not None}
        return d