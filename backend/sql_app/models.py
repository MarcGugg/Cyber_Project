from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)

#     items = relationship("Item", back_populates="owner")


# class Item(Base):
#     __tablename__ = "items"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))

#     owner = relationship("User", back_populates="items")



# TODO make a seperate industry events table? Relationship w CompanyDetail
# TODO implement products table. relationship with companies


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    category = Column(String(150), primary_key=True)
    logo_file = Column(String(150))
    logo_url = Column(String(150))
    logo_old = Column(String(150))
    logo_new = Column(String(150))

    company_details = relationship('CompanyDetail', back_populates='category')

    def to_dict(self):
        return {
            'id': self.id,
            'category': self.category,
            'logoFile': self.logo_file,
            'logoUrl': self.logo_url,
            'logoOld': self.logo_old,
            'logoNew': self.logo_new
        }

class FundingDetails(Base):
    __tablename__ = 'funding_details'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    logo = Column(String(150))
    amount_raised = Column(String(150))
    date_of_funding = Column(String(150))
    funding_round = Column(String(150))
    ceo = Column(String(150))
    total_amount_raised = Column(String(150))
    category = Column(String(150))
    established = Column(Integer)
    location = Column(String(150))
    employees = Column(Integer)
    lead_investor = Column(String(150))

    company_detail_id = Column(Integer, ForeignKey('company_detail.id'))


    company = relationship('CompanyDetail', back_populates='funding_details', foreign_keys=[company_detail_id])
   

    def to_dict(self):
        return {
            'id': self.id,
            'logo': self.logo,
            'amountRaised': self.amount_raised,
            'dateOfFunding': self.date_of_funding,
            'fundingRound': self.funding_round,
            'ceo': self.ceo,
            'totalAmountRaised': self.total_amount_raised,
            'category': self.category,
            'established': self.established,
            'location': self.location,
            'employees': self.employees,
            'leadInvestor': self.lead_investor
        }
    def to_dict_inclusive(self):
        return {
            'id': self.id,
            'logo': self.logo,
            'amountRaised': self.amount_raised,
            'dateOfFunding': self.date_of_funding,
            'fundingRound': self.funding_round,
            'ceo': self.ceo,
            'totalAmountRaised': self.total_amount_raised,
            'category': self.category,
            'established': self.established,
            'location': self.location,
            'employees': self.employees,
            'leadInvestor': self.lead_investor,
            'company': self.company.to_dict()
        }
    

