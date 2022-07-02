import info
from typing import Dict


def calculate_spread(barrel_type) -> Dict[str, float]:

    spread_info = {}

    if barrel_type is not None and barrel_type in info.BARREL_TYPES:
        barrel_percent = info.BARREL_STABILIZER_PERCENT[barrel_type]

        spread_stand_hip = info.SPREAD_INFO["spread_stand_hip"]
        spread_stand_hip_run = info.SPREAD_INFO["spread_stand_hip_run"]
        spread_stand_hip_sprint = info.SPREAD_INFO["spread_stand_hip_sprint"]
        spread_crouch_hip = info.SPREAD_INFO["spread_crouch_hip"]
        spread_air_hip = info.SPREAD_INFO["spread_air_hip"]

        temp = (spread_stand_hip * barrel_percent) / 100
        spread_stand_hip -= temp
        spread_info["stand_hip"] = spread_stand_hip

        temp = (spread_stand_hip_run * barrel_percent) / 100
        spread_stand_hip_run -= temp
        spread_info["stand_hip_run"] = spread_stand_hip_run

        temp = (spread_stand_hip_sprint * barrel_percent) / 100
        spread_stand_hip_sprint -= temp
        spread_info["stand_hip_sprint"] = spread_stand_hip_sprint

        temp = (spread_crouch_hip * barrel_percent) / 100
        spread_crouch_hip -= temp
        spread_info["crouch_hip"] = spread_crouch_hip

        temp = (spread_air_hip * barrel_percent) / 100
        spread_air_hip -= temp
        spread_info["air_hip"] = spread_air_hip

        return spread_info

    if barrel_type is None:
        return info.SPREAD_INFO

    else:
        return {
            "error": "Incorrect barrel type"
        }


def validate_mag(mag_type) -> bool:
    if mag_type in info.MAG_TYPES:
        return True

    return False