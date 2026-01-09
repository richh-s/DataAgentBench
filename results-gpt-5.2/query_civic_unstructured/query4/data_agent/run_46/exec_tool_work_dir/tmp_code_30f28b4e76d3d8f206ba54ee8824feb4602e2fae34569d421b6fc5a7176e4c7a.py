code = """import json, re, pandas as pd

path_docs = var_call_0Q7uZWEBbZuq7uCVz0h5szhe
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

path_fund = var_call_PvNbNrBHZsCagTWdhhs24FkZ
with open(path_fund, 'r', encoding='utf-8') as f:
    fund = json.load(f)

df_f = pd.DataFrame(fund)
if not df_f.empty:
    df_f['Total_Amount'] = pd.to_numeric(df_f['Total_Amount'], errors='coerce').fillna(0).astype(int)
proj_names = set(df_f['Project_Name'].dropna().astype(str).tolist()) if not df_f.empty else set()

spring_pat = re.compile(r'(spring\s*,?\s*2022|2022\s*-\s*spring|2022\s+spring)', re.I)

def is_spring_2022(s: str) -> bool:
    return bool(spring_pat.search(s))

spring_started = set()

for d in docs:
    text = d.get('text','') or ''
    if not text:
        continue
    lines = [ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        if not ln:
            continue
        for pn in proj_names:
            if pn and pn in ln:
                window = "\n".join(lines[i:i+15])
                if is_spring_2022(window) and re.search(r'\bbegin\s+construction\b', window, flags=re.I):
                    spring_started.add(pn)
                if is_spring_2022(window) and re.search(r'\bstart\b\s*:', window, flags=re.I):
                    spring_started.add(pn)

if len(spring_started) == 0:
    for d in docs:
        text = d.get('text','') or ''
        if not text:
            continue
        lines = [ln.strip() for ln in text.splitlines()]
        for i in range(len(lines)):
            window = "\n".join(lines[i:i+10])
            if is_spring_2022(window) and re.search(r'\bbegin\s+construction\b', window, flags=re.I):
                for j in range(i, max(-1, i-12), -1):
                    for pn in proj_names:
                        if pn and pn in lines[j]:
                            spring_started.add(pn)
                            break
                    if len(spring_started)>0:
                        break

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
