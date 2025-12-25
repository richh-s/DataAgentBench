code = """import json
import re

# Load Level 5 CPC symbols
with open(locals()['var_function-call-12897152274516833287'], 'r') as f:
    cpc_level_5_data = json.load(f)

valid_level_5_symbols = set()
for item in cpc_level_5_data:
    symbol = item['symbol']
    valid_level_5_symbols.add(symbol)

# Load Publication Data
with open(locals()['var_function-call-3331944263005986506'], 'r') as f:
    publication_data = json.load(f)

def extract_year(date_str):
    if not date_str:
        return None
    # Use simple regex [0-9]{4} to avoid JSON escaping issues with backslash
    match = re.search(r'[0-9]{4}', date_str)
    if match:
        y = int(match.group(0))
        if 1900 <= y <= 2100:
            return y
    return None

counts = {}
years_seen = set()

for record in publication_data:
    year = extract_year(record.get('filing_date'))
    if year:
        years_seen.add(year)
    
    if year is None:
        continue
    
    cpc_json = record.get('cpc')
    if not cpc_json:
        continue
    
    try:
        cpc_list = json.loads(cpc_json)
    except:
        continue
        
    # Per patent, track unique Level 5 symbols to avoid double counting
    patent_symbols = set()
    for entry in cpc_list:
        code = entry.get('code', '')
        if len(code) >= 4:
            prefix = code[:4]
            if prefix in valid_level_5_symbols:
                patent_symbols.add(prefix)
    
    for symbol in patent_symbols:
        if symbol not in counts:
            counts[symbol] = {}
        counts[symbol][year] = counts[symbol].get(year, 0) + 1

# Calculate EMA and find Best Year
alpha = 0.2
results = []

# Determine global year range to handle zeros properly?
# EMA definition usually iterates through available data points or time steps.
# If a year has 0 filings, should EMA decay? Yes.
# So we need the full range of years [min_year_global, max_year_global] or [min_year_symbol, max_year_symbol].
# Usually EMA is calculated over the timeline of the entity.
# I'll use [min_year_symbol, max_year_symbol] or maybe [min_year_global, 2022].
# "Best year is 2022" implies we consider the trajectory up to 2022.
# If max_year in data is > 2022, we should include it.
# I'll use the range [min_year_seen, max_year_seen] for all symbols to be fair?
# Or just per symbol?
# "highest exponential moving average of patent filings each year... whose best year is 2022"
# This implies comparing EMA(year) for all years.
# I will use the range of years present in the dataset (min_global to max_global).

if years_seen:
    global_min_year = min(years_seen)
    global_max_year = max(years_seen)
else:
    global_min_year = 2000
    global_max_year = 2022

for symbol, year_counts in counts.items():
    ema = 0
    first = True
    max_ema = -1.0
    best_year = -1
    
    # We should probably start from the first year the symbol appeared?
    # Or from global start?
    # If we start from global start with 0s, EMA will stay 0 until first appearance.
    # If we start from first appearance, init is Count.
    # I'll start from the first year the symbol has a filing.
    
    symbol_years = sorted(year_counts.keys())
    if not symbol_years:
        continue
        
    start_y = symbol_years[0]
    # We must go up to at least 2022 to check if 2022 is the best.
    # If data goes beyond 2022, we must check those too.
    end_y = max(global_max_year, 2022) 
    
    # Iterate year by year
    for y in range(start_y, end_y + 1):
        count = year_counts.get(y, 0)
        
        if first:
            ema = count
            first = False
        else:
            ema = alpha * count + (1 - alpha) * ema
        
        if ema > max_ema:
            max_ema = ema
            best_year = y
            
    # Check condition
    if best_year == 2022:
        results.append(symbol)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-12897152274516833287': 'file_storage/function-call-12897152274516833287.json', 'var_function-call-2754207959508784250': 'file_storage/function-call-2754207959508784250.json', 'var_function-call-4967704344600692517': [{'applicationReferences': '[]', 'breakdownCode': 'False', 'childGroups': '[\n  {\n    "description": "",\n    "symbols": [\n      "A41D1/00",\n      "A41D3/00",\n      "A41D5/00",\n      "A41D7/00",\n      "A41D10/00",\n      "A41D11/00",\n      "A41D13/00",\n      "A41D15/00",\n      "A41D17/00",\n      "A41D19/00",\n      "A41D20/00",\n      "A41D23/00",\n      "A41D25/00",\n      "A41D27/00",\n      "A41D29/00",\n      "A41D31/00"\n    ]\n  },\n  {\n    "description": "",\n    "symbols": [\n      "A41D2200/00",\n      "A41D2300/00",\n      "A41D2400/00",\n      "A41D2500/00",\n      "A41D2600/00"\n    ]\n  }\n]', 'children': '[\n  "A41D1/00",\n  "A41D10/00",\n  "A41D11/00",\n  "A41D13/00",\n  "A41D15/00",\n  "A41D17/00",\n  "A41D19/00",\n  "A41D20/00",\n  "A41D2200/00",\n  "A41D23/00",\n  "A41D2300/00",\n  "A41D2400/00",\n  "A41D25/00",\n  "A41D2500/00",\n  "A41D2600/00",\n  "A41D27/00",\n  "A41D29/00",\n  "A41D3/00",\n  "A41D31/00",\n  "A41D5/00",\n  "A41D7/00"\n]', 'dateRevised': '20230201.0', 'definition': '[\n  "Outerwear covers athletic garments, jackets, trousers, shorts, skirts, maternity clothing, overgarments (overcoats, capes), dressing-gowns, bathing costumes, and pyjamas.",\n  "In particular, the following subjects are classified as follows:",\n  "Jackets, e.g. dress jackets or sport coats, are classified in",\n  "Waistcoats, vests, jerseys, sweaters and T-shirts are classified in",\n  "For blouse, e.g. women\'s top, classify in",\n  "For overalls, e.g. coveralls or bodysuits for adult, classify in",\n  "For leggings, e.g. chaps, classify in"\n]', 'glossary': '[\n  {\n    "description": "Dressing-gown",\n    "target": [\n      "a loose gown worn while making one\'s toilet or when in dishabille."\n    ]\n  },\n  {\n    "description": "Jacket",\n    "target": [\n      "lightweight long-sleeve garment typically having a collar and lapel extending below the front sides of the collar providing a central opening between the lapels, also referred to as a dress jacket or sport coat"\n    ]\n  },\n  {\n    "description": "Waistcoat",\n    "target": [\n      "upper body garment without sleeves also referred to as a vest in American English"\n    ]\n  },\n  {\n    "description": "Vest",\n    "target": [\n      "T-shirt or casual top with or without sleeves"\n    ]\n  },\n  {\n    "description": "Jersey",\n    "target": [\n      "knitted garment with or without sleeves, also referred to as a sweater in American English"\n    ]\n  },\n  {\n    "description": "Sweater",\n    "target": [\n      "garment typically worn for playing team sports, also referred to as a jersey in American English"\n    ]\n  },\n  {\n    "description": "Blouse",\n    "target": [\n      "shirt having features specific to women, also referred to as a women\'s top"\n    ]\n  },\n  {\n    "description": "Overalls",\n    "target": [\n      "a one-piece garment having an upper body portion (e.g. short or long sleeve top, bib secured by shoulder straps, etc.) and lower body portion (e.g. pants, shorts, etc.), also referred to as coveralls or bodysuits"\n    ]\n  },\n  {\n    "description": "Leggings",\n    "target": [\n      "lower body overgarment with or without seats for protecting a garment worn underneath, also referred to as chaps"\n    ]\n  },\n  {\n    "description": "Shirt",\n    "target": [\n      "an upper body garment having a collar and an opening at the front which is fastened closed via fastening elements (e.g. buttons) disposed adjacent the opening, also referred to as a men\'s dress shirt, button-up shirt or button-down shirt"\n    ]\n  },\n  {\n    "description": "Chemise",\n    "target": [\n      "undergarment with shoulder strap worn beneath dress or the like, also referred to as a slip"\n    ]\n  },\n  {\n    "description": "Bodices",\n    "target": [\n      "baby garment usually with sleeves but leaving the legs uncovered and fastening means at the crotch, also referred to as a onesie"\n    ]\n  }\n]', 'informativeReferences': '[\n  {\n    "description": "Button down shirt or formal dress shirt",\n    "target": [\n      "A41B1/00"\n    ]\n  },\n  {\n    "description": "Chemise, e.g. slips with shoulder straps worn beneath a dress",\n    "target": [\n      "A41B9/06"\n    ]\n  },\n  {\n    "description": "Chemise, e.g. slips that only cover the lower body",\n    "target": [\n      "A41B9/10"\n    ]\n  },\n  {\n    "description": "Overalls, e.g. coveralls or bodysuits (for babies)",\n    "target": [\n      "A41B13/005"\n    ]\n  },\n  {\n    "description": "Bodices, e.g. baby onesies",\n    "target": [\n      "A41B13/08"\n    ]\n  },\n  {\n    "description": "Straps, bands",\n    "target": [\n      "A45C13/30"\n    ]\n  },\n  {\n    "description": "Carrying straps around neck",\n    "target": [\n      "A45F2003/002"\n    ]\n  },\n  {\n    "description": "Carrying straps around waist",\n    "target": [\n      "A45F3/005"\n    ]\n  },\n  {\n    "description": "Carrying straps",\n    "target": [\n      "A45F3/14"\n    ]\n  },\n  {\n    "description": "Carriers for hand articles",\n    "target": [\n      "A45F5/00"\n    ]\n  },\n  {\n    "description": "Fastening articles to the garment",\n    "target": [\n      "A45F5/02"\n    ]\n  },\n  {\n    "description": "Carriers for holding garments",\n    "target": [\n      "A45F5/06"\n    ]\n  },\n  {\n    "description": "Garment bags",\n    "target": [\n      "A47G25/54"\n    ]\n  },\n  {\n    "description": "Detecting heart/pulse rate for diagnostic purposes, worn by patient",\n    "target": [\n      "A61B5/02438"\n    ]\n  },\n  {\n    "description": "Orthopaedic slings, straps for holding arms",\n    "target": [\n      "A61F5/3746"\n    ]\n  },\n  {\n    "description": "Electromedical stimulation with electrodes",\n    "target": [\n      "A61N1/36014"\n    ]\n  },\n  {\n    "description": "Magnetotherapy",\n    "target": [\n      "A61N2/00"\n    ]\n  },\n  {\n    "description": "Radiation therapy",\n    "target": [\n      "A61N5/00"\n    ]\n  },\n  {\n    "description": "Packaging for clothing",\n    "target": [\n      "B65D85/18"\n    ]\n  },\n  {\n    "description": "Supports for musical instruments, straps",\n    "target": [\n      "G10G5/005"\n    ]\n  }\n]', 'ipcConcordant': 'None', 'level': '5.0', 'limitingReferences': '[]', 'notAllocatable': 'True', 'parents': '[\n  "A41",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[\n  {\n    "description": "",\n    "target": [\n      "A41D1/02"\n    ]\n  },\n  {\n    "description": "",\n    "target": [\n      "A41D1/04"\n    ]\n  },\n  {\n    "description": "",\n    "target": [\n      "A41D1/18"\n    ]\n  },\n  {\n    "description": "",\n    "target": [\n      "A41D13/02"\n    ]\n  },\n  {\n    "description": "",\n    "target": [\n      "A41D17/02"\n    ]\n  }\n]', 'status': 'published', 'symbol': 'A41D', 'synonyms': '[]', 'titleFull': 'OUTERWEAR; PROTECTIVE GARMENTS; ACCESSORIES', 'titlePart': '[\n  "OUTERWEAR",\n  "PROTECTIVE GARMENTS",\n  "ACCESSORIES"\n]'}], 'var_function-call-3343747556887399127': [{'count(*)': '277813'}], 'var_function-call-3331944263005986506': 'file_storage/function-call-3331944263005986506.json', 'var_function-call-7702672752144131909': [], 'var_function-call-5634381672666200725': [], 'var_function-call-4981711249810845324': {'num_level_5_symbols': 677, 'num_records': 277813, 'years_seen': [], 'num_symbols_found_in_data': 0, 'total_cpc_matches': 0, 'sample_counts': None}, 'var_function-call-14387484744382783114': [{'date': 'dated 5th March 2019', 'extracted': 'No Match'}, {'date': 'March the 18th, 2019', 'extracted': 'No Match'}, {'date': '29th March 2019', 'extracted': 'No Match'}, {'date': 'on March 29th, 2019', 'extracted': 'No Match'}, {'date': '2nd April 2019', 'extracted': 'No Match'}, {'date': 'on April 8th, 2019', 'extracted': 'No Match'}, {'date': '15th April 2019', 'extracted': 'No Match'}, {'date': 'April 19th, 2019', 'extracted': 'No Match'}, {'date': '2019, April 24th', 'extracted': 'No Match'}, {'date': 'April 26th, 2019', 'extracted': 'No Match'}, {'date': 'on April 30th, 2019', 'extracted': 'No Match'}, {'date': 'dated 1st May 2019', 'extracted': 'No Match'}, {'date': '2019, May 15th', 'extracted': 'No Match'}, {'date': 'May 15th, 2019', 'extracted': 'No Match'}, {'date': 'June the 6th, 2019', 'extracted': 'No Match'}, {'date': 'on June 7th, 2019', 'extracted': 'No Match'}, {'date': '14th of June, 2019', 'extracted': 'No Match'}, {'date': '2019 on Jun 14th', 'extracted': 'No Match'}, {'date': 'dated 18th June 2019', 'extracted': 'No Match'}, {'date': 'June the 19th, 2019', 'extracted': 'No Match'}]}

exec(code, env_args)
