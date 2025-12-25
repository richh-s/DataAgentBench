code = """import json
import pandas as pd
from dateutil import parser
import datetime

# Load data
with open(locals()['var_function-call-3949446733573800408'], 'r') as f:
    cpc_defs = json.load(f)
with open(locals()['var_function-call-3949446733573800903'], 'r') as f:
    patents = json.load(f)

level4_map = {item['symbol']: item['titleFull'] for item in cpc_defs}
level4_symbols = set(level4_map.keys())

start_date = datetime.datetime(2019, 7, 1)
end_date = datetime.datetime(2019, 12, 31)

valid_records = []
all_years_set = set()

for p in patents:
    # Filter Date
    try:
        g_date = parser.parse(p['grant_date'])
        if not (start_date <= g_date <= end_date):
            continue
    except:
        continue

    # Filter DE
    p_info = p.get('Patents_info', '')
    if 'DE-' not in p_info and 'Germany' not in p_info and ' DE ' not in p_info:
        continue
    
    # Extract Filing Year
    try:
        f_date = parser.parse(p['filing_date'])
        f_year = f_date.year
        all_years_set.add(f_year)
    except:
        continue

    # Extract CPC
    try:
        cpc_list = json.loads(p['cpc'])
        seen = set()
        for c in cpc_list:
            code = c.get('code', '')
            if len(code) >= 3:
                sym = code[:3]
                if sym in level4_symbols and sym not in seen:
                    valid_records.append({'symbol': sym, 'year': f_year})
                    seen.add(sym)
    except:
        continue

df = pd.DataFrame(valid_records)

if df.empty:
    print("__RESULT__:")
    print(json.dumps([]))
else:
    # Global Year Range
    min_year = min(all_years_set)
    max_year = max(all_years_set)
    full_range = pd.DataFrame({'year': range(min_year, max_year + 1)})
    
    results = []
    
    # Group by Symbol
    # We need to fill zeros for years with no patents for a specific symbol
    counts = df.groupby(['symbol', 'year']).size().reset_index(name='count')
    
    for symbol in counts['symbol'].unique():
        sym_counts = counts[counts['symbol'] == symbol]
        merged = pd.merge(full_range, sym_counts, on='year', how='left').fillna(0)
        merged = merged.sort_values('year')
        
        # EMA
        merged['ema'] = merged['count'].ewm(alpha=0.1, adjust=False).mean()
        
        max_ema = merged['ema'].max()
        best_year = int(merged.loc[merged['ema'].idxmax()]['year'])
        title = level4_map.get(symbol, 'N/A')
        
        results.append({
            "title": title,
            "code": symbol,
            "best_year": best_year,
            "max_ema": max_ema
        })
        
    # Sort
    results.sort(key=lambda x: x['max_ema'], reverse=True)
    
    print("__RESULT__:")
    print(json.dumps(results))"""

env_args = {'var_function-call-249731938256102390': 'file_storage/function-call-249731938256102390.json', 'var_function-call-17156139253207712376': 'file_storage/function-call-17156139253207712376.json', 'var_function-call-17156139253207714637': [{'Patents_info': 'VITTORI GIANFRANCO DE holds the FR patent filing (app. number FR-7811408-A), with publication number FR-2388575-B3.', 'grant_date': '1980 on Nov 14th', 'filing_date': '18th of April, 1978', 'cpc': '[\n  {\n    "code": "E01F9/627",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E04H12/32",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E01F9/685",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E04H12/32",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E01F9/627",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E01F9/685",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A63B57/40",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A63C19/062",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A63B57/357",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A63C19/062",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A63B57/40",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.', 'grant_date': '2006 on Apr 27th', 'filing_date': '18th of April, 2005', 'cpc': '[\n  {\n    "code": "G01K1/024",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01K1/024",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01K2207/02",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "G01K2207/02",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.', 'grant_date': 'Nov 29th, 2007', 'filing_date': '2006, May 11th', 'cpc': '[\n  {\n    "code": "B65B35/38",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "B65G25/02",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B65B5/103",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B65B65/02",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B65B43/56",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B65B5/103",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B65B65/02",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B65B35/38",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "B65B43/56",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B65G25/02",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.', 'grant_date': '2009, January 29th', 'filing_date': '30th June 2007', 'cpc': '[\n  {\n    "code": "H01F41/0233",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01F27/263",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'Patents_info': 'MITUTOYO CORP holds the DE patent filing (app. number DE-10037981-A), with pub. number DE-10037981-B4.', 'grant_date': '19th of October, 2017', 'filing_date': 'on August 3rd, 2000', 'cpc': '[\n  {\n    "code": "G01D5/34715",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01D5/36",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_function-call-3949446733573800408': 'file_storage/function-call-3949446733573800408.json', 'var_function-call-3949446733573800903': 'file_storage/function-call-3949446733573800903.json', 'var_function-call-9111100024939923774': [{'CPC Group Code': 'B29', 'Full Title': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL', 'Best Year': 2007, 'Max EMA': 1.0}, {'CPC Group Code': 'F02', 'Full Title': 'COMBUSTION ENGINES; HOT-GAS OR COMBUSTION-PRODUCT ENGINE PLANTS', 'Best Year': 2017, 'Max EMA': 0.2916541}, {'CPC Group Code': 'G01', 'Full Title': 'MEASURING; TESTING', 'Best Year': 2018, 'Max EMA': 0.29000000000000004}, {'CPC Group Code': 'H01', 'Full Title': 'ELECTRIC ELEMENTS', 'Best Year': 2018, 'Max EMA': 0.24174653401000004}, {'CPC Group Code': 'B60', 'Full Title': 'VEHICLES IN GENERAL', 'Best Year': 2018, 'Max EMA': 0.22465900000000003}, {'CPC Group Code': 'F04', 'Full Title': 'POSITIVE - DISPLACEMENT MACHINES FOR LIQUIDS; PUMPS FOR LIQUIDS OR ELASTIC FLUIDS', 'Best Year': 2018, 'Max EMA': 0.22465900000000003}, {'CPC Group Code': 'F16', 'Full Title': 'ENGINEERING ELEMENTS AND UNITS; GENERAL MEASURES FOR PRODUCING AND MAINTAINING EFFECTIVE FUNCTIONING OF MACHINES OR INSTALLATIONS; THERMAL INSULATION IN GENERAL', 'Best Year': 2018, 'Max EMA': 0.21343969000000007}, {'CPC Group Code': 'A61', 'Full Title': 'MEDICAL OR VETERINARY SCIENCE; HYGIENE', 'Best Year': 2016, 'Max EMA': 0.2}, {'CPC Group Code': 'G02', 'Full Title': 'OPTICS', 'Best Year': 2018, 'Max EMA': 0.18100000000000002}, {'CPC Group Code': 'Y02', 'Full Title': 'TECHNOLOGIES OR APPLICATIONS FOR MITIGATION OR ADAPTATION AGAINST CLIMATE CHANGE', 'Best Year': 2017, 'Max EMA': 0.16561000000000003}], 'var_function-call-13835226166886944916': {'Total fetched': 75, 'DE patents': 70, 'H2 2019 patents': 29, 'Valid patents': 27}}

exec(code, env_args)
