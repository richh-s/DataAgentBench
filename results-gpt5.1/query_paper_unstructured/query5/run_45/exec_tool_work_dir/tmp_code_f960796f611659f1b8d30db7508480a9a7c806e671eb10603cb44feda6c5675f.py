code = """import json, re
from collections import defaultdict

# Load citations data from file path (string with json path)
file_path_cit = var_call_GVH7E80WgGIIUOrQHowuizCa
with open(file_path_cit, 'r') as f:
    records = json.load(f)

# Load full paper docs from file path
file_path_docs = var_call_7AyymjQ5AVvJOeuc0ur1XTTi
with open(file_path_docs, 'r') as f:
    paper_docs = json.load(f)

chi_titles = set()
venue_pattern = re.compile(r"CHI\s+'?\d{2}|ACM\s+CHI|CHI Conference", re.IGNORECASE)

for doc in paper_docs:
    filename = doc.get('filename','')
    text = doc.get('text','') or ''
    title = filename.rsplit('.txt',1)[0]
    if venue_pattern.search(text[:2000]):
        chi_titles.add(title)

# Sum citation counts for CHI papers cited in 2020

total_citations = 0
for r in records:
    title = r.get('title')
    if title in chi_titles:
        try:
            c = int(r.get('citation_count',0))
        except Exception:
            c = 0
        total_citations += c

print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_call_GVH7E80WgGIIUOrQHowuizCa': 'file_storage/call_GVH7E80WgGIIUOrQHowuizCa.json', 'var_call_7AyymjQ5AVvJOeuc0ur1XTTi': 'file_storage/call_7AyymjQ5AVvJOeuc0ur1XTTi.json'}

exec(code, env_args)
