# from fastapi import APIRouter

# from app.api.schemas import RouteRequest, RouteResponse
# from app.config import settings

# router = APIRouter()


# @router.get("/health")
# def health():
#     return {
#         "status": "healthy",
#         "application": settings.APP_NAME
#     }


# @router.post("/route", response_model=RouteResponse)
# def route(request: RouteRequest):

#     prompt = request.prompt.lower()

#     # Simple routing logic
#     if "python" in prompt or "code" in prompt:
#         model = "accounts/fireworks/models/deepseek-v3"

#     elif len(prompt) < 40:
#         model = "accounts/fireworks/models/llama-v3p1-8b-instruct"

#     else:
#         model = settings.DEFAULT_MODEL

#     return RouteResponse(
#         selected_model=model,
#         confidence=0.95,
#         response="This is a placeholder response.",
#         token_usage=120
#     )

# from fastapi import APIRouter

# from app.schemas import RouteRequest, RouteResponse
# from app.router.router import HybridRouter
# from app.config import settings

# router = APIRouter()

# agent = HybridRouter()


# @router.get("/health")
# def health():
#     return {
#         "status": "healthy",
#         "application": settings.APP_NAME
#     }


# @router.get("/route")
# def route_info():
#     """
#     Browser-friendly endpoint.
#     """
#     return {
#         "message": "Hybrid Token-Efficient Routing Agent",
#         "usage": "Send a POST request to /route with JSON data.",
#         "example": {
#             "prompt": "Write Python Bubble Sort"
#         }
#     }


# @router.post("/route", response_model=RouteResponse)
# def route(request: RouteRequest):
#     return agent.route(request.prompt)

from fastapi import APIRouter

from app.schemas import RouteRequest, RouteResponse
from app.router.router import HybridRouter
from app.config import settings

router = APIRouter()

agent = HybridRouter()


@router.get("/health")
def health():
    return {
        "status": "healthy",
        "application": settings.APP_NAME
    }


@router.get("/route")
def route_info():
    return {
        "message": "Hybrid Token-Efficient Routing Agent",
        "usage": "Send a POST request to /route with JSON data.",
        "example": {
            "prompt": "Write Python Bubble Sort"
        }
    }


@router.post("/route", response_model=RouteResponse)
def route(request: RouteRequest):
    return agent.route(request.prompt)