code = """import json, re
from pathlib import Path

# Load full Mongo results
mongo_path = Path(var_call_yHEPQSa84SodeT6Ra2FgWUs8)
with mongo_path.open() as f:
    mongo_docs = json.load(f)

# Extract CHI titles from text (look for 'CHI' and a year near the beginning)
chi_titles = set()
for doc in mongo_docs:
    text = doc.get('text', '')[:2000]
    if re.search(r"CHI\s+'?\d{2}|Conference on Human Factors in Computing Systems", text, re.IGNORECASE):
        filename = doc.get('filename', '')
        if filename.lower().endswith('.txt'):
            title = filename[:-4]
        else:
            title = filename
        chi_titles.add(title)

# Load full citations results
cit_path = Path(var_call_uFyWQZ48a49gVq7EYdPG3Hjf)
with cit_path.open() as f:
    cit_rows = json.load(f)

# Sum citation counts in 2020 for CHI papers
chi_titles_lower = {t.lower() for t in chi_titles}

total_citations = 0
for row in cit_rows:
    title = row.get('title', '')
    if title.lower() in chi_titles_lower:
        try:
            c = int(row.get('citation_count', 0))
        except ValueError:
            c = 0
        total_citations += c

result = json.dumps(total_citations)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_yHEPQSa84SodeT6Ra2FgWUs8': 'file_storage/call_yHEPQSa84SodeT6Ra2FgWUs8.json', 'var_call_uFyWQZ48a49gVq7EYdPG3Hjf': 'file_storage/call_uFyWQZ48a49gVq7EYdPG3Hjf.json'}

exec(code, env_args)
