code = """import json
import re
from datetime import datetime

file_path = locals()['var_function-call-16013154277933524664']
with open(file_path, 'r') as f:
    data = json.load(f)

def parse_date(date_str):
    if not date_str:
        return None
    # Year
    year_match = re.search(r'\d{4}', date_str)
    if not year_match:
        return None
    year = int(year_match.group(0))
    
    # Month
    months = {
        'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
        'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
    }
    month = 1
    lower_str = date_str.lower()
    for m, num in months.items():
        if m in lower_str:
            month = num
            break
            
    # Day
    day_match = re.search(r'(\d{1,2})(?:st|nd|rd|th)?', lower_str)
    # The first number found might be the year if year comes first "2019, June 17th"
    # So we need to be careful.
    # Usually day is 1-31.
    # Let's find all numbers.
    nums = re.findall(r'\d+', lower_str)
    day = 1
    for n in nums:
        if int(n) == year:
            continue
        if 1 <= int(n) <= 31:
            day = int(n)
            break
            
    try:
        return datetime(year, month, day)
    except:
        return None

filtered_patents = []
for p in data:
    g_date_str = p.get('grant_date', '')
    g_date = parse_date(g_date_str)
    
    # Check H2 2019
    if not g_date or not (datetime(2019, 7, 1) <= g_date <= datetime(2019, 12, 31)):
        continue
        
    # Check DE
    info = p.get('Patents_info', '')
    is_de = False
    if re.search(r'\bfrom DE\b', info, re.IGNORECASE) or \
       re.search(r'\bDE patent\b', info, re.IGNORECASE) or \
       re.search(r'DE-\d+', info):
        is_de = True
        
    if not is_de:
        continue
        
    # Filing Date
    f_date_str = p.get('filing_date', '')
    f_date = parse_date(f_date_str)
    if not f_date:
        continue
    filing_year = f_date.year
    
    # CPC
    cpc_json = p.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_json)
    except:
        cpc_list = []
        
    # Extract Level 4 (Class, 3 chars)
    codes = set()
    for item in cpc_list:
        code = item.get('code', '')
        if len(code) >= 3:
            codes.add(code[:3])
            
    filtered_patents.append({
        'filing_year': filing_year,
        'cpc_codes': list(codes)
    })

# Aggregation
counts = {} # {code: {year: count}}
for p in filtered_patents:
    yr = p['filing_year']
    for code in p['cpc_codes']:
        if code not in counts:
            counts[code] = {}
        counts[code][yr] = counts[code].get(yr, 0) + 1

# EMA
results = []
smoothing_factor = 0.1

for code, year_counts in counts.items():
    if not year_counts:
        continue
    years = sorted(year_counts.keys())
    # Fill range
    min_year = years[0]
    max_year = years[-1]
    
    ema = None
    best_ema = -1
    best_year = None
    
    for y in range(min_year, max_year + 1):
        val = year_counts.get(y, 0)
        if ema is None:
            ema = val
        else:
            ema = val * smoothing_factor + ema * (1 - smoothing_factor)
        
        if ema > best_ema:
            best_ema = ema
            best_year = y
            
    results.append({
        'cpc_code': code,
        'best_ema': best_ema,
        'best_year': best_year
    })

results.sort(key=lambda x: x['best_ema'], reverse=True)
top_results = results[:20]

print("__RESULT__:")
print(json.dumps(top_results))"""

env_args = {'var_function-call-7596832698006438446': 'file_storage/function-call-7596832698006438446.json', 'var_function-call-15018955197929013117': [{'Patents_info': 'VITTORI GIANFRANCO DE holds the FR patent filing (app. number FR-7811408-A), with publication number FR-2388575-B3.'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.'}, {'Patents_info': 'MITUTOYO CORP holds the DE patent filing (app. number DE-10037981-A), with pub. number DE-10037981-B4.'}], 'var_function-call-10909241304662770037': [{'symbol': 'A01K2227/108', 'level': '9.0', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'level': '9.0', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'level': '9.0', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'level': '9.0', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'level': '9.0', 'titleFull': 'Ovine'}], 'var_function-call-9645515799168749745': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-857415788462902268': [{'symbol': 'A', 'level': '2.0'}, {'symbol': 'A01', 'level': '4.0'}, {'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01B1/00', 'level': '7.0'}], 'var_function-call-16013154277933524664': 'file_storage/function-call-16013154277933524664.json', 'var_function-call-6280867316487424436': [], 'var_function-call-4520269633117553141': {'total_records': 216, 'sample_grant_dates': ['14th Mar 2019', '2019 on Jul 12th', 'on October 31st, 2019', 'on November 5th, 2019', '8th Jan 2019'], 'sample_patents_info': ['Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'In US, the patent application (no. US-201314655932-A) is held by SERINPET LTDA REPRESENTACIONES Y SERVICIOS DE PETROLEOS and has pub. number US-10465517-B2.', 'Patent application (number US-201415314902-A) from US, held by HEWLETT PACKARD ENTPR DEV LP, with publication number US-10176043-B2.'], 'sample_cpc': ['[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]']}, 'var_function-call-7499445062165805207': [{'info': 'Patent application (no. DE-102013211266-A) from DE', 'g_date_str': '14th Mar 2019', 'g_date': 'None', 'is_h2_2019': False}, {'info': 'In DE, the application (number DE-102007032978-A) ', 'g_date_str': 'dated 21st November 2019', 'g_date': 'None', 'is_h2_2019': False}, {'info': 'The DE application (number DE-102009046500-A) is o', 'g_date_str': 'Mar 21st, 2019', 'g_date': 'None', 'is_h2_2019': False}, {'info': 'The DE patent application (no. DE-102010042467-A) ', 'g_date_str': '5th of December, 2019', 'g_date': 'None', 'is_h2_2019': False}, {'info': 'In DE, the patent filing (application no. DE-11201', 'g_date_str': '22nd of August, 2019', 'g_date': 'None', 'is_h2_2019': False}, {'info': 'In DE, the patent filing (application number DE-10', 'g_date_str': 'September the 19th, 2019', 'g_date': 'None', 'is_h2_2019': False}, {'info': 'DIEFFENBACHER GMBH MASCHINEN holds the DE patent a', 'g_date_str': 'on March 14th, 2019', 'g_date': 'None', 'is_h2_2019': False}, {'info': 'The DE patent filing (application number DE-102018', 'g_date_str': '28th Feb 2019', 'g_date': 'None', 'is_h2_2019': False}, {'info': 'The DE application (number DE-102014111322-A) is o', 'g_date_str': '17th of October, 2019', 'g_date': 'None', 'is_h2_2019': False}, {'info': 'In DE, the patent application (no. DE-102014209298', 'g_date_str': 'on March 21st, 2019', 'g_date': 'None', 'is_h2_2019': False}]}

exec(code, env_args)
