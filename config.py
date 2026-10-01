import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    # Flask Secret Key
    SECRET_KEY = "Replace_This_With_A_Long_Random_Secret_Key_2026"

    # SQLite Database
    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///" + os.path.join(BASE_DIR, "database", "website.db")
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Upload Configuration
    UPLOAD_FOLDER = os.path.join(
        BASE_DIR,
        "static",
        "uploads",
        "products"
    )

    # Maximum upload size (16 MB)
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    # Allowed image extensions
    ALLOWED_EXTENSIONS = {
        "png",
        "jpg",
        "jpeg",
        "gif",
        "webp"
    }

    # Fixed Product Categories
    PRODUCT_CATEGORIES = [
        "Electronics",
        "building equipments",
        "plumbing tools",
        
        "Home & Kitchen",

        "Accessories",
    
        "Furniture",
        "Others"
    ]

    # Business Information
    BUSINESS_NAME = "Cwebs Hardware"

    WHATSAPP_NUMBER = "254796261591"

    EMAIL = "colourswebs1@gmail.com"

    PHONE = "+254796261591"

    ADDRESS = "Nairobi, Kenya"

