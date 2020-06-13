from fastapi import FastAPI, Depends, Header, HTTPException, Request
from fastapi.openapi.utils import get_openapi
from apis import values

app = FastAPI(title="My Super Project",
    description="This is a very fancy project, with auto docs for the API and everything",
    version="2.5.0",
    docs_url='/')

@app.middleware("http")
async def mask_server(request: Request, call_next):
    print("Request Invoked")
    response = await call_next(request)
    print("Response Processed")
    return response

# def custom_openapi(openapi_prefix: str):
#     if app.openapi_schema:
#         return app.openapi_schema
#     openapi_schema = get_openapi(
#         title="Custom title",
#         version="2.5.0",
#         description="This is a very custom OpenAPI schema",
#         routes=app.routes,
#         openapi_prefix=openapi_prefix,
#     )
#     openapi_schema["info"]["x-logo"] = {
#         "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
#     }
#     app.openapi_schema = openapi_schema
#     return app.openapi_schema


# app.openapi = custom_openapi


app.include_router(values.router)
@app.get("/root")
async def root():
    return {"message": "Hello World"}