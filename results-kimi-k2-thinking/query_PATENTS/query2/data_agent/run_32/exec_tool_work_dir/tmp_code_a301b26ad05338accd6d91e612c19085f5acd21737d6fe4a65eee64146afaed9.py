code = """import pandas as pd
import numpy as np
import json
import re
from datetime import datetime

# Process the German patents data directly from the query result
german_patents = var_functions.query_db:12

# Parse dates and extract CPC level 4 data
def parse_grant_date(date_str):
    if not date_str:
        return None
    try:
        # Extract month and year
        date_str = str(date_str).lower()
        year_match = re.search(r'(\d{4})', date_str)
        if year_match:
            year = int(year_match.group(1))
            if year == 2019:
                # Check for second half of 2019
                months_2nd_half = ['july', 'august', 'september', 'october', 'november', 'december']
                for i, month in enumerate(months_2nd_half, 7):
                    if month in date_str:
                        return year, i
        return None
    except:
        return None

def get_cpc_level_4(code):
    if not code:
        return None
    try:
        # Extract main part before /
        main_part = str(code).split('/')[0]
        # Clean up alphanumeric characters
        clean_part = re.sub(r'[^A-Z0-9]$', '', main_part)
        return clean_part
    except:
        return None

# Filter for second half 2019 and extract CPC data
filtered_patents = []
cpc_counts_by_month = {}

for patent in german_patents:
    grant_info = parse_grant_date(patent.get('grant_date'))
    if grant_info:
        year, month = grant_info
        cpc_data = patent.get('cpc', '[]')
        try:
            cpc_list = json.loads(cpc_data) if isinstance(cpc_data, str) else cpc_data
            for cpc_item in cpc_list:
                cpc_code = cpc_item.get('code')
                if cpc_code:
                    level_4 = get_cpc_level_4(cpc_code)
                    if level_4:
                        # Count by month
                        key = (year, month, level_4)
                        cpc_counts_by_month[key] = cpc_counts_by_month.get(key, 0) + 1
                        
                        filtered_patents.append({
                            'grant_date': patent.get('grant_date'),
                            'cpc_full': cpc_code,
                            'cpc_level_4': level_4,
                            'year': year,
                            'month': month
                        })
        except:
            continue

print(f'Processed {len(filtered_patents)} CPC entries from German patents granted in 2019')
print(f'Unique CPC Level 4 codes: {len(set(p["cpc_level_4"] for p in filtered_patents))}')
print('Sample data:', filtered_patents[:3])"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': 'Date parsing and CPC level 4 extraction functions ready', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:16': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0'}]}

exec(code, env_args)
