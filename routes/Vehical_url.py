from fastapi import APIRouter
from fastapi.responses import JSONResponse

from models.vehical_models import CarBrand , CarModel
from config.mongodb import db_vehicles
from schemas.Vehical_schema import carsEntity , carsBrandEntity

from bson.objectid import ObjectId

vehicle = APIRouter()

@vehicle.get('/get_cars')
async def find_all_cars():
    try:
        data = carsEntity(db_vehicles['CarModel'].find())
        return data

    except Exception as e:
        print("Server is temporarily unavailable in find_all_cars function =========> " , e)
        return JSONResponse (status_code = 400, content = {"message": "Server is temporarily unavailable"})

@vehicle.post('/add_car/{Car_Brand_id}')
async def create_car(Brand_id,car: CarModel):
    try:

        if len(Brand_id) != 24:
                return JSONResponse (status_code = 400, content = {"message": "Invalid CarBrand ID"})

        else:
            temp = db_vehicles['CarBrand'].find_one({'_id' : ObjectId(Brand_id)})
            if temp:
                data = db_vehicles['CarModel'].insert_one(dict(car))
                if not data.inserted_id:
                    return JSONResponse (status_code = 400, content = {"message": "Data is not save Successfully"})
                return {"message":"success"}
            else:
                return JSONResponse (status_code = 400, content = {"message": "Brand Id is Incorrect"})


    except Exception as e:
        print("Something went wrong in create_car function =========> " , e)
        return JSONResponse (status_code = 400, content = {"message": "Server is temporarily unavailable"})

@vehicle.put('/update_car/{id}')
async def Update_car(id,car: CarModel):
    try:
        if len(id) != 24:
            return JSONResponse (status_code = 400, content = {"message": "Invalid ID"})

        data = db_vehicles['CarModel'].find_one_and_update(
            {"_id": ObjectId(str(id))},
            { "$set" : dict(car)}
        )

        if not data:
            return JSONResponse (status_code = 400, content = {"message": "Data is not save Successfully"})
        return {"message":"success"}

    except Exception as e:
        print("Something went wrong in Update_car function =========> " , e)
        return JSONResponse (status_code = 400, content = {"message": "Server is temporarily unavailable"})

@vehicle.delete('/delete_car/{id}')
async def delete_car(id):
    try:
        if len(id) != 24:
            return JSONResponse (status_code = 400, content = {"message": "Invalid ID"})

        data = db_vehicles['CarModel'].delete_one(
            {"_id": ObjectId(id)}
        )

        if data.deleted_count == 0:
            return JSONResponse (status_code = 400, content = {"message": "Data is not delete Successfully"})
        return {"message":"success"}
        

    except Exception as e:
        print("Something went wrong in delete_car function =========> " , e)
        return JSONResponse (status_code = 400, content = {"message": "Server is temporarily unavailable"})


@vehicle.get('/get_brand')
async def find_all_carBrands():
    try:
        data = carsBrandEntity(db_vehicles['CarBrand'].find())
        return data

    except Exception as e:
        print("Server is temporarily unavailable in find_all_carBrands function =========> " , e)
        return JSONResponse (status_code = 400, content = {"message": "Server is temporarily unavailable"})

@vehicle.post('/add_brand')
async def create_carBrand(Brand: CarBrand):
    try:
        data = db_vehicles['CarBrand'].insert_one(dict(Brand))
        if not data.inserted_id:
            return JSONResponse (status_code = 400, content = {"message": "Data is not save Successfully"})
        return {"message":"success"}

    except Exception as e:
        print("Something went wrong in create_carBrand function =========> " , e)
        return JSONResponse (status_code = 400, content = {"message": "Server is temporarily unavailable"})

@vehicle.put('/update_brand/{id}')
async def Update_carBrand(id,Brand: CarBrand):
    try:
        if len(id) != 24:
            return JSONResponse (status_code = 400, content = {"message": "Invalid ID"})

        data = db_vehicles['CarBrand'].find_one_and_update(
            {"_id": ObjectId(str(id))},
            { "$set" : dict(Brand)}
        )

        if not data:
            return JSONResponse (status_code = 400, content = {"message": "Data is not save Successfully"})
        return {"message":"success"}

    except Exception as e:
        print("Something went wrong in Update_carBrand function =========> " , e)
        return JSONResponse (status_code = 400, content = {"message": "Server is temporarily unavailable"})

@vehicle.delete('/delete_brand/{id}')
async def delete_carBrand(id):
    try:
        if len(id) != 24:
            return JSONResponse (status_code = 400, content = {"message": "Invalid ID"})

        data = db_vehicles['CarBrand'].delete_one(
            {"_id": ObjectId(id)}
        )

        if data.deleted_count == 0:
            return JSONResponse (status_code = 400, content = {"message": "Data is not delete Successfully"})
        return {"message":"success"}
        

    except Exception as e:
        print("Something went wrong in delete_carBrand function =========> " , e)
        return JSONResponse (status_code = 400, content = {"message": "Server is temporarily unavailable"})
