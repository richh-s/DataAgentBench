code = """import json
import pandas as pd
import re
from datetime import datetime

# Read the query results
file_path = var_functions.query_db:5
with open(file_path, 'r') as f:
    patents_data = json.load(f)

# Filter for German patents and second half of 2019
german_patents = []
for patent in patents_data:
    patents_info = patent.get('Patents_info', '')
    grant_date = patent.get('grant_date', '')
    cpc = patent.get('cpc', '[]')
    
    # Check if it's a German patent
    if 'DE-' in patents_info:
        # Parse grant date to check if it's in second half of 2019
        try:
            # Extract year from grant date
            year_match = re.search(r'2019', grant_date)
            if year_match:
                # Try to parse the full date
                date_patterns = [
                    r'(\d{1,2})[\w]*\s+(\w+)\s+2019',
                    r'(\w+)\s+(\d{1,2})[\w]*,?\s+2019',
                    r'2019\s+on\s+(\w+)\s+(\d{1,2})[\w]*',
                    r'dated\s+(\w+)\s+(\d{1,2})[\w]*,?\s+2019'
                ]
                
                parsed_date = None
                for pattern in date_patterns:
                    match = re.search(pattern, grant_date, re.IGNORECASE)
                    if match:
                        # Try to construct a date string
                        if len(match.groups()) == 2:
                            day_or_month1, day_or_month2 = match.groups()
                            # Try to identify which is day and which is month
                            month_names = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 
                                         'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
                            month = None
                            day = None
                            
                            for i, name in enumerate(month_names):
                                if day_or_month1.lower().startswith(name):
                                    month = i + 1
                                    day = int(day_or_month2) if day_or_month2.isdigit() else 1
                                    break
                                elif day_or_month2.lower().startswith(name):
                                    month = i + 1
                                    day = int(day_or_month1) if day_or_month1.isdigit() else 1
                                    break
                            
                            if month and day:
                                parsed_date = datetime(2019, month, day)
                                break
                
                if parsed_date and parsed_date >= datetime(2019, 7, 1):
                    # Extract CPC codes
                    try:
                        cpc_list = json.loads(cpc) if isinstance(cpc, str) else cpc
                        cpc_codes = [item.get('code') for item in cpc_list if item.get('code')]
                    except:
                        cpc_codes = []
                    
                    german_patents.append({
                        'patents_info': patents_info,
                        'grant_date': grant_date,
                        'grant_date_parsed': parsed_date,
                        'cpc_codes': cpc_codes
                    })
        except Exception as e:
            continue

print('__RESULT__:')
print(json.dumps({
    'total_german_patents': len(german_patents),
    'sample_patents': german_patents[:3]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
