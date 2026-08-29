from fastapi import FastAPI, Query, Path, HTTPException
from models import MenuResponse
from data import chai_menu


app = FastAPI(
    title= "Chai Point menu API",
    description= "Read only menu API for any UI"
)

@app.get("/")
def root():
    return {"message": "Welcome to chai point menu API"}

@app.get("/menu", response_model= MenuResponse)
def get_menu(category: str = Query(None, description= "Filter by category")):
    if category:
        filtered = [item for item in chai_menu if item["category"] == category]
        if not filtered:
            raise HTTPException(status_code= 404, detail= f"There is no item found for the category {category}")
        return MenuResponse(
            status= "success",
            count=len(filtered),
            items=filtered
        )
    else:
        return MenuResponse(
            status= "success",
            count=len(chai_menu),
            items=chai_menu
        )

@app.get("/menu/{item_id}", response_model= MenuResponse)
def get_menu_with_id(item_id: int = Path(..., description= "Get the menu based on item_id")):
    for item in chai_menu:
        if item["id"] == item_id:
            return MenuResponse(
                status= "success",
                count= 1,
                items=[item]
            )
    raise HTTPException(status_code= 404, detail= f"There is no item found for this item_id {item_id}")
