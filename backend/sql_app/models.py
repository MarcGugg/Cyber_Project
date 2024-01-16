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
    #company = db.Column(db.String(150), db.ForeignKey('companydetail.company'), primary_key=True)
    company = Column(String(150), primary_key=True)
    amount_raised = Column(String(150))
    date_of_funding = Column(String(150), primary_key=True)
    funding_round = Column(String(150),primary_key=True)
    ceo = Column(String(150))
    total_amount_raised = Column(String(150))
    category = Column(String(150))
    established = Column(Integer)
    location = Column(String(150))
    employees = Column(Integer)
    lead_investor = Column(String(150))
    #round_url = db.Column(db.String(150))
    # company_id = Column(Integer, ForeignKey('company_detail.id'))
    company_detail_id = Column(Integer, ForeignKey('company_detail.id'))


    company_detail = relationship('CompanyDetail', back_populates='funding_details', foreign_keys=[company_detail_id])
    # company_detail = relationship('CompanyDetail', back_populates='funding_details', foreign_keys=[company_detail_id], remote_side='CompanyDetail.id')


    def to_dict(self):
        return {
            'id': self.id,
            'logo': self.logo,
            'company': self.company,
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
            'company': self.company,
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
            'companyDetail': self.company_detail.to_dict()
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
    corporate_customers = Column(String, index=True, nullable=True)
    customer_size = Column(String, index=True, nullable=True)
    customer_count = Column(String, index=True, nullable=True)
    tech_stack = Column(String, index=True, nullable=True)
    product_integrations = Column(String, index=True, nullable=True)
    pricing = Column(String, index=True, nullable=True)
    industry_awards = Column(String, index=True, nullable=True)
    industry_events = Column(String, index=True, nullable=True)
    executive_team = Column(String, index=True, nullable=True)
    # category = Column(String, index=True, nullable=True) #this will be a relationship

    category_id = Column(Integer, ForeignKey('categories.id'))
    # funding_details_id = Column(Integer, ForeignKey('funding_details.id'))
    
    category = relationship('Category', back_populates='company_details', foreign_keys=[category_id])
    funding_details = relationship('FundingDetails', back_populates='company_detail')

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
            'industryAwards': self.industry_awards,
            'industryEvents': self.industry_events,
            'executiveTeam': self.executive_team
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
            'industryAwards': self.industry_awards,
            'industryEvents': self.industry_events,
            'executiveTeam': self.executive_team,
            'category': self.category.to_dict(),
            'fundingDetails': [funding.to_dict() for funding in self.funding_details]
        }



# Category.company_details = relationship('CompanyDetail', back_populates='category')
# CompanyDetail.category = relationship('Category', back_populates='company_details')

# FundingDetails.company = relationship('CompanyDetail', back_populates='funding_details')
# CompanyDetail.funding_details = relationship('FundingDetails', back_populates='company')

