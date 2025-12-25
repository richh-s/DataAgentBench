code = """import json
import pandas as pd
from dateutil import parser
import datetime

# Load the query result
file_path = locals()['var_function-call-13913984678859708403']
with open(file_path, 'r') as f:
    data = json.load(f)

# Define H2 2019 range
start_date = datetime.datetime(2019, 7, 1)
end_date = datetime.datetime(2019, 12, 31)

filtered_groups = {} # Key: Group Code (Level 4), Value: {year: count}

for row in data:
    g_date_str = row['grant_date']
    f_date_str = row['filing_date']
    cpc_json = row['cpc']
    
    try:
        g_date = parser.parse(g_date_str, fuzzy=True)
    except:
        continue
        
    if start_date <= g_date <= end_date:
        try:
            f_date = parser.parse(f_date_str, fuzzy=True)
            f_year = f_date.year
        except:
            continue
            
        try:
            cpcs = json.loads(cpc_json)
        except:
            continue
            
        # Extract Level 4 codes (first 3 chars)
        # Use a set to avoid double counting same group for same patent?
        # "patent filings each year" -> Usually one patent counts as 1 filing for that technology area.
        # If a patent has multiple codes in the same group, does it count once or multiple times?
        # Usually distinct patent count per group.
        
        codes = set()
        for item in cpcs:
            code = item.get('code', '')
            if len(code) >= 3:
                l4 = code[:3]
                codes.add(l4)
        
        for code in codes:
            if code not in filtered_groups:
                filtered_groups[code] = {}
            filtered_groups[code][f_year] = filtered_groups[code].get(f_year, 0) + 1

# Calculate EMA
results = []
alpha = 0.1

for code, year_counts in filtered_groups.items():
    if not year_counts:
        continue
        
    years = sorted(year_counts.keys())
    min_year = years[0]
    max_year = years[-1]
    
    # Fill range?
    # If we strictly follow "patent filings each year", we should probably consider the range.
    # However, for a sparse set, filling zeros might dampen the EMA too much if the range is huge.
    # But usually EMA is time-dependent.
    # I'll fill years from min_year to max_year.
    
    ema = None
    max_ema = -1
    best_year = None
    
    # Iterate through all years in range
    full_range = range(min_year, max_year + 1)
    
    current_ema = 0
    # Initialization
    # First year with data:
    first_val = year_counts.get(min_year, 0)
    current_ema = first_val
    
    if current_ema > max_ema:
        max_ema = current_ema
        best_year = min_year
        
    for y in range(min_year + 1, max_year + 1):
        count = year_counts.get(y, 0)
        current_ema = alpha * count + (1 - alpha) * current_ema
        
        if current_ema > max_ema:
            max_ema = current_ema
            best_year = y
            
    # Also considering if max_ema should be tracked at each step. Yes.
    
    results.append({
        "group_code": code,
        "max_ema": max_ema,
        "best_year": best_year
    })

# Sort by max_ema desc
results.sort(key=lambda x: x['max_ema'], reverse=True)

# Output top results (e.g. top 20) and list of codes to query titles
top_results = results[:50] # Adjust limit as needed
codes_to_query = list(set(r['group_code'] for r in top_results))

print("__RESULT__:")
print(json.dumps({"top_results": top_results, "codes_to_query": codes_to_query}))"""

env_args = {'var_function-call-1051471489737895158': ['publicationinfo'], 'var_function-call-1051471489737895217': 'file_storage/function-call-1051471489737895217.json', 'var_function-call-1051471489737895276': ['cpc_definition'], 'var_function-call-12786041316617542540': [{'symbol': 'A01K2227/108', 'level': '9.0', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'level': '9.0', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'level': '9.0', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'level': '9.0', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'level': '9.0', 'titleFull': 'Ovine'}], 'var_function-call-12786041316617541661': [{'count(*)': '277813'}], 'var_function-call-13929303436024433786': [{'symbol': 'A01B1/00', 'level': '7.0', 'titleFull': 'Hand tools'}, {'symbol': 'A', 'level': '2.0', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'A01', 'level': '4.0', 'titleFull': 'AGRICULTURE; FORESTRY; ANIMAL HUSBANDRY; HUNTING; TRAPPING; FISHING'}, {'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}], 'var_function-call-13929303436024433193': [{'Patents_info': 'Patent application (number DE-10317286-A) from DE, belonging to NICOLAY VERWALTUNGS GMBH, with publication no. DE-10317286-B3.', 'cpc': '[\n  {\n    "code": "Y10S439/909",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y10S439/909",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01R13/631",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01R13/5224",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01R13/5224",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01R13/631",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'dated 7th October 2004', 'filing_date': 'dated 9th April 2003'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.', 'cpc': '[\n  {\n    "code": "G01K1/024",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01K1/024",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01K2207/02",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "G01K2207/02",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]', 'grant_date': '2006 on Apr 27th', 'filing_date': '18th of April, 2005'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.', 'cpc': '[\n  {\n    "code": "B65B35/38",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "B65G25/02",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B65B5/103",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B65B65/02",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B65B43/56",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B65B5/103",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B65B65/02",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B65B35/38",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "B65B43/56",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B65G25/02",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'Nov 29th, 2007', 'filing_date': '2006, May 11th'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.', 'cpc': '[\n  {\n    "code": "H01F41/0233",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01F27/263",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]', 'grant_date': '2009, January 29th', 'filing_date': '30th June 2007'}, {'Patents_info': 'In DE, the patent filing (application no. DE-102009032362-A) is owned by MARTOR KG and has pub. number DE-102009032362-B3.', 'cpc': '[\n  {\n    "code": "B26B5/003",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B26B5/001",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B26B5/003",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B26B5/001",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': '17th Jun 2010', 'filing_date': '2009, July 8th'}], 'var_function-call-16175897474908021526': [{'length': '3', 'count': '137'}], 'var_function-call-13913984678859708403': 'file_storage/function-call-13913984678859708403.json'}

exec(code, env_args)
