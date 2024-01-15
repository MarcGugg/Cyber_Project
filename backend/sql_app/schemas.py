from typing import Union, List, Optional, Any
from pydantic import BaseModel



class CategoryBase(BaseModel):
    category: str
    logo_file: Optional[str] = None
    logo_url: Optional[str] = None
    logo_old: Optional[str] = None
    logo_new: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    class Config:
        orm_mode = True


class CompanyDetailBase(BaseModel):
    company: str
    company_url: str
    linkedin_url: Optional[str] = None
    year_founded: Optional[int] = None
    employees: Optional[int] = None
    headcount_direction: Optional[str] = None
    hq_country: Optional[str] = None
    hq_city: Optional[str] = None
    subcategory: Optional[str] = None
    customer_industries: Optional[str] = None
    corporate_customers: Optional[str] = None
    customer_size: Optional[str] = None
    customer_count: Optional[str] = None
    tech_stack: Optional[str] = None
    product_integrations: Optional[str] = None
    pricing: Optional[str] = None
    industry_awards: Optional[str] = None
    industry_events: Optional[str] = None
    executive_team: Optional[str] = None

    class Config:
        alias_generator = lambda x: x[0].lower() + x[1:]
        allow_population_by_field_name = True

class CompanyDetailCreate(CompanyDetailBase):
    pass

class CompanyDetail(CompanyDetailBase):
    # category: Any  # Use Any for flexibility
    # funding_details: List[Any] = []  # Use Any for flexibility
    category: Category
    funding_details: List["FundingDetail"] = []

    class Config:
        orm_mode = True


class FundingDetailBase(BaseModel):
    logo: Optional[str] = None
    amount_raised: Optional[str] = None
    date_of_funding: str
    funding_round: str
    ceo: Optional[str] = None
    total_amount_raised: Optional[str] = None
    category: Optional[str] = None
    established: Optional[int] = None
    location: Optional[str] = None
    employees: Optional[int] = None
    lead_investor: Optional[str] = None

class FundingDetailCreate(FundingDetailBase):
    pass

class FundingDetail(FundingDetailBase):
    company: CompanyDetail

    class Config:
        orm_mode = True



# class ItemBase(BaseModel):
#     title: str
#     description: Union[str, None] = None


# class ItemCreate(ItemBase):
#     pass


# class Item(ItemBase):
#     id: int
#     owner_id: int

#     class Config:
#         orm_mode = True


# class UserBase(BaseModel):
#     email: str


# class UserCreate(UserBase):
#     password: str


# class User(UserBase):
#     id: int
#     is_active: bool
#     # items: list[Item] = []

#     class Config:
#         orm_mode = True


# class CompanyBase(BaseModel):
#     name: str


# class CompanyCreate(CompanyBase):
#     pass


# class Company(CompanyBase):
#     id: int

#     class Config:
#         orm_mode = True