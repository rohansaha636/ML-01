from pydantic import BaseModel, Field

class PlacementRequest(BaseModel):
    cgpa: float = Field(..., ge=0, le=10, description="CGPA must be between 1 and 10")
    iq: int = Field(..., ge=0, le=100, description="IQ must be between 1 and 100")

class PlacementResponse(BaseModel):
    placement: str
