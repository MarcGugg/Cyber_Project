from sqlalchemy.orm import Session

from . import models

from . import schemas


# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()


# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()


# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()


# def create_user(db: Session, user: schemas.UserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item



def get_all_companies(db: Session):
    companies = db.query(models.CompanyDetail).all()

    if not companies:
        return []

    companies_as_dict = [company.to_dict_inclusive() for company in companies]

    # return {'CompanyDetail': companies_as_dict}
    return companies_as_dict
    # if companies:
    #     return companies
    
    # return None

def get_one_company(db: Session, company_id: int):
    company = db.query(models.CompanyDetail).get(company_id)

    company_as_dict = company.to_dict_inclusive()

    if company:
        
        return company_as_dict
    
    return None
        