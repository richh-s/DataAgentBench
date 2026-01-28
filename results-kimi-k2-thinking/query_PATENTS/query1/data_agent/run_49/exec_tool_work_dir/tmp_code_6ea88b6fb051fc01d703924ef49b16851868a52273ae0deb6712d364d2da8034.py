code = """import json, pandas as pd, re, numpy as np

# Load CPC level 5 symbols
cpc5_file = locals()['var_functions.query_db:16']
cpc5_symbols = set(item['symbol'] for item in json.load(open(cpc5_file)))

# Process data in a memory-efficient way
file_path = locals()['var_functions.query_db:2']

# Load and filter data in one pass to reduce memory
level5_data = []
year_pattern = re.compile(r'(\d{4})')

with open(file_path, 'r') as f:
    data = json.load(f)
    
for record in data[:50000]:  # Process subset for initial analysis
    cpc_str = record.get('cpc', '')
    if not cpc_str or not cpc_str.strip().startswith('['):
        continue
    
    try:
        codes = json.loads(cpc_str.strip())
    except:
        continue
    
    # Extract year
    date_str = record.get('filing_date', '')
    if not date_str:
        continue
    
    clean_date = re.sub(r'^(dated|on)\s+', '', date_str, flags=re.IGNORECASE)
    match = year_pattern.search(clean_date)
    if not match:
        continue
    
    year = int(match.group(1))
    if year < 2015 or year > 2024:  # Focus on recent years
        continue
    
    # Extract level 5 CPC codes
    for item in codes:
        code = item.get('code', '')
        if not code:
            continue
        group = code.split('/')[0] if '/' in code else code
        
        # Map to level 5
        for symbol in cpc5_symbols:
            if group.startswith(symbol):
                level5_data.append((symbol, year))
                break

print(f'Processed {len(level5_data)} level 5 CPC entries from recent years')

if level5_data:
    df = pd.DataFrame(level5_data, columns=['cpc_level5', 'year'])
    print(f'Unique groups: {df["cpc_level5"].nunique()}')
    
    # Get yearly counts
    yearly_counts = df.groupby(['cpc_level5', 'year']).size().reset_index(name='count')
    
    min_year = int(yearly_counts['year'].min())
    max_year = int(yearly_counts['year'].max())
    all_years = list(range(min_year, max_year + 1))
    
    print(f'Processing EMA for years {min_year}-{max_year}')
    
    # Process each group
    alpha = 0.2
    result_2022 = []
    
    for group in yearly_counts['cpc_level5'].unique():
        group_data = yearly_counts[yearly_counts['cpc_level5'] == group].sort_values('year')
        years = group_data['year'].values
        counts = group_data['count'].values
        
        # Create full timeline
        full_counts = np.zeros(len(all_years))
        year_to_pos = {y: i for i, y in enumerate(all_years)}
        
        for y, c in zip(years, counts):
            if y in year_to_pos:
                full_counts[year_to_pos[y]] = c
        
        # Calculate EMA
        ema_values = []
        ema = None
        for count in full_counts:
            if ema is None:
                ema = float(count)
            else:
                ema = alpha * count + (1 - alpha) * ema
            ema_values.append(ema)
        
        if ema_values:
            max_idx = np.argmax(ema_values)
            best_year = all_years[max_idx]
            if best_year == 2022:
                result_2022.append(group)
    
    final_result = {'cpc_groups_best_year_2022': sorted(result_2022), 'count': len(result_2022)}
else:
    final_result = {'cpc_groups_best_year_2022': [], 'count': 0}

print('__RESULT__:')
print(json.dumps(final_result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_records': 277813, 'sample_record': {'cpc': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02E60/10",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/582",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]', 'filing_date': 'dated 5th March 2019'}}, 'var_functions.query_db:10': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}, {'symbol': 'A01N', 'level': '5.0', 'titleFull': 'PRESERVATION OF BODIES OF HUMANS OR ANIMALS OR PLANTS OR PARTS THEREOF; BIOCIDES, e.g. AS DISINFECTANTS, AS PESTICIDES OR AS HERBICIDES; PEST REPELLANTS OR ATTRACTANTS; PLANT GROWTH REGULATORS'}, {'symbol': 'A01P', 'level': '5.0', 'titleFull': 'BIOCIDAL, PEST REPELLANT, PEST ATTRACTANT OR PLANT GROWTH REGULATORY ACTIVITY OF CHEMICAL COMPOUNDS OR PREPARATIONS'}, {'symbol': 'A01D', 'level': '5.0', 'titleFull': 'HARVESTING; MOWING'}, {'symbol': 'A01L', 'level': '5.0', 'titleFull': 'SHOEING OF ANIMALS'}, {'symbol': 'A01K', 'level': '5.0', 'titleFull': 'ANIMAL HUSBANDRY; AVICULTURE; APICULTURE; PISCICULTURE; FISHING; REARING OR BREEDING ANIMALS, NOT OTHERWISE PROVIDED FOR; NEW BREEDS OF ANIMALS'}], 'var_functions.execute_python:12': {'sample_dates': ['dated 5th March 2019', 'March the 18th, 2019', '29th March 2019', 'on March 29th, 2019', '2nd April 2019', 'on April 8th, 2019', '15th April 2019', 'April 19th, 2019', '2019, April 24th', 'April 26th, 2019']}, 'var_functions.execute_python:14': {'total_records_processed': 2675476, 'unique_cpc_groups': 9921, 'year_range': {'min': 1900, 'max': 2024}, 'sample_yearly_counts': [{'cpc_group': 'A01B1', 'year': 1941, 'count': 4}, {'cpc_group': 'A01B1', 'year': 1948, 'count': 2}, {'cpc_group': 'A01B1', 'year': 1950, 'count': 2}, {'cpc_group': 'A01B1', 'year': 1954, 'count': 1}, {'cpc_group': 'A01B1', 'year': 1959, 'count': 1}, {'cpc_group': 'A01B1', 'year': 1967, 'count': 1}, {'cpc_group': 'A01B1', 'year': 1981, 'count': 1}, {'cpc_group': 'A01B1', 'year': 1986, 'count': 2}, {'cpc_group': 'A01B1', 'year': 1990, 'count': 2}, {'cpc_group': 'A01B1', 'year': 1993, 'count': 2}]}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'total_cpc5_symbols': 677, 'sample_symbols': ['B64G', 'B21D', 'F16F', 'F01C', 'H01L', 'D01F', 'B41M', 'A61G', 'F23R', 'F15C']}, 'var_functions.execute_python:24': {'cpc_groups_best_year_2022': [], 'total_found': 0}, 'var_functions.execute_python:26': {'year_range': {'min': 1900, 'max': 2024}, 'unique_cpc_groups': 9921, 'top_groups': [{'cpc_group': 'A61K31', 'total': 31940}, {'cpc_group': 'H01L21', 'total': 29931}, {'cpc_group': 'H01L2224', 'total': 24551}, {'cpc_group': 'G06F3', 'total': 23228}, {'cpc_group': 'A61B5', 'total': 19962}, {'cpc_group': 'H01L2924', 'total': 19121}, {'cpc_group': 'Y10T428', 'total': 17555}, {'cpc_group': 'H04N21', 'total': 16669}, {'cpc_group': 'H01L29', 'total': 16321}, {'cpc_group': 'H04N19', 'total': 16154}, {'cpc_group': 'A61K9', 'total': 15610}, {'cpc_group': 'A61K8', 'total': 11952}, {'cpc_group': 'H01M4', 'total': 11780}, {'cpc_group': 'G02F1', 'total': 11579}, {'cpc_group': 'C07K2317', 'total': 11365}, {'cpc_group': 'G06F16', 'total': 11334}, {'cpc_group': 'H01M10', 'total': 11227}, {'cpc_group': 'H01L23', 'total': 10412}, {'cpc_group': 'A61B17', 'total': 10118}, {'cpc_group': 'G01N33', 'total': 10037}]}, 'var_functions.query_db:28': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A21B', 'level': '5.0'}, {'symbol': 'A21C', 'level': '5.0'}, {'symbol': 'A21D', 'level': '5.0'}, {'symbol': 'A22B', 'level': '5.0'}, {'symbol': 'A22C', 'level': '5.0'}, {'symbol': 'A23B', 'level': '5.0'}, {'symbol': 'A23C', 'level': '5.0'}, {'symbol': 'A23D', 'level': '5.0'}, {'symbol': 'A23F', 'level': '5.0'}, {'symbol': 'A23G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A23K', 'level': '5.0'}, {'symbol': 'A23L', 'level': '5.0'}, {'symbol': 'A23N', 'level': '5.0'}, {'symbol': 'A23P', 'level': '5.0'}, {'symbol': 'A23V', 'level': '5.0'}, {'symbol': 'A24B', 'level': '5.0'}, {'symbol': 'A24C', 'level': '5.0'}, {'symbol': 'A24D', 'level': '5.0'}, {'symbol': 'A24F', 'level': '5.0'}, {'symbol': 'A41B', 'level': '5.0'}, {'symbol': 'A41C', 'level': '5.0'}, {'symbol': 'A41D', 'level': '5.0'}, {'symbol': 'A41F', 'level': '5.0'}, {'symbol': 'A41G', 'level': '5.0'}, {'symbol': 'A41H', 'level': '5.0'}, {'symbol': 'A42B', 'level': '5.0'}, {'symbol': 'A42C', 'level': '5.0'}, {'symbol': 'A43B', 'level': '5.0'}, {'symbol': 'A43C', 'level': '5.0'}, {'symbol': 'A43D', 'level': '5.0'}, {'symbol': 'A44B', 'level': '5.0'}, {'symbol': 'A44C', 'level': '5.0'}, {'symbol': 'A44D', 'level': '5.0'}, {'symbol': 'A45B', 'level': '5.0'}, {'symbol': 'A45C', 'level': '5.0'}, {'symbol': 'A45D', 'level': '5.0'}, {'symbol': 'A45F', 'level': '5.0'}]}

exec(code, env_args)
