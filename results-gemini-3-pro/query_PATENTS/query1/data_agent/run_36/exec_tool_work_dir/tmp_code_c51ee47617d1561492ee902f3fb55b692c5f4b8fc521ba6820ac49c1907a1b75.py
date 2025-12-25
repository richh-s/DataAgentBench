code = """import json
import re

path_level5 = locals()['var_function-call-483881578667801507']
path_patents = locals()['var_function-call-15113980107006050527']

with open(path_level5, 'r') as f:
    level5_data = json.load(f)
level5_symbols = set(item['symbol'] for item in level5_data)

with open(path_patents, 'r') as f:
    patents = json.load(f)

# Use safer regex
year_pattern = re.compile(r'(19|20)\d{2}')

counts = {}
years_found = set()

for p in patents:
    fdate = p.get('filing_date', '')
    if not fdate:
        continue
    match = year_pattern.search(fdate)
    if not match:
        continue
    year = int(match.group(0))
    # Filter reasonable years to avoid noise
    if year < 1900 or year > 2030:
        continue
        
    years_found.add(year)
    
    cpc_str = p.get('cpc', '')
    if not cpc_str:
        continue
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
        
    patent_codes = set()
    for item in cpc_list:
        code = item.get('code', '')
        if len(code) >= 4:
            sub = code[:4]
            if sub in level5_symbols:
                patent_codes.add(sub)
    
    for code in patent_codes:
        if code not in counts:
            counts[code] = {}
        counts[code][year] = counts[code].get(year, 0) + 1

if not years_found:
    print("__RESULT__:")
    print(json.dumps("No years found"))
else:
    min_year_global = min(years_found)
    max_year_global = max(years_found)
    
    # Calculate EMA
    best_years = {}
    for code, year_counts in counts.items():
        ema = None
        max_ema = -1.0
        best_y = -1
        
        code_years = sorted(year_counts.keys())
        first_code_year = code_years[0]
        
        # Iterate from first year of this code to global max
        for y in range(first_code_year, max_year_global + 1):
            val = year_counts.get(y, 0)
            if ema is None:
                ema = float(val)
            else:
                ema = 0.2 * val + 0.8 * ema
            
            if ema > max_ema:
                max_ema = ema
                best_y = y
        
        best_years[code] = best_y

    # Result
    res = [code for code, y in best_years.items() if y == 2022]
    
    # Sort for deterministic output
    res.sort()
    
    print("__RESULT__:")
    print(json.dumps(res))"""

env_args = {'var_function-call-1503751298057536887': [{'symbol': 'A01H'}, {'symbol': 'A01F'}, {'symbol': 'A01C'}, {'symbol': 'A01G'}, {'symbol': 'A23J'}, {'symbol': 'A01N'}, {'symbol': 'A01P'}, {'symbol': 'A01D'}, {'symbol': 'A01L'}, {'symbol': 'A01K'}], 'var_function-call-1503751298057535580': [{'COUNT(*)': '277813'}], 'var_function-call-3975318486678292011': [{'level': '4.0', 'symbol': 'A01', 'titleFull': 'AGRICULTURE; FORESTRY; ANIMAL HUSBANDRY; HUNTING; TRAPPING; FISHING'}, {'level': '4.0', 'symbol': 'A21', 'titleFull': 'BAKING; EDIBLE DOUGHS'}, {'level': '4.0', 'symbol': 'A22', 'titleFull': 'BUTCHERING; MEAT TREATMENT; PROCESSING POULTRY OR FISH'}, {'level': '4.0', 'symbol': 'A23', 'titleFull': 'FOODS OR FOODSTUFFS; TREATMENT THEREOF, NOT COVERED BY OTHER CLASSES'}, {'level': '4.0', 'symbol': 'A24', 'titleFull': "TOBACCO; CIGARS; CIGARETTES; SIMULATED SMOKING DEVICES; SMOKERS' REQUISITES"}, {'level': '4.0', 'symbol': 'A41', 'titleFull': 'WEARING APPAREL'}, {'level': '4.0', 'symbol': 'A42', 'titleFull': 'HEADWEAR'}, {'level': '4.0', 'symbol': 'A43', 'titleFull': 'FOOTWEAR'}, {'level': '4.0', 'symbol': 'A44', 'titleFull': 'HABERDASHERY; JEWELLERY'}, {'level': '4.0', 'symbol': 'A45', 'titleFull': 'HAND OR TRAVELLING ARTICLES'}, {'level': '4.0', 'symbol': 'A46', 'titleFull': 'BRUSHWARE'}, {'level': '4.0', 'symbol': 'A47', 'titleFull': 'FURNITURE; DOMESTIC ARTICLES OR APPLIANCES; COFFEE MILLS; SPICE MILLS; SUCTION CLEANERS IN GENERAL'}, {'level': '4.0', 'symbol': 'A61', 'titleFull': 'MEDICAL OR VETERINARY SCIENCE; HYGIENE'}, {'level': '4.0', 'symbol': 'A62', 'titleFull': 'LIFE-SAVING; FIRE-FIGHTING'}, {'level': '4.0', 'symbol': 'A63', 'titleFull': 'SPORTS; GAMES; AMUSEMENTS'}, {'level': '4.0', 'symbol': 'A99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION'}, {'level': '4.0', 'symbol': 'B01', 'titleFull': 'PHYSICAL OR CHEMICAL PROCESSES OR APPARATUS IN GENERAL'}, {'level': '4.0', 'symbol': 'B02', 'titleFull': 'CRUSHING, PULVERISING, OR DISINTEGRATING; PREPARATORY TREATMENT OF GRAIN FOR MILLING'}, {'level': '4.0', 'symbol': 'B03', 'titleFull': 'SEPARATION OF SOLID MATERIALS USING LIQUIDS OR USING PNEUMATIC TABLES OR JIGS; MAGNETIC OR ELECTROSTATIC SEPARATION OF SOLID MATERIALS FROM SOLID MATERIALS OR FLUIDS; SEPARATION BY HIGH-VOLTAGE ELECTRIC FIELDS'}, {'level': '4.0', 'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}], 'var_function-call-4474426584226387452': [{'level': '5.0', 'symbol': 'A62B'}, {'level': '5.0', 'symbol': 'A63G'}, {'level': '5.0', 'symbol': 'A63K'}, {'level': '5.0', 'symbol': 'A63B'}, {'level': '7.0', 'symbol': 'C13B50/00'}], 'var_function-call-227886120050006717': [{'cpc': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02E60/10",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/582",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_function-call-4039319436300256404': [{'length': '4', 'count': '677'}], 'var_function-call-483881578667801507': 'file_storage/function-call-483881578667801507.json', 'var_function-call-15113980107006050527': 'file_storage/function-call-15113980107006050527.json', 'var_function-call-15072831718708230019': [], 'var_function-call-17927729965813099341': {'dates': ['dated 5th March 2019', 'March the 18th, 2019', '29th March 2019', 'on March 29th, 2019', '2nd April 2019'], 'years_found': ['2019', '2019', '2019', '2019', '2019']}}

exec(code, env_args)
