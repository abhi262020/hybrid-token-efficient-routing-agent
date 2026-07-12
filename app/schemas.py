from pydantic import BaseModel


class RouteRequest(BaseModel):
    prompt: str


class RouteResponse(BaseModel):
    model: str
    task: str
    complexity: int
    confidence: float
    tokens: int
    response: str