code = """import re, json, pandas as pd

# Load full civic docs
path = var_call_tCxhwZjUUbPMoBfvramAj4VS
with open(path, 'r') as f:
    civic_docs = json.load(f)

funding = pd.DataFrame(var_call_aaOR3I98biJkDrzOfwH4Oqpx)
funding['Amount'] = funding['Amount'].astype(int)

text = '\n'.join(doc['text'] for doc in civic_docs)

# Heuristic extraction: find project lines mentioning completion in 2022 and that look park-related
projects = []
for line in text.split('\n'):
    l = line.strip()
    if not l:
        continue
    if 'Construction was completed' in l or 'Construction was completed,' in l or 'completed November 2022' in l or 'completed, November 2022' in l:
        if '2022' in l:
            # get a window of 3 previous lines to guess project name
            pass

# Instead, manually search for known park-related projects completed in 2022 using simple patterns
park_keywords = ['Park', 'playground', 'Playground']

completed_2022_projects = set()
for doc in civic_docs:
    lines = doc['text'].split('\n')
    for i, line in enumerate(lines):
        if 'Construction was completed' in line and '2022' in line:
            # look upward for a line that appears to be a project title
            for j in range(i-1, max(-1, i-6), -1):
                name_line = lines[j].strip()
                if not name_line:
                    continue
                # heuristic: title case and not too long
                if len(name_line) < 120 and any(k in name_line for k in park_keywords):
                    completed_2022_projects.add(name_line.strip())
                    break

# Map these inferred names to funding Project_Name by approximate match (contains)
matched_funding = funding[funding['Project_Name'].apply(
    lambda pn: any(pn in p or p in pn for p in completed_2022_projects)
)]

# Additionally, include obviously park-related projects with "Park" in name where we know from preview they were completed 2022
extra_candidates = funding[funding['Project_Name'].str.contains('Park', case=False, na=False)]

# From the agenda preview we know: Bluffs Park Shade Structure completed November 2022, Point Dume Walkway Repairs (park-ish), Broad Beach Road Water Quality Repair not park
# Filter extra candidates to specific ones by name heuristics: include 'Bluffs Park Shade Structure', 'Trancas Canyon Park Playground', 'Legacy Park', 'Malibu Bluffs Park', 'Malibu Park'
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
