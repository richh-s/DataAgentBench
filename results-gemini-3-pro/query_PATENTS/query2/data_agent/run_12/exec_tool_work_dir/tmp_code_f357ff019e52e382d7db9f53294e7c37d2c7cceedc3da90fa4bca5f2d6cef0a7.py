code = """import json
import re

with open(locals()['var_function-call-6414003164698615798'], 'r') as f:
    data = json.load(f)

months = {
    'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6,
    'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12,
    'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'jun': 6,
    'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
}

def parse_date_robust(date_str):
    if not date_str: return None
    s = date_str.lower().replace(',', ' ').replace('.', ' ').replace('of', ' ').replace('the', ' ')
    y_match = re.search(r'\b(20\d{2})\b', s)
    if not y_match: return None
    year = int(y_match.group(1))
    month = None
    for m_name in sorted(months.keys(), key=len, reverse=True):
        if m_name in s:
            month = months[m_name]
            break
    if not month: return None
    return year, month

debug_log = []
count_de = 0
count_grant = 0
count_filing = 0
count_cpc = 0

for row in data:
    p_info = row.get('Patents_info', '')
    if not (re.search(r'\bDE[- ]', p_info) or "from DE" in p_info or "In DE" in p_info or "Germany" in p_info):
        continue
    count_de += 1
    
    g_str = row.get('grant_date', '')
    gym = parse_date_robust(g_str)
    if not gym: 
        debug_log.append(f"Grant Date Parse Fail: {g_str}")
        continue
    gy, gm = gym
    if not (gy == 2019 and gm >= 7):
        continue
    count_grant += 1
    
    f_str = row.get('filing_date', '')
    fym = parse_date_robust(f_str)
    if not fym:
        debug_log.append(f"Filing Date Parse Fail: {f_str}")
        continue
    count_filing += 1
    
    cpc_json = row.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_json)
        if cpc_list:
            count_cpc += 1
        else:
            debug_log.append("CPC Empty List")
    except:
        debug_log.append("CPC JSON Fail")

print("__RESULT__:")
print(json.dumps({
    "de": count_de,
    "grant": count_grant,
    "filing": count_filing,
    "cpc": count_cpc,
    "log": debug_log[:5]
}))"""

env_args = {'var_function-call-1868465921641692363': 'file_storage/function-call-1868465921641692363.json', 'var_function-call-6414003164698615067': [{'symbol': 'A01K2227/108', 'level': '9.0', 'titleFull': 'Swine'}], 'var_function-call-6414003164698615798': 'file_storage/function-call-6414003164698615798.json', 'var_function-call-4244802832919163477': [{'symbol': 'A', 'level': '2.0', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'A01', 'level': '4.0', 'titleFull': 'AGRICULTURE; FORESTRY; ANIMAL HUSBANDRY; HUNTING; TRAPPING; FISHING'}, {'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'G06F', 'level': '5.0', 'titleFull': 'ELECTRIC DIGITAL DATA PROCESSING'}, {'symbol': 'A01B1/00', 'level': '7.0', 'titleFull': 'Hand tools'}, {'symbol': 'G06F9/00', 'level': '7.0', 'titleFull': 'Arrangements for program control, e.g. control units'}], 'var_function-call-14093412893191991109': [], 'var_function-call-8691657811473980173': [], 'var_function-call-5507538740903062421': {'total_records': 4833, 'de_matches_count': 32, 'sample_de_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'sample_de_grant_date': '14th Mar 2019', 'parsed_sample_date': 'Parse Error', 'de_h2_2019_count': 0}, 'var_function-call-1410127800540734811': {'debug_dates': [], 'msg': 'No data after filtering'}, 'var_function-call-14949167756059639455': ['14th Mar 2019', 'dated 21st November 2019', '22nd of August, 2019', 'September the 19th, 2019', 'on March 21st, 2019', 'August the 29th, 2019', '2019 on Mar 28th', '2019, December 24th', 'December 24th, 2019', 'dated 9th May 2019'], 'var_function-call-7669612119011012441': []}

exec(code, env_args)
