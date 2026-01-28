code = """import json, re, os

with open(var_call_oJoF5udjL7vBxJLgbzgZUcb2, 'r') as f:
    citations = json.load(f)

with open(var_call_rw24AkDdDGPYU4o6GdWSQuEO, 'r') as f:
    docs = json.load(f)

chi_titles = set()
for doc in docs:
    text = doc.get('text', '')
    header = text[:1500].upper()
    if 'CHI ' in header or "CHI'" in header or '\nCHI\n' in header:
        filename = doc.get('filename', '')
        if filename.lower().endswith('.txt'):
            title = filename[:-4]
        else:
            title = filename
        chi_titles.add(title)

Total = 0
for row in citations:
    title = row.get('title')
    if title in chi_titles:
        try:
            c = int(row.get('citation_count', 0))
        except Exception:
            c = 0
        Total += c

print("__RESULT__:")
print(json.dumps(Total))"""

env_args = {'var_call_oJoF5udjL7vBxJLgbzgZUcb2': 'file_storage/call_oJoF5udjL7vBxJLgbzgZUcb2.json', 'var_call_rw24AkDdDGPYU4o6GdWSQuEO': 'file_storage/call_rw24AkDdDGPYU4o6GdWSQuEO.json'}

exec(code, env_args)
