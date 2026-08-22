class Config:
    SECRET_KEY = "senhasupersecreta"

    SQLALCHEMY_DATABASE_URI = (
        "mysql+mysqlconnector://root:110806le@localhost/playmusica"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False