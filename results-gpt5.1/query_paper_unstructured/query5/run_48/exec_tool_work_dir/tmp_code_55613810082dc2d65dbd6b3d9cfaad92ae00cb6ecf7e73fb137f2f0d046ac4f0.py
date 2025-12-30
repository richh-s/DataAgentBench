code = """import json, re

# Load full Mongo results
with open(var_call_vZvb5sUtr0kPSOxPpzVgBJNu, 'r') as f:
    mongo_docs = json.load(f)

# Extract CHI titles from text
chi_titles = set()
for doc in mongo_docs:
    text = doc.get('text', '')
    # Heuristic: look for lines containing CHI and a year
    if re.search(r"CHI '\d{2}", text) or re.search(r"CHI\s+\d{4}", text):
        filename = doc.get('filename', '')
        if filename.lower().endswith('.txt'):
            title = filename[:-4]
        else:
            title = filename
        chi_titles.add(title)

# Load citation results
with open(var_call_QQvWS4czr642OwtNpNmyzOLM, 'r') as f:
    citations = json.load(f)

# Sum citations for CHI titles in 2020
chi_citation_total = 0
for row in citations:
    title = row.get('title')
    if title in chi_titles:
        try:
            chi_citation_total += int(row.get('citation_count', 0))
        except ValueError:
            pass

result = chi_citation_total

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_vZvb5sUtr0kPSOxPpzVgBJNu': 'file_storage/call_vZvb5sUtr0kPSOxPpzVgBJNu.json', 'var_call_QQvWS4czr642OwtNpNmyzOLM': 'file_storage/call_QQvWS4czr642OwtNpNmyzOLM.json'}

exec(code, env_args)
