code = """import json
import re

# Load citations data from file path
file_path_cit = var_call_wGtovJDfY5fwXNtQUn7Sqfgh
with open(file_path_cit, 'r') as f:
    citations = json.load(f)

# Load paper docs from file path
file_path_docs = var_call_pkzqV8VBcYQwi95mlBQuFw0i
with open(file_path_docs, 'r') as f:
    paper_docs = json.load(f)

chi_titles = set()
for doc in paper_docs:
    filename = doc.get('filename', '') or ''
    text = doc.get('text', '') or ''
    title = re.sub(r'\.txt$', '', filename)
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

print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_call_wGtovJDfY5fwXNtQUn7Sqfgh': 'file_storage/call_wGtovJDfY5fwXNtQUn7Sqfgh.json', 'var_call_pkzqV8VBcYQwi95mlBQuFw0i': 'file_storage/call_pkzqV8VBcYQwi95mlBQuFw0i.json'}

exec(code, env_args)
