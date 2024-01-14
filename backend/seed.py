from faker import Faker
from sqlalchemy.orm import Session
from sql_app.models import CompanyDetail, FundingDetails, Category

fake = Faker()

def seed_data(db: Session):
    
    for _ in range(10):  # Adjust the number as needed
        
        company_detail = CompanyDetail(
            company=fake.company(),
            company_url=fake.url(),
            linkedin_url=fake.url() if fake.boolean(chance_of_getting_true=50) else None,
            year_founded=fake.random_int(min=1900, max=2022),
            employees=fake.random_int(min=1, max=10000),
            headcount_direction=fake.random_element(elements=("Up", "Down", "Stable")),
            hq_country=fake.country(),
            hq_city=fake.city(),
            subcategory=fake.random_element(elements=("Subcategory1", "Subcategory2", "Subcategory3")),
            customer_industries=fake.text(),
            corporate_customers=fake.text(),
            customer_size=fake.random_element(elements=("Small", "Medium", "Large")),
            customer_count=fake.random_int(min=1, max=1000),
            tech_stack=fake.text(),
            product_integrations=fake.text(),
            pricing=fake.text(),
            industry_awards=fake.text(),
            industry_events=fake.text(),
            executive_team=fake.text(),
        )

        db.add(company_detail)
    
    for _ in range(10):
    
        category = Category(
            category=fake.word(),
            logo_file=fake.file_name(extension="png"),
            logo_url=fake.url(),
            logo_old=fake.url(),
            logo_new=fake.url(),
        )

        db.add(category)

    for _ in range(10):
    
        funding_details = FundingDetails(
            logo=fake.url(),  # Assuming logo is a URL, adjust accordingly
            company=fake.company(),
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
        )

        db.add(funding_details)

    
    db.commit()
        
if __name__ == "__main__":
    # This block ensures that the seeding script is executed only when run directly
    from sql_app.database import SessionLocal  # Import your SQLAlchemy SessionLocal
    
    db = SessionLocal()
    seed_data(db)