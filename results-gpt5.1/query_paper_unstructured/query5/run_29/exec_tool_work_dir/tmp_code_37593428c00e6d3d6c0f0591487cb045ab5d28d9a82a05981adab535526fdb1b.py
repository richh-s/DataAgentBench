code = """import json, re
from pathlib import Path

# Load prior results
cit_path = Path(var_call_kB1YoNiHm543eI1dJwm1uy81)
with cit_path.open() as f:
    citations = json.load(f)

paper_path = Path(var_call_keGFtrATsqTA7PBDCow06AK9)
with paper_path.open() as f:
    papers = json.load(f)

venue_by_title = {}
for doc in papers:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text','')
    head = text[:2000].upper()
    if ' CHI ' in head or 'CHI CONFERENCE' in head or 'ACM CHI' in head:
        venue_by_title[title] = 'CHI'

chi_titles = set(venue_by_title.keys())

total = 0
for row in citations:
    if row['title'] in chi_titles:
        try:
            total += int(row['citation_count'])
        except Exception:
            pass

print("__RESULT__:")
print(json.dumps(total))"""

env_args = {'var_call_kB1YoNiHm543eI1dJwm1uy81': 'file_storage/call_kB1YoNiHm543eI1dJwm1uy81.json', 'var_call_keGFtrATsqTA7PBDCow06AK9': 'file_storage/call_keGFtrATsqTA7PBDCow06AK9.json'}

exec(code, env_args)
