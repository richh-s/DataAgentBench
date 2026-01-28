code = """import json
import re

# Load data files
cpc_level5_data = json.loads(open('/root/shared/8be7b2fb-7b6f-4f3f-8b3f-9b7b1b3f7a6f.json').read())
publications_data = json.loads(open('/root/shared/1b7b1b3f-7a6f-4f3f-8b3f-9b7b1b3f7a6f.json').read())

# Create CPC level 5 set
cpc_level5_set = set([item['symbol'] for item in cpc_level5_data])

# Initialize counters
cpc_yearly_counts = {}
valid = 0
invalid = 0

# Process publications
for record in publications_data:
    try:
        # Extract year from publication date
        pub_date = record.get('publication_date', '')
        year_match = re.search(r'(\d{4})', pub_date)
        if not year_match:
            invalid += 1
            continue
        year = int(year_match.group(1))
        if year < 2000 or year > 2030:
            invalid += 1
            continue
        
        # Extract CPC codes
        cpc_json = record.get('cpc', '')
        cpc_codes = json.loads(cpc_json)
        for cpc_item in cpc_codes:
            code = cpc_item.get('code', '')
            if code:
                main_group = code.split('/')[0]
                if main_group in cpc_level5_set:
                    if main_group not in cpc_yearly_counts:
                        cpc_yearly_counts[main_group] = {}
                    cpc_yearly_counts[main_group][year] = cpc_yearly_counts[main_group].get(year, 0) + 1
                    valid += 1
    except:
        invalid += 1

# Calculate EMA
alpha = 0.2
result_codes = []

for cpc_code, yearly_data in cpc_yearly_counts.items():
    years = sorted(yearly_data.keys())
    counts = [yearly_data[year] for year in years]
    
    ema = None
    max_ema = -1
    best_year_idx = 0
    
    for i, count in enumerate(counts):
        ema = count if ema is None else alpha * count + (1 - alpha) * ema
        if ema > max_ema:
            max_ema = ema
            best_year_idx = i
    
    if years[best_year_idx] == 2022:
        result_codes.append(cpc_code)

print('__RESULT__:')
print(json.dumps(result_codes))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:7': ['cpc_definition'], 'var_functions.query_db:8': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:13': 'file_storage/functions.query_db:13.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:26': [{'total_records': '277813'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:29': 'file_storage/functions.query_db:29.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:33': 'file_storage/functions.query_db:33.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:41': 'file_storage/functions.query_db:41.json'}

exec(code, env_args)