class CompanyDetail(Base):
    __tablename__ = "company_detail"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    company = Column(String, index=True, nullable=False)
    company_url = Column(String, index=True, nullable=False)
    linkedin_url = Column(String, index=True, nullable=True)
    year_founded = Column(Integer, index=True, nullable=True)
    employees = Column(Integer, index=True, nullable=True)
    headcount_direction = Column(String, index=True, nullable=True)
    hq_country = Column(String, index=True, nullable=True)
    hq_city = Column(String, index=True, nullable=True)
    subcategory = Column(String, index=True, nullable=True)
    customer_industries = Column(String, index=True, nullable=True) #this may also be a relationship?
    customer_size = Column(String, index=True, nullable=True)
    customer_count = Column(String, index=True, nullable=True)
    tech_stack = Column(String, index=True, nullable=True)
    product_integrations = Column(String, index=True, nullable=True)
    pricing = Column(String, index=True, nullable=True)
    # industry_awards = Column(String, index=True, nullable=True)
    industry_events = Column(String, index=True, nullable=True)


    category_id = Column(Integer, ForeignKey('categories.id'))

    
    category = relationship('Category', back_populates='company_details', foreign_keys=[category_id])
    funding_details = relationship('FundingDetails', back_populates='company')
    
    executives = relationship('Executive', back_populates='company')
 
    corporate_customers = relationship('CorporateCustomer', back_populates='vendor')

    industry_awards = relationship('IndustryAward', back_populates='company')

    products = relationship('Product', back_populates='company')

    def to_dict(self):
        return {
            'id': self.id,
            'company': self.company,
            'companyUrl': self.company_url,
            'linkedinUrl': self.linkedin_url,
            'yearFounded': self.year_founded,
            'employees': self.employees,
            'headcountDirection': self.headcount_direction,
            'hqCountry': self.hq_country,
            'hqCity': self.hq_city,
            'subcategory': self.subcategory,
            'customerIndustries': self.customer_industries,
            'corporateCustomers': self.corporate_customers,
            'customerSize': self.customer_size,
            'customerCount': self.customer_count,
            'techStack': self.tech_stack,
            'productIntegrations': self.product_integrations,
            'pricing': self.pricing,
            # 'industryAwards': self.industry_awards,
            'industryEvents': self.industry_events
        }
    
    def to_dict_inclusive(self):
        return {
            'id': self.id,
            'company': self.company,
            'companyUrl': self.company_url,
            'linkedinUrl': self.linkedin_url,
            'yearFounded': self.year_founded,
            'employees': self.employees,
            'headcountDirection': self.headcount_direction,
            'hqCountry': self.hq_country,
            'hqCity': self.hq_city,
            'subcategory': self.subcategory,
            'customerIndustries': self.customer_industries,
            'corporateCustomers': self.corporate_customers,
            'customerSize': self.customer_size,
            'customerCount': self.customer_count,
            'techStack': self.tech_stack,
            'productIntegrations': self.product_integrations,
            'pricing': self.pricing,
            'industryAwards': [award.to_dict() for award in self.industry_awards],
            'industryEvents': self.industry_events,
            'executives': [executive.to_dict() for executive in self.executives],
            'category': self.category.to_dict(),
            'fundingDetails': [funding.to_dict() for funding in self.funding_details],
            'corporateCustomers': [customer.to_dict() for customer in self.corporate_customers],
            'products': [product.to_dict() for product in self.products]
        }
    
class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, nullable=False)

    company_detail_id = Column(Integer, ForeignKey('company_detail.id'))

    company = relationship('CompanyDetail', back_populates='products', foreign_keys=[company_detail_id])

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
    
    def to_dict_inclusive(self):
        return {
            'id': self.id,
            'name': self.name,
            'company': self.company.to_dict()
        }


class IndustryAward(Base):
    __tablename__ = 'industry_awards'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, nullable=False)
    year = Column(Integer, index=True, nullable=True)
    issuing_organization = Column(String, index=True, nullable=True)
    
    company_detail_id = Column(Integer, ForeignKey('company_detail.id'))

    company = relationship('CompanyDetail', back_populates='industry_awards', foreign_keys=[company_detail_id])

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'year': self.year,
            'issuingOrg': self.issuing_organization
        }
    
    def to_dict_inclusive(self):
        return {
            'id': self.id,
            'name': self.name,
            'year': self.year,
            'issuingOrg': self.issuing_organization,
            'company': self.company.to_dict()
        }


class Executive(Base):
    __tablename__ = 'executives'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, nullable=False)
    title = Column(String, index=True, nullable=False)
    company_detail_id = Column(Integer, ForeignKey('company_detail.id'))


    company = relationship('CompanyDetail', back_populates='executives', foreign_keys=[company_detail_id])

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'title': self.title
        }
    
    def to_dict_inclusive(self):
        return {
            'id': self.id,
            'name': self.name,
            'title': self.title,
            'company': self.company.to_dict()
        }



    
class CorporateCustomer(Base):
    __tablename__ = 'corporate_customers'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, nullable=False)
    vendor_id = Column(Integer, ForeignKey('company_detail.id'))

    vendor = relationship('CompanyDetail', back_populates='corporate_customers', foreign_keys=[vendor_id])

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
    
    def to_dict_inclusive(self):
        return {
            'id': self.id,
            'name': self.name,
            'vendor': self.vendor.to_dict()
        }



# Category.company_details = relationship('CompanyDetail', back_populates='category')
# CompanyDetail.category = relationship('Category', back_populates='company_details')

# FundingDetails.company = relationship('CompanyDetail', back_populates='funding_details')
# CompanyDetail.funding_details = relationship('FundingDetails', back_populates='company')

