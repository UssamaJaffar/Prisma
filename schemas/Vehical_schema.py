def carBrandEntity(item) -> dict:
    return{
        "id": str(item.get('_id')),
        "name": item.get('name'),
        'logo': item.get('logo'),
        "description": item.get('description')
    }

def carsBrandEntity(entity) -> list:
    return [carBrandEntity(item) for item in entity]

def carEntity(item) -> dict:
    return{
        "id": str(item.get('_id')),
        "name": item.get('name'),
        'description': item.get('description'),
        "CarBrand_id": str(item.get('CarBrand_id'))
    }

def carsEntity(entity) -> list:
    return [carEntity(item) for item in entity]
