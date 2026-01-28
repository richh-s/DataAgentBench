code = """import json, re, pandas as pd

# Load civic docs
path_docs = var_call_0DCnIGEXcMuqapHOE2JF1Tyv
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Load funding per project
path_fund = var_call_BABB2XE4sOVEK9sPlcT0ixNa
with open(path_fund, 'r', encoding='utf-8') as f:
    fund = json.load(f)
fund_map = {r['Project_Name']: int(r['total_amount']) for r in fund}

# Heuristic extraction: find project blocks followed by 'Project Schedule:' and then 'Begin Construction: <when>'
# Use list of funded project names to match in text
project_names = sorted(fund_map.keys(), key=len, reverse=True)

spring2022_projects = set()

# Define spring 2022 patterns
spring_pat = re.compile(r"\bBegin Construction\s*:\s*([^\n\r]+)")

def is_spring_2022(val:str)->bool:
    v = val.strip()
    if '2022' not in v:
        return False
    vlow = v.lower()
    if 'spring' in vlow:
        return True
    # month names
    for m in ['march','april','may']:
        if m in vlow:
            return True
    # numeric months
    # match 2022-03 .. 2022-05 or 03/2022 etc.
    if re.search(r"2022\s*[-/]\s*0?3\b", vlow):
        return True
    if re.search(r"2022\s*[-/]\s*0?4\b", vlow):
        return True
    if re.search(r"2022\s*[-/]\s*0?5\b", vlow):
        return True
    if re.search(r"0?3\s*[-/]\s*2022\b", vlow):
        return True
    if re.search(r"0?4\s*[-/]\s*2022\b", vlow):
        return True
    if re.search(r"0?5\s*[-/]\s*2022\b", vlow):
        return True
    return False

for d in docs:
    text = d.get('text','')
    if 'Begin Construction' not in text:
        continue
    # split into lines to locate occurrences and scan upwards for project name
    lines = text.splitlines()
    for i,line in enumerate(lines):
        if 'Begin Construction' in line:
            m = spring_pat.search(line)
            if not m and i+1 < len(lines):
                # sometimes value is next line
                m = spring_pat.search(line + ' ' + lines[i+1])
            if not m:
                continue
            when = m.group(1).strip()
            if not is_spring_2022(when):
                continue
            # search backwards within previous 15 lines for a funded project name
            window = '\n'.join(lines[max(0,i-20):i])
            found = None
            for pn in project_names:
                if pn in window:
                    found = pn
                    break
            if found:
                spring2022_projects.add(found)

count_projects = len(spring2022_projects)
total_funding = sum(fund_map.get(p,0) for p in spring2022_projects)

out = {
    'projects_started_spring_2022_count': count_projects,
    'total_funding_usd': total_funding,
    'projects': sorted(list(spring2022_projects))
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_0DCnIGEXcMuqapHOE2JF1Tyv': 'file_storage/call_0DCnIGEXcMuqapHOE2JF1Tyv.json', 'var_call_VwE648V2zSPolLt170slfXOy': ['Funding'], 'var_call_BABB2XE4sOVEK9sPlcT0ixNa': 'file_storage/call_BABB2XE4sOVEK9sPlcT0ixNa.json'}

exec(code, env_args)
