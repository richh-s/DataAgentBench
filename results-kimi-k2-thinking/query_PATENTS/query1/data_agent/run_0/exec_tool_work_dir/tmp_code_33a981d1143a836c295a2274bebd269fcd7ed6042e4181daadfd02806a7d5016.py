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
    
    # Extract CPC codes and years
    extracted_data = []
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
                    extracted_data.append({'cpc_code': code, 'year': year})
        except:
            continue
    
    # Create DataFrame
    df = pd.DataFrame(extracted_data)
    
    # Count filings per CPC code per year
    yearly_counts = df.groupby(['cpc_code', 'year']).size().reset_index(name='count')
    
    # Get all CPC codes and years
    cpc_codes = yearly_counts['cpc_code'].unique()
    years = sorted(yearly_counts['year'].unique())
    
    # Create a complete matrix (CPC codes x years)
    complete_matrix = []
    for cpc in cpc_codes:
        cpc_data = yearly_counts[yearly_counts['cpc_code'] == cpc]
        year_counts = {row['year']: row['count'] for _, row in cpc_data.iterrows()}
        
        # Fill missing years with 0
        row = [cpc]
        for year in years:
            row.append(year_counts.get(year, 0))
        complete_matrix.append(row)
    
    # Create DataFrame with years as columns
    df_matrix = pd.DataFrame(complete_matrix, columns=['cpc_code'] + years)
    
    # Calculate EMA for each CPC code (smoothing factor 0.2)
    alpha = 0.2
    ema_data = []
    
    for _, row in df_matrix.iterrows():
        cpc = row['cpc_code']
        counts = row[years].values
        
        # Calculate EMA
        ema_values = []
        ema_prev = counts[0]  # Initialize with first value
        ema_values.append(ema_prev)
        
        for i in range(1, len(counts)):
            ema_current = alpha * counts[i] + (1 - alpha) * ema_prev
            ema_values.append(ema_current)
            ema_prev = ema_current
        
        # Find best year (year with highest EMA)
        max_ema_index = np.argmax(ema_values)
        best_year = years[max_ema_index]
        best_ema = ema_values[max_ema_index]
        
        ema_data.append({
            'cpc_code': cpc,
            'best_year': best_year,
            'best_ema': best_ema,
            'years': years,
            'ema_values': ema_values
        })
    
    ema_df = pd.DataFrame(ema_data)
    
    # Filter to only CPC codes where best year is 2022
    best_2022 = ema_df[ema_df['best_year'] == 2022]
    
    result = {
        'total_cpc_codes': len(cpc_codes),
        'year_range': f"{min(years)} to {max(years)}",
        'best_2022_count': len(best_2022),
        'sample_best_2022': best_2022.head(10).to_dict('records')
    }

print("__RESULT__:")
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': [{'total': '277813'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:24': {'total_publications': 277813, 'extracted_pairs': 103409, 'sample': [{'cpc_code': 'C01B33/00', 'year': 2021}, {'cpc_code': 'C01B35/00', 'year': 2021}, {'cpc_code': 'H01M10/0565', 'year': 2021}, {'cpc_code': 'H01M10/0562', 'year': 2021}, {'cpc_code': 'C01G45/006', 'year': 2021}, {'cpc_code': 'H01M10/0566', 'year': 2021}, {'cpc_code': 'H01M10/052', 'year': 2021}, {'cpc_code': 'C01P2002/76', 'year': 2021}, {'cpc_code': 'C01G45/006', 'year': 2021}, {'cpc_code': 'Y02E60/10', 'year': 2021}]}, 'var_functions.query_db:26': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}], 'var_functions.query_db:28': [{'symbol': 'A01B1/00', 'level': '7.0'}, {'symbol': 'A01B1/02', 'level': '8.0'}, {'symbol': 'A01B1/022', 'level': '9.0'}, {'symbol': 'A01B1/024', 'level': '9.0'}, {'symbol': 'A01B1/026', 'level': '9.0'}, {'symbol': 'A01B1/028', 'level': '9.0'}, {'symbol': 'A01B1/04', 'level': '9.0'}, {'symbol': 'A01B1/06', 'level': '8.0'}, {'symbol': 'A01B1/065', 'level': '9.0'}, {'symbol': 'A01B1/08', 'level': '9.0'}]}

exec(code, env_args)
