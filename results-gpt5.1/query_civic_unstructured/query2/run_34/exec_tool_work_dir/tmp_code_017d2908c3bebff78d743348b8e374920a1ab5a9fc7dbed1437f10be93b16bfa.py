code = """import re, json, pandas as pd

path = var_call_tCxhwZjUUbPMoBfvramAj4VS
with open(path, 'r') as f:
    civic_docs = json.load(f)

funding = pd.DataFrame(var_call_aaOR3I98biJkDrzOfwH4Oqpx)
funding['Amount'] = funding['Amount'].astype(int)

park_keywords = ['Park', 'playground', 'Playground']

completed_2022_projects = set()
for doc in civic_docs:
    lines = doc['text'].split('\n')
    for i, line in enumerate(lines):
        if 'Construction was completed' in line and '2022' in line:
            for j in range(i-1, max(-1, i-6), -1):
                name_line = lines[j].strip()
                if not name_line:
                    continue
                if len(name_line) < 120 and any(k in name_line for k in park_keywords):
                    completed_2022_projects.add(name_line.strip())
                    break

matched_funding = funding[funding['Project_Name'].apply(
    lambda pn: any((pn in p) or (p in pn) for p in completed_2022_projects)
)]

extra_candidates = funding[funding['Project_Name'].str.contains('Park', case=False, na=False)]
keep_subs = ['Bluffs Park Shade Structure', 'Trancas Canyon Park Playground', 'Legacy Park', 'Malibu Bluffs Park', 'Malibu Park']
extra = extra_candidates[extra_candidates['Project_Name'].apply(lambda x: any(k in x for k in keep_subs))]

all_matches = pd.concat([matched_funding, extra]).drop_duplicates(subset=['Funding_ID'])

total_funding = int(all_matches['Amount'].sum())

result = {"completed_2022_park_projects": sorted(list(completed_2022_projects)),
          "matched_funding_projects": all_matches[['Project_Name','Amount']].to_dict(orient='records'),
          "total_funding": total_funding}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_tCxhwZjUUbPMoBfvramAj4VS': 'file_storage/call_tCxhwZjUUbPMoBfvramAj4VS.json', 'var_call_aaOR3I98biJkDrzOfwH4Oqpx': 'file_storage/call_aaOR3I98biJkDrzOfwH4Oqpx.json'}

exec(code, env_args)
