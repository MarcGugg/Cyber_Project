from typing import Union, List, Optional, Any
from pydantic import BaseModel, Field



class CategoryBase(BaseModel):
    category: str
    logo_file: Optional[str] = Field(alias='logoFile')
    logo_url: Optional[str] = Field(alias='logoUrl')
    logo_old: Optional[str] = Field(alias='logoOld')
    logo_new: Optional[str] = Field(alias='logoNew')

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    class Config:
        orm_mode = True



class CompanyDetailBase(BaseModel):
    id: int
    company: str
    company_url: Optional[str] = Field(alias="companyUrl")
    linkedin_url: Optional[str] = Field(alias='linkedinUrl')
    year_founded: Optional[int] = Field(alias='yearFounded')
    employees: Optional[int] = None
    headcount_direction: Optional[str] = Field(alias='headcountDirection')
    hq_country: Optional[str] = Field(alias='hqCountry')
    hq_city: Optional[str] = Field(alias='hqCity')
    subcategory: Optional[str] = None
    customer_industries: Optional[str] = Field(alias='customerIndustries')
    customer_size: Optional[str] = Field(alias='customerSize')
    customer_count: Optional[str] = Field(alias='customerCount')
    tech_stack: Optional[str] = Field(alias='techStack')
    product_integrations: Optional[str] = Field(alias='productIntegrations')
    pricing: Optional[str] = None
    # industry_awards: Optional[str] = Field(alias='industryAwards')
    industry_events: Optional[str] = Field(alias='industryEvents')

class CompanyDetailCreate(CompanyDetailBase):
    pass

class CompanyDetail(CompanyDetailBase):
    id: int

    class Config:
        orm_mode = True

class CompanyDetail(CompanyDetailBase):
    executives: List['Executive']
    category: Category
    fundingDetails: List['FundingDetails']
    corporateCustomers: List['CorporateCustomer']
    industryAwards: List['IndustryAward']

    class Config:
        orm_mode = True

    class Config:
        alias_generator = lambda x: x[0].lower() + x[1:]

    class Config:
        fields = {
            "funding_details": "fundingDetails",
            "corporate_customers": "corporateCustomers",
            "industry_awards": "industryAwards"
            # Add more aliases as needed for other fields
        }



class ProductBase(BaseModel):
    id: int
    name: str

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    company: Optional[CompanyDetail] = None

    class Config:
        orm_mode = True


# potential logic for IndustryEvent table
# class IndustryEventBase(BaseModel):
#     id: int
#     name: int
#     year: int

# class IndustryEventCreate(IndustryEventBase):
#     pass

# class IndustryEvent(IndustryEventBase):
#     participants: Optional[CompanyDetail] = None
        



# potential logic for Product table
# class ProductBase(BaseModel):
#     id: int
#     name: int

# class ProductCreate(ProductBase):
#     pass

# class Product(ProductBase):
#     company: Optional[CompanyDetail] = None

#     class Config:
#         orm_mode = True




class IndustryAwardBase(BaseModel):
    id: int
    name: str
    year: int
    issuing_organization: Optional[str] = Field(alias='issuingOrg')

class IndustryAwardCreate(IndustryAwardBase):
    # company_detail_id = Optional[int] = None
    pass

class IndustryAward(IndustryAwardBase):
    company: Optional[CompanyDetail] = None

    class Config:
        orm_mode = True






class CorporateCustomerBase(BaseModel):
    id: int
    name: str

class CorporateCustomerCreate(CorporateCustomerBase):
    vendor_id: Optional[int] = None

class CorporateCustomer(CorporateCustomerBase):
    vendor: Optional[CompanyDetail] = None

    class Config:
        orm_mode = True





class ExecutiveBase(BaseModel):
    id: int
    name: str
    title: str

class ExecutiveCreate(ExecutiveBase):
    pass

class Executive(ExecutiveBase):
    # MAKE THIS OPTIONAL BY FOLLOWING WHAT WAS DONE IN FUNDING DETAILS TABLE
    # company: CompanyDetail
    company: Optional[CompanyDetail] = None

    class Config:
        orm_mode = True

class ExecutiveInclusive(Executive):
    pass





class FundingDetailsBase(BaseModel):
    logo: Optional[str] = None
    amount_raised: Optional[str] = Field(alias='amountRaised')
    date_of_funding: str = Field(alias='dateOfFunding')
    funding_round: str = Field(alias='fundingRound')
    ceo: Optional[str] = None
    total_amount_raised: Optional[str] = Field(alias='totalAmountRaised')
    category: Optional[str] = None
    established: Optional[int] = None
    location: Optional[str] = None
    employees: Optional[int] = None
    lead_investor: Optional[str] = Field(alias='leadInvestor')

class FundingDetailsCreate(FundingDetailsBase):
    pass

class FundingDetails(FundingDetailsBase):
    company: Optional[CompanyDetail] = None

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