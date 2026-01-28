code = """import json
import re

# Load data from storage paths provided by previous tool calls
with open(var_call_1sy2EAmn2hPEFkep0c11JWFu, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_EfxXsrQD5f5UJ8SOm4SNG3rz, 'r') as f:
    funding = json.load(f)

# Prepare funding dict and list of unique project names with amounts
funding_by_project = {}
for rec in funding:
    name = rec.get('Project_Name')
    amt = rec.get('Amount')
    try:
        amt_int = int(amt)
    except:
        try:
            amt_int = int(float(amt))
        except:
            amt_int = 0
    # If multiple funding rows for same project, sum them
    funding_by_project[name] = funding_by_project.get(name, 0) + amt_int

project_names = list(funding_by_project.keys())

# Define regex patterns for Spring 2022 and March-May 2022
patterns = [
    re.compile(r"\bSpring[ ,\-]*(2022|\\'22)\b", re.IGNORECASE),
    re.compile(r"\b(2022)[ ,\-]*Spring\b", re.IGNORECASE),
    re.compile(r"\b(March|Mar|April|Apr|May)\b[ .,/-]*(2022|\\'22)\b", re.IGNORECASE),
    re.compile(r"\b(2022)[-/.](03|04|05)\b"),
    re.compile(r"\b(03|04|05)[-/](2022)\b"),
]

# Also look for phrases like 'Begin Construction: Spring 2022' etc
phrase_pattern = re.compile(r"(Begin Construction|Advertise|Complete Design|Project Schedule|Begin Construction):?[^\n]{0,80}", re.IGNORECASE)

matched_projects = set()

# For each project name, search in civic documents text for nearby patterns
for pname in project_names:
    pname_lower = pname.lower()
    found = False
    for doc in civic_docs:
        text = doc.get('text','')
        text_lower = text.lower()
        # find occurrences of project name (case-insensitive)
        start = 0
        while True:
            idx = text_lower.find(pname_lower, start)
            if idx == -1:
                break
            # extract window
            win_start = max(0, idx-300)
            win_end = min(len(text), idx + len(pname) + 300)
            window = text[win_start:win_end]
            # check patterns in window
            for pat in patterns:
                if pat.search(window):
                    matched_projects.add(pname)
                    found = True
                    break
            if found:
                break
            # also check phrase context for year mention
            phrase_match = phrase_pattern.search(window)
            if phrase_match:
                phrase_win = phrase_match.group(0)
                # check if phrase_win contains 2022 or spring or month
                if re.search(r"2022|\\'22|spring|march|mar|april|apr|may", phrase_win, re.IGNORECASE):
                    matched_projects.add(pname)
                    found = True
                    break
            start = idx + 1
        if found:
            break

# Prepare result
matched_list = sorted(list(matched_projects))
count = len(matched_list)

# Sum funding for matched projects
total_funding = 0
for p in matched_list:
    total_funding += funding_by_project.get(p,0)

result = {
    'count': count,
    'total_funding': total_funding,
    'projects': matched_list
}

import json
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_kSM3FdQY4FQ0hzQ5QbDB9gSg': ['civic_docs'], 'var_call_AkSZPXv5Eo9yhyVh4kfApsb3': ['Funding'], 'var_call_1sy2EAmn2hPEFkep0c11JWFu': 'file_storage/call_1sy2EAmn2hPEFkep0c11JWFu.json', 'var_call_EfxXsrQD5f5UJ8SOm4SNG3rz': 'file_storage/call_EfxXsrQD5f5UJ8SOm4SNG3rz.json'}

exec(code, env_args)
