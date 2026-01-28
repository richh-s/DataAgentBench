code = """import json
import pandas as pd
import numpy as np
import re

# Load CPC data from publication database
pub_file_path = locals()['var_functions.query_db:6']
with open(pub_file_path, 'r') as f:
    pub_data = json.load(f)

# Load level 5 CPC symbols from definition database
cpc5_file_path = locals()['var_functions.query_db:14']
with open(cpc5_file_path, 'r') as f:
    cpc5_data = json.load(f)

# Create set of level 5 CPC symbols for fast lookup
cpc5_symbols = set()
for item in cpc5_data:
    symbol = item.get('symbol', '')
    if symbol:
        cpc5_symbols.add(symbol)

# Parse CPC codes and extract years, filtering for level 5 CPCs
parsed_data = []
for record in pub_data:
    cpc_str = record.get('cpc', '[]')
    pub_date_str = record.get('publication_date', '')
    
    # Extract year from publication date (format: "Aug 3rd, 2021")
    year_match = re.search(r',\s*(\d{4})', pub_date_str)
    if year_match:
        year = int(year_match.group(1))
    else:
        continue
    
    # Parse CPC JSON
    try:
        if isinstance(cpc_str, str):
            cpc_list = json.loads(cpc_str)
        else:
            cpc_list = cpc_str
        
        if isinstance(cpc_list, list):
            for cpc_item in cpc_list:
                if isinstance(cpc_item, dict):
                    full_code = cpc_item.get('code', '')
                    if full_code:
                        # Extract CPC group code (first part before / or space)
                        group_code = full_code.split('/')[0].split()[0]
                        # Check if this is a level 5 CPC
                        if group_code in cpc5_symbols:
                            parsed_data.append({
                                'year': year,
                                'cpc_group': group_code
                            })
    except:
        continue

# Create DataFrame
if not parsed_data:
    result = {'cpc_groups_2022': [], 'total_count': 0, 'error': 'No data parsed'}
else:
    df = pd.DataFrame(parsed_data)
    
    # Filter for recent years (focus on 2000-2024 for meaningful EMA)
    df_recent = df[df['year'] >= 2000].copy()
    
    # Group by year and CPC group to count filings
    yearly_counts = df_recent.groupby(['year', 'cpc_group']).size().reset_index(name='count')
    
    # Pivot to have years as columns and CPC groups as rows
    pivot_df = yearly_counts.pivot(index='cpc_group', columns='year', values='count')
    pivot_df = pivot_df.fillna(0)
    
    # Calculate Exponential Moving Average (EMA) with smoothing factor 0.2
    alpha = 0.2
    
    # For each CPC group, calculate EMA across years
    best_years = {}
    
    for cpc_group in pivot_df.index:
        values = []
        years = []
        
        # Collect values and years for this CPC group
        for year in sorted(pivot_df.columns):
            value = pivot_df.loc[cpc_group, year]
            if value > 0:  # Only consider years with filings
                values.append(value)
                years.append(year)
        
        if len(values) >= 2:  # Need at least 2 points for EMA
            # Calculate EMA
            ema_values = []
            ema = values[0]  # Initialize with first value
            
            for i, value in enumerate(values):
                if i == 0:
                    ema_values.append(ema)
                else:
                    ema = alpha * value + (1 - alpha) * ema
                    ema_values.append(ema)
            
            # Store EMA values by year
            ema_by_year = dict(zip(years, ema_values)
            
            # Find year with highest EMA
            best_year = max(ema_by_year.keys(), key=lambda y: ema_by_year[y])
            best_years[cpc_group] = best_year
    
    # Filter for CPC groups where best year is 2022
    cpc_2022 = [cpc for cpc, year in best_years.items() if year == 2022]
    
    # Prepare final result
    result = {
        'cpc_groups_2022': sorted(cpc_2022),
        'total_count': len(cpc_2022)
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:5': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}, {'symbol': 'A01N', 'level': '5.0', 'titleFull': 'PRESERVATION OF BODIES OF HUMANS OR ANIMALS OR PLANTS OR PARTS THEREOF; BIOCIDES, e.g. AS DISINFECTANTS, AS PESTICIDES OR AS HERBICIDES; PEST REPELLANTS OR ATTRACTANTS; PLANT GROWTH REGULATORS'}, {'symbol': 'A01P', 'level': '5.0', 'titleFull': 'BIOCIDAL, PEST REPELLANT, PEST ATTRACTANT OR PLANT GROWTH REGULATORY ACTIVITY OF CHEMICAL COMPOUNDS OR PREPARATIONS'}, {'symbol': 'A01D', 'level': '5.0', 'titleFull': 'HARVESTING; MOWING'}, {'symbol': 'A01L', 'level': '5.0', 'titleFull': 'SHOEING OF ANIMALS'}, {'symbol': 'A01K', 'level': '5.0', 'titleFull': 'ANIMAL HUSBANDRY; AVICULTURE; APICULTURE; PISCICULTURE; FISHING; REARING OR BREEDING ANIMALS, NOT OTHERWISE PROVIDED FOR; NEW BREEDS OF ANIMALS'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'total_records': 277813, 'parsed_records': 1333969, 'year_range': '1837 to 2024'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
