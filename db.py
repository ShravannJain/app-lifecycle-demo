from sqlmodel import SQLModel,Field,create_engine,Session

class Notes(SQLModel,table=True):
    id:int | None=Field(default=None,primary_key=True)
    title:str
    content:str
    
# adding rows
Notes_1=Notes(title="todays journal",content="An overview of what i done")
Notes_2=Notes(title="random",content="an randome event idk")
Notes_3=Notes(title="agaiin idk",content="idk what to write here")

# creating the table using the database engine
engine=create_engine("sqlite:///database.db")
SQLModel.metadata.create_all(engine)

# adding data
with Session(engine) as session:
    session.add(Notes_1)
    session.add(Notes_2)
    session.add(Notes_3)
    session.commit()