code = """import json
import re
import os

file_path = locals()['var_functions.query_db:6']

# Initialize data structures
patents_by_year = {}
cpc_count_by_year = {}
years_processed = set()

# Process data in chunks to avoid memory issues
chunk_size = 10000
count = 0

with open(file_path, 'r') as f:
    data = json.load(f)
    
    for record in data:
        # Parse publication date
        pub_date_str = record['publication_date']
        year_match = re.search(r'\d{4}', pub_date_str)
        if year_match:
            year = year_match.group()
            years_processed.add(year)
            
            # Parse CPC codes
            try:
                cpc_data = json.loads(record['cpc'])
                for cpc_entry in cpc_data:
                    cpc_code = cpc_entry['code']
                    
                    # Initialize year if needed
                    if year not in patents_by_year:
                        patents_by_year[year] = 0
                        cpc_count_by_year[year] = {}
                    
                    patents_by_year[year] += 1
                    if cpc_code not in cpc_count_by_year[year]:
                        cpc_count_by_year[year][cpc_code] = 0
                    cpc_count_by_year[year][cpc_code] += 1
            except:
                continue
        
        count += 1

sorted_years = sorted(list(years_processed), key=int)
overall_cpc_codes = set()
for year_data in cpc_count_by_year.values():
    overall_cpc_codes.update(year_data.keys())

print("__RESULT__:")
print(json.dumps({
    "total_records": count,
    "years_available": sorted_years,
    "total_cpc_codes": len(overall_cpc_codes)
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
