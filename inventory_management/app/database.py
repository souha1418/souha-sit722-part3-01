from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

#SQLALCHEMY_DATABASE_URL = "postgresql://admin:E5OJuKRE14iotwfsvHwJeqsjaKK1eKmO@dpg-cq0nb2aju9rs73b0500g-a.oregon-postgres.render.com/part2" #os.getenv("DATABASE_URL")
SQLALCHEMY_DATABASE_URL = "postgresql://sit722_part3_user:MdwAsc0tjC0B20e0DCkvmjWyeAIxdeGR@dpg-cr7rncrtq21c739euie0-a.oregon-postgres.render.com/sit722_part3" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
