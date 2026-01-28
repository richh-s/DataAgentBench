code = """import json, re, os

# Load full citations result
with open(var_call_oJoF5udjL7vBxJLgbzgZUcb2, 'r') as f:
    citations = json.load(f)

# Load full paper docs result
with open(var_call_rw24AkDdDGPYU4o6GdWSQuEO, 'r') as f:
    docs = json.load(f)

# Build mapping from title to venue using heuristic on text
chi_titles = set()
for doc in docs:
    text = doc.get('text','')
    # Heuristic: look for CHI in the first 1000 characters around top header lines
    header = text[:1500].upper()
    if 'CHI ' in header or "CHI'" in header or '\nCHI\n' in header:
        # derive title from filename
        filename = doc.get('filename','')
        if filename.lower().endswith('.txt'):
            title = filename[:-4]
        else:
            title = filename
        chi_titles.add(title)

# Sum citation counts for 2020 for titles that are CHI papers
Total = 0
for row in citations:
    title = row.get('title')
    if title in chi_titles:
        try:
            c = int(row.get('citation_count',0))
        except:
            c = 0
        Total += c

result = Total

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_oJoF5udjL7vBxJLgbzgZUcb2': 'file_storage/call_oJoF5udjL7vBxJLgbzgZUcb2.json', 'var_call_rw24AkDdDGPYU4o6GdWSQuEO': 'file_storage/call_rw24AkDdDGPYU4o6GdWSQuEO.json'}

exec(code, env_args)
