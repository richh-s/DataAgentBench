code = """import re, json, pandas as pd

with open(var_call_czCIqYV9JkB35ksFyAYXASFo, 'r') as f:
    civic_docs = json.load(f)

texts = ' '.join(d['text'] for d in civic_docs)

projects = {}
pattern1 = r"([A-Z][A-Za-z0-9 &()'-]+Park[ A-Za-z0-9&()'-]*)(?:\n|\r|\s)+(?:\(cid:[0-9]+\) )?Updates:[^\n]*\n(?:.*?)(Construction was completed|construction was completed|completed,?)\s*(November 2022|December 2022|October 2022|September 2022|2022)"
for m in re.finditer(pattern1, texts, re.IGNORECASE|re.DOTALL):
    name = re.sub(r"\s+", " ", m.group(1)).strip()
    projects[name] = '2022'

pattern2 = r"(Bluffs Park Shade Structure)[^\n]*Construction was completed November 2022"
for m in re.finditer(pattern2, texts, re.IGNORECASE):
    name = re.sub(r"\s+", " ", m.group(1)).strip()
    projects[name] = '2022'

funding = var_call_GKMTqe3eDghpSYGqBqjF81D6

park_project_names = set(projects.keys())

pattern3 = r"([A-Z][A-Za-z0-9 '&()-]*Park[ A-Za-z0-9'&()-]*?)\s*(?:Project)?\s*\n[^\n]*Construction was completed[^\n]*2022"
for m in re.finditer(pattern3, texts, re.IGNORECASE):
    name = re.sub(r"\s+", " ", m.group(1)).strip()
    park_project_names.add(name)

from difflib import get_close_matches

selected = []
for row in funding:
    pname = row['Project_Name']
    if 'Park' in pname:
        match = get_close_matches(pname, list(park_project_names), n=1, cutoff=0.7)
        if match:
            selected.append(int(row['Amount']))

total = sum(selected)

result = {"total_funding_2022_completed_park_projects": total, "matched_park_projects": sorted(list(park_project_names)), "selected_funding_records_count": len(selected)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_czCIqYV9JkB35ksFyAYXASFo': 'file_storage/call_czCIqYV9JkB35ksFyAYXASFo.json', 'var_call_GKMTqe3eDghpSYGqBqjF81D6': 'file_storage/call_GKMTqe3eDghpSYGqBqjF81D6.json'}

exec(code, env_args)
