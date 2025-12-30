code = """import json
import re

# Load citations data
citations = var_call_wGtovJDfY5fwXNtQUn7Sqfgh

# Load paper docs from file path
file_path = var_call_pkzqV8VBcYQwi95mlBQuFw0i
with open(file_path, 'r') as f:
    paper_docs = json.load(f)

# Build a map from title to venue using filename and text heuristics
chi_titles = set()
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '') or ''
    # title is filename without .txt
    title = re.sub(r'\.txt$', '', filename)
    # Heuristic: consider it CHI if ' CHI ' or "CHI '" or "CHI 20" appears near top or with ACM
    header = text[:1000].upper()
    if ' CHI ' in header or "CHI '" in header or 'CHI CONFERENCE' in header:
        chi_titles.add(title)

# Sum citation counts in 2020 for CHI papers
total_citations = 0
for row in citations:
    title = row.get('title')
    if title in chi_titles:
        try:
            c = int(row.get('citation_count', 0))
        except Exception:
            c = 0
        total_citations += c

result = total_citations

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_wGtovJDfY5fwXNtQUn7Sqfgh': 'file_storage/call_wGtovJDfY5fwXNtQUn7Sqfgh.json', 'var_call_pkzqV8VBcYQwi95mlBQuFw0i': 'file_storage/call_pkzqV8VBcYQwi95mlBQuFw0i.json'}

exec(code, env_args)
