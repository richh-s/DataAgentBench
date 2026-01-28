code = """import json
import pandas as pd
from datetime import datetime
import numpy as np

# Load full data from the stored file path
result_key = 'var_functions.query_db:26'
file_path = None
if result_key in locals():
    file_path = locals()[result_key]
elif result_key in globals():
    file_path = globals()[result_key]

if not file_path:
    print('__RESULT__:')
    print(json.dumps({'error': 'File path not found'}))
else:
    # Load and process data
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    # Parse dates and extract CPC codes
    records = []
    for record in data:
        date_str = record['publication_date']
        # Extract year from various date formats
        year_match = None
        if ',' in date_str:
            # Format like "Aug 3rd, 2021" or "2020, April 7th"
            parts = date_str.split(',')
            for part in parts:
                part = part.strip()
                if len(part) == 4 and part.isdigit():
                    year_match = part
                    break
        if not year_match:
            # Try to find 4-digit year anywhere
            import re
            year_match = re.search(r'\b(20\d{2})\b', date_str)
            if year_match:
                year_match = year_match.group(1)
        
        if year_match:
            year = int(year_match)
            cpc_list = json.loads(record['cpc'])
            for cpc in cpc_list:
                code = cpc['code']
                # CPC level is determined by the number of hierarchical separators
                # Level 1: A, B, C, etc.
                # Level 2: A01, B02, etc. 
                # Level 3: A01B, B02C, etc.
                # Level 4: A01B1/00, B02C3/00, etc.
                # Level 5: A01B1/02, B02C3/04, etc.
                
                # Extract level 5 codes: contain "/" and have digits after "/"
                if '/' in code:
                    base, subgroup = code.split('/')
                    if subgroup != '00':  # Level 5, not level 4
                        records.append({
                            'year': year,
                            'cpc_code': code,
                            'cpc_base': base
                        })
    
    # Create DataFrame
    df = pd.DataFrame(records)
    
    # Group by year and CPC code to count filings
    yearly_counts = df.groupby(['year', 'cpc_code']).size().reset_index(name='count')
    
    # Get all unique CPC codes and years
    cpc_codes = yearly_counts['cpc_code'].unique()
    years = sorted(yearly_counts['year'].unique())
    
    # Calculate EMA for each CPC code
    ema_results = []
    smoothing_factor = 0.2
    
    for cpc in cpc_codes:
        cpc_data = yearly_counts[yearly_counts['cpc_code'] == cpc].copy()
        cpc_data = cpc_data.set_index('year').reindex(years, fill_value=0)
        
        # Calculate EMA
        ema = []
        if len(cpc_data) > 0:
            ema_val = cpc_data.iloc[0]['count']  # Initialize with first value
            ema.append({'year': cpc_data.index[0], 'ema': float(ema_val), 'count': int(cpc_data.iloc[0]['count'])})
            
            for i in range(1, len(cpc_data)):
                current_count = cpc_data.iloc[i]['count']
                ema_val = (smoothing_factor * current_count) + ((1 - smoothing_factor) * ema_val)
                ema.append({'year': cpc_data.index[i], 'ema': float(ema_val), 'count': int(current_count)})
        
        # Find year with highest EMA
        if ema:
            best_year = max(ema, key=lambda x: x['ema'])
            ema_results.append({
                'cpc_code': cpc,
                'best_year': best_year['year'],
                'best_ema': best_year['ema'],
                'best_count': best_year['count']
            })
    
    # Filter for CPC codes where best year is 2022
    result_2022 = [r for r in ema_results if r['best_year'] == 2022]
    
    # Sort by EMA value descending
    result_2022_sorted = sorted(result_2022, key=lambda x: x['best_ema'], reverse=True)
    
    # Extract just the CPC codes
    final_cpc_codes = [r['cpc_code'] for r in result_2022_sorted]
    
    print('__RESULT__:')
    print(json.dumps(final_cpc_codes))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B29', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B33', 'titleFull': 'ADDITIVE MANUFACTURING TECHNOLOGY', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'C22', 'titleFull': 'METALLURGY; FERROUS OR NON-FERROUS ALLOYS; TREATMENT OF ALLOYS OR NON-FERROUS METALS', 'level': '4.0', 'parents': '[\n  "C"\n]'}, {'symbol': 'D99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0', 'parents': '[\n  "D"\n]'}, {'symbol': 'F28', 'titleFull': 'HEAT EXCHANGE IN GENERAL', 'level': '4.0', 'parents': '[\n  "F"\n]'}, {'symbol': 'B', 'titleFull': 'PERFORMING OPERATIONS; TRANSPORTING', 'level': '2.0', 'parents': '[]'}, {'symbol': 'H', 'titleFull': 'ELECTRICITY', 'level': '2.0', 'parents': '[]'}, {'symbol': 'Y', 'titleFull': 'GENERAL TAGGING OF NEW TECHNOLOGICAL DEVELOPMENTS; GENERAL TAGGING OF CROSS-SECTIONAL TECHNOLOGIES SPANNING OVER SEVERAL SECTIONS OF THE IPC; TECHNICAL SUBJECTS COVERED BY FORMER USPC CROSS-REFERENCE ART COLLECTIONS [XRACs] AND DIGESTS', 'level': '2.0', 'parents': '[]'}, {'symbol': 'D', 'titleFull': 'TEXTILES; PAPER', 'level': '2.0', 'parents': '[]'}, {'symbol': 'F', 'titleFull': 'MECHANICAL ENGINEERING; LIGHTING; HEATING; WEAPONS; BLASTING', 'level': '2.0', 'parents': '[]'}, {'symbol': 'E', 'titleFull': 'FIXED CONSTRUCTIONS', 'level': '2.0', 'parents': '[]'}, {'symbol': 'C', 'titleFull': 'CHEMISTRY; METALLURGY', 'level': '2.0', 'parents': '[]'}, {'symbol': 'G', 'titleFull': 'PHYSICS', 'level': '2.0', 'parents': '[]'}, {'symbol': 'A', 'titleFull': 'HUMAN NECESSITIES', 'level': '2.0', 'parents': '[]'}], 'var_functions.execute_python:24': {'total_records': 100, 'sample_keys': ['publication_date', 'cpc'], 'sample_pub_dates': ['Aug 3rd, 2021', 'Oct 6th, 2020', 'Sep 21st, 2021', '2020, April 7th', 'Mar 23rd, 2021'], 'sample_cpc_count': 38, 'sample_cpc_codes': ['C01B33/00', 'C01B35/00', 'H01M10/0565']}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
