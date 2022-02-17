from anyio import CapacityLimiter
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

@vehicle.get('/get_cars/CarBrand')
async def find_all_cars_by_BrandName(brandName:str = None):
    try:
        temp = db_vehicles['CarBrand'].find_one({'name' : brandName.capitalize()} , {'_id': 1})
        if temp:
            data = carsEntity(db_vehicles['CarModel'].find({'CarBrand_id': temp['_id']}))
            return data
        else:
            return JSONResponse (status_code = 400, content = {"message": "No Brand found"})

    except Exception as e:
        print("Server is temporarily unavailable in find_all_cars_by_BrandName function =========> " , e)
        return JSONResponse (status_code = 400, content = {"message": "Server is temporarily unavailable"})

@vehicle.get('/get_cars/tags')
async def find_all_cars_by_tags(tag:str):
    try:
        tag = tag.split(',')
        print(tag)
        data = carsEntity(db_vehicles['CarModel'].find(
                {'name' : {'$in': tag} }
            )
        )
        return data
        
    except Exception as e:
        print("Server is temporarily unavailable in find_all_cars_by_tags function =========> " , e)
        return JSONResponse (status_code = 400, content = {"message": "Server is temporarily unavailable"})


@vehicle.post('/add_car/{Car_Brand_id}')
async def create_car(Brand_id,car: CarModel):
    try:

        if len(Brand_id) != 24:
                return JSONResponse (status_code = 400, content = {"message": "Invalid CarBrand ID"})

        else:
            temp = db_vehicles['CarBrand'].find_one({'_id' : ObjectId(Brand_id)} , {'_id': 1})
            if temp:
                
                car = dict(car)
                car['CarBrand_id'] = str(temp['_id'])
                car['name'] = car['name'].capitalize()

                data = db_vehicles['CarModel'].insert_one(car)
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
        Brand = dict(Brand)
        Brand['name'] = Brand['name'].capitalize()

        temp = db_vehicles['CarBrand'].find_one({'name' : Brand['name']} , {'_id': 1})

        if not temp:
            data = db_vehicles['CarBrand'].insert_one(Brand)
            
            if not data.inserted_id:
                return JSONResponse (status_code = 400, content = {"message": "Data is not save Successfully"})

        else:
            return JSONResponse (status_code = 400, content = {"message": "Brand Name must be unique"})

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
