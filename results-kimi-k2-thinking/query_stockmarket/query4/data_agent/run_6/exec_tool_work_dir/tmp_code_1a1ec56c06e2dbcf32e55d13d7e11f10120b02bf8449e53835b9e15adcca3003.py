code = """import pandas as pd

# Connect to stockinfo database and get NYSE non-ETF stocks
import sqlite3
conn = sqlite3.connect('stockinfo_database')
query = """
SELECT Symbol, "Company Description" 
FROM stockinfo 
WHERE "Listing Exchange" = 'N' 
  AND ETF = 'N'
"""

nyse_stocks = pd.read_sql_query(query, conn)
conn.close()

print(f"Found {len(nyse_stocks)} NYSE non-ETF stocks")
print("First few:", nyse_stocks.head())

# Save to JSON
nyse_stocks.to_json('nyse_stocks.json', orient='records')
print('__RESULT__:')
print('nyse_stocks.json')"""

env_args = {'var_functions.list_db:0': 'file_storage/functions.list_db:0.json', 'var_functions.query_db:2': [{'Symbol': 'AEFC', 'Company Description': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.', 'ETF': 'N'}, {'Symbol': 'AIN', 'Company Description': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.', 'ETF': 'N'}, {'Symbol': 'AIV', 'Company Description': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.', 'ETF': 'N'}, {'Symbol': 'AIZP', 'Company Description': 'Assurant, Inc. specializes in providing a diverse range of insurance products and services, focusing on lifestyle and housing solutions to protect what matters most to their customers.', 'ETF': 'N'}, {'Symbol': 'AJRD', 'Company Description': 'Aerojet Rocketdyne Holdings, Inc. specializes in developing advanced propulsion systems and aerospace technologies, playing a crucial role in powering rockets and missiles for both defense and space exploration.', 'ETF': 'N'}, {'Symbol': 'AL', 'Company Description': 'Air Lease Corporation specializes in leasing commercial aircraft to airlines worldwide, providing them with flexible fleet solutions and financial support.', 'ETF': 'N'}, {'Symbol': 'AMN', 'Company Description': 'AMN Healthcare Services Inc. specializes in providing workforce solutions and staffing services to healthcare facilities, ensuring they have access to the skilled professionals necessary for quality patient care.', 'ETF': 'N'}, {'Symbol': 'AMP', 'Company Description': 'Ameriprise Financial, Inc. offers comprehensive financial services, specializing in wealth management, asset management, and insurance solutions to help clients plan and achieve their financial goals.', 'ETF': 'N'}, {'Symbol': 'AMT', 'Company Description': 'American Tower Corporation is a leading real estate investment trust that specializes in owning, operating, and developing wireless and broadcast communication towers across the globe.', 'ETF': 'N'}, {'Symbol': 'ARD', 'Company Description': 'Ardagh Group S.A. specializes in manufacturing and supplying sustainable packaging solutions, with a focus on glass and metal containers for leading brands across various industries.', 'ETF': 'N'}]}

exec(code, env_args)
