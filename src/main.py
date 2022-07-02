from fastapi import FastAPI
from carbine import Carbine
import info
from generics import calculate_spread, validate_mag


app = FastAPI()


@app.get("/")
async def yes():
    return {
        "message": "DA"
    }


@app.get("/ping")
async def ping():
    return {
        "message": "pong"
    }


@app.post("/custom_attachments")
async def custom_attachments(carbine: Carbine):
    barrel_type = (carbine.barrel).lower()
    magazine_type = (carbine.mag).lower()

    autoreload = False

    spread_info = calculate_spread(barrel_type=barrel_type)

    if validate_mag(magazine_type):
        if magazine_type is None or magazine_type == "default":
            magazine_info = info.MAGAZINE_SIZE["default"]
        else:
            if magazine_type == "legendary": autoreload = True

            magazine_info = info.MAGAZINE_SIZE[magazine_type]

    else:
        magazine_info = {
            "error": "Incorrect mag type"
            }

    data = {
        "spread_info": spread_info,
        "mag_info": {
            "max_ammo": magazine_info,
            "autoreload": autoreload
        }
    }

    return data


@app.get("/everything")
async def everything():
    data = {
        "weapon_type": info.WEAPON_TYPE,
        "ammo_type": info.AMMO_TYPE,
        "img_path": info.IMG_PATH,
        "magazine_size": info.MAGAZINE_SIZE,
        "fire_modes": info.FIRE_MODES,
        "attachment_slots": info.ATTACHMENT_SLOTS,
        "optics": info.OPTICS     
    }

    return data


@app.get("/optics")
async def optics():
    return info.OPTICS


@app.get("/slots")
async def slots():
    return info.ATTACHMENT_SLOTS


@app.get("/mag_size")
async def mag_size():
    return info.MAGAZINE_SIZE


@app.get("/fire_modes")
async def fire_modes():
    return info.FIRE_MODES


@app.get("/weapon_type")
async def weapon_type():
    return info.WEAPON_TYPE


@app.get("/ammo_type")
async def ammo_type():
    return info.AMMO_TYPE


@app.get("/img")
async def image():
    return info.IMG_PATH


