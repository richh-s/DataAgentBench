code = """import re, json, pandas as pd

path = var_call_IhMg6d9cSG9ZTmEOIkt7uIbz
with open(path, 'r') as f:
    civic_docs = json.load(f)

funding = pd.DataFrame(var_call_qI763MC8p6fpacXCr6aiaoRx)
funding['Amount'] = funding['Amount'].astype(int)

texts = [d.get('text','') for d in civic_docs]

projects = []
for text in texts:
    lines = text.split('\n')
    for line in lines:
        m = re.match(r"(\d{4} .+?)(?: - |\s+)(Spring|Summer|Fall|Winter)\s*(\d{4})", line)
        if m:
            name = m.group(1).strip()
            season = m.group(2)
            year = m.group(3)
            st = year + '-' + season
            projects.append({'Project_Name': name, 'st': st})

for text in texts:
    for block in text.split('\n\n'):
        lines = block.split('\n')
        if not lines:
            continue
        pname = lines[0].strip()
        if len(pname) < 5 or len(pname.split()) < 2:
            continue
        if not re.search(r"\d", pname):
            continue
        block_str = " ".join(lines[1:])
        if re.search(r"Spring\s*2022", block_str):
            projects.append({'Project_Name': pname, 'st': '2022-Spring'})

proj_df = pd.DataFrame(projects).drop_duplicates(subset=['Project_Name','st'])

spring_2022 = proj_df[proj_df['st'] == '2022-Spring']
merged = pd.merge(funding, spring_2022, on='Project_Name', how='inner')

count_projects = int(merged['Project_Name'].nunique())
 total_funding = int(merged['Amount'].sum())

result = {'projects_started_spring_2022': count_projects, 'total_funding_spring_2022': total_funding}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_IhMg6d9cSG9ZTmEOIkt7uIbz': 'file_storage/call_IhMg6d9cSG9ZTmEOIkt7uIbz.json', 'var_call_qI763MC8p6fpacXCr6aiaoRx': 'file_storage/call_qI763MC8p6fpacXCr6aiaoRx.json', 'var_call_ci1OkIuI0WF9B768RfJ5LeQb': ['civic_docs'], 'var_call_O627E59gAdk62n1WJw740oL4': ['Funding']}

exec(code, env_args)
