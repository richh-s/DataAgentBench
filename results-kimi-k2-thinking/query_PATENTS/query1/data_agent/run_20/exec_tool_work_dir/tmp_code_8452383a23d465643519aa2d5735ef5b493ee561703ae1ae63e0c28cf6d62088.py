code = """import json
import re
import os

# Access the storage variable using locals()
storage_var = locals()['var_functions.query_db:38']

# Load records from the file
records = []
if isinstance(storage_var, str) and os.path.exists(storage_var):
    with open(storage_var, 'r') as f:
        records = json.load(f)
    print("Loaded records: " + str(len(records)))
else:
    print("Could not access data file")

# Process records
patent_entries = []
for record in records:
    pub_date = record.get('publication_date', '')
    year_match = re.search(r'(\d{4})', pub_date)
    if year_match:
        year = int(year_match.group(1))
        cpc_str = record.get('cpc', '[]')
        try:
            cpc_list = json.loads(cpc_str)
            for cpc_item in cpc_list:
                cpc_code = cpc_item.get('code', '')
                if cpc_code:
                    patent_entries.append({'cpc': cpc_code, 'year': year})
        except:
            continue

print("Extracted entries: " + str(len(patent_entries)))

# Group by level 5 CPC
from collections import defaultdict

def get_level_5_code(cpc_full_code):
    if not cpc_full_code:
        return None
    if '/' in cpc_full_code:
        main_part = cpc_full_code.split('/')[0]
        i = len(main_part) - 1
        while i >= 0 and main_part[i].isdigit():
            i -= 1
        return main_part[:i+1]
    else:
        return cpc_full_code

level_5_counts = defaultdict(lambda: defaultdict(int))
for entry in patent_entries:
    level_5 = get_level_5_code(entry['cpc'])
    if level_5 and len(level_5) >= 3:
        level_5_counts[level_5][entry['year']] += 1

print("Level 5 CPC codes: " + str(len(level_5_counts)))

# Calculate EMA
alpha = 0.2
cpc_best_year = {}
for cpc_code, yearly_counts in level_5_counts.items():
    years = sorted(yearly_counts.keys())
    if not years:
        continue
    ema_values = {years[0]: yearly_counts[years[0]]}
    for i in range(1, len(years)):
        year = years[i]
        current_value = yearly_counts[year]
        prev_ema = ema_values[years[i-1]]
        ema_values[year] = alpha * current_value + (1 - alpha) * prev_ema
    best_year = max(ema_values.keys(), key=lambda y: ema_values[y])
    cpc_best_year[cpc_code] = best_year

# Find CPC codes with best year 2022
cpc_2022_best = [cpc_code for cpc_code, best_year in cpc_best_year.items() if best_year == 2022]

print("2022 best year CPC codes: " + str(len(cpc_2022_best)))

# Return sorted list
result_codes = sorted(cpc_2022_best)
print("__RESULT__:")
print(json.dumps(result_codes))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}, {'symbol': 'A01N', 'level': '5.0', 'titleFull': 'PRESERVATION OF BODIES OF HUMANS OR ANIMALS OR PLANTS OR PARTS THEREOF; BIOCIDES, e.g. AS DISINFECTANTS, AS PESTICIDES OR AS HERBICIDES; PEST REPELLANTS OR ATTRACTANTS; PLANT GROWTH REGULATORS'}, {'symbol': 'A01P', 'level': '5.0', 'titleFull': 'BIOCIDAL, PEST REPELLANT, PEST ATTRACTANT OR PLANT GROWTH REGULATORY ACTIVITY OF CHEMICAL COMPOUNDS OR PREPARATIONS'}, {'symbol': 'A01D', 'level': '5.0', 'titleFull': 'HARVESTING; MOWING'}, {'symbol': 'A01L', 'level': '5.0', 'titleFull': 'SHOEING OF ANIMALS'}, {'symbol': 'A01K', 'level': '5.0', 'titleFull': 'ANIMAL HUSBANDRY; AVICULTURE; APICULTURE; PISCICULTURE; FISHING; REARING OR BREEDING ANIMALS, NOT OTHERWISE PROVIDED FOR; NEW BREEDS OF ANIMALS'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:24': 'initialized', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:36': 'Data loaded: 100 records', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
