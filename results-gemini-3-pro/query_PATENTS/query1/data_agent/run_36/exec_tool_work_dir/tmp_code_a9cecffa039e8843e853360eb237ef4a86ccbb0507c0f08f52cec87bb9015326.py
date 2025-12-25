code = """import json
import re

# Load Level 5 symbols
with open('var_function-call-483881578667801507.json', 'r') as f:
    level5_data = json.load(f)
level5_symbols = set(item['symbol'] for item in level5_data)

# Load patent data
with open('var_function-call-15113980107006050527.json', 'r') as f:
    patents = json.load(f)

# Regex for year
year_pattern = re.compile(r'\b(19|20)\d{2}\b')

# Aggregation: symbol -> year -> count
counts = {}

for p in patents:
    fdate = p.get('filing_date', '')
    if not fdate:
        continue
    
    # Extract year
    match = year_pattern.search(fdate)
    if not match:
        continue
    year = int(match.group(0))
    
    # Extract CPC
    cpc_str = p.get('cpc', '')
    if not cpc_str:
        continue
    
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
        
    # Get unique level 5 codes for this patent
    patent_codes = set()
    for item in cpc_list:
        code = item.get('code', '')
        if len(code) >= 4:
            sub = code[:4]
            if sub in level5_symbols:
                patent_codes.add(sub)
    
    # Update counts
    for code in patent_codes:
        if code not in counts:
            counts[code] = {}
        counts[code][year] = counts[code].get(year, 0) + 1

# Determine global year range
all_years = set()
for c in counts:
    all_years.update(counts[c].keys())

if not all_years:
    print("__RESULT__:")
    print("[]")
else:
    min_year = min(all_years)
    max_year = max(all_years)
    
    # Calculate EMA and find best year
    result_codes = []
    
    for code, year_counts in counts.items():
        ema = None
        max_ema = -1
        best_year = -1
        
        # Iterate through the full range of years for correct time series
        # Or should we iterate from the first year specific to the code?
        # "Moving average" implies continuity.
        # I'll iterate from min_year to max_year.
        # If no filings before, EMA stays 0 (or undefined until first filing).
        # Standard EMA usually starts from first observation.
        
        # Let's find first year for this code
        code_years = sorted(year_counts.keys())
        if not code_years:
            continue
        first_code_year = code_years[0]
        
        # Iterate from first_code_year to max_year
        for y in range(first_code_year, max_year + 1):
            val = year_counts.get(y, 0)
            if ema is None:
                ema = val
            else:
                ema = 0.2 * val + 0.8 * ema
            
            if ema > max_ema:
                max_ema = ema
                best_year = y
            elif ema == max_ema:
                # If equal, prefer the later year? Or earlier?
                # Usually "peak" is the highest. If tie, maybe keep the latest.
                # But float equality is rare.
                best_year = y
        
        if best_year == 2022:
            result_codes.append(code)

    print("__RESULT__:")
    print(json.dumps(result_codes))"""

env_args = {'var_function-call-1503751298057536887': [{'symbol': 'A01H'}, {'symbol': 'A01F'}, {'symbol': 'A01C'}, {'symbol': 'A01G'}, {'symbol': 'A23J'}, {'symbol': 'A01N'}, {'symbol': 'A01P'}, {'symbol': 'A01D'}, {'symbol': 'A01L'}, {'symbol': 'A01K'}], 'var_function-call-1503751298057535580': [{'COUNT(*)': '277813'}], 'var_function-call-3975318486678292011': [{'level': '4.0', 'symbol': 'A01', 'titleFull': 'AGRICULTURE; FORESTRY; ANIMAL HUSBANDRY; HUNTING; TRAPPING; FISHING'}, {'level': '4.0', 'symbol': 'A21', 'titleFull': 'BAKING; EDIBLE DOUGHS'}, {'level': '4.0', 'symbol': 'A22', 'titleFull': 'BUTCHERING; MEAT TREATMENT; PROCESSING POULTRY OR FISH'}, {'level': '4.0', 'symbol': 'A23', 'titleFull': 'FOODS OR FOODSTUFFS; TREATMENT THEREOF, NOT COVERED BY OTHER CLASSES'}, {'level': '4.0', 'symbol': 'A24', 'titleFull': "TOBACCO; CIGARS; CIGARETTES; SIMULATED SMOKING DEVICES; SMOKERS' REQUISITES"}, {'level': '4.0', 'symbol': 'A41', 'titleFull': 'WEARING APPAREL'}, {'level': '4.0', 'symbol': 'A42', 'titleFull': 'HEADWEAR'}, {'level': '4.0', 'symbol': 'A43', 'titleFull': 'FOOTWEAR'}, {'level': '4.0', 'symbol': 'A44', 'titleFull': 'HABERDASHERY; JEWELLERY'}, {'level': '4.0', 'symbol': 'A45', 'titleFull': 'HAND OR TRAVELLING ARTICLES'}, {'level': '4.0', 'symbol': 'A46', 'titleFull': 'BRUSHWARE'}, {'level': '4.0', 'symbol': 'A47', 'titleFull': 'FURNITURE; DOMESTIC ARTICLES OR APPLIANCES; COFFEE MILLS; SPICE MILLS; SUCTION CLEANERS IN GENERAL'}, {'level': '4.0', 'symbol': 'A61', 'titleFull': 'MEDICAL OR VETERINARY SCIENCE; HYGIENE'}, {'level': '4.0', 'symbol': 'A62', 'titleFull': 'LIFE-SAVING; FIRE-FIGHTING'}, {'level': '4.0', 'symbol': 'A63', 'titleFull': 'SPORTS; GAMES; AMUSEMENTS'}, {'level': '4.0', 'symbol': 'A99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION'}, {'level': '4.0', 'symbol': 'B01', 'titleFull': 'PHYSICAL OR CHEMICAL PROCESSES OR APPARATUS IN GENERAL'}, {'level': '4.0', 'symbol': 'B02', 'titleFull': 'CRUSHING, PULVERISING, OR DISINTEGRATING; PREPARATORY TREATMENT OF GRAIN FOR MILLING'}, {'level': '4.0', 'symbol': 'B03', 'titleFull': 'SEPARATION OF SOLID MATERIALS USING LIQUIDS OR USING PNEUMATIC TABLES OR JIGS; MAGNETIC OR ELECTROSTATIC SEPARATION OF SOLID MATERIALS FROM SOLID MATERIALS OR FLUIDS; SEPARATION BY HIGH-VOLTAGE ELECTRIC FIELDS'}, {'level': '4.0', 'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}], 'var_function-call-4474426584226387452': [{'level': '5.0', 'symbol': 'A62B'}, {'level': '5.0', 'symbol': 'A63G'}, {'level': '5.0', 'symbol': 'A63K'}, {'level': '5.0', 'symbol': 'A63B'}, {'level': '7.0', 'symbol': 'C13B50/00'}], 'var_function-call-227886120050006717': [{'cpc': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02E60/10",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/582",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_function-call-4039319436300256404': [{'length': '4', 'count': '677'}], 'var_function-call-483881578667801507': 'file_storage/function-call-483881578667801507.json', 'var_function-call-15113980107006050527': 'file_storage/function-call-15113980107006050527.json'}

exec(code, env_args)
