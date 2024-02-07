from faker import Faker
from sqlalchemy.orm import Session
from sql_app.models import CompanyDetail, FundingDetails, Category, Executive
from sql_app.models import CorporateCustomer, IndustryAward
import random

fake = Faker()

def seed_data(db: Session):
    for _ in range(10):

        category = Category(
            category=fake.word(),
            logo_file=fake.file_name(extension="png"),
            logo_url=fake.url(),
            logo_old=fake.url(),
            logo_new=fake.url(),
        )

        db.add(category)
    
    db.commit()

    existing_categories = db.query(Category).all()

    for _ in range(10):  # Adjust the number as needed
        
        curr_category = fake.random_element(existing_categories)

        company_detail = CompanyDetail(
            company=fake.company(),
            company_url=fake.url(),
            linkedin_url=fake.url() if fake.boolean(chance_of_getting_true=50) else None,
            category=curr_category,
            year_founded=fake.random_int(min=1900, max=2022),
            employees=fake.random_int(min=1, max=10000),
            headcount_direction=fake.random_element(elements=("Up", "Down", "Stable")),
            hq_country=fake.country(),
            hq_city=fake.city(),
            subcategory=fake.random_element(elements=("Subcategory1", "Subcategory2", "Subcategory3")),
            customer_industries=fake.text(),
            customer_size=fake.random_element(elements=("Small", "Medium", "Large")),
            customer_count=fake.random_int(min=1, max=1000),
            tech_stack=fake.text(),
            product_integrations=fake.text(),
            pricing=fake.text(),
            # industry_awards=fake.text(),
            industry_events=fake.text()
        )

        db.add(company_detail)
    
    db.commit()

    existing_company_details = db.query(CompanyDetail).all()

    for _ in range(10):

        company_detail = fake.random_element(existing_company_details)
    
        funding_details = FundingDetails(
            logo=fake.url(),  # Assuming logo is a URL, adjust accordingly
            amount_raised=fake.random_int(min=100000, max=10000000),
            date_of_funding=fake.date_this_decade(),
            funding_round=fake.random_element(elements=("Seed", "Series A", "Series B", "Series C")),
            ceo=fake.name(),
            total_amount_raised=fake.random_int(min=100000, max=100000000),
            category=fake.random_element(elements=("Category1", "Category2", "Category3")),
            established=fake.random_int(min=1900, max=2022),
            location=fake.city(),
            employees=fake.random_int(min=1, max=10000),
            lead_investor=fake.name(),
            company=company_detail
        )

        db.add(funding_details)
    

    db.commit()
    

    for _ in range(len(existing_company_details)):
        titles = ['CEO', 'CFO', 'President']
        random_company = fake.random_element(existing_company_details)

        for title in titles:

            new_executive = Executive(
                name = fake.name(),
                title = title,
                company = random_company
            )

            db.add(new_executive)

        existing_company_details.remove(random_company)

    db.commit()

    
    
    existing_company_details = db.query(CompanyDetail).all()
    for _ in range(10):

        corporate_customer = CorporateCustomer(
            name = fake.company(),
            vendor = fake.random_element(existing_company_details)
        )

        db.add(corporate_customer)
    
    db.commit()


    award_categories = ['Best', 'Outstanding', 'Exceptional', 'Remarkable', 'Innovative', 'Creative', 'Inspiring', 'Top', 'Superb']

# Define a list of possible award types
    award_types = ['Achievement', 'Performance', 'Excellence', 'Contribution', 'Innovation', 'Leadership', 'Service', 'Collaboration', 'Impact']


    for _ in range(10):
        award_category = fake.random_element(award_categories)
        award_type = fake.random_element(award_types)

        new_award = IndustryAward(
            name = award_category + ' ' + award_type,
            year = random.randint(1980, 2024),
            issuing_organization = fake.company(),
            company = fake.random_element(existing_company_details)
        )

        db.add(new_award)

    db.commit()
        
if __name__ == "__main__":
    # This block ensures that the seeding script is executed only when run directly
    from sql_app.database import SessionLocal  # Import your SQLAlchemy SessionLocal
    
    db = SessionLocal()
    seed_data(db)