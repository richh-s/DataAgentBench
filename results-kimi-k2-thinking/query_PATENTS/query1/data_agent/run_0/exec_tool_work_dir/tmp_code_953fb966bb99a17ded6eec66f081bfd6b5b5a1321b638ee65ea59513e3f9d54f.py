code = """import json
import re
import pandas as pd
import numpy as np
from collections import defaultdict

# Load the publication data
storage_key = 'var_functions.query_db:8'
file_path = locals().get(storage_key, None)

if file_path is None:
    result = {'error': 'File path not accessible'}
else:
    # Read the data
    with open(file_path, 'r') as f:
        publications = json.load(f)
    
    # Aggregate directly to yearly counts per CPC code
    cpc_year_counts = defaultdict(lambda: defaultdict(int))
    years_set = set()
    
    print('Processing publications...')
    processed = 0
    for pub in publications:
        cpc_json = pub.get('cpc', '[]')
        pub_date = pub.get('publication_date', '')
        
        # Get year from date
        year = None
        if pub_date:
            match = re.search(r'(\d{4})', pub_date)
            if match:
                year = int(match.group(1))
        
        if not year:
            continue
        
        years_set.add(year)
        
        # Parse CPC codes
        try:
            if isinstance(cpc_json, str):
                cpc_list = json.loads(cpc_json)
            else:
                cpc_list = cpc_json
                
            for cpc_item in cpc_list:
                code = cpc_item.get('code', '')
                # Check if level 5: has subgroup 
                if code and '/' in code:
                    cpc_year_counts[code][year] += 1
        except:
            continue
        
        processed += 1
        if processed % 50000 == 0:
            print(f'  Processed {processed}/{len(publications)} publications')
    
    print(f'Total processed: {processed}')
    
    # Convert to sorted years
    years = sorted(list(years_set))
    print(f'Years: {years}')
    
    # Create matrix and calculate EMAs
    alpha = 0.2
    best_2022_codes = []
    
    print(f'Calculating EMA for {len(cpc_year_counts)} CPC codes...')
    
    for cpc, year_counts in cpc_year_counts.items():
        # Get counts for all years
        counts = [year_counts.get(year, 0) for year in years]
        
        # Calculate EMA
        ema_values = []
        ema_prev = counts[0]
        ema_values.append(ema_prev)
        
        for i in range(1, len(counts)):
            ema_current = alpha * counts[i] + (1 - alpha) * ema_prev
            ema_values.append(ema_current)
            ema_prev = ema_current
        
        # Check if best year is 2022
        if 2022 in years:
            max_ema_index = np.argmax(ema_values)
            if years[max_ema_index] == 2022:
                best_2022_codes.append(cpc)
    
    print(f'CPC codes with best year 2022: {len(best_2022_codes)}')
    
    result = {
        'cpc_codes_best_2022': best_2022_codes,
        'count': len(best_2022_codes),
        'years_range': f"{min(years)} to {max(years)}"
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': [{'total': '277813'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:24': {'total_publications': 277813, 'extracted_pairs': 103409, 'sample': [{'cpc_code': 'C01B33/00', 'year': 2021}, {'cpc_code': 'C01B35/00', 'year': 2021}, {'cpc_code': 'H01M10/0565', 'year': 2021}, {'cpc_code': 'H01M10/0562', 'year': 2021}, {'cpc_code': 'C01G45/006', 'year': 2021}, {'cpc_code': 'H01M10/0566', 'year': 2021}, {'cpc_code': 'H01M10/052', 'year': 2021}, {'cpc_code': 'C01P2002/76', 'year': 2021}, {'cpc_code': 'C01G45/006', 'year': 2021}, {'cpc_code': 'Y02E60/10', 'year': 2021}]}, 'var_functions.query_db:26': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}], 'var_functions.query_db:28': [{'symbol': 'A01B1/00', 'level': '7.0'}, {'symbol': 'A01B1/02', 'level': '8.0'}, {'symbol': 'A01B1/022', 'level': '9.0'}, {'symbol': 'A01B1/024', 'level': '9.0'}, {'symbol': 'A01B1/026', 'level': '9.0'}, {'symbol': 'A01B1/028', 'level': '9.0'}, {'symbol': 'A01B1/04', 'level': '9.0'}, {'symbol': 'A01B1/06', 'level': '8.0'}, {'symbol': 'A01B1/065', 'level': '9.0'}, {'symbol': 'A01B1/08', 'level': '9.0'}]}

exec(code, env_args)
