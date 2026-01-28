code = """import json
import re
from collections import defaultdict, Counter
from datetime import datetime

# Get file path
file_path = var_functions.query_db_54
print(f"Loading data from {file_path}")

# Load patent data
with open(file_path, 'r') as f:
    patents = json.load(f)

print(f"Total patents loaded: {len(patents)}")

# Function to parse grant date
def parse_grant_date(date_str):
    """Parse grant date to extract year and month"""
    if not date_str:
        return None, None
    
    # Extract year
    year_match = re.search(r'20(17|18|19)', date_str)
    if not year_match:
        return None, None
    
    year = int('20' + year_match.group(1))
    
    # Extract month (simplified - look for month abbreviations)
    months = {
        'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
        'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
    }
    
    date_str_lower = date_str.lower()
    for month_abbr, month_num in months.items():
        if month_abbr in date_str_lower:
            return year, month_num
    
    return year, None

# Function to extract CPC level 4 codes
def extract_cpc_level4(cpc_json):
    """Extract CPC codes at level 4 (first 4 characters)"""
    if not cpc_json or cpc_json == '[]':
        return []
    
    try:
        cpc_list = json.loads(cpc_json)
        level4_codes = set()
        for item in cpc_list:
            if isinstance(item, dict) and 'code' in item:
                code = item['code']
                # Get first 4 characters for level 4
                if len(code) >= 4:
                    level4_codes.add(code[:4])
        return list(level4_codes)
    except:
        return []

# Process patents by year and month
cpc_trends = defaultdict(lambda: defaultdict(int))  # {year: {month: {cpc_code: count}}}
cpc_totals = defaultdict(lambda: defaultdict(int))  # {cpc_code: {year: total}}
monthly_cpc_counts = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))  # {year: {month: {cpc: count}}}

# Collect monthly data
for patent in patents:
    year, month = parse_grant_date(patent.get('grant_date', ''))
    if not year or not month:
        continue
    
    cpc_codes = extract_cpc_level4(patent.get('cpc', ''))
    if not cpc_codes:
        continue
    
    for cpc in cpc_codes:
        cpc_totals[cpc][year] += 1
        if month:
            monthly_cpc_counts[year][month][cpc] += 1

# Print summary
print(f"\nCPC codes found: {len(cpc_totals)}")
print("Years available:", sorted(set(y for year_counts in monthly_cpc_counts.values() for y in [year for year in monthly_cpc_counts.keys()])))

# Calculate Exponential Moving Average for each CPC code
# EMA formula: EMA_t = α * value_t + (1-α) * EMA_{t-1}
alpha = 0.1

# Store results: {cpc: {year: max_ema, best_month: month, monthly_emas: {month: ema}}}
cpc_ema_results = defaultdict(lambda: {'best_ema': 0, 'best_year': None, 'best_month': None})

for cpc in cpc_totals.keys():
    best_ema = 0
    best_period = None
    period_emas = {}
    
    # For each year-month combination
    for year in sorted(monthly_cpc_counts.keys()):
        ema = None  # Initialize EMA
        
        # Sort months in order
        months = sorted(monthly_cpc_counts[year].keys())
        for month in months:
            count = monthly_cpc_counts[year][month].get(cpc, 0)
            
            if ema is None:
                # Initialize EMA with first value
                ema = count
            else:
                # EMA formula
                ema = alpha * count + (1 - alpha) * ema
            
            period_key = f"{year}-{month:02d}"
            period_emas[period_key] = ema
            
            # Track best EMA
            if ema > best_ema:
                best_ema = ema
                best_period = (year, month)
    
    cpc_ema_results[cpc] = {
        'best_ema': best_ema,
        'best_period': best_period,
        'period_emas': period_emas
    }

# Sort by best EMA
top_cpc = sorted(cpc_ema_results.items(), key=lambda x: x[1]['best_ema'], reverse=True)

print(f"\nTop 10 CPC codes by EMA:")
for i, (cpc, data) in enumerate(top_cpc[:10]):
    period = data['best_period']
    if period:
        year, month = period
        print(f"{i+1}. CPC {cpc}: EMA = {data['best_ema']:.2f} in {year}-{month:02d}")
    else:
        print(f"{i+1}. CPC {cpc}: No data")

# Now get full titles for these CPC codes from CPC definition database
top_cpc_codes = [code for code, _ in top_cpc[:10]]

print("__RESULT__:")
print(json.dumps({
    'total_cpc_codes': len(cpc_totals),
    'top_10_cpc_ema': [(code, data['best_period'], data['best_ema']) for code, data in top_cpc[:10]],
    'top_cpc_codes': top_cpc_codes
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'In RU, the patent filing (app. number RU-2017142236-A) is held by Sletov Aleksandr Anatolevich and has publication no. RU-2682615-C1.', 'grant_date': 'Mar 19th, 2019', 'cpc': '[\n  {\n    "code": "A61D1/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/645",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/6425",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/64",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/60",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/58",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The RU patent application (number RU-2018105657-A) is held by OBSHCHESTVO S OGRANICHENNOJ OTVETSTVENNOSTYU VORMKHOLS VNEDRENIE and has publication no. RU-2681783-C1.', 'grant_date': 'Mar 12th, 2019', 'cpc': '[\n  {\n    "code": "E21B33/136",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E21B33/134",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'grant_date': '2019 on Jul 12th', 'cpc': '[\n  {\n    "code": "G01S13/42",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S5/18",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41G3/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41H13/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'Patent application (number RU-2016134259-A) from RU, owned by KVINETIK LTD, with publication number RU-2681957-C2.', 'grant_date': 'on March 14th, 2019', 'cpc': '[\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/37",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DK patent application (number DK-14719221-T) is held by JASKE WOLFGANG and has publication number DK-2965013-T3.', 'grant_date': 'July 8th, 2019', 'cpc': '[\n  {\n    "code": "F25B2339/047",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D17/02",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B2400/061",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02B10/70",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D2200/20",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02B30/52",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D17/0005",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02B30/18",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D2200/123",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DK patent filing (application number DK-14835716-T) is owned by UNIV OSLO HF and has pub. number DK-3069138-T3.', 'grant_date': '8th April 2019', 'cpc': '[\n  {\n    "code": "G01N33/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N33/56977",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N33/56977",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/572",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61K39/39",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N2333/70539",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/55527",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C07K14/70503",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C07K14/70539",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/5158",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61K39/0011",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N33/505",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K39/0011",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/5158",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The RU patent application (ID RU-2018146701-U) is held by [] and has publication no. RU-189707-U1.', 'grant_date': '2019, May 30th', 'cpc': '[\n  {\n    "code": "B60P1/48",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The ES patent application (ID ES-11727548-T) is assigned to LOHR IND and has pub. number ES-2713511-T3.', 'grant_date': '22nd May 2019', 'cpc': '[\n  {\n    "code": "B61D3/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B61D3/182",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B61D3/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B61D3/16",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02T30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'Patents_info': 'In RU, the patent filing (application no. RU-2019124341-U) is owned by [] and has pub. number RU-193787-U1.', 'grant_date': '2019 on Nov 14th', 'cpc': '[\n  {\n    "code": "F16K17/192",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16L43/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_functions.list_db:4': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:56': 'file_storage/functions.query_db:56.json'}

exec(code, env_args)
