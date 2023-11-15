class Config:
    APP_NAME = "VIS-BLOG"

    DB_NAME = ""
    DB_USER = ""
    DB_PASSWORD = ""
    DB_DRIVER = ""
    DB_HOST = ""
    DB_PORT = ""
    SQLALCHEMY_DATABASE_URI = f"{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SECRET_KEY = r"=CvE2l&M.7"
    DEBUG = True
