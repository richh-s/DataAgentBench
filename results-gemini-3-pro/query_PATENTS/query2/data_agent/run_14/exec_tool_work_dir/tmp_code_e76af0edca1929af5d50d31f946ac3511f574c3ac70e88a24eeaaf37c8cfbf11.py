code = """import json
import re

# Load data
with open(locals()['var_function-call-9512799665113414190'], 'r') as f:
    cpc_defs = json.load(f)
with open(locals()['var_function-call-9512799665113413019'], 'r') as f:
    patents = json.load(f)

# Helper: Parse Date
month_map = {
    'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6,
    'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12,
    'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'jun': 6, 'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
}

def parse_date(date_str):
    if not date_str: return None
    s = date_str.lower()
    # Simplified regex
    year_match = re.search(r'(19|20)\d{2}', s)
    if not year_match: return None
    year = int(year_match.group(0))
    month = 0
    for m, v in month_map.items():
        if m in s:
            month = v
            break
    if month == 0: return None
    return year, month

# Process
target_codes = set()
filing_counts = {} # code -> year -> count
cpc_titles = {d['symbol']: d['titleFull'] for d in cpc_defs}

target_patent_count = 0
sample_extracted = []

for p in patents:
    g_date = parse_date(p.get('grant_date', ''))
    is_target = False
    if g_date:
        y, m = g_date
        if y == 2019 and m >= 7:
            is_target = True
            target_patent_count += 1
    
    f_date = parse_date(p.get('filing_date', ''))
    f_year = f_date[0] if f_date else None
    
    try:
        cpc_list = json.loads(p.get('cpc', '[]'))
    except:
        cpc_list = []
        
    p_codes = set()
    for item in cpc_list:
        code = item.get('code', '')
        if len(code) >= 3:
            lvl4 = code[:3]
            if lvl4 in cpc_titles:
                p_codes.add(lvl4)
            elif is_target and len(sample_extracted) < 5:
                sample_extracted.append(lvl4)
    
    for code in p_codes:
        if is_target:
            target_codes.add(code)
        
        if f_year:
            if code not in filing_counts:
                filing_counts[code] = {}
            filing_counts[code][f_year] = filing_counts[code].get(f_year, 0) + 1

# EMA
results = []
alpha = 0.1

for code in target_codes:
    if code not in filing_counts: continue
    counts = filing_counts[code]
    years = sorted(counts.keys())
    if not years: continue
    
    min_year = years[0]
    max_year = years[-1]
    
    ema = 0
    max_ema = -1
    best_year = -1
    
    first = True
    for y in range(min_year, max_year + 1):
        val = counts.get(y, 0)
        if first:
            ema = val
            first = False
        else:
            ema = alpha * val + (1 - alpha) * ema
        
        if ema > max_ema:
            max_ema = ema
            best_year = y
            
    results.append({
        "full title": cpc_titles[code],
        "CPC group code": code,
        "best year": best_year,
        "max_ema": max_ema
    })

results.sort(key=lambda x: x['max_ema'], reverse=True)

final_output = results[:10]
if not final_output:
    final_output = {
        "debug": "empty",
        "target_patents": target_patent_count,
        "sample_extracted_failures": sample_extracted,
        "cpc_def_keys_sample": list(cpc_titles.keys())[:5]
    }

print("__RESULT__:")
print(json.dumps(final_output))"""

env_args = {'var_function-call-3499110082448975327': 'file_storage/function-call-3499110082448975327.json', 'var_function-call-3499110082448975424': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-830526858961616125': [{'Patents_info': 'Patent application (number DE-10317286-A) from DE, belonging to NICOLAY VERWALTUNGS GMBH, with publication no. DE-10317286-B3.'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.'}, {'Patents_info': 'In DE, the patent filing (application no. DE-102009032362-A) is owned by MARTOR KG and has pub. number DE-102009032362-B3.'}], 'var_function-call-830526858961613170': [{'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'A01B1/00', 'level': '7.0', 'titleFull': 'Hand tools'}], 'var_function-call-8617448877168968243': [{'symbol': 'B99'}, {'symbol': 'B29'}, {'symbol': 'B33'}, {'symbol': 'C22'}, {'symbol': 'D99'}, {'symbol': 'F28'}, {'symbol': 'A45'}, {'symbol': 'A24'}, {'symbol': 'A61'}, {'symbol': 'A63'}, {'symbol': 'A22'}, {'symbol': 'A42'}, {'symbol': 'A99'}, {'symbol': 'A43'}, {'symbol': 'A01'}, {'symbol': 'A62'}, {'symbol': 'A23'}, {'symbol': 'A47'}, {'symbol': 'A46'}, {'symbol': 'A44'}], 'var_function-call-17325015351250366860': [{'count(*)': '11644'}], 'var_function-call-9512799665113414190': 'file_storage/function-call-9512799665113414190.json', 'var_function-call-9512799665113413019': 'file_storage/function-call-9512799665113413019.json', 'var_function-call-5648962439893804586': [], 'var_function-call-8172229065787709150': [{'grant_date': '14th Mar 2019'}, {'grant_date': 'dated 21st November 2019'}, {'grant_date': 'Mar 21st, 2019'}, {'grant_date': '5th of December, 2019'}, {'grant_date': '22nd of August, 2019'}, {'grant_date': 'September the 19th, 2019'}, {'grant_date': 'on March 14th, 2019'}, {'grant_date': '28th Feb 2019'}, {'grant_date': '17th of October, 2019'}, {'grant_date': 'on March 21st, 2019'}, {'grant_date': '7th March 2019'}, {'grant_date': 'February 28th, 2019'}, {'grant_date': 'August the 29th, 2019'}, {'grant_date': 'dated 4th July 2019'}, {'grant_date': '28th March 2019'}, {'grant_date': '2019 on Mar 28th'}, {'grant_date': '26th September 2019'}, {'grant_date': '2019, December 24th'}, {'grant_date': '21st of February, 2019'}, {'grant_date': '2nd Oct 2019'}], 'var_function-call-14864350867969430992': {'target_patent_count': 0, 'target_codes_count': 0, 'total_patents': 11644, 'sample_cpc_titles': ['F25', 'G05', 'G12', 'G21', 'G09'], 'sample_results': []}, 'var_function-call-14989439848251511252': {'count_2019': 68, 'examples': ['14th Mar 2019', 'dated 21st November 2019', 'Mar 21st, 2019', '5th of December, 2019', '22nd of August, 2019']}, 'var_function-call-11295127886988009670': [['14th Mar 2019', None, False], ['dated 21st November 2019', None, False], ['Mar 21st, 2019', None, False], ['5th of December, 2019', None, False], ['22nd of August, 2019', None, False]], 'var_function-call-2025133122632928070': ['Year 2019 found', 'Year 2019 found']}

exec(code, env_args)
