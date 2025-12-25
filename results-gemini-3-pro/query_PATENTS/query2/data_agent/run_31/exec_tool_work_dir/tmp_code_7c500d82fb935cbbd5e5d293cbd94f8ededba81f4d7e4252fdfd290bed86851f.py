code = """import json
import pandas as pd
from dateutil import parser
import datetime

# Load data
with open(locals()['var_function-call-3949446733573800408'], 'r') as f:
    cpc_defs = json.load(f)

with open(locals()['var_function-call-3949446733573800903'], 'r') as f:
    patents = json.load(f)

# Create CPC Level 4 lookup
# The query results for level=4 were 3-char symbols (Classes).
level4_map = {item['symbol']: item['titleFull'] for item in cpc_defs}
level4_symbols = set(level4_map.keys())

# Define date range
start_date = datetime.datetime(2019, 7, 1)
end_date = datetime.datetime(2019, 12, 31)

valid_patents = []

for p in patents:
    # Filter by Grant Date
    try:
        g_date = parser.parse(p['grant_date'])
        if not (start_date <= g_date <= end_date):
            continue
    except:
        continue

    # Filter by Germany (DE)
    # The SQL filtered loosely. Let's be stricter.
    # Check if 'DE-' appears in Patents_info which typically contains "publication number DE-..." or "application no. DE-..."
    p_info = p['Patents_info']
    if 'DE-' not in p_info and 'Germany' not in p_info and ' DE ' not in p_info:
        continue
    
    # Extract Filing Year
    try:
        f_date = parser.parse(p['filing_date'])
        f_year = f_date.year
    except:
        continue

    # Extract CPC codes and map to Level 4
    try:
        cpc_list = json.loads(p['cpc'])
        # Codes are like "B65B35/38". Level 4 symbols are "B65".
        # Extract first 3 chars.
        patent_cpcs = set()
        for c in cpc_list:
            code = c.get('code', '')
            if len(code) >= 3:
                symbol = code[:3]
                if symbol in level4_symbols:
                    patent_cpcs.add(symbol)
        
        for sym in patent_cpcs:
            valid_patents.append({'symbol': sym, 'year': f_year})
            
    except:
        continue

df = pd.DataFrame(valid_patents)

if df.empty:
    print("__RESULT__:")
    print(json.dumps([]))
else:
    # Group by Symbol and Year
    counts = df.groupby(['symbol', 'year']).size().reset_index(name='count')
    
    # Create full range of years for each symbol to ensure continuity
    min_year = counts['year'].min()
    max_year = counts['year'].max()
    all_years = pd.DataFrame({'year': range(min_year, max_year + 1)})
    
    results = []
    
    for symbol, group in counts.groupby('symbol'):
        # Merge with all_years
        merged = pd.merge(all_years, group, on='year', how='left').fillna(0)
        merged = merged.sort_values('year')
        
        # Calculate EMA (alpha=0.1)
        # adjust=False corresponds to: y_t = alpha * x_t + (1-alpha) * y_{t-1}
        merged['ema'] = merged['count'].ewm(alpha=0.1, adjust=False).mean()
        
        # Find best year (max EMA)
        max_ema = merged['ema'].max()
        best_row = merged.loc[merged['ema'].idxmax()]
        best_year = int(best_row['year'])
        
        title = level4_map.get(symbol, "Unknown")
        
        results.append({
            "CPC Group Code": symbol,
            "Full Title": title,
            "Best Year": best_year,
            "Max EMA": max_ema
        })

    # Sort by Max EMA descending
    results.sort(key=lambda x: x['Max EMA'], reverse=True)
    
    # Output top results (e.g., top 10)
    print("__RESULT__:")
    print(json.dumps(results[:10])) # Return top 10 for brevity, or all if requested. The query implies finding "the" areas, plural. I'll show top 5-10."""

env_args = {'var_function-call-249731938256102390': 'file_storage/function-call-249731938256102390.json', 'var_function-call-17156139253207712376': 'file_storage/function-call-17156139253207712376.json', 'var_function-call-17156139253207714637': [{'Patents_info': 'VITTORI GIANFRANCO DE holds the FR patent filing (app. number FR-7811408-A), with publication number FR-2388575-B3.', 'grant_date': '1980 on Nov 14th', 'filing_date': '18th of April, 1978', 'cpc': '[\n  {\n    "code": "E01F9/627",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E04H12/32",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E01F9/685",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E04H12/32",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E01F9/627",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E01F9/685",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A63B57/40",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A63C19/062",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A63B57/357",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A63C19/062",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A63B57/40",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.', 'grant_date': '2006 on Apr 27th', 'filing_date': '18th of April, 2005', 'cpc': '[\n  {\n    "code": "G01K1/024",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01K1/024",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01K2207/02",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "G01K2207/02",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.', 'grant_date': 'Nov 29th, 2007', 'filing_date': '2006, May 11th', 'cpc': '[\n  {\n    "code": "B65B35/38",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "B65G25/02",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B65B5/103",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B65B65/02",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B65B43/56",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B65B5/103",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B65B65/02",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B65B35/38",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "B65B43/56",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B65G25/02",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.', 'grant_date': '2009, January 29th', 'filing_date': '30th June 2007', 'cpc': '[\n  {\n    "code": "H01F41/0233",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01F27/263",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'Patents_info': 'MITUTOYO CORP holds the DE patent filing (app. number DE-10037981-A), with pub. number DE-10037981-B4.', 'grant_date': '19th of October, 2017', 'filing_date': 'on August 3rd, 2000', 'cpc': '[\n  {\n    "code": "G01D5/34715",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01D5/36",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_function-call-3949446733573800408': 'file_storage/function-call-3949446733573800408.json', 'var_function-call-3949446733573800903': 'file_storage/function-call-3949446733573800903.json'}

exec(code, env_args)
