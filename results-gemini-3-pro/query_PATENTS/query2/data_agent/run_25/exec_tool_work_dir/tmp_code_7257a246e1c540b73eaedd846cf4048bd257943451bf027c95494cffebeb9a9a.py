code = """import json
import re
import pandas as pd

# Load data
with open(locals()['var_function-call-3965758477070812416'], 'r') as f:
    cpc_defs = json.load(f)
cpc_titles = {item['symbol']: item['titleFull'] for item in cpc_defs}

with open(locals()['var_function-call-5448675020633306303'], 'r') as f:
    patents = json.load(f)

def parse_date(date_str):
    if not isinstance(date_str, str): return None, None
    # Find year: 4 digits starting with 19 or 20
    y_match = re.search(r'(19|20)\d{2}', date_str)
    if not y_match: return None, None
    year = int(y_match.group(0))
    
    months = {
        'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
        'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
    }
    month = None
    lower_s = date_str.lower()
    for m_str, m_int in months.items():
        if m_str in lower_s:
            month = m_int
            break
    return year, month

data = []

for p in patents:
    # Filter Country (Refine SQL results)
    info = p.get('Patents_info', '')
    # Check strict DE presence if needed, but SQL already filtered for '%DE%' or '%Germany%'
    # Let's rely on SQL filter to catch "in Germany" aspect, as 216 is a reasonable subset
    # But wait, RU/AU/US patents were in the preview.
    # I MUST filter for DE here.
    is_de = False
    if 'DE-' in info or 'from DE' in info or 'country_code: DE' in info or 'Germany' in info:
        is_de = True
    if not is_de:
        # Check simple 'DE' with boundaries if desperate, but 'DE-' covers publication numbers.
        # Check sample RU patent: "from RU... publication no. RU-..."
        # It was matched in SQL because maybe 'DE' was in the name?
        # "FEDERALNOE... DE..."
        # So I must filter out those.
        # Strict check: "DE-" in text (publication number) OR "from DE".
        pass
    
    # Let's be reasonably strict.
    if not (re.search(r'DE\s*-\s*\d', info) or 'from DE' in info or 'Germany' in info):
        continue

    # Filter Date: H2 2019
    gd = p.get('grant_date', '')
    y, m = parse_date(gd)
    if y != 2019: continue
    if m is None or m < 7: continue
    
    # Get Filing Year
    fd = p.get('filing_date', '')
    fy, _ = parse_date(fd)
    if not fy: continue
    
    # Get CPC
    cpc_json = p.get('cpc', '[]')
    try:
        codes = json.loads(cpc_json)
    except:
        continue
    
    seen = set()
    for item in codes:
        code = item.get('code', '')
        if len(code) >= 3:
            grp = code[:3] # Level 4
            if grp in cpc_titles:
                seen.add(grp)
    
    for grp in seen:
        data.append({'year': fy, 'group': grp})

if not data:
    print("__RESULT__:")
    print("[]")
else:
    df = pd.DataFrame(data)
    # Pivot
    counts = df.groupby(['year', 'group']).size().unstack(fill_value=0)
    
    # Fill range
    if not counts.empty:
        full_idx = range(counts.index.min(), counts.index.max() + 1)
        counts = counts.reindex(full_idx, fill_value=0)
        
        # EMA
        ema = counts.ewm(alpha=0.1, adjust=False).mean()
        
        results = []
        for col in ema.columns:
            max_val = ema[col].max()
            best_y = ema[col].idxmax()
            results.append({
                "Full title": cpc_titles[col],
                "CPC group code": col,
                "Best year": int(best_y),
                "Max EMA": max_val
            })
        
        # Sort
        results.sort(key=lambda x: x['Max EMA'], reverse=True)
        
        # Clean
        final = [{k: v for k, v in r.items() if k != 'Max EMA'} for r in results]
        
        print("__RESULT__:")
        print(json.dumps(final[:50]))"""

env_args = {'var_function-call-16594278227079316675': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-16594278227079319092': 'file_storage/function-call-16594278227079319092.json', 'var_function-call-6081656753288550270': [{'level': '2.0', 'symbol': 'A', 'titleFull': 'HUMAN NECESSITIES'}, {'level': '4.0', 'symbol': 'A01', 'titleFull': 'AGRICULTURE; FORESTRY; ANIMAL HUSBANDRY; HUNTING; TRAPPING; FISHING'}, {'level': '4.0', 'symbol': 'A21', 'titleFull': 'BAKING; EDIBLE DOUGHS'}, {'level': '4.0', 'symbol': 'A22', 'titleFull': 'BUTCHERING; MEAT TREATMENT; PROCESSING POULTRY OR FISH'}, {'level': '4.0', 'symbol': 'A23', 'titleFull': 'FOODS OR FOODSTUFFS; TREATMENT THEREOF, NOT COVERED BY OTHER CLASSES'}, {'level': '4.0', 'symbol': 'A24', 'titleFull': "TOBACCO; CIGARS; CIGARETTES; SIMULATED SMOKING DEVICES; SMOKERS' REQUISITES"}, {'level': '4.0', 'symbol': 'A41', 'titleFull': 'WEARING APPAREL'}, {'level': '4.0', 'symbol': 'A42', 'titleFull': 'HEADWEAR'}, {'level': '4.0', 'symbol': 'A43', 'titleFull': 'FOOTWEAR'}, {'level': '4.0', 'symbol': 'A44', 'titleFull': 'HABERDASHERY; JEWELLERY'}, {'level': '4.0', 'symbol': 'A45', 'titleFull': 'HAND OR TRAVELLING ARTICLES'}, {'level': '4.0', 'symbol': 'A46', 'titleFull': 'BRUSHWARE'}, {'level': '4.0', 'symbol': 'A47', 'titleFull': 'FURNITURE; DOMESTIC ARTICLES OR APPLIANCES; COFFEE MILLS; SPICE MILLS; SUCTION CLEANERS IN GENERAL'}, {'level': '4.0', 'symbol': 'A61', 'titleFull': 'MEDICAL OR VETERINARY SCIENCE; HYGIENE'}, {'level': '4.0', 'symbol': 'A62', 'titleFull': 'LIFE-SAVING; FIRE-FIGHTING'}, {'level': '4.0', 'symbol': 'A63', 'titleFull': 'SPORTS; GAMES; AMUSEMENTS'}, {'level': '4.0', 'symbol': 'A99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION'}, {'level': '5.0', 'symbol': 'A01B', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'level': '5.0', 'symbol': 'A01C', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'level': '5.0', 'symbol': 'A01D', 'titleFull': 'HARVESTING; MOWING'}], 'var_function-call-5448675020633306303': 'file_storage/function-call-5448675020633306303.json', 'var_function-call-3965758477070812416': 'file_storage/function-call-3965758477070812416.json', 'var_function-call-14751869824581945649': [], 'var_function-call-4071173780002865268': {'total': 216, 'cnt_2019': 0, 'cnt_h2': 0, 'cnt_both': 0, 'samples': []}, 'var_function-call-16385586842686664976': ['14th Mar 2019', '2019 on Jul 12th', 'on October 31st, 2019', 'on November 5th, 2019', '8th Jan 2019', 'dated 8th October 2019', 'July the 9th, 2019', 'August the 6th, 2019', 'Apr 2nd, 2019', 'dated 21st November 2019'], 'var_function-call-6212525844481284984': [['NoMatch', None], ['NoMatch', None], ['NoMatch', None], ['NoMatch', None], ['NoMatch', None]]}

exec(code, env_args)
