code = """import json
import re

# Load Filings
with open(locals()['var_function-call-7782197232993617340'], 'r') as f:
    filings_data = json.load(f)

# Load Level 5 CPC symbols
with open(locals()['var_function-call-16702837744120307450'], 'r') as f:
    cpc_level5_data = json.load(f)

valid_cpc_level5 = set()
for item in cpc_level5_data:
    if 'symbol' in item:
        valid_cpc_level5.add(item['symbol'])

debug_info = {}

# Check Years
years = set()
sample_dates = []
for filing in filings_data[:100]:
    f_date = filing.get('filing_date', '')
    if f_date:
        sample_dates.append(f_date)
        match = re.search(r'\b(18|19|20)\d{2}\b', f_date)
        if match:
            years.add(int(match.group(0)))

# Check CPC matching
sample_cpc_codes = []
matched_codes = set()
for filing in filings_data[:100]:
    cpc_json_str = filing.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_json_str)
        for entry in cpc_list:
            code = entry.get('code', '')
            sample_cpc_codes.append(code)
            if len(code) >= 4:
                subclass = code[:4]
                if subclass in valid_cpc_level5:
                    matched_codes.add(subclass)
    except:
        pass

debug_info['sample_dates'] = sample_dates
debug_info['extracted_years'] = list(years)
debug_info['sample_cpc_codes'] = sample_cpc_codes[:10]
debug_info['matched_codes_sample'] = list(matched_codes)
debug_info['total_valid_level5'] = len(valid_cpc_level5)
debug_info['valid_level5_sample'] = list(valid_cpc_level5)[:10]

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-15891582207541011171': 'file_storage/function-call-15891582207541011171.json', 'var_function-call-11737208954615889978': [{'count(*)': '277813'}], 'var_function-call-16702837744120307450': 'file_storage/function-call-16702837744120307450.json', 'var_function-call-1429926228084239010': [{'symbol': 'A01K2227/108', 'level': '9.0', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'level': '9.0', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'level': '9.0', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'level': '9.0', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'level': '9.0', 'titleFull': 'Ovine'}, {'symbol': 'A01K2227/106', 'level': '9.0', 'titleFull': 'Primate'}, {'symbol': 'A01K2227/706', 'level': '9.0', 'titleFull': 'Insects, e.g. Drosophila melanogaster, medfly'}, {'symbol': 'A01K2227/703', 'level': '9.0', 'titleFull': 'Worms, e.g. Caenorhabdities elegans'}, {'symbol': 'A01K2267/025', 'level': '9.0', 'titleFull': 'Animal producing cells or organs for transplantation'}, {'symbol': 'A01K2267/0393', 'level': '9.0', 'titleFull': 'Animal model comprising a reporter system for screening tests'}], 'var_function-call-7073709861002867650': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}, {'symbol': 'A01N', 'level': '5.0', 'titleFull': 'PRESERVATION OF BODIES OF HUMANS OR ANIMALS OR PLANTS OR PARTS THEREOF; BIOCIDES, e.g. AS DISINFECTANTS, AS PESTICIDES OR AS HERBICIDES; PEST REPELLANTS OR ATTRACTANTS; PLANT GROWTH REGULATORS'}, {'symbol': 'A01P', 'level': '5.0', 'titleFull': 'BIOCIDAL, PEST REPELLANT, PEST ATTRACTANT OR PLANT GROWTH REGULATORY ACTIVITY OF CHEMICAL COMPOUNDS OR PREPARATIONS'}, {'symbol': 'A01D', 'level': '5.0', 'titleFull': 'HARVESTING; MOWING'}, {'symbol': 'A01L', 'level': '5.0', 'titleFull': 'SHOEING OF ANIMALS'}, {'symbol': 'A01K', 'level': '5.0', 'titleFull': 'ANIMAL HUSBANDRY; AVICULTURE; APICULTURE; PISCICULTURE; FISHING; REARING OR BREEDING ANIMALS, NOT OTHERWISE PROVIDED FOR; NEW BREEDS OF ANIMALS'}], 'var_function-call-7782197232993617340': 'file_storage/function-call-7782197232993617340.json', 'var_function-call-2550816962134600101': []}

exec(code, env_args)
