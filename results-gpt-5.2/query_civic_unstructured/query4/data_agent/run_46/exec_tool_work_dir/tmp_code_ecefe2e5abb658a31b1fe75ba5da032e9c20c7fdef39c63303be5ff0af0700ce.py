code = """import json, re, pandas as pd

# Load civic docs
path_docs = var_call_0Q7uZWEBbZuq7uCVz0h5szhe
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Load funding per project
path_fund = var_call_PvNbNrBHZsCagTWdhhs24FkZ
with open(path_fund, 'r', encoding='utf-8') as f:
    fund = json.load(f)

df_f = pd.DataFrame(fund)
if df_f.empty:
    spring_projects = []
else:
    df_f['Total_Amount'] = pd.to_numeric(df_f['Total_Amount'], errors='coerce').fillna(0).astype(int)

# Build a set of project names we know from funding (likely superset)
proj_names = set(df_f['Project_Name'].dropna().astype(str).tolist())

# Parse projects from each doc by scanning for each project name and nearby schedule lines.
# Heuristic: if a project name appears and within next 10 lines there is 'Begin' or 'Start' with 'Spring 2022' or 'Spring, 2022' or 'Spring 2022' etc.

def is_spring_2022(text):
    t = text.lower()
    # Accept formats: 'spring 2022', 'spring, 2022', '2022-spring'
    return ('spring 2022' in t) or ('spring, 2022' in t) or ('2022-spring' in t) or ('2022 spring' in t)

spring_started = set()

for d in docs:
    text = d.get('text','')
    if not text:
        continue
    lines = [ln.strip() for ln in text.splitlines()]
    # map lowercase to original for searching
    for i, ln in enumerate(lines):
        if not ln:
            continue
        # check if line contains a known project name exactly
        for pn in list(proj_names):
            if pn and pn in ln:
                window = '\n'.join(lines[i:i+15])
                # consider started if any begin construction/advertise/start indicates spring 2022
                if re.search(r'(begin|start)\s+(construction|work)?\s*:\s*.*', window, flags=re.I) and is_spring_2022(window):
                    spring_started.add(pn)
                # also if schedule line has 'Start:'
                if re.search(r'\b(start|st)\b\s*[:\-]', window, flags=re.I) and is_spring_2022(window):
                    spring_started.add(pn)
                # also if any line just 'Begin Construction: Spring 2022'
                if is_spring_2022(window) and re.search(r'begin\s+construction\s*:\s*spring', window, flags=re.I):
                    spring_started.add(pn)

# If no matches found (heuristic may be too strict), fall back to looser: any project name in doc where any nearby line contains 'Spring 2022' and 'Begin'
if len(spring_started)==0:
    for d in docs:
        text = d.get('text','')
        if not text:
            continue
        lines = [ln.strip() for ln in text.splitlines()]
        for i, ln in enumerate(lines):
            if not ln:
                continue
            if is_spring_2022('\n'.join(lines[i:i+10])) and re.search(r'begin\s+construction', '\n'.join(lines[i:i+10]), flags=re.I):
                # find closest previous line that matches a project name
                for j in range(i, max(-1, i-10), -1):
                    for pn in proj_names:
                        if pn and pn in lines[j]:
                            spring_started.add(pn)
                            break
                    if spring_started:
                        break

# Sum funding
if df_f.empty:
    total = 0
else:
    total = int(df_f[df_f['Project_Name'].isin(list(spring_started))]['Total_Amount'].sum())

result = {
    "spring_2022_projects_started_count": int(len(spring_started)),
    "spring_2022_projects_started_total_funding": total,
    "projects_matched": sorted(list(spring_started))
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_XVPW0uwbUkYJDpsmO3y4DnPe': ['Funding'], 'var_call_DgOgimI8R0WdhykFaKB9TJVq': ['civic_docs'], 'var_call_0Q7uZWEBbZuq7uCVz0h5szhe': 'file_storage/call_0Q7uZWEBbZuq7uCVz0h5szhe.json', 'var_call_PvNbNrBHZsCagTWdhhs24FkZ': 'file_storage/call_PvNbNrBHZsCagTWdhhs24FkZ.json'}

exec(code, env_args)
