code = """import json, re

path_docs = var_call_0DCnIGEXcMuqapHOE2JF1Tyv
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

path_fund = var_call_BABB2XE4sOVEK9sPlcT0ixNa
with open(path_fund, 'r', encoding='utf-8') as f:
    fund = json.load(f)
fund_map = {r['Project_Name']: int(r['total_amount']) for r in fund}
project_names = sorted(fund_map.keys(), key=len, reverse=True)

spring2022_projects = set()

spring_pat = re.compile(r"\\bBegin Construction\\s*:\\s*([^\\n\\r]+)")

def is_spring_2022(val):
    v = val.strip()
    if '2022' not in v:
        return False
    vlow = v.lower()
    if 'spring' in vlow:
        return True
    for m in ['march','april','may']:
        if m in vlow:
            return True
    if re.search(r"2022\\s*[-/]\\s*0?3\\b", vlow):
        return True
    if re.search(r"2022\\s*[-/]\\s*0?4\\b", vlow):
        return True
    if re.search(r"2022\\s*[-/]\\s*0?5\\b", vlow):
        return True
    if re.search(r"0?3\\s*[-/]\\s*2022\\b", vlow):
        return True
    if re.search(r"0?4\\s*[-/]\\s*2022\\b", vlow):
        return True
    if re.search(r"0?5\\s*[-/]\\s*2022\\b", vlow):
        return True
    return False

for d in docs:
    text = d.get('text','')
    if 'Begin Construction' not in text:
        continue
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if 'Begin Construction' not in line:
            continue
        m = spring_pat.search(line)
        if (not m) and (i + 1 < len(lines)):
            m = spring_pat.search(line + ' ' + lines[i+1])
        if not m:
            continue
        when = m.group(1).strip()
        if not is_spring_2022(when):
            continue
        window = "\\n".join(lines[max(0, i-20):i])
        found = None
        for pn in project_names:
            if pn in window:
                found = pn
                break
        if found:
            spring2022_projects.add(found)

count_projects = len(spring2022_projects)
total_funding = sum(fund_map.get(p, 0) for p in spring2022_projects)

out = {
    'projects_started_spring_2022_count': count_projects,
    'total_funding_usd': total_funding,
    'projects': sorted(spring2022_projects)
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_0DCnIGEXcMuqapHOE2JF1Tyv': 'file_storage/call_0DCnIGEXcMuqapHOE2JF1Tyv.json', 'var_call_VwE648V2zSPolLt170slfXOy': ['Funding'], 'var_call_BABB2XE4sOVEK9sPlcT0ixNa': 'file_storage/call_BABB2XE4sOVEK9sPlcT0ixNa.json'}

exec(code, env_args)
