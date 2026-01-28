code = """import json
import re
from collections import defaultdict, Counter
from datetime import datetime

# Load patent data
file_path = var_functions.query_db_60
with open(file_path, 'r') as f:
    patents = json.load(f)

print(f"Loaded {len(patents)} German patents from 2019")

# Function to extract month from grant date
def extract_month(date_str):
    """Extract month from grant date string"""
    date_str_lower = date_str.lower()
    months = {
        'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
        'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
    }
    for month_abbr, month_num in months.items():
        if month_abbr in date_str_lower:
            return month_num
    return None

# Function to extract CPC level 4 codes
def extract_cpc_level4(cpc_json):
    """Extract CPC level 4 codes from CPC JSON string"""
    if not cpc_json or cpc_json == '[]':
        return []
    try:
        cpc_list = json.loads(cpc_json)
        level4_codes = set()
        for item in cpc_list:
            if isinstance(item, dict) and 'code' in item:
                code = item['code']
                if len(code) >= 4:
                    level4_codes.add(code[:4])
        return list(level4_codes)
    except:
        return []

# Process patents: count filings per CPC level 4 per month (for second half 2019)
cpc_monthly_counts = defaultdict(lambda: defaultdict(int))  # {cpc: {month: count}}

for patent in patents:
    grant_date = patent.get('grant_date', '')
    if not grant_date or '2019' not in grant_date:
        continue
    
    month = extract_month(grant_date)
    if not month or month < 7:  # Filter for second half (July-December)
        continue
    
    cpc_codes = extract_cpc_level4(patent.get('cpc', ''))
    for cpc in cpc_codes:
        cpc_monthly_counts[cpc][month] += 1

print(f"Found {len(cpc_monthly_counts)} unique CPC level 4 codes in second half 2019")
print("Monthly counts for top CPC codes:")
for cpc in sorted(cpc_monthly_counts.keys())[:5]:
    counts = {month: cpc_monthly_counts[cpc][month] for month in range(7, 13)}
    print(f"  {cpc}: {counts}")

# Calculate Exponential Moving Average (EMA) for each CPC code
alpha = 0.1  # Smoothing factor

cpc_ema_results = defaultdict(list)  # {cpc: [(month, ema, count)]}
best_cpc_periods = {}

for cpc in cpc_monthly_counts:
    ema = 0
    ema_history = []
    
    # Process months in chronological order (July to December)
    for month in range(7, 13):
        count = cpc_monthly_counts[cpc][month]
        
        # EMA formula: EMA_t = α * value_t + (1-α) * EMA_{t-1}
        if month == 7:  # First period
            ema = count
        else:
            ema = alpha * count + (1 - alpha) * ema
        
        ema_history.append((month, ema, count))
    
    cpc_ema_results[cpc] = ema_history
    
    # Find best (highest EMA) period
    best_month, best_ema, best_count = max(ema_history, key=lambda x: x[1])
    best_cpc_periods[cpc] = {
        'best_month': best_month,
        'best_ema': best_ema,
        'patents_in_month': best_count
    }

# Sort CPC codes by best EMA
top_cpc_by_ema = sorted(best_cpc_periods.items(), key=lambda x: x[1]['best_ema'], reverse=True)

print(f"\nTop 15 CPC codes by EMA in second half 2019:")
for i, (cpc, data) in enumerate(top_cpc_by_ema[:15]):
    print(f"{i+1:2d}. CPC {cpc}: Best EMA = {data['best_ema']:.2f} (in month {data['best_month']}, {data['patents_in_month']} patents)")

result = {
    'total_cpc_codes': len(cpc_monthly_counts),
    'top_cpc_codes': [(cpc, data['best_ema'], data['best_month'], data['patents_in_month']) 
                     for cpc, data in top_cpc_by_ema[:20]]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'In RU, the patent filing (app. number RU-2017142236-A) is held by Sletov Aleksandr Anatolevich and has publication no. RU-2682615-C1.', 'grant_date': 'Mar 19th, 2019', 'cpc': '[\n  {\n    "code": "A61D1/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/645",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/6425",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/64",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/60",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/58",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The RU patent application (number RU-2018105657-A) is held by OBSHCHESTVO S OGRANICHENNOJ OTVETSTVENNOSTYU VORMKHOLS VNEDRENIE and has publication no. RU-2681783-C1.', 'grant_date': 'Mar 12th, 2019', 'cpc': '[\n  {\n    "code": "E21B33/136",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E21B33/134",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'grant_date': '2019 on Jul 12th', 'cpc': '[\n  {\n    "code": "G01S13/42",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S5/18",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41G3/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41H13/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'Patent application (number RU-2016134259-A) from RU, owned by KVINETIK LTD, with publication number RU-2681957-C2.', 'grant_date': 'on March 14th, 2019', 'cpc': '[\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/37",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DK patent application (number DK-14719221-T) is held by JASKE WOLFGANG and has publication number DK-2965013-T3.', 'grant_date': 'July 8th, 2019', 'cpc': '[\n  {\n    "code": "F25B2339/047",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D17/02",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B2400/061",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02B10/70",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D2200/20",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02B30/52",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D17/0005",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02B30/18",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D2200/123",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DK patent filing (application number DK-14835716-T) is owned by UNIV OSLO HF and has pub. number DK-3069138-T3.', 'grant_date': '8th April 2019', 'cpc': '[\n  {\n    "code": "G01N33/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N33/56977",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N33/56977",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/572",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61K39/39",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N2333/70539",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/55527",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C07K14/70503",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C07K14/70539",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/5158",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61K39/0011",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N33/505",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K39/0011",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/5158",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The RU patent application (ID RU-2018146701-U) is held by [] and has publication no. RU-189707-U1.', 'grant_date': '2019, May 30th', 'cpc': '[\n  {\n    "code": "B60P1/48",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The ES patent application (ID ES-11727548-T) is assigned to LOHR IND and has pub. number ES-2713511-T3.', 'grant_date': '22nd May 2019', 'cpc': '[\n  {\n    "code": "B61D3/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B61D3/182",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B61D3/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B61D3/16",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02T30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'Patents_info': 'In RU, the patent filing (application no. RU-2019124341-U) is owned by [] and has pub. number RU-193787-U1.', 'grant_date': '2019 on Nov 14th', 'cpc': '[\n  {\n    "code": "F16K17/192",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16L43/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_functions.list_db:4': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:56': 'file_storage/functions.query_db:56.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json', 'var_functions.query_db:66': [{'symbol': 'A23L', 'titleFull': 'FOODS, FOODSTUFFS, OR NON-ALCOHOLIC BEVERAGES, NOT COVERED BY SUBCLASSES A21D OR A23B-A23J; THEIR PREPARATION OR TREATMENT, e.g. COOKING, MODIFICATION OF NUTRITIVE QUALITIES, PHYSICAL TREATMENT; PRESERVATION OF FOODS OR FOODSTUFFS, IN GENERAL'}, {'symbol': 'B23K', 'titleFull': 'SOLDERING OR UNSOLDERING; WELDING; CLADDING OR PLATING BY SOLDERING OR WELDING; CUTTING BY APPLYING HEAT LOCALLY, e.g. FLAME CUTTING; WORKING BY LASER BEAM'}, {'symbol': 'B27N', 'titleFull': 'MANUFACTURE BY DRY PROCESSES OF ARTICLES, WITH OR WITHOUT ORGANIC BINDING AGENTS, MADE FROM PARTICLES OR FIBRES CONSISTING OF WOOD OR OTHER LIGNOCELLULOSIC OR LIKE ORGANIC MATERIAL'}, {'symbol': 'B63B', 'titleFull': 'SHIPS OR OTHER WATERBORNE VESSELS; EQUIPMENT FOR SHIPPING\xa0'}, {'symbol': 'F02D', 'titleFull': 'CONTROLLING COMBUSTION ENGINES'}, {'symbol': 'F02M', 'titleFull': 'SUPPLYING COMBUSTION ENGINES IN GENERAL WITH COMBUSTIBLE MIXTURES OR CONSTITUENTS THEREOF'}, {'symbol': 'G01R', 'titleFull': 'MEASURING ELECTRIC VARIABLES; MEASURING MAGNETIC VARIABLES'}, {'symbol': 'G06F', 'titleFull': 'ELECTRIC DIGITAL DATA PROCESSING'}, {'symbol': 'B41F', 'titleFull': 'PRINTING MACHINES OR PRESSES'}]}

exec(code, env_args)
