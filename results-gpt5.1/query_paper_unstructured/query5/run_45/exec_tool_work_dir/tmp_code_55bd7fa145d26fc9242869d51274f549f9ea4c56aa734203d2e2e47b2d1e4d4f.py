code = """import json, re
from collections import defaultdict

# Load citations data (already a list of dicts)
records = var_call_GVH7E80WgGIIUOrQHowuizCa

# Load full paper docs from file path
file_path = var_call_7AyymjQ5AVvJOeuc0ur1XTTi
with open(file_path, 'r') as f:
    paper_docs = json.load(f)

# Build mapping from title to whether venue is CHI
chi_titles = set()
venue_pattern = re.compile(r"CHI\s+'?\d{2}|ACM\s+CHI|CHI Conference", re.IGNORECASE)
year_pattern = re.compile(r"\b(19|20)\d{2}\b")

for doc in paper_docs:
    filename = doc.get('filename','')
    text = doc.get('text','') or ''
    title = filename.rsplit('.txt',1)[0]
    # Heuristic: check if venue line contains CHI
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

result = total_citations

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_GVH7E80WgGIIUOrQHowuizCa': 'file_storage/call_GVH7E80WgGIIUOrQHowuizCa.json', 'var_call_7AyymjQ5AVvJOeuc0ur1XTTi': 'file_storage/call_7AyymjQ5AVvJOeuc0ur1XTTi.json'}

exec(code, env_args)
