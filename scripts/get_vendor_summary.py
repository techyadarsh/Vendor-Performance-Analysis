import pandas as pd
import os
#from sqlalchemy import create_engine
import pandas as pd 
import sqlite3
import time
import logging
from ingestion_db import ingest_db

logging.basicConfig(
    filename="logs/get_vendor_summary.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s",
    filemode="a"
)

def create_connection(conn):
    """ This function will merge the different tables to get the overall vendor summary and adding new columns to resultant data"""
    vendor_sales_summary = pd.read_sql_query("""
    WITH freight_summary AS (
        SELECT
            VendorNumber, 
            SUM(freight) AS freight_cost
        FROM Vendor_invoice
        GROUP BY VendorNumber
    ),
                                            
    purchase_summary AS (
        SELECT              
                                                
                p.vendornumber,
                p.vendorname,
                p.purchaseprice,
                p.brand,
                p.description,
                pp.volume,
                pp.price AS actual_price,
                SUM(p.quantity) AS total_purchased_quantity,
                SUM(p.dollars) AS total_purchased_dollars
        FROM purchases p
        JOIN purchase_prices pp
        ON p.brand = pp.brand
        WHERE p.purchaseprice > 0 
        GROUP BY p.vendornumber, p.vendorname, p.brand, p.description, pp.price, pp.volume
    ),
                                            
    sales_summary AS (
        SELECT  
                s.vendorno,
                s.vendorname,
                s.brand,          
                SUM(s.salesdollars) AS total_sales_dollars,
                SUM(s.salesprice) AS total_sales_price,
                SUM(s.salesquantity) AS total_sales_quantity,
                SUM(s.excisetax) AS total_excise_tax
        FROM sales s
        GROUP BY s.vendorno, s.brand
    )
                                            
    SELECT
        ps.vendornumber,
        ps.vendorname,
        ps.brand,
        ps.description,
        ps.actual_price,
        ps.volume,
        ps.total_purchased_quantity,
        ps.total_purchased_dollars,
        ss.total_sales_dollars,
        ss.total_excise_tax,
        ss.total_sales_price,
        ss.total_sales_quantity, 
        fs.freight_cost
    FROM purchase_summary ps
    LEFT JOIN sales_summary ss
        ON ps.vendornumber = ss.vendorno AND ps.brand = ss.brand
    LEFT JOIN freight_summary fs
        ON ps.vendornumber = fs.vendornumber
    ORDER BY ps.total_purchased_dollars DESC       
    """,conn)
    return vendor_sales_summary


def clean_data(df):
    """ This function will clean the data"""
    # changing datatype to float
    df['volume'] = df['volume'].astype(float)

    # filling missing value with 0
    df.fillna(0,inplace=True)

    # removing space from categorical columns
    df['vendorname'] = df['vendorname'].str.strip()
    df['description'] = df['description'].str.strip()

    # creating new columns for better analysis
    vendor_sales_summary['gross_profit'] = vendor_sales_summary['total_sales_dollars'] - vendor_sales_summary['total_purchased_dollars']
    vendor_sales_summary['profit_margin'] =( vendor_sales_summary['gross_profit'] / vendor_sales_summary['total_sales_dollars'])*100
    vendor_sales_summary['stock_turnover'] = vendor_sales_summary['total_sales_quantity'] / vendor_sales_summary['total_purchased_quantity']
    vendor_sales_summary['sales_to_purchase_ratio'] = vendor_sales_summary['total_sales_dollars'] / vendor_sales_summary['total_purchased_dollars']


    return df
if __name__ == '__main__':
    # creating database connection
    conn = sqlite3.connect('invetory_database.db')

    logging.info('Creating Vendor Summary Table...')
    summary_df = create_vendor_summary(conn)
    logging.info(summary_df.head())

    logging.info('Cleaning data...')
    clean_df = clean_data(summary_df)
    logging.info(clean_df.head())

    logging.info('Ingesting data..')
    ingest_db(clean_df,'vendor_sales_summary',conn)
    logging.info('Completed')

                          
