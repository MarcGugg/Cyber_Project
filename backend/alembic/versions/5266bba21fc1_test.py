"""test

Revision ID: 5266bba21fc1
Revises: 
Create Date: 2024-01-10 19:52:58.597612

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5266bba21fc1'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table('categories',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('category', sa.String(), nullable=False),
        sa.Column('logo_file', sa.String()),
        sa.Column('logo_url', sa.String()),
        sa.Column('logo_old', sa.String()),
        sa.Column('logo_new', sa.String()),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('funding_details',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('logo', sa.String()),
        sa.Column('amount_raised', sa.String()),
        sa.Column('date_of_funding', sa.String()),
        sa.Column('funding_round', sa.String()),
        sa.Column('ceo', sa.String()),
        sa.Column('total_amount_raised', sa.String()),
        sa.Column('category', sa.String()),
        sa.Column('established', sa.Integer()),
        sa.Column('location', sa.String()),
        sa.Column('employees', sa.Integer()),
        sa.Column('lead_investor', sa.String()),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('company_detail',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('company', sa.String(), nullable=False),
        sa.Column('company_url', sa.String(), nullable=False),
        sa.Column('linkedin_url', sa.String(), nullable=True),
        sa.Column('year_founded', sa.Integer(), nullable=True),
        sa.Column('employees', sa.Integer(), nullable=True),
        sa.Column('headcount_direction', sa.String(), nullable=True),
        sa.Column('hq_country', sa.String(), nullable=True),
        sa.Column('hq_city', sa.String(), nullable=True),
        sa.Column('subcategory', sa.String(), nullable=True),
        sa.Column('customer_industries', sa.String(), nullable=True),
        sa.Column('customer_size', sa.String(), nullable=True),
        sa.Column('customer_count', sa.String(), nullable=True),
        sa.Column('tech_stack', sa.String(), nullable=True),
        sa.Column('product_integrations', sa.String(), nullable=True),
        sa.Column('pricing', sa.String(), nullable=True),
        sa.Column('industry_awards', sa.String(), nullable=True),
        sa.Column('industry_events', sa.String(), nullable=True),
        sa.Column('category_id', sa.Integer(), sa.ForeignKey('categories.id')),
        sa.Column('category', sa.String()),
        
        sa.ForeignKeyConstraint(['category_id'], ['categories.id']),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('executives',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('company_detail_id', sa.Integer(), sa.ForeignKey('company_detail.id')),

        sa.ForeignKeyConstraint(['company_detail_id'], ['company_detail.id']),
        sa.PrimaryKeyConstraint('id')       
    )
    
    
    op.create_table('corporate_customers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('vendor_id', sa.Integer(), sa.ForeignKey('company_detail.id')),

        sa.ForeignKeyConstraint(['vendor_id'], ['company_detail.id']),
        sa.PrimaryKeyConstraint('id')                
    )

    op.create_table('industry_awards',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('year', sa.Integer()),
        sa.Column('issuing_organization', sa.String()),
        sa.Column('company_detail_id', sa.Integer(), sa.ForeignKey('company_detail.id')),

        sa.ForeignKeyConstraint(['company_detail_id'], ['company_detail.id']),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('products',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('company_detail_id', sa.Integer(), sa.ForeignKey('company_detail.id')),
        
        sa.ForeignKeyConstraint(['company_detail_id'], ['company_detail.id']),
        sa.PrimaryKeyConstraint('id')                
    )

    op.add_column('funding_details', sa.Column('company_detail_id', sa.Integer(), sa.ForeignKey('company_detail.id'))) #this line is necessary for the seeders to work
    
    op.add_column('company_detail', sa.Column('category_id', sa.Integer(), sa.ForeignKey('categories.id')))

    # op.add_column('executives', sa.Column('company_detail_id', sa.Integer(), sa.ForeignKey('company_detail.id')))
    # op.add_column('company_detail', sa.Column('funding_details_id', sa.Integer(), sa.ForeignKey('funding_details.id')))

    # op.create_foreign_key('fk_company_detail_category_id', 'company_detail', 'categories', ['category_id'], ['id'])
    # op.create_foreign_key('fk_company_detail_funding_details_id', 'company_detail', 'funding_details', ['funding_details_id'], ['id'])


def downgrade() -> None:
    op.drop_table('products')
    op.drop_table('industry_awards')
    op.drop_table('corporate_customers')
    op.drop_table('executives')
    op.drop_table('company_detail')
    op.drop_table('funding_details')
    op.drop_table('categories')
    
    # op.drop_column('funding_details', 'company_detail_id')
    
    # op.drop_column('company_detail', 'category_id')
    # op.drop_column('company_detail', 'funding_details_id')