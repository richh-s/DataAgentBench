code = """import json
import pandas as pd
import re
from datetime import datetime

# Load data
with open(locals()['var_function-call-7392100381193129002'], 'r') as f:
    data = json.load(f)

# Helper to parse dates
def parse_date(d_str):
    if not d_str: return None
    # Formats seen: "dated 5th March 2019", "3rd August 2021", "2013, June 17th", "on December 4th, 2017", "Mar 19th, 2019"
    # Strategy: extract day, month, year using regex
    # Months: January, February... or Jan, Feb...
    d_str = d_str.lower()
    months = {
        'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
        'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12,
        'january': 1, 'february': 2, 'march': 3, 'april': 4, 'june': 6,
        'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12
    }
    
    # Try to find year (4 digits)
    year_match = re.search(r'\d{4}', d_str)
    if not year_match: return None
    year = int(year_match.group(0))
    
    # Try to find month
    month = None
    for m_name, m_val in months.items():
        if m_name in d_str:
            month = m_val
            break
    if not month: return None
    
    # Try to find day (1-31)
    # Look for digits not year
    # Regex for day: \b\d{1,2}(st|nd|rd|th)?\b
    # Remove year from string to avoid confusion
    d_str_no_year = d_str.replace(str(year), '')
    day_match = re.search(r'\b(\d{1,2})(?:st|nd|rd|th)?\b', d_str_no_year)
    day = int(day_match.group(1)) if day_match else 1 # Default to 1st if not found
    
    try:
        return datetime(year, month, day)
    except:
        return None

filtered_patents = []
for p in data:
    # 1. Filter Grant Date (H2 2019: July 1 - Dec 31)
    g_date = parse_date(p.get('grant_date'))
    if not g_date: continue
    if not (g_date.year == 2019 and g_date.month >= 7):
        continue
        
    # 2. Filter DE patents
    # Look for "from DE", "In DE", "The DE application"
    p_info = p.get('Patents_info', '')
    if not p_info: continue
    
    is_de = False
    if 'from de' in p_info.lower(): is_de = True
    elif 'in de' in p_info.lower(): is_de = True
    elif 'the de application' in p_info.lower(): is_de = True
    elif 'de-' in p_info: is_de = True # fallback
    
    if not is_de: continue
    
    # 3. Extract Filing Year
    f_date = parse_date(p.get('filing_date'))
    if not f_date: continue
    filing_year = f_date.year
    
    # 4. Extract CPC Level 4 (Class)
    cpc_json = p.get('cpc')
    if not cpc_json: continue
    try:
        cpcs = json.loads(cpc_json)
        # cpcs is a list of dicts with 'code'
        codes = set()
        for c in cpcs:
            code = c.get('code')
            if code and len(code) >= 3:
                # Level 4 is usually the Class, e.g. A01. First 3 chars.
                # Ensure the 3rd char is a digit if it's a standard class (e.g. A01).
                # But sometimes classes are different? The DB showed 'B04', 'B23'.
                # Let's just take first 3 chars.
                codes.add(code[:3])
        
        for c4 in codes:
            filtered_patents.append({
                'year': filing_year,
                'cpc': c4
            })
            
    except:
        continue

# Process Data
if not filtered_patents:
    print('__RESULT__:')
    print('[]')
else:
    df = pd.DataFrame(filtered_patents)
    
    # Count per year per CPC
    counts = df.groupby(['year', 'cpc']).size().reset_index(name='count')
    
    # Pivot to have years as index, CPC as columns. Fill 0.
    pivot = counts.pivot(index='year', columns='cpc', values='count').fillna(0)
    
    # Reindex to full year range to ensure continuity?
    # Or just use the years present. Using years present is safer if gaps are large, but EMA assumes time steps.
    # Let's reindex from min year to max year.
    min_year = int(pivot.index.min())
    max_year = int(pivot.index.max())
    full_idx = range(min_year, max_year + 1)
    pivot = pivot.reindex(full_idx, fill_value=0)
    
    # Calculate EMA
    # Smoothing factor alpha = 0.1
    ema = pivot.ewm(alpha=0.1, adjust=False).mean()
    
    # Find CPC with highest EMA each year
    top_cpc_per_year = ema.idxmax(axis=1)
    top_cpcs = set(top_cpc_per_year.values)
    
    # Also find best year for each of these CPCs
    results = []
    for cpc in top_cpcs:
        # Get EMA series for this cpc
        series = ema[cpc]
        best_year = series.idxmax()
        max_ema = series.max()
        results.append({
            'cpc_group_code': cpc,
            'best_year': int(best_year),
            'max_ema': float(max_ema) # optional
        })
        
    print('__RESULT__:')
    print(json.dumps(results))"""

env_args = {'var_function-call-14178245345415368620': 'file_storage/function-call-14178245345415368620.json', 'var_function-call-17556402076037921836': [{'Patents_info': 'The US patent application (no. US-201916389545-A) is assigned to MODERNATX INC and has pub. number US-10695419-B2.'}, {'Patents_info': 'Application (ID US-201916412740-A) from US, assigned to LEGACY RES AND DEVELOPMENT GROUP LLC, with publication no. US-10898606-B2.'}, {'Patents_info': 'TANDEM DIABETES CARE INC holds the US patent filing (app. number US-201916444452-A), with publication number US-10918785-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916560126-A) is belonging to DENSO CORP and has pub. number US-10897184-B2.'}, {'Patents_info': 'The US patent filing (app. number US-201916584394-A) is owned by DEPUY SYNTHES PRODUCTS INC and has publication no. US-11911287-B2.'}], 'var_function-call-15868652628589228505': [{'Patents_info': 'In AT, the patent filing (application no. AT-52022-U) is assigned to ST Extruded Products Germany GmbH and has publication no. AT-17758-U1.'}, {'Patents_info': 'Application (no. AU-2006246481-A) from AU, belonging to KAO GERMANY GMBH, with pub. number AU-2006246481-B2.'}, {'Patents_info': 'TRELLEBORG AUTOMOTIVE GERMANY holds the PL patent application (number PL-07728345-T), with publication no. PL-2010798-T3.'}, {'Patents_info': 'The DE application (number DE-102008034343-A) is assigned to CONTINENTAL MECH COMPONENTS GERMANY GMBH and has pub. number DE-102008034343-B4.'}, {'Patents_info': 'In EP, the application (ID EP-18829350-A) is belonging to MEYER BURGER GERMANY GMBH and has pub. number EP-3729486-C0.'}], 'var_function-call-7392100381193129002': 'file_storage/function-call-7392100381193129002.json', 'var_function-call-11562275123716587300': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-15353267789016829381': [{'symbol': 'A', 'level': '2.0', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'A01', 'level': '4.0', 'titleFull': 'AGRICULTURE; FORESTRY; ANIMAL HUSBANDRY; HUNTING; TRAPPING; FISHING'}, {'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}], 'var_function-call-2260508789965284583': [{'symbol': 'A01B1/00', 'level': '7.0', 'titleFull': 'Hand tools'}]}

exec(code, env_args)
