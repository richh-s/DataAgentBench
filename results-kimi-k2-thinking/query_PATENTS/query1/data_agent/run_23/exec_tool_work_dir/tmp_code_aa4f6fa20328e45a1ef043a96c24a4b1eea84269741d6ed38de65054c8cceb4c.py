code = """import json
import pandas as pd
import re
from datetime import datetime

# Debug: Check what's in our local variables and globals
print('Local variables starting with var_:')
local_vars = [k for k in locals().keys() if k.startswith('var_')]
print(local_vars)

print('\nGlobal variables starting with var_:')
global_vars = [k for k in globals().keys() if k.startswith('var_')]
print(global_vars)

# Try to access the file path differently
# The variable should contain the file path string
file_var_name = 'var_functions.query_db:26'
file_path = None

if file_var_name in globals():
    file_path = globals()[file_var_name]
    print(f'\nFound {file_var_name} in globals: {file_path}')
elif file_var_name in locals():
    file_path = locals()[file_var_name]
    print(f'\nFound {file_var_name} in locals: {file_path}')
else:
    # List all variables to see what's available
    print('\nAll available variables:')
    all_vars = list(globals().keys()) + list(locals().keys())
    db_vars = [v for v in all_vars if 'query_db' in v or 'cpc' in v]
    print(db_vars)

# If we found the file path, process it
if file_path:
    print(f'\nProcessing file: {file_path}')
    
    # Read the data in chunks
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    print(f'Total records: {len(data)}')
    
    # Sample the data to verify structure
    if data:
        print('Sample record keys:', list(data[0].keys()))
        print('Sample publication_date:', data[0].get('publication_date'))
        print('Sample CPC codes:', data[0].get('cpc')[:200])
    
    # Process in batches to avoid timeout
    batch_size = 10000
    all_yearly_counts = []
    
    year_pattern = re.compile(r'\b(20\d{2})\b')  # Pattern to extract year
    
    for batch_start in range(0, len(data), batch_size):
        batch = data[batch_start:batch_start + batch_size]
        batch_records = []
        
        for record in batch:
            try:
                # Extract year from publication_date
                date_str = record.get('publication_date', '')
                year_match = year_pattern.search(date_str)
                
                if year_match:
                    year = int(year_match.group(1))
                    
                    # Parse CPC codes and extract level 5 codes
                    cpc_json = record.get('cpc', '[]')
                    if cpc_json and cpc_json != '[]':
                        try:
                            cpc_list = json.loads(cpc_json)
                            for cpc in cpc_list:
                                code = cpc.get('code', '')
                                # Check if it's level 5: contains "/" and subgroup != "00"
                                if '/' in code:
                                    base, subgroup = code.split('/')
                                    if subgroup != '00':  # This is level 5
                                        batch_records.append({
                                            'year': year,
                                            'cpc_code': code,
                                            'base': base
                                        })
                        except json.JSONDecodeError:
                            continue  # Skip invalid JSON
            except Exception as e:
                continue  # Skip problematic records
        
        # Add to overall collection
        all_yearly_counts.extend(batch_records)
        
        if batch_start % 50000 == 0:
            print(f'Processed {batch_start} records, found {len(all_yearly_counts)} CPC records')
    
    print(f'\nTotal CPC level 5 records found: {len(all_yearly_counts)}')
    
    # Create DataFrame and calculate yearly counts
    if all_yearly_counts:
        df = pd.DataFrame(all_yearly_counts)
        
        # Group by year and CPC code
        yearly_counts = df.groupby(['year', 'cpc_code']).size().reset_index(name='count')
        
        print(f'Yearly counts shape: {yearly_counts.shape}')
        print(f'Year range: {sorted(yearly_counts["year"].unique())}')
        
        # Get unique CPC codes and years
        cpc_codes = yearly_counts['cpc_code'].unique()
        years = sorted(yearly_counts['year'].unique())
        
        print(f'Number of unique CPC codes: {len(cpc_codes)}')
        print(f'Number of unique years: {len(years)}')
        
        # Calculate EMA for each CPC code
        smoothing_factor = 0.2
        ema_results = []
        
        # Process a reasonable subset for this analysis
        for i, cpc in enumerate(cpc_codes):
            if i % 1000 == 0:
                print(f'Processing CPC {i}/{len(cpc_codes)}')
            
            try:
                # Get data for this CPC code
                cpc_data = yearly_counts[yearly_counts['cpc_code'] == cpc].copy()
                
                # Create complete timeline with all years
                timeline = pd.DataFrame({'year': years})
                cpc_full = timeline.merge(cpc_data, on='year', how='left').fillna(0)
                
                # Calculate EMA
                ema_values = []
                ema_val = None
                
                for _, row in cpc_full.iterrows():
                    count = row['count']
                    if ema_val is None:
                        ema_val = count
                    else:
                        ema_val = (smoothing_factor * count) + ((1 - smoothing_factor) * ema_val)
                    ema_values.append(ema_val)
                
                cpc_full['ema'] = ema_values
                
                # Find year with highest EMA
                best_idx = cpc_full['ema'].idxmax()
                best_year = int(cpc_full.loc[best_idx, 'year'])
                best_ema = float(cpc_full.loc[best_idx, 'ema'])
                best_count = int(cpc_full.loc[best_idx, 'count'])
                
                ema_results.append({
                    'cpc_code': cpc,
                    'best_year': best_year,
                    'best_ema': best_ema,
                    'best_count': best_count
                })
                
            except Exception as e:
                print(f'Error processing CPC {cpc}: {e}')
                continue
        
        # Filter for CPC codes where best year is 2022
        results_2022 = [r for r in ema_results if r['best_year'] == 2022]
        
        # Sort by EMA value (highest first)
        results_2022_sorted = sorted(results_2022, key=lambda x: x['best_ema'], reverse=True)
        
        print(f'\nFound {len(results_2022_sorted)} CPC codes with best year 2022')
        
        # Extract just the CPC codes as requested
        final_cpc_codes = [r['cpc_code'] for r in results_2022_sorted]
        
        # Prepare final result
        result = {
            'total_cpc_codes_analyzed': len(cpc_codes),
            'codes_with_best_year_2022': len(results_2022_sorted),
            'cpc_codes_best_year_2022': final_cpc_codes,
            'summary': f'Identified {len(results_2022_sorted)} CPC level 5 codes whose exponential moving average of patent filings peaked in 2022'
        }
        
        print('__RESULT__:')
        print(json.dumps(result, indent=2))
        
    else:
        print('__RESULT__:')
        print(json.dumps({'error': 'No CPC level 5 records found in data'}))
else:
    print('__RESULT__:')
    print(json.dumps({'error': 'Could not locate CPC data file'}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B29', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B33', 'titleFull': 'ADDITIVE MANUFACTURING TECHNOLOGY', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'C22', 'titleFull': 'METALLURGY; FERROUS OR NON-FERROUS ALLOYS; TREATMENT OF ALLOYS OR NON-FERROUS METALS', 'level': '4.0', 'parents': '[\n  "C"\n]'}, {'symbol': 'D99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0', 'parents': '[\n  "D"\n]'}, {'symbol': 'F28', 'titleFull': 'HEAT EXCHANGE IN GENERAL', 'level': '4.0', 'parents': '[\n  "F"\n]'}, {'symbol': 'B', 'titleFull': 'PERFORMING OPERATIONS; TRANSPORTING', 'level': '2.0', 'parents': '[]'}, {'symbol': 'H', 'titleFull': 'ELECTRICITY', 'level': '2.0', 'parents': '[]'}, {'symbol': 'Y', 'titleFull': 'GENERAL TAGGING OF NEW TECHNOLOGICAL DEVELOPMENTS; GENERAL TAGGING OF CROSS-SECTIONAL TECHNOLOGIES SPANNING OVER SEVERAL SECTIONS OF THE IPC; TECHNICAL SUBJECTS COVERED BY FORMER USPC CROSS-REFERENCE ART COLLECTIONS [XRACs] AND DIGESTS', 'level': '2.0', 'parents': '[]'}, {'symbol': 'D', 'titleFull': 'TEXTILES; PAPER', 'level': '2.0', 'parents': '[]'}, {'symbol': 'F', 'titleFull': 'MECHANICAL ENGINEERING; LIGHTING; HEATING; WEAPONS; BLASTING', 'level': '2.0', 'parents': '[]'}, {'symbol': 'E', 'titleFull': 'FIXED CONSTRUCTIONS', 'level': '2.0', 'parents': '[]'}, {'symbol': 'C', 'titleFull': 'CHEMISTRY; METALLURGY', 'level': '2.0', 'parents': '[]'}, {'symbol': 'G', 'titleFull': 'PHYSICS', 'level': '2.0', 'parents': '[]'}, {'symbol': 'A', 'titleFull': 'HUMAN NECESSITIES', 'level': '2.0', 'parents': '[]'}], 'var_functions.execute_python:24': {'total_records': 100, 'sample_keys': ['publication_date', 'cpc'], 'sample_pub_dates': ['Aug 3rd, 2021', 'Oct 6th, 2020', 'Sep 21st, 2021', '2020, April 7th', 'Mar 23rd, 2021'], 'sample_cpc_count': 38, 'sample_cpc_codes': ['C01B33/00', 'C01B35/00', 'H01M10/0565']}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': [{'total': '277813'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:36': {'error': 'CPC data file not found'}}

exec(code, env_args)
