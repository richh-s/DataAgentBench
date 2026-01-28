code = """import json
import re
from collections import defaultdict
from datetime import datetime

# Load the publication data
file_path = 'file_storage/functions.query_db:26.json'
with open(file_path, 'r') as f:
    publications = json.load(f)

print(f"Loaded {len(publications)} publications")

# Sample some dates to understand the format
sample_dates = []
for i, pub in enumerate(publications):
    if i < 20:
        sample_dates.append(pub['publication_date'])
    else:
        break

print("Sample publication dates:")
for date in sample_dates:
    print(f"  '{date}'")

# Function to extract year from various date formats
def extract_year(date_str):
    if not date_str:
        return None
    
    # Try to find a 4-digit year at the end
    match = re.search(r'(\d{4})\s*$', date_str.strip())
    if match:
        year_str = match.group(1)
        # Validate it's a reasonable year for patents (1970-2030)
        year = int(year_str)
        if 1970 <= year <= 2030:
            return str(year)
    
    return None

# Test the year extraction
print("\nExtracted years from sample dates:")
for date in sample_dates:
    year = extract_year(date)
    print(f"  '{date}' -> {year}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['publicationinfo'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:14': {'file_exists': False, 'checked_paths': ['/tmp/tmp_result_6.json', 'tmp_result_6.json', '/tmp/tmptmp_result_6.json']}, 'var_functions.execute_python:20': {'file_exists': True, 'num_records': 277813, 'first_record_keys': ['cpc', 'year']}, 'var_functions.execute_python:24': {'total_publications': 277813, 'available_years': 218, 'first_10_years': [' 1st', ' 2nd', ' 3rd', ' 4th', ' 5th', ' 6th', ' 7th', ' 8th', ' 9th', '10th'], 'last_10_years': ['23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st', 'Date'], 'total_cpc_groups': 9960, 'level_5_codes_count': 7247, 'sample_level_5_codes': ['C01B33', 'C01B35', 'H01M10', 'C01G45', 'Y02E60', 'H01M4', 'F16H47', 'F16H37', 'F16H3', 'B29C70']}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
