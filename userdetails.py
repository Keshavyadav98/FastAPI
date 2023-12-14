from fastapi import FastAPI
from datetime import date
from email.mine import image
from beanie import Document
from models.stylist import Stylist
from pydantic import BaseModel, EmailStr
from enum import Enum
from typing import Optional, Any


class Userdetails(Document):
    user_id : str
    first_name : str
    last_name : str
    mobile_no : int
    points : int

    class collection:
        name = "userdetails"

    class config:
        schema_extra = {
            "example" : {
                "user_id" : "63fb75334d0cbcc711ee2232",
                "first_name" : "keshav",
                "last_name" : "yadav",
                "mobile_no" : 7906518272,
                "points" : 10
            }
        }
