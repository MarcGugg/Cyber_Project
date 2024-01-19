from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from . import crud, models

from . import schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    '*'
    # "http://localhost.tiangolo.com",
    # "https://localhost.tiangolo.com",
    # "http://localhost",
    # "http://localhost:8080",
    # "http://localhost:5173/" #react front end
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)


# @app.get("/users/", response_model=list[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users


# @app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


# @app.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)


# @app.get("/items/", response_model=list[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items




@app.get("/companies", response_model=list[schemas.CompanyDetail])
def get_companies(db: Session = Depends(get_db)):
    print("")
    print("")
    print("")
    print("HELLO FROM BACKEND")
    print("")
    print("")
    print("")
    companies = crud.get_all_companies(db)
    print('')
    print('')
    print('')
    print('')
    print('')
    print('COMPANIES', companies)
    print('')
    print('')
    print('')
    print('')
    print('')

    
    if companies:
        # return [company.to_dict_inclusive() for company in companies]
        # return companies['CompanyDetail']
        return companies
    
    return None


@app.get("/companies/{company_id}", response_model=schemas.CompanyDetail)
def get_company(company_id: int, db: Session = Depends(get_db)):
    company = crud.get_one_company(db, company_id = company_id)

    if company:
        return company
    
@app.get("/funding/{funding_id}", response_model=schemas.FundingDetails)
def get_funding(funding_id: int, db: Session = Depends(get_db)):
    funding = crud.get_funding(db, funding_id=funding_id)

    print("")
    print("")
    print("")
    print("")
    print("FUNDING FROM MAIN", funding)
    print("")
    print("")
    print("")

    if funding:
        return funding
    return None