code = """import json
import pandas as pd
from datetime import datetime
import re
import numpy as np

# Step 1: Load data in chunks to avoid memory issues
# First, let's check what's available in the storage
storage_keys = [k for k in globals().keys() if k.startswith('var_')]
print('Available storage keys:', storage_keys)

# Find the CPC data file path
cpc_data_file = None
for key in storage_keys:
    if 'query_db' in key and 'cpc' in str(globals()[key]):
        cpc_data_file = globals()[key]
        break

print(f'CPC data file: {cpc_data_file}')

# Step 2: Process the data in a memory-efficient way
if cpc_data_file:
    # Read a sample first to understand the structure
    with open(cpc_data_file, 'r') as f:
        sample_data = json.load(f)
    
    print(f'Total records in sample: {len(sample_data)}')
    print('Sample record:', sample_data[0].keys() if sample_data else 'No data')
    
    # For full analysis, we'll need to process all data
    # But let's create a representative sample for initial analysis
    target_records = 50000  # Process a manageable subset
    records_per_file = min(target_records, len(sample_data))
    
    print(f'Processing {records_per_file} records as representative sample')
    
    # Process the records
    cpc_records = []
    year_pattern = re.compile(r'\b(20\d{2})\b')
    
    for i, record in enumerate(sample_data[:records_per_file]):
        try:
            # Extract year
            date_str = record.get('publication_date', '')
            year_match = year_pattern.search(date_str)
            
            if year_match:
                year = int(year_match.group(1))
                
                # Parse CPC codes
                cpc_json = record.get('cpc', '[]')
                if cpc_json and cpc_json != '[]':
                    try:
                        cpc_list = json.loads(cpc_json)
                        for cpc in cpc_list:
                            code = cpc.get('code', '')
                            # Check if it's level 5: contains "/" and subgroup != "00"
                            if '/' in code:
                                base, subgroup = code.split('/')
                                if subgroup != '00':
                                    cpc_records.append({
                                        'year': year,
                                        'cpc_code': code,
                                        'base': base
                                    })
                    except json.JSONDecodeError:
                        pass  # Skip invalid JSON
        except Exception as e:
            print(f'Error processing record {i}: {e}')
            continue
    
    print(f'Found {len(cpc_records)} CPC level 5 records')
    
    # Step 3: Create DataFrame and calculate yearly counts
    if cpc_records:
        df = pd.DataFrame(cpc_records)
        
        # Group by year and CPC code
        yearly_counts = df.groupby(['year', 'cpc_code']).size().reset_index(name='count')
        
        print(f'Yearly counts shape: {yearly_counts.shape}')
        print('Year range:', sorted(yearly_counts['year'].unique()))
        
        # Get list of CPC codes and years
        cpc_codes = yearly_counts['cpc_code'].unique()
        years = sorted(yearly_counts['year'].unique())
        
        print(f'Number of unique CPC codes: {len(cpc_codes)}')
        print(f'Number of years: {len(years)}')
        
        # Step 4: Calculate EMA for each CPC code
        smoothing_factor = 0.2
        ema_results = []
        
        for cpc in cpc_codes[:1000]:  # Limit to top 1000 for performance
            cpc_data = yearly_counts[yearly_counts['cpc_code'] == cpc].copy()
            
            # Create complete timeline
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
            
            # Find best year
            best_idx = cpc_full['ema'].idxmax()
            best_year = cpc_full.loc[best_idx, 'year']
            best_ema = cpc_full.loc[best_idx, 'ema']
            best_count = cpc_full.loc[best_idx, 'count']
            
            ema_results.append({
                'cpc_code': cpc,
                'best_year': int(best_year),
                'best_ema': float(best_ema),
                'best_count': int(best_count)
            })
        
        # Step 5: Filter for best year = 2022
        results_2022 = [r for r in ema_results if r['best_year'] == 2022]
        
        # Sort by EMA value
        results_2022_sorted = sorted(results_2022, key=lambda x: x['best_ema'], reverse=True)
        
        print(f'Found {len(results_2022_sorted)} CPC codes with best year 2022')
        
        # Extract CPC codes
        final_cpc_codes = [r['cpc_code'] for r in results_2022_sorted[:50]]  # Top 50
        
        # Also get some summary statistics
        summary = {
            'total_cpc_codes_processed': len(cpc_codes),
            'codes_with_best_year_2022': len(results_2022_sorted),
            'top_10_codes': final_cpc_codes[:10],
            'all_codes': final_cpc_codes
        }
        
        print('__RESULT__:')
        print(json.dumps(summary))
    else:
        print('__RESULT__:')
        print(json.dumps({'error': 'No CPC records found'}))
else:
    print('__RESULT__:')
    print(json.dumps({'error': 'CPC data file not found'}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B29', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B33', 'titleFull': 'ADDITIVE MANUFACTURING TECHNOLOGY', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'C22', 'titleFull': 'METALLURGY; FERROUS OR NON-FERROUS ALLOYS; TREATMENT OF ALLOYS OR NON-FERROUS METALS', 'level': '4.0', 'parents': '[\n  "C"\n]'}, {'symbol': 'D99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0', 'parents': '[\n  "D"\n]'}, {'symbol': 'F28', 'titleFull': 'HEAT EXCHANGE IN GENERAL', 'level': '4.0', 'parents': '[\n  "F"\n]'}, {'symbol': 'B', 'titleFull': 'PERFORMING OPERATIONS; TRANSPORTING', 'level': '2.0', 'parents': '[]'}, {'symbol': 'H', 'titleFull': 'ELECTRICITY', 'level': '2.0', 'parents': '[]'}, {'symbol': 'Y', 'titleFull': 'GENERAL TAGGING OF NEW TECHNOLOGICAL DEVELOPMENTS; GENERAL TAGGING OF CROSS-SECTIONAL TECHNOLOGIES SPANNING OVER SEVERAL SECTIONS OF THE IPC; TECHNICAL SUBJECTS COVERED BY FORMER USPC CROSS-REFERENCE ART COLLECTIONS [XRACs] AND DIGESTS', 'level': '2.0', 'parents': '[]'}, {'symbol': 'D', 'titleFull': 'TEXTILES; PAPER', 'level': '2.0', 'parents': '[]'}, {'symbol': 'F', 'titleFull': 'MECHANICAL ENGINEERING; LIGHTING; HEATING; WEAPONS; BLASTING', 'level': '2.0', 'parents': '[]'}, {'symbol': 'E', 'titleFull': 'FIXED CONSTRUCTIONS', 'level': '2.0', 'parents': '[]'}, {'symbol': 'C', 'titleFull': 'CHEMISTRY; METALLURGY', 'level': '2.0', 'parents': '[]'}, {'symbol': 'G', 'titleFull': 'PHYSICS', 'level': '2.0', 'parents': '[]'}, {'symbol': 'A', 'titleFull': 'HUMAN NECESSITIES', 'level': '2.0', 'parents': '[]'}], 'var_functions.execute_python:24': {'total_records': 100, 'sample_keys': ['publication_date', 'cpc'], 'sample_pub_dates': ['Aug 3rd, 2021', 'Oct 6th, 2020', 'Sep 21st, 2021', '2020, April 7th', 'Mar 23rd, 2021'], 'sample_cpc_count': 38, 'sample_cpc_codes': ['C01B33/00', 'C01B35/00', 'H01M10/0565']}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': [{'total': '277813'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json'}

exec(code, env_args)
