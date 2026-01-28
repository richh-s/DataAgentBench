code = """import json, re
with open(var_call_5rHtrHNCXLAWFEXzgsUP2BJs, 'r', encoding='utf-8') as f:
    records = json.load(f)

def is_germany(info):
    if not info or not isinstance(info, str):
        return False
    if re.search(r'\bDE\b|\bDE-', info):
        return True
    if re.search(r'In\s+DE\b|from\s+DE\b|The DE application|The DE patent', info):
        return True
    return False

months = {m.lower(): i for i,m in enumerate(['', 'January','February','March','April','May','June','July','August','September','October','November','December'])}
shorts = {'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'sept':9,'oct':10,'nov':11,'dec':12}

def extract_year_month(s):
    if not s or not isinstance(s, str):
        return None, None
    y_match = re.search(r'(20\d{2})', s)
    year = int(y_match.group(1)) if y_match else None
    m = None
    mm = re.search(r'\b(January|February|March|April|May|June|July|August|September|October|November|December)\b', s)
    if mm:
        m = months[mm.group(1).lower()]
    else:
        mm2 = re.search(r'\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)\b', s)
        if mm2:
            m = shorts[mm2.group(1).lower()]
    return year, m


def extract_filing_year(s):
    if not s or not isinstance(s, str):
        return None
    m = re.search(r'(20\d{2})', s)
    return int(m.group(1)) if m else None

count_total = len(records)
count_germany = 0
count_germany_grant2019 = 0
count_germany_grant2019_h2 = 0
count_with_filing_year = 0
examples = []

for rec in records:
    info = rec.get('Patents_info') or ''
    if is_germany(info):
        count_germany += 1
        grant = rec.get('grant_date') or ''
        y, m = extract_year_month(grant)
        if y == 2019:
            count_germany_grant2019 += 1
            if m and m >= 7:
                count_germany_grant2019_h2 += 1
                filing = rec.get('filing_date') or ''
                f = extract_filing_year(filing)
                if f:
                    count_with_filing_year += 1
                else:
                    if len(examples) < 10:
                        examples.append({'Patents_info': info, 'grant_date': grant, 'filing_date': filing})

res = {'total': count_total, 'germany_total': count_germany, 'germany_grant2019': count_germany_grant2019, 'germany_grant2019_h2': count_germany_grant2019_h2, 'with_filing_year': count_with_filing_year, 'examples_missing_filing': examples}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_aotf5Uc4J2te04vTC8sI8JrG': ['publicationinfo'], 'var_call_IVHWtrdfXTmXDR9hUhfcqliw': ['cpc_definition'], 'var_call_pmiPwWzDql1MApaUfscIR8R0': 'file_storage/call_pmiPwWzDql1MApaUfscIR8R0.json', 'var_call_96ynt5c54hdqWNWAPK3VhPur': 'file_storage/call_96ynt5c54hdqWNWAPK3VhPur.json', 'var_call_NsvNsGurGkwfOEmVn6LEFA53': 'file_storage/call_NsvNsGurGkwfOEmVn6LEFA53.json', 'var_call_5rHtrHNCXLAWFEXzgsUP2BJs': 'file_storage/call_5rHtrHNCXLAWFEXzgsUP2BJs.json', 'var_call_JfappaY2weevdUnaJZefgNUK': [], 'var_call_2XPqZhmiMIE2tG6E4kVTdTym': {'total_records': 211, 'de_candidates': 0, 'de_h2_2019': 0, 'sample': []}, 'var_call_JYMRIndR2IxmIxVTHhgbHqN8': {'total': 211, 'cnt_contains_DE': 210, 'cnt_from_DE': 14, 'examples_with_DE_dash': []}, 'var_call_ma8cV75gThAyCVwBmIrwfoZw': 'file_storage/call_ma8cV75gThAyCVwBmIrwfoZw.json', 'var_call_MgNAq0SxMiubgkG2SEDEG9Oc': []}

exec(code, env_args)
