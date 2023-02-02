from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:(here put your personal user)@localhost:3306/(your db name)")

meta = MetaData()

connection = engine.connect()