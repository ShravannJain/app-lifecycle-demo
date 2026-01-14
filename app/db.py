from sqlmodel import SQLModel,Field,create_engine,Session

class Notes(SQLModel,table=True):
    id:int | None=Field(default=None,primary_key=True)
    title:str
    content:str
    
# creating the table using the database engine
engine=create_engine("sqlite:///database.db")
SQLModel.metadata.create_all(engine)


# creating session
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    
def get_session():
    with Session(engine) as session:
        yield session
        