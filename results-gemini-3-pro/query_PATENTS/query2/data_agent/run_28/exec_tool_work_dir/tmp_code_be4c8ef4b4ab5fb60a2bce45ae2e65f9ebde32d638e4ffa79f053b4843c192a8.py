code = """import json
import pandas as pd
import re

# Load data
cpc_defs_file = locals()['var_function-call-4145452741131447632']
patents_file = locals()['var_function-call-7275035853467232807']

with open(cpc_defs_file, 'r') as f:
    cpc_defs = json.load(f)

with open(patents_file, 'r') as f:
    patents = json.load(f)

# Build map for Level 4 Titles
cpc_titles = {d['symbol']: d['titleFull'] for d in cpc_defs}

def parse_date(date_str):
    if not isinstance(date_str, str): return None
    # Remove ordinal suffixes (1st, 2nd, 3rd, 4th, etc.)
    clean_str = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', date_str)
    # Remove 'dated', 'on', 'the', 'dated', etc.
    clean_str = re.sub(r'\b(on|dated|the|of)\b', '', clean_str, flags=re.IGNORECASE)
    # Remove commas and extra spaces
    clean_str = clean_str.replace(',', ' ').strip()
    clean_str = re.sub(r'\s+', ' ', clean_str)
    
    try:
        dt = pd.to_datetime(clean_str, errors='coerce')
        if pd.notnull(dt):
            return dt
    except:
        pass
    return None

filtered_patents = []
for p in patents:
    # Filter Germany
    info = p.get('Patents_info', '')
    if not ('from DE' in info or 'no. DE-' in info or 'number DE-' in info or 'publication no. DE-' in info or 'publication number DE-' in info):
        continue
        
    # Filter Grant Date (H2 2019)
    g_date = parse_date(p.get('grant_date'))
    if not g_date:
        continue
    if g_date.year != 2019:
        continue
    if g_date.month < 7: # H2 starts July
        continue
        
    # Get Filing Year
    f_date = parse_date(p.get('filing_date'))
    if not f_date:
        continue
    filing_year = f_date.year
    
    # Get CPC Level 4
    cpc_json = p.get('cpc', '[]')
    try:
        cpcs = json.loads(cpc_json)
    except:
        continue
        
    codes = set()
    for item in cpcs:
        code = item.get('code', '')
        # Level 4 is Class (3 chars, e.g. B01)
        # Verify it matches [A-H][0-9][0-9]
        if len(code) >= 3:
            cls = code[:3]
            if re.match(r'^[A-H]\d{2}$', cls):
                codes.add(cls)
    
    for c in codes:
        filtered_patents.append({'cpc': c, 'year': filing_year})

# Aggregate
if not filtered_patents:
    print("__RESULT__:")
    print(json.dumps([]))
else:
    df = pd.DataFrame(filtered_patents)
    # Group by CPC and Year
    counts = df.groupby(['cpc', 'year']).size().reset_index(name='count')
    
    results = []
    # For each CPC
    for cpc_code, group in counts.groupby('cpc'):
        # Sort by year
        group = group.sort_values('year')
        years = group['year'].values
        cnts = group['count'].values
        
        if len(years) == 0:
            continue
            
        min_y = int(years.min())
        max_y = int(years.max())
        
        full_years = list(range(min_y, max_y + 1))
        y_map = dict(zip(years, cnts))
        
        series = [y_map.get(y, 0) for y in full_years]
        
        # Calculate EMA
        alpha = 0.1
        ema_values = []
        current_ema = series[0] 
        ema_values.append(current_ema)
        
        for val in series[1:]:
            current_ema = alpha * val + (1 - alpha) * current_ema
            ema_values.append(current_ema)
            
        # Find max EMA
        max_val = -1
        best_y = -1
        
        for y, val in zip(full_years, ema_values):
            if val > max_val:
                max_val = val
                best_y = y
        
        title = cpc_titles.get(cpc_code, "Unknown Title")
        
        results.append({
            "full_title": title,
            "cpc_group_code": cpc_code,
            "best_year": int(best_y),
            "max_ema": float(max_val)
        })

    # Sort by max_ema desc
    results.sort(key=lambda x: x['max_ema'], reverse=True)
    
    # Final output
    final_output = []
    for r in results:
        final_output.append({
            "full_title": r['full_title'],
            "cpc_group_code": r['cpc_group_code'],
            "best_year": r['best_year']
        })
        
    print("__RESULT__:")
    print(json.dumps(final_output, indent=2))"""

env_args = {'var_function-call-7351366711499102361': 'file_storage/function-call-7351366711499102361.json', 'var_function-call-11515452664161874980': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}], 'var_function-call-11515452664161874233': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': '14th Mar 2019', 'filing_date': '2013, June 17th'}, {'Patents_info': 'In RU, the patent filing (app. number RU-2017142236-A) is held by Sletov Aleksandr Anatolevich and has publication no. RU-2682615-C1.', 'cpc': '[\n  {\n    "code": "A61D1/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/645",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/6425",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/64",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/60",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/58",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'Mar 19th, 2019', 'filing_date': 'on December 4th, 2017'}, {'Patents_info': 'The RU patent application (number RU-2018105657-A) is held by OBSHCHESTVO S OGRANICHENNOJ OTVETSTVENNOSTYU VORMKHOLS VNEDRENIE and has publication no. RU-2681783-C1.', 'cpc': '[\n  {\n    "code": "E21B33/136",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E21B33/134",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'Mar 12th, 2019', 'filing_date': '2018 on Feb 15th'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'cpc': '[\n  {\n    "code": "G01S13/42",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S5/18",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41G3/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41H13/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': '2019 on Jul 12th', 'filing_date': '23rd May 2018'}, {'Patents_info': 'Patent application (number RU-2016134259-A) from RU, owned by KVINETIK LTD, with publication number RU-2681957-C2.', 'cpc': '[\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/37",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'on March 14th, 2019', 'filing_date': 'Jan 26th, 2015'}], 'var_function-call-1416837484132766701': [{'symbol': 'G06', 'level': '4.0'}, {'symbol': 'G06F', 'level': '5.0'}, {'symbol': 'G06F9/45533', 'level': '11.0'}], 'var_function-call-4145452741131447632': 'file_storage/function-call-4145452741131447632.json', 'var_function-call-7275035853467232807': 'file_storage/function-call-7275035853467232807.json'}

exec(code, env_args)
