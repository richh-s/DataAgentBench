code = """import json
import pandas as pd
from dateutil import parser
import re

# Load data
with open(locals()['var_function-call-14097541545032493746'], 'r') as f:
    data = json.load(f)

# Helper to parse dates
def parse_date(date_str):
    try:
        # Remove 'on ', 'the ', etc to help parser
        clean_str = re.sub(r'(on |the |of )', '', date_str, flags=re.IGNORECASE)
        dt = parser.parse(clean_str, fuzzy=True)
        return dt
    except:
        return None

filtered_records = []

for row in data:
    # 1. Parse Grant Date
    g_date = parse_date(row.get('grant_date', ''))
    if not g_date:
        continue
    
    # Filter: Second half of 2019 (July 1 to Dec 31)
    if not (g_date.year == 2019 and g_date.month >= 7):
        continue

    # 2. Parse Country (Germany)
    # Check Patents_info for "from DE" or similar indicators
    p_info = row.get('Patents_info', '')
    if not p_info:
        continue
    
    # Simple heuristic for country: "from DE" or "assigned to ... from DE" or "Patent application ... from DE"
    # Also look for "In DE," at start.
    is_germany = False
    if "from DE" in p_info or "In DE" in p_info:
        is_germany = True
    elif "DE-" in p_info and ("patent application" in p_info.lower() or "publication" in p_info.lower()):
        # checking if the patent itself is DE
        # The summary usually says "The DE patent application..."
        if "The DE patent" in p_info or "Patent application ... from DE" in p_info:
             is_germany = True
        # If it says "assigned to ... from DE", it might be assignee country, not patent country.
        # But usually "from XX" refers to the origin/jurisdiction in these summaries.
        # Let's stricter check: look for "from DE" associated with application/filing.
    
    # Re-evaluating text patterns from samples:
    # "Patent application (no. DE-...) from DE..." -> Yes
    # "In RU, the patent filing..." -> No
    # "The DK patent application... from DK..." -> No
    
    if "from DE" in p_info or "In DE" in p_info or "The DE patent" in p_info:
        is_germany = True
    
    if not is_germany:
        continue

    # 3. Parse Filing Date
    f_date = parse_date(row.get('filing_date', ''))
    if not f_date:
        continue
    filing_year = f_date.year

    # 4. Parse CPC
    cpc_json = row.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_json)
    except:
        cpc_list = []
    
    # Extract Level 4 codes (Classes, 3 chars, e.g., 'G06')
    # Use a set to avoid double counting same CPC group for same patent?
    # Usually "filings count" counts the patent once per group.
    
    codes = set()
    for item in cpc_list:
        code = item.get('code', '')
        if len(code) >= 3:
            # Level 4 corresponds to Class (e.g. B04)
            # Code format: A01B... -> Class is A01
            # Wait. "B04" in database has 3 chars. "A01" has 3 chars.
            # So I take first 3 characters.
            group_code = code[:3]
            codes.add(group_code)
    
    for c in codes:
        filtered_records.append({
            'cpc_group': c,
            'filing_year': filing_year
        })

# Create DataFrame
df = pd.DataFrame(filtered_records)

if df.empty:
    print('__RESULT__:')
    print(json.dumps([]))
else:
    # Count filings per CPC per Year
    counts = df.groupby(['cpc_group', 'filing_year']).size().reset_index(name='count')
    
    # Sort
    counts = counts.sort_values(['cpc_group', 'filing_year'])
    
    results = []
    
    # Calculate EMA and find max
    # Group by CPC
    for cpc, group in counts.groupby('cpc_group'):
        # Create full range of years?
        # EMA usually runs on time series.
        # If years are missing, count is 0.
        min_year = group['filing_year'].min()
        max_year = group['filing_year'].max()
        full_range = range(min_year, max_year + 1)
        
        # Reindex to fill missing years with 0
        group = group.set_index('filing_year').reindex(full_range, fill_value=0).reset_index()
        group = group.rename(columns={'index': 'filing_year'})
        
        # Calculate EMA
        # Pandas ewm: alpha=0.1, adjust=False (recursive formula)
        # S_t = alpha * Y_t + (1-alpha) * S_{t-1} matches adjust=False
        group['ema'] = group['count'].ewm(alpha=0.1, adjust=False).mean()
        
        # Find row with max EMA
        best_row = group.loc[group['ema'].idxmax()]
        
        results.append({
            'cpc_group': cpc,
            'best_year': int(best_row['filing_year']),
            'max_ema': float(best_row['ema'])
        })
    
    # Sort results by max_ema descending (optional, but good for "highest")
    # The query asks for "CPC technology areas ... with the highest ...". 
    # Usually implies returning the top ones or all sorted. 
    # I'll return all sorted.
    results.sort(key=lambda x: x['max_ema'], reverse=True)
    
    print('__RESULT__:')
    print(json.dumps(results))"""

env_args = {'var_function-call-4700514525902219296': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-4700514525902218863': [{'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': '14th Mar 2019', 'filing_date': '2013, June 17th', 'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.'}, {'cpc': '[\n  {\n    "code": "A61D1/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/645",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/6425",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/64",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/60",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/58",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'Mar 19th, 2019', 'filing_date': 'on December 4th, 2017', 'Patents_info': 'In RU, the patent filing (app. number RU-2017142236-A) is held by Sletov Aleksandr Anatolevich and has publication no. RU-2682615-C1.'}, {'cpc': '[\n  {\n    "code": "E21B33/136",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E21B33/134",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'Mar 12th, 2019', 'filing_date': '2018 on Feb 15th', 'Patents_info': 'The RU patent application (number RU-2018105657-A) is held by OBSHCHESTVO S OGRANICHENNOJ OTVETSTVENNOSTYU VORMKHOLS VNEDRENIE and has publication no. RU-2681783-C1.'}, {'cpc': '[\n  {\n    "code": "G01S13/42",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S5/18",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41G3/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41H13/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': '2019 on Jul 12th', 'filing_date': '23rd May 2018', 'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.'}, {'cpc': '[\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/37",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'on March 14th, 2019', 'filing_date': 'Jan 26th, 2015', 'Patents_info': 'Patent application (number RU-2016134259-A) from RU, owned by KVINETIK LTD, with publication number RU-2681957-C2.'}], 'var_function-call-2784290657964579743': [{'symbol': 'G', 'level': '2.0', 'titleFull': 'PHYSICS'}, {'symbol': 'G06', 'level': '4.0', 'titleFull': 'COMPUTING; CALCULATING OR COUNTING'}, {'symbol': 'G06F', 'level': '5.0', 'titleFull': 'ELECTRIC DIGITAL DATA PROCESSING'}, {'symbol': 'G06F9/00', 'level': '7.0', 'titleFull': 'Arrangements for program control, e.g. control units'}], 'var_function-call-14097541545032493746': 'file_storage/function-call-14097541545032493746.json'}

exec(code, env_args)
