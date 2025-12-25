code = """import json
import re

# Load Level 5 CPC symbols
with open(locals()['var_function-call-12897152274516833287'], 'r') as f:
    cpc_level_5_data = json.load(f)

valid_level_5_symbols = set()
for item in cpc_level_5_data:
    symbol = item['symbol']
    valid_level_5_symbols.add(symbol)

print(f"DEBUG: Number of valid Level 5 symbols: {len(valid_level_5_symbols)}")
print(f"DEBUG: Sample symbols: {list(valid_level_5_symbols)[:10]}")

# Load Publication Data
with open(locals()['var_function-call-3331944263005986506'], 'r') as f:
    publication_data = json.load(f)

print(f"DEBUG: Number of publication records: {len(publication_data)}")

def extract_year(date_str):
    if not date_str:
        return None
    match = re.search(r'\b(19|20)\d{2}\b', date_str)
    if match:
        return int(match.group(0))
    return None

counts = {}
years_seen = set()

for i, record in enumerate(publication_data):
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
        
    for entry in cpc_list:
        code = entry.get('code', '')
        if len(code) >= 4:
            prefix = code[:4]
            if prefix in valid_level_5_symbols:
                if prefix not in counts:
                    counts[prefix] = {}
                counts[prefix][year] = counts[prefix].get(year, 0) + 1

print(f"DEBUG: Years seen: {sorted(list(years_seen))}")
print(f"DEBUG: Number of symbols found in data: {len(counts)}")
if len(counts) > 0:
    sample_key = list(counts.keys())[0]
    print(f"DEBUG: Sample counts for {sample_key}: {counts[sample_key]}")

# Check EMA for one sample
alpha = 0.2
results = []
debug_ema = []

for symbol, year_counts in counts.items():
    years = sorted(year_counts.keys())
    if not years:
        continue
        
    min_year = years[0]
    max_year = years[-1]
    
    # If the max year in the data is less than 2022, we can't find 2022 as best year.
    if max_year < 2022:
        continue

    full_years = range(min_year, max_year + 1)
    
    ema = 0
    first = True
    max_ema = -1
    best_year = -1
    
    for y in full_years:
        count = year_counts.get(y, 0)
        if first:
            ema = count
            first = False
        else:
            ema = alpha * count + (1 - alpha) * ema
        
        if ema > max_ema:
            max_ema = ema
            best_year = y
            
    if best_year == 2022:
        results.append(symbol)
    
    if len(debug_ema) < 5:
        debug_ema.append({'symbol': symbol, 'best_year': best_year, 'max_ema': max_ema, 'years': years})

print(f"DEBUG: Sample EMA results: {debug_ema}")
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-12897152274516833287': 'file_storage/function-call-12897152274516833287.json', 'var_function-call-2754207959508784250': 'file_storage/function-call-2754207959508784250.json', 'var_function-call-4967704344600692517': [{'applicationReferences': '[]', 'breakdownCode': 'False', 'childGroups': '[\n  {\n    "description": "",\n    "symbols": [\n      "A41D1/00",\n      "A41D3/00",\n      "A41D5/00",\n      "A41D7/00",\n      "A41D10/00",\n      "A41D11/00",\n      "A41D13/00",\n      "A41D15/00",\n      "A41D17/00",\n      "A41D19/00",\n      "A41D20/00",\n      "A41D23/00",\n      "A41D25/00",\n      "A41D27/00",\n      "A41D29/00",\n      "A41D31/00"\n    ]\n  },\n  {\n    "description": "",\n    "symbols": [\n      "A41D2200/00",\n      "A41D2300/00",\n      "A41D2400/00",\n      "A41D2500/00",\n      "A41D2600/00"\n    ]\n  }\n]', 'children': '[\n  "A41D1/00",\n  "A41D10/00",\n  "A41D11/00",\n  "A41D13/00",\n  "A41D15/00",\n  "A41D17/00",\n  "A41D19/00",\n  "A41D20/00",\n  "A41D2200/00",\n  "A41D23/00",\n  "A41D2300/00",\n  "A41D2400/00",\n  "A41D25/00",\n  "A41D2500/00",\n  "A41D2600/00",\n  "A41D27/00",\n  "A41D29/00",\n  "A41D3/00",\n  "A41D31/00",\n  "A41D5/00",\n  "A41D7/00"\n]', 'dateRevised': '20230201.0', 'definition': '[\n  "Outerwear covers athletic garments, jackets, trousers, shorts, skirts, maternity clothing, overgarments (overcoats, capes), dressing-gowns, bathing costumes, and pyjamas.",\n  "In particular, the following subjects are classified as follows:",\n  "Jackets, e.g. dress jackets or sport coats, are classified in",\n  "Waistcoats, vests, jerseys, sweaters and T-shirts are classified in",\n  "For blouse, e.g. women\'s top, classify in",\n  "For overalls, e.g. coveralls or bodysuits for adult, classify in",\n  "For leggings, e.g. chaps, classify in"\n]', 'glossary': '[\n  {\n    "description": "Dressing-gown",\n    "target": [\n      "a loose gown worn while making one\'s toilet or when in dishabille."\n    ]\n  },\n  {\n    "description": "Jacket",\n    "target": [\n      "lightweight long-sleeve garment typically having a collar and lapel extending below the front sides of the collar providing a central opening between the lapels, also referred to as a dress jacket or sport coat"\n    ]\n  },\n  {\n    "description": "Waistcoat",\n    "target": [\n      "upper body garment without sleeves also referred to as a vest in American English"\n    ]\n  },\n  {\n    "description": "Vest",\n    "target": [\n      "T-shirt or casual top with or without sleeves"\n    ]\n  },\n  {\n    "description": "Jersey",\n    "target": [\n      "knitted garment with or without sleeves, also referred to as a sweater in American English"\n    ]\n  },\n  {\n    "description": "Sweater",\n    "target": [\n      "garment typically worn for playing team sports, also referred to as a jersey in American English"\n    ]\n  },\n  {\n    "description": "Blouse",\n    "target": [\n      "shirt having features specific to women, also referred to as a women\'s top"\n    ]\n  },\n  {\n    "description": "Overalls",\n    "target": [\n      "a one-piece garment having an upper body portion (e.g. short or long sleeve top, bib secured by shoulder straps, etc.) and lower body portion (e.g. pants, shorts, etc.), also referred to as coveralls or bodysuits"\n    ]\n  },\n  {\n    "description": "Leggings",\n    "target": [\n      "lower body overgarment with or without seats for protecting a garment worn underneath, also referred to as chaps"\n    ]\n  },\n  {\n    "description": "Shirt",\n    "target": [\n      "an upper body garment having a collar and an opening at the front which is fastened closed via fastening elements (e.g. buttons) disposed adjacent the opening, also referred to as a men\'s dress shirt, button-up shirt or button-down shirt"\n    ]\n  },\n  {\n    "description": "Chemise",\n    "target": [\n      "undergarment with shoulder strap worn beneath dress or the like, also referred to as a slip"\n    ]\n  },\n  {\n    "description": "Bodices",\n    "target": [\n      "baby garment usually with sleeves but leaving the legs uncovered and fastening means at the crotch, also referred to as a onesie"\n    ]\n  }\n]', 'informativeReferences': '[\n  {\n    "description": "Button down shirt or formal dress shirt",\n    "target": [\n      "A41B1/00"\n    ]\n  },\n  {\n    "description": "Chemise, e.g. slips with shoulder straps worn beneath a dress",\n    "target": [\n      "A41B9/06"\n    ]\n  },\n  {\n    "description": "Chemise, e.g. slips that only cover the lower body",\n    "target": [\n      "A41B9/10"\n    ]\n  },\n  {\n    "description": "Overalls, e.g. coveralls or bodysuits (for babies)",\n    "target": [\n      "A41B13/005"\n    ]\n  },\n  {\n    "description": "Bodices, e.g. baby onesies",\n    "target": [\n      "A41B13/08"\n    ]\n  },\n  {\n    "description": "Straps, bands",\n    "target": [\n      "A45C13/30"\n    ]\n  },\n  {\n    "description": "Carrying straps around neck",\n    "target": [\n      "A45F2003/002"\n    ]\n  },\n  {\n    "description": "Carrying straps around waist",\n    "target": [\n      "A45F3/005"\n    ]\n  },\n  {\n    "description": "Carrying straps",\n    "target": [\n      "A45F3/14"\n    ]\n  },\n  {\n    "description": "Carriers for hand articles",\n    "target": [\n      "A45F5/00"\n    ]\n  },\n  {\n    "description": "Fastening articles to the garment",\n    "target": [\n      "A45F5/02"\n    ]\n  },\n  {\n    "description": "Carriers for holding garments",\n    "target": [\n      "A45F5/06"\n    ]\n  },\n  {\n    "description": "Garment bags",\n    "target": [\n      "A47G25/54"\n    ]\n  },\n  {\n    "description": "Detecting heart/pulse rate for diagnostic purposes, worn by patient",\n    "target": [\n      "A61B5/02438"\n    ]\n  },\n  {\n    "description": "Orthopaedic slings, straps for holding arms",\n    "target": [\n      "A61F5/3746"\n    ]\n  },\n  {\n    "description": "Electromedical stimulation with electrodes",\n    "target": [\n      "A61N1/36014"\n    ]\n  },\n  {\n    "description": "Magnetotherapy",\n    "target": [\n      "A61N2/00"\n    ]\n  },\n  {\n    "description": "Radiation therapy",\n    "target": [\n      "A61N5/00"\n    ]\n  },\n  {\n    "description": "Packaging for clothing",\n    "target": [\n      "B65D85/18"\n    ]\n  },\n  {\n    "description": "Supports for musical instruments, straps",\n    "target": [\n      "G10G5/005"\n    ]\n  }\n]', 'ipcConcordant': 'None', 'level': '5.0', 'limitingReferences': '[]', 'notAllocatable': 'True', 'parents': '[\n  "A41",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[\n  {\n    "description": "",\n    "target": [\n      "A41D1/02"\n    ]\n  },\n  {\n    "description": "",\n    "target": [\n      "A41D1/04"\n    ]\n  },\n  {\n    "description": "",\n    "target": [\n      "A41D1/18"\n    ]\n  },\n  {\n    "description": "",\n    "target": [\n      "A41D13/02"\n    ]\n  },\n  {\n    "description": "",\n    "target": [\n      "A41D17/02"\n    ]\n  }\n]', 'status': 'published', 'symbol': 'A41D', 'synonyms': '[]', 'titleFull': 'OUTERWEAR; PROTECTIVE GARMENTS; ACCESSORIES', 'titlePart': '[\n  "OUTERWEAR",\n  "PROTECTIVE GARMENTS",\n  "ACCESSORIES"\n]'}], 'var_function-call-3343747556887399127': [{'count(*)': '277813'}], 'var_function-call-3331944263005986506': 'file_storage/function-call-3331944263005986506.json', 'var_function-call-7702672752144131909': []}

exec(code, env_args)
