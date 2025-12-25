code = """import json
import re
from collections import defaultdict

# Load data
with open(locals()['var_function-call-4974488808225168135'], 'r') as f:
    patents = json.load(f)

with open(locals()['var_function-call-4381654191407381320'], 'r') as f:
    titles_list = json.load(f)

cpc_titles = {item['symbol']: item['titleFull'] for item in titles_list}

def parse_year(date_str):
    match = re.search(r'\b(19|20)\d{2}\b', date_str)
    if match:
        return int(match.group(0))
    return None

def is_h2_2019(date_str):
    if not date_str: return False
    if '2019' not in date_str: return False
    months_h2 = ['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 
                 'July', 'August', 'September', 'October', 'November', 'December']
    for m in months_h2:
        if m in date_str:
            return True
    return False

filtered_patents = []
for p in patents:
    if is_h2_2019(p.get('grant_date', '')):
        p_info = p.get('Patents_info', '')
        # Check for Germany
        if re.search(r'\bDE\b', p_info) or "Germany" in p_info or "German" in p_info:
            # Double check to avoid false positives if possible
            # But \bDE\b is quite specific in this context
            
            f_year = parse_year(p.get('filing_date', ''))
            if f_year:
                filtered_patents.append({
                    'year': f_year,
                    'cpc': p.get('cpc', '[]')
                })

# Aggregation
counts = defaultdict(lambda: defaultdict(int)) # code -> year -> count
all_years = set()

for p in filtered_patents:
    f_year = p['year']
    try:
        cpc_data = json.loads(p['cpc'])
    except:
        continue
        
    unique_codes = set()
    for item in cpc_data:
        code = item.get('code', '')
        if len(code) >= 3:
            cls = code[:3]
            unique_codes.add(cls)
            
    for cls in unique_codes:
        counts[cls][f_year] += 1
        all_years.add(f_year)

# EMA Calculation
alpha = 0.1
results = []

if not all_years:
    print("__RESULT__:")
    print("[]")
    exit()

min_y = min(all_years)
max_y = max(all_years)
timeline = range(min_y, max_y + 1)

for code, year_counts in counts.items():
    current_ema = 0
    max_ema = -1.0
    best_year = -1
    
    # Initialize EMA
    # If using recursive: S_t = alpha*Y_t + (1-alpha)*S_{t-1}
    # For t=0 (min_y), S_0 = Y_0 ?
    # Let's use that.
    
    first = True
    
    for y in timeline:
        cnt = year_counts.get(y, 0)
        if first:
            current_ema = cnt
            first = False
        else:
            current_ema = alpha * cnt + (1 - alpha) * current_ema
        
        if current_ema > max_ema:
            max_ema = current_ema
            best_year = y
            
    results.append({
        "full_title": cpc_titles.get(code, "N/A"),
        "cpc_group_code": code,
        "best_year": best_year,
        "max_ema": max_ema
    })

results.sort(key=lambda x: x['max_ema'], reverse=True)
top_results = results[:10] # Top 10

print("__RESULT__:")
print(json.dumps(top_results))"""

env_args = {'var_function-call-543765259574918097': 'file_storage/function-call-543765259574918097.json', 'var_function-call-4974488808225165482': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-4974488808225168135': 'file_storage/function-call-4974488808225168135.json', 'var_function-call-15178168180992510459': [{'symbol': 'H', 'level': '2.0', 'titleFull': 'ELECTRICITY'}, {'symbol': 'H01', 'level': '4.0', 'titleFull': 'ELECTRIC ELEMENTS'}, {'symbol': 'H01L', 'level': '5.0', 'titleFull': 'SEMICONDUCTOR DEVICES NOT COVERED BY CLASS H10'}, {'symbol': 'H01L21/00', 'level': '7.0', 'titleFull': 'Processes or apparatus adapted for the manufacture or treatment of semiconductor or solid state devices or of parts thereof'}], 'var_function-call-4381654191407381320': 'file_storage/function-call-4381654191407381320.json', 'var_function-call-6590596862173077174': [], 'var_function-call-1330180563282511566': ['Total patents: 4833', 'Grant: 14th Mar 2019 | Info: Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-1020...', '   -> Contains DE', 'Grant: Mar 19th, 2019 | Info: In RU, the patent filing (app. number RU-2017142236-A) is held by Sletov Aleksandr Anatolevich and h...', '   -> NO DE', 'Grant: Mar 12th, 2019 | Info: The RU patent application (number RU-2018105657-A) is held by OBSHCHESTVO S OGRANICHENNOJ OTVETSTVEN...', '   -> NO DE', 'Grant: 2019 on Jul 12th | Info: Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE O...', '   -> Contains DE', 'Grant: on March 14th, 2019 | Info: Patent application (number RU-2016134259-A) from RU, owned by KVINETIK LTD, with publication number ...', '   -> NO DE', 'Grant: July 8th, 2019 | Info: The DK patent application (number DK-14719221-T) is held by JASKE WOLFGANG and has publication numbe...', '   -> NO DE', 'Grant: 8th April 2019 | Info: The DK patent filing (application number DK-14835716-T) is owned by UNIV OSLO HF and has pub. number...', '   -> NO DE', 'Grant: 2019, May 30th | Info: The RU patent application (ID RU-2018146701-U) is held by [] and has publication no. RU-189707-U1....', '   -> NO DE', 'Grant: 22nd May 2019 | Info: The ES patent application (ID ES-11727548-T) is assigned to LOHR IND and has pub. number ES-2713511-...', '   -> NO DE', 'Grant: 2019 on Nov 14th | Info: In RU, the patent filing (application no. RU-2019124341-U) is owned by [] and has pub. number RU-193...', '   -> NO DE'], 'var_function-call-18171548689147745344': [], 'var_function-call-10317123642952335460': {'h2_count': 2435, 'countries': {'Unknown': 2435}}, 'var_function-call-2886822797528215099': ['Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'The DK patent application (number DK-14719221-T) is held by JASKE WOLFGANG and has publication number DK-2965013-T3.', 'In RU, the patent filing (application no. RU-2019124341-U) is owned by [] and has pub. number RU-193787-U1.', 'In KR, the application (ID KR-20170006144-U) is belonging to [] and has pub. number KR-200489330-Y1.', '[] holds the KR application (ID KR-20180005063-U), with pub. number KR-200489690-Y1.', 'The FR patent application (number FR-1550824-A) is owned by OBERTHUR TECHNOLOGIES and has pub. number FR-3032292-B1.', 'Application (ID EP-13874810-A) from EP, held by HONG KONG R&D CENTRE FOR LOGISTICS AND SUPPLY CHAIN MANAGEMENT ENABLING TECH LIMITED, with publication number EP-2954502-B1.', 'AI ALPINE US BIDCO INC holds the EP patent filing (application number EP-14189312-A), with pub. number EP-2865859-B1.', 'The EP application (ID EP-15715423-A) is assigned to PEPTITECH S R L and has publication no. EP-3125917-B1.', 'BERNSTEIN AG holds the EP patent filing (application no. EP-16782246-A), with pub. number EP-3365735-B1.']}

exec(code, env_args)
