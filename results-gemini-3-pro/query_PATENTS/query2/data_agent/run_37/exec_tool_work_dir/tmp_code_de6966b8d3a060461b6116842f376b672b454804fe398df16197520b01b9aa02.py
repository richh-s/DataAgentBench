code = """import json
import re

with open(locals()['var_function-call-11543888931216263098'], 'r') as f:
    data = json.load(f)

with open(locals()['var_function-call-16387991390808413708'], 'r') as f:
    titles_list = json.load(f)
titles_map = {item['symbol']: item['titleFull'] for item in titles_list}

def parse_date_to_year_month(date_str):
    if not date_str: return None, None
    months = {
        'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6,
        'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12,
        'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'jun': 6, 'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
    }
    date_str = date_str.lower()
    # Find year: 4 digits
    matches = re.findall(r'(19|20)\d{2}', date_str)
    if not matches:
        return None, None
    # If multiple years, pick one? Usually just one.
    # findall returns list of groups.
    # Actually re.findall(r'(19|20)\d{2}') returns the group capture (19 or 20).
    # Correct regex: r'((?:19|20)\d{2})'
    year_match = re.search(r'(19|20)\d{2}', date_str)
    if not year_match: return None, None
    year = int(year_match.group(0))
    
    month = None
    for m_name, m_num in months.items():
        if m_name in date_str:
            month = m_num
            break
    return year, month

filings = {}

for record in data:
    g_date = record.get('grant_date', '')
    g_year, g_month = parse_date_to_year_month(g_date)
    
    # Filter H2 2019
    if g_year != 2019: continue
    if g_month is None or g_month < 7: continue
    
    f_date = record.get('filing_date', '')
    f_year, _ = parse_date_to_year_month(f_date)
    if f_year is None: continue
    
    cpc_json = record.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_json)
    except:
        continue
    
    seen_classes = set()
    for item in cpc_list:
        code = item.get('code', '')
        if len(code) >= 3:
            cls = code[:3]
            if re.match(r'^[A-H]\d{2}$', cls):
                seen_classes.add(cls)
                
    for cls in seen_classes:
        if cls not in filings:
            filings[cls] = {}
        filings[cls][f_year] = filings[cls].get(f_year, 0) + 1

# Calculate EMA
results = []
alpha = 0.1

for cls, year_counts in filings.items():
    if not year_counts: continue
    years = sorted(year_counts.keys())
    min_year = years[0]
    max_year = years[-1]
    
    ema = 0
    best_ema = -1.0
    best_year = None
    
    # Initialize with first year count
    ema = year_counts[min_year]
    if ema > best_ema:
        best_ema = ema
        best_year = min_year
        
    for y in range(min_year + 1, max_year + 1):
        count = year_counts.get(y, 0)
        ema = (count * alpha) + (ema * (1 - alpha))
        if ema > best_ema:
            best_ema = ema
            best_year = y
            
    results.append({
        "class": cls,
        "title": titles_map.get(cls, "N/A"),
        "best_year": best_year,
        "max_ema": best_ema
    })

results.sort(key=lambda x: x['max_ema'], reverse=True)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-4774163761277503972': 'file_storage/function-call-4774163761277503972.json', 'var_function-call-12755170999949966242': ['publicationinfo'], 'var_function-call-17983425627878789748': [{'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.'}, {'Patents_info': 'In DE, the patent application (no. DE-10130631-A) is owned by SCHNEIDER SIEGHARD and has publication number DE-10130631-B4.'}, {'Patents_info': 'The DE patent application (no. DE-10134061-A) is belonging to MOSMATIC AG NECKER and has publication number DE-10134061-B4.'}, {'Patents_info': 'In DE, the patent application (no. DE-10147111-A) is belonging to VISTEON GLOBAL TECH INC and has publication number DE-10147111-B4.'}], 'var_function-call-3520023833909275240': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-14298847436406348240': 'file_storage/function-call-14298847436406348240.json', 'var_function-call-17296021972275604149': [{'symbol': 'B', 'level': '2.0', 'titleFull': 'PERFORMING OPERATIONS; TRANSPORTING'}, {'symbol': 'B04B', 'level': '5.0', 'titleFull': 'CENTRIFUGES'}, {'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}], 'var_function-call-11543888931216263098': 'file_storage/function-call-11543888931216263098.json', 'var_function-call-16387991390808413708': 'file_storage/function-call-16387991390808413708.json', 'var_function-call-1586333864231123704': [], 'var_function-call-3733650298785102899': {'total': 22, 'grant_2019': 0, 'grant_h2': 0, 'de_filter': 0, 'filing_parsed': 0, 'cpc_ok': 0, 'sample': []}, 'var_function-call-470999213175906048': ['14th Mar 2019', 'dated 21st November 2019', 'Mar 21st, 2019', '22nd of August, 2019', 'on March 14th, 2019', 'on March 21st, 2019', '7th March 2019', 'August the 29th, 2019', '26th September 2019', 'August the 14th, 2019', 'dated 9th May 2019', 'December 19th, 2019', '7th of March, 2019', '24th December 2019', '2019, May 23rd', '2019, May 29th', '28th Nov 2019', 'October the 10th, 2019', 'dated 10th October 2019', 'May 9th, 2019', '2019, October 2nd', '6th of June, 2019']}

exec(code, env_args)
