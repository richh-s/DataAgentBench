code = """import json
import pandas as pd
import re
from datetime import datetime

# Read the German patents data
file_path = locals()['var_functions.query_db:12']
with open(file_path, 'r') as f:
    patents_data = json.load(f)

# Filter for German patents granted in second half of 2019
month_map = {
    'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
    'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
}

german_patents = []
for patent in patents_data:
    patents_info = patent.get('Patents_info', '')
    grant_date = patent.get('grant_date', '')
    cpc = patent.get('cpc', '[]')
    title_localized = patent.get('title_localized', '[]')
    publication_date = patent.get('publication_date', '')
    
    # Check if it's a German patent
    if 'DE-' in patents_info:
        # Check if it's 2019
        if '2019' in grant_date:
            # Try to extract month
            month = None
            grant_date_lower = grant_date.lower()
            
            for month_name, month_num in month_map.items():
                if month_name in grant_date_lower:
                    month = month_num
                    break
            
            # If we found a month and it's in second half (July-Dec)
            if month and month >= 7:
                # Extract CPC codes
                try:
                    cpc_list = json.loads(cpc) if isinstance(cpc, str) else cpc
                    cpc_codes = [item.get('code') for item in cpc_list if item.get('code')]
                except:
                    cpc_codes = []
                
                # Extract title
                try:
                    title_list = json.loads(title_localized) if isinstance(title_localized, str) else title_localized
                    if title_list and len(title_list) > 0:
                        # Try to get German title first, then English, then any
                        title = ''
                        for lang_pref in ['de', 'en']:
                            for t in title_list:
                                if t.get('language') == lang_pref and t.get('text'):
                                    title = t.get('text')
                                    break
                            if title:
                                break
                        if not title and title_list[0].get('text'):
                            title = title_list[0].get('text')
                    else:
                        title = ''
                except:
                    title = ''
                
                if cpc_codes:  # Only add if there are CPC codes
                    german_patents.append({
                        'patents_info': patents_info,
                        'grant_date': grant_date,
                        'grant_month': month,
                        'cpc_codes': cpc_codes,
                        'title': title,
                        'publication_date': publication_date
                    })

print('__RESULT__:')
print(json.dumps({
    'total_german_patents_h2_2019': len(german_patents),
    'sample_patents': german_patents[:3]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'total_german_patents': 1, 'sample_patents': [{'patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'grant_month': 11, 'cpc_codes': ['B41F21/102', 'B41F22/00', 'B41F21/00']}]}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
