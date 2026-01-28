code = """import json, pandas as pd, re, numpy as np
import time

# Load data efficiently
print("Loading data...")
file_path = locals()['var_functions.query_db:2']
cpc5_file = locals()['var_functions.query_db:16']

data = json.load(open(file_path))
cpc5_symbols = set(item['symbol'] for item in json.load(open(cpc5_file)))

print(f'Loaded {len(data)} patents and {len(cpc5_symbols)} level 5 CPC symbols')

# Pre-compile regex for efficiency
year_pattern = re.compile(r'(\d{4})')
prefix_pattern = re.compile(r'^(dated|on)\s+', re.IGNORECASE)

# Efficient CPC parsing and year extraction
def extract_data(record):
    # Extract CPC codes
    cpc_str = record.get('cpc', '')
    if not cpc_str or not cpc_str.strip().startswith('['):
        return []
    
    try:
        codes = json.loads(cpc_str.strip())
    except:
        return []
    
    # Extract year from filing date
    date_str = record.get('filing_date', '')
    if not date_str:
        return []
    
    clean_date = prefix_pattern.sub('', date_str)
    year_match = year_pattern.search(clean_date)
    if not year_match:
        return []
    
    year = int(year_match.group(1))
    if not (1900 <= year <= 2030):
        return []
    
    # Map to level 5 and collect data
    result = []
    for item in codes:
        code = item.get('code', '')
        if not code:
            continue
        
        # Extract group (part before /)
        group = code.split('/')[0] if '/' in code else code
        
        # Check if it maps to a level 5 symbol
        for symbol in cpc5_symbols:
            if group.startswith(symbol):
                result.append((symbol, year))
                break
    
    return result

# Process data in batches and collect level 5 CPC data
level5_data = []
batch_size = 10000
start_time = time.time()

for i, record in enumerate(data):
    if i % batch_size == 0 and i > 0:
        elapsed = time.time() - start_time
        print(f'Processed {i}/{len(data)} records ({elapsed:.1f}s)')
    
    extracted = extract_data(record)
    level5_data.extend(extracted)

# Create DataFrame
df = pd.DataFrame(level5_data, columns=['cpc_level5', 'year'])
print(f'Extracted {len(df)} level 5 CPC entries in {time.time() - start_time:.1f}s')
print(f'Unique level 5 groups: {df["cpc_level5"].nunique()}')

# Filter for recent data (2015-2024) to focus on relevant years
recent_df = df[(df['year'] >= 2015) & (df['year'] <= 2024)].copy()
print(f'Recent data (2015-2024): {len(recent_df)} entries')

if len(recent_df) == 0:
    result = {'cpc_groups_best_year_2022': [], 'count': 0}
else:
    # Get yearly counts
    yearly_counts = recent_df.groupby(['cpc_level5', 'year']).size().reset_index(name='count')
    
    # Get year range
    min_year = int(yearly_counts['year'].min())
    max_year = int(yearly_counts['year'].max())
    all_years = list(range(min_year, max_year + 1))
    
    print(f'Year range for EMA: {min_year} to {max_year}')
    print(f'Total yearly count records: {len(yearly_counts)}')
    
    # Calculate EMA for each group efficiently
    alpha = 0.2
    result_2022 = []
    
    for group in yearly_counts['cpc_level5'].unique():
        group_data = yearly_counts[yearly_counts['cpc_level5'] == group].sort_values('year')
        years = group_data['year'].values
        counts = group_data['count'].values
        
        # Create full timeline
        year_to_idx = {year: i for i, year in enumerate(all_years)}
        full_counts = np.zeros(len(all_years))
        
        for y, c in zip(years, counts):
            if y in year_to_idx:
                full_counts[year_to_idx[y]] = c
        
        # Calculate EMA
        ema = 0
        first_value = True
        ema_values = []
        
        for count in full_counts:
            if first_value:
                ema = count
                first_value = False
            else:
                ema = alpha * count + (1 - alpha) * ema
            ema_values.append(ema)
        
        # Find best year
        if ema_values:
            max_idx = np.argmax(ema_values)
            best_year = all_years[max_idx]
            if best_year == 2022:
                result_2022.append(group)
    
    result = {'cpc_groups_best_year_2022': sorted(result_2022), 'count': len(result_2022)}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_records': 277813, 'sample_record': {'cpc': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02E60/10",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/582",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]', 'filing_date': 'dated 5th March 2019'}}, 'var_functions.query_db:10': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}, {'symbol': 'A01N', 'level': '5.0', 'titleFull': 'PRESERVATION OF BODIES OF HUMANS OR ANIMALS OR PLANTS OR PARTS THEREOF; BIOCIDES, e.g. AS DISINFECTANTS, AS PESTICIDES OR AS HERBICIDES; PEST REPELLANTS OR ATTRACTANTS; PLANT GROWTH REGULATORS'}, {'symbol': 'A01P', 'level': '5.0', 'titleFull': 'BIOCIDAL, PEST REPELLANT, PEST ATTRACTANT OR PLANT GROWTH REGULATORY ACTIVITY OF CHEMICAL COMPOUNDS OR PREPARATIONS'}, {'symbol': 'A01D', 'level': '5.0', 'titleFull': 'HARVESTING; MOWING'}, {'symbol': 'A01L', 'level': '5.0', 'titleFull': 'SHOEING OF ANIMALS'}, {'symbol': 'A01K', 'level': '5.0', 'titleFull': 'ANIMAL HUSBANDRY; AVICULTURE; APICULTURE; PISCICULTURE; FISHING; REARING OR BREEDING ANIMALS, NOT OTHERWISE PROVIDED FOR; NEW BREEDS OF ANIMALS'}], 'var_functions.execute_python:12': {'sample_dates': ['dated 5th March 2019', 'March the 18th, 2019', '29th March 2019', 'on March 29th, 2019', '2nd April 2019', 'on April 8th, 2019', '15th April 2019', 'April 19th, 2019', '2019, April 24th', 'April 26th, 2019']}, 'var_functions.execute_python:14': {'total_records_processed': 2675476, 'unique_cpc_groups': 9921, 'year_range': {'min': 1900, 'max': 2024}, 'sample_yearly_counts': [{'cpc_group': 'A01B1', 'year': 1941, 'count': 4}, {'cpc_group': 'A01B1', 'year': 1948, 'count': 2}, {'cpc_group': 'A01B1', 'year': 1950, 'count': 2}, {'cpc_group': 'A01B1', 'year': 1954, 'count': 1}, {'cpc_group': 'A01B1', 'year': 1959, 'count': 1}, {'cpc_group': 'A01B1', 'year': 1967, 'count': 1}, {'cpc_group': 'A01B1', 'year': 1981, 'count': 1}, {'cpc_group': 'A01B1', 'year': 1986, 'count': 2}, {'cpc_group': 'A01B1', 'year': 1990, 'count': 2}, {'cpc_group': 'A01B1', 'year': 1993, 'count': 2}]}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'total_cpc5_symbols': 677, 'sample_symbols': ['B64G', 'B21D', 'F16F', 'F01C', 'H01L', 'D01F', 'B41M', 'A61G', 'F23R', 'F15C']}, 'var_functions.execute_python:24': {'cpc_groups_best_year_2022': [], 'total_found': 0}, 'var_functions.execute_python:26': {'year_range': {'min': 1900, 'max': 2024}, 'unique_cpc_groups': 9921, 'top_groups': [{'cpc_group': 'A61K31', 'total': 31940}, {'cpc_group': 'H01L21', 'total': 29931}, {'cpc_group': 'H01L2224', 'total': 24551}, {'cpc_group': 'G06F3', 'total': 23228}, {'cpc_group': 'A61B5', 'total': 19962}, {'cpc_group': 'H01L2924', 'total': 19121}, {'cpc_group': 'Y10T428', 'total': 17555}, {'cpc_group': 'H04N21', 'total': 16669}, {'cpc_group': 'H01L29', 'total': 16321}, {'cpc_group': 'H04N19', 'total': 16154}, {'cpc_group': 'A61K9', 'total': 15610}, {'cpc_group': 'A61K8', 'total': 11952}, {'cpc_group': 'H01M4', 'total': 11780}, {'cpc_group': 'G02F1', 'total': 11579}, {'cpc_group': 'C07K2317', 'total': 11365}, {'cpc_group': 'G06F16', 'total': 11334}, {'cpc_group': 'H01M10', 'total': 11227}, {'cpc_group': 'H01L23', 'total': 10412}, {'cpc_group': 'A61B17', 'total': 10118}, {'cpc_group': 'G01N33', 'total': 10037}]}, 'var_functions.query_db:28': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A21B', 'level': '5.0'}, {'symbol': 'A21C', 'level': '5.0'}, {'symbol': 'A21D', 'level': '5.0'}, {'symbol': 'A22B', 'level': '5.0'}, {'symbol': 'A22C', 'level': '5.0'}, {'symbol': 'A23B', 'level': '5.0'}, {'symbol': 'A23C', 'level': '5.0'}, {'symbol': 'A23D', 'level': '5.0'}, {'symbol': 'A23F', 'level': '5.0'}, {'symbol': 'A23G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A23K', 'level': '5.0'}, {'symbol': 'A23L', 'level': '5.0'}, {'symbol': 'A23N', 'level': '5.0'}, {'symbol': 'A23P', 'level': '5.0'}, {'symbol': 'A23V', 'level': '5.0'}, {'symbol': 'A24B', 'level': '5.0'}, {'symbol': 'A24C', 'level': '5.0'}, {'symbol': 'A24D', 'level': '5.0'}, {'symbol': 'A24F', 'level': '5.0'}, {'symbol': 'A41B', 'level': '5.0'}, {'symbol': 'A41C', 'level': '5.0'}, {'symbol': 'A41D', 'level': '5.0'}, {'symbol': 'A41F', 'level': '5.0'}, {'symbol': 'A41G', 'level': '5.0'}, {'symbol': 'A41H', 'level': '5.0'}, {'symbol': 'A42B', 'level': '5.0'}, {'symbol': 'A42C', 'level': '5.0'}, {'symbol': 'A43B', 'level': '5.0'}, {'symbol': 'A43C', 'level': '5.0'}, {'symbol': 'A43D', 'level': '5.0'}, {'symbol': 'A44B', 'level': '5.0'}, {'symbol': 'A44C', 'level': '5.0'}, {'symbol': 'A44D', 'level': '5.0'}, {'symbol': 'A45B', 'level': '5.0'}, {'symbol': 'A45C', 'level': '5.0'}, {'symbol': 'A45D', 'level': '5.0'}, {'symbol': 'A45F', 'level': '5.0'}]}

exec(code, env_args)
