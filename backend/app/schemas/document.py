from pydantic import BaseModel
class  DocumentResponses(BaseModel):
    id : int
    filenmae: str
    
    class Config:
        from_attributes = True