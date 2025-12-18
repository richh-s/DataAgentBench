code = """import pandas as pd
import json
import re

# Load the full result from the JSON file for patent publications
with open(locals()['var_function-call-14622800233827138684'], 'r') as f:
    publication_data = json.load(f)

# Load the full result from the JSON file for CPC definitions (level 5)
with open(locals()['var_function-call-16156661485933672654'], 'r') as f:
    cpc_definition_data = json.load(f)

# Extract level 5 CPC symbols as a set for efficient lookup
level_5_cpc_symbols_set = set([entry['symbol'] for entry in cpc_definition_data])

# Function to extract the relevant level 5 CPC code from a full CPC code
def get_level_5_match(cpc_code_full):
    # Generate possible prefixes that could be level 5 symbols
    parts = []
    current_part = ""
    for char in cpc_code_full:
        if char == '/':
            break
        current_part += char
        parts.append(current_part)

    # Iterate through parts from longest to shortest to find the most specific level 5 match
    for part in reversed(parts):
        if part in level_5_cpc_symbols_set:
            return part
    return None # No level 5 match found

records = []
for entry in publication_data:
    filing_date_str = entry.get('filing_date')
    cpc_data = entry.get('cpc')

    if filing_date_str and cpc_data:
        # Efficiently extract year using regex
        year_match = re.search(r'\\b(19|20)\\d{2}\\b', filing_date_str)
        if not year_match:
            continue # Skip if year cannot be extracted
        filing_year = int(year_match.group(0))

        try:
            cpc_list = json.loads(cpc_data)
            for cpc_item in cpc_list:
                cpc_code_full = cpc_item.get('code')
                if cpc_code_full:
                    matched_level_5_code = get_level_5_match(cpc_code_full)
                    if matched_level_5_code:
                        records.append({'cpc_code': matched_level_5_code, 'filing_year': filing_year})

        except json.JSONDecodeError:
            continue # Skip if cpc_data is not valid JSON

df = pd.DataFrame(records)

# If df is empty, return an empty list
if df.empty:
    print("__RESULT__:")
    print(json.dumps([]))
else:
    # Count patent filings per CPC code per year
    filings_per_year = df.groupby(['cpc_code', 'filing_year']).size().reset_index(name='filings')

    # Calculate EMA
    smoothing_factor = 0.2

    # Sort by cpc_code and filing_year for efficient grouped EMA calculation
    filings_per_year = filings_per_year.sort_values(by=['cpc_code', 'filing_year'])

    # Calculate EMA within each cpc_code group using transform
    filings_per_year['ema'] = filings_per_year.groupby('cpc_code')['filings'].transform(
        lambda x: x.ewm(alpha=smoothing_factor, adjust=False).mean()
    )

    # Find the year with the highest EMA for each CPC code
    best_ema_year = filings_per_year.loc[filings_per_year.groupby('cpc_code')['ema'].idxmax()]

    # Filter for CPC codes whose best year is 2022
    cpc_codes_2022_best = best_ema_year[best_ema_year['filing_year'] == 2022]['cpc_code'].tolist()

    print("__RESULT__:")
    print(json.dumps(cpc_codes_2022_best))"""

env_args = {'var_function-call-16036621143290588479': ['publicationinfo'], 'var_function-call-17677642065960427698': 'file_storage/function-call-17677642065960427698.json', 'var_function-call-6409921778620027728': ['cpc_definition'], 'var_function-call-14622800233827138684': 'file_storage/function-call-14622800233827138684.json', 'var_function-call-18355725859426800648': 'file_storage/function-call-18355725859426800648.json', 'var_function-call-3356983374149566720': 'file_storage/function-call-3356983374149566720.json', 'var_function-call-1410682702598000053': [], 'var_function-call-15455879809922809981': [{'symbol': 'A01H', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES', 'level': '5.0'}, {'symbol': 'A01F', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE', 'level': '5.0'}, {'symbol': 'A01C', 'titleFull': 'PLANTING; SOWING; FERTILISING', 'level': '5.0'}, {'symbol': 'A01G', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING', 'level': '5.0'}, {'symbol': 'A23J', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS', 'level': '5.0'}, {'symbol': 'A01N', 'titleFull': 'PRESERVATION OF BODIES OF HUMANS OR ANIMALS OR PLANTS OR PARTS THEREOF; BIOCIDES, e.g. AS DISINFECTANTS, AS PESTICIDES OR AS HERBICIDES; PEST REPELLANTS OR ATTRACTANTS; PLANT GROWTH REGULATORS', 'level': '5.0'}, {'symbol': 'A01P', 'titleFull': 'BIOCIDAL, PEST REPELLANT, PEST ATTRACTANT OR PLANT GROWTH REGULATORY ACTIVITY OF CHEMICAL COMPOUNDS OR PREPARATIONS', 'level': '5.0'}, {'symbol': 'A01D', 'titleFull': 'HARVESTING; MOWING', 'level': '5.0'}, {'symbol': 'A01L', 'titleFull': 'SHOEING OF ANIMALS', 'level': '5.0'}, {'symbol': 'A01K', 'titleFull': 'ANIMAL HUSBANDRY; AVICULTURE; APICULTURE; PISCICULTURE; FISHING; REARING OR BREEDING ANIMALS, NOT OTHERWISE PROVIDED FOR; NEW BREEDS OF ANIMALS', 'level': '5.0'}], 'var_function-call-13030963289959727673': 'file_storage/function-call-13030963289959727673.json', 'var_function-call-16156661485933672654': 'file_storage/function-call-16156661485933672654.json'}

exec(code, env_args)
