from pydantic import BaseModel, Field

class PlacementRequest(BaseModel):
    cgpa: int = Field(..., ge=0, le=10, description="CGPA must be between 1 and 10")
    internship: int = Field(..., ge=0, le=10, description="Internship must be between 0 and 10")

class PlacementResponse(BaseModel):
    placement: str
