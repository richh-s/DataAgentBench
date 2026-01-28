code = """import json, re, pandas as pd

# Load civic docs
civic_src = var_call_J1kf87NrIr8g7mZPJ8wFbgVe
if isinstance(civic_src, str) and civic_src.endswith('.json'):
    with open(civic_src, 'r', encoding='utf-8') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_src

# Load funding aggregates
fund_src = var_call_nPGsOlMdaBZ0SjqkCM0yapGa
if isinstance(fund_src, str) and fund_src.endswith('.json'):
    with open(fund_src, 'r', encoding='utf-8') as f:
        funding = json.load(f)
else:
    funding = fund_src

fund_map = {r['Project_Name']: int(r['Total_Amount']) for r in funding}
project_names = list(fund_map.keys())

# Regex for schedules
spring2022_re = re.compile(r'\b(Spring\s*2022|2022\s*Spring|Spring\s*,?\s*2022|2022-?Spring)\b', re.IGNORECASE)
# also capture explicit months in Spring 2022
months_re = re.compile(r'\b2022\s*[-/]?\s*(March|Mar|April|Apr|May)\b|\b2022\s*[-/]\s*(0?3|0?4|0?5)\b|\b(0?3|0?4|0?5)\s*[-/]\s*2022\b', re.IGNORECASE)

started_projects = set()

for doc in civic_docs:
    text = doc.get('text','') or ''
    # only consider docs that mention Spring 2022 in schedule context
    if ('Spring' not in text and 'spring' not in text and '2022' not in text):
        continue
    for pn in project_names:
        if pn in text:
            # check for start markers nearby
            idx = text.find(pn)
            window = text[idx: idx+2000]  # look ahead
            # heuristics: look for "Begin" or "Start" lines and Spring 2022/months
            if re.search(r'\b(Begin|Start)\w*\s+(Construction|Work|Design|Project)?\b', window, re.IGNORECASE) and (spring2022_re.search(window) or months_re.search(window)):
                started_projects.add(pn)
            else:
                # sometimes schedule lists without 'Begin' near name; check within 400 chars around any 'Begin' occurrences later in doc
                # If project name appears and somewhere within 400 chars after a 'Begin' token there is Spring 2022
                for m in re.finditer(r'\b(Begin|Start)\w*\b', window, re.IGNORECASE):
                    w2 = window[m.start(): m.start()+400]
                    if spring2022_re.search(w2) or months_re.search(w2):
                        started_projects.add(pn)
                        break

# compute totals
count = len(started_projects)
total_funding = sum(fund_map[p] for p in started_projects)

out = {
    "projects_started_spring_2022": count,
    "total_funding_dollars": total_funding,
    "matched_projects": sorted(started_projects)
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_gYGqGuUGlR03T0rq7Mp3mqVV': ['Funding'], 'var_call_J1kf87NrIr8g7mZPJ8wFbgVe': 'file_storage/call_J1kf87NrIr8g7mZPJ8wFbgVe.json', 'var_call_nPGsOlMdaBZ0SjqkCM0yapGa': 'file_storage/call_nPGsOlMdaBZ0SjqkCM0yapGa.json'}

exec(code, env_args)
