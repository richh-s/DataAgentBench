code = """import json, re
with open(var_call_5rHtrHNCXLAWFEXzgsUP2BJs, 'r', encoding='utf-8') as f:
    records = json.load(f)

def extract_country(s):
    import re
    patterns = [r'from\s+([A-Z]{2})\b', r'In\s+([A-Z]{2})\b', r'\b([A-Z]{2})-\d', r'\bID\s*([A-Z]{2})-']
    for p in patterns:
        m = re.search(p, s)
        if m:
            return m.group(1)
    return None

count_total = len(records)
count_de = 0
count_h2_2019 = 0
sample = []

for rec in records:
    info = rec.get('Patents_info') or ''
    country = extract_country(info) or ''
    if country == 'DE' or re.search(r'\bDE[- ]', info):
        count_de += 1
        grant = rec.get('grant_date') or ''
        y = None
        m = None
        ym = re.search(r'(20\d{2})', grant)
        if ym:
            y = int(ym.group(1))
        mon = re.search(r'\b(January|February|March|April|May|June|July|August|September|October|November|December)\b', grant)
        if mon:
            month = mon.group(1)
        else:
            month = None
        if y==2019 and month:
            # check month number
            months = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}
            if months.get(month,0) >=7:
                count_h2_2019 += 1
                if len(sample) < 10:
                    sample.append({'Patents_info': info, 'grant_date': rec.get('grant_date'), 'cpc': rec.get('cpc'), 'filing_date': rec.get('filing_date')})

import json
res = {'total_records': count_total, 'de_candidates': count_de, 'de_h2_2019': count_h2_2019, 'sample': sample}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_aotf5Uc4J2te04vTC8sI8JrG': ['publicationinfo'], 'var_call_IVHWtrdfXTmXDR9hUhfcqliw': ['cpc_definition'], 'var_call_pmiPwWzDql1MApaUfscIR8R0': 'file_storage/call_pmiPwWzDql1MApaUfscIR8R0.json', 'var_call_96ynt5c54hdqWNWAPK3VhPur': 'file_storage/call_96ynt5c54hdqWNWAPK3VhPur.json', 'var_call_NsvNsGurGkwfOEmVn6LEFA53': 'file_storage/call_NsvNsGurGkwfOEmVn6LEFA53.json', 'var_call_5rHtrHNCXLAWFEXzgsUP2BJs': 'file_storage/call_5rHtrHNCXLAWFEXzgsUP2BJs.json', 'var_call_JfappaY2weevdUnaJZefgNUK': []}

exec(code, env_args)
