code = """import json
import re

# Load titles (cited in 2020)
path_titles = locals().get('var_function-call-1495859486444725251')
with open(path_titles, 'r') as f:
    titles = set(json.load(f))

# Load fetched docs
path_docs = locals().get('var_function-call-4693824508147823644')
with open(path_docs, 'r') as f:
    docs = json.load(f)

print(f"Fetched {len(docs)} documents.")

# Check coverage
fetched_filenames = set(d['filename'] for d in docs)
found_titles = []
for t in titles:
    if t + ".txt" in fetched_filenames:
        found_titles.append(t)

print(f"Found {len(found_titles)} out of {len(titles)} cited papers in the fetched documents.")

# Process citations
# I need the citation counts for each title.
# I need to load the citation data again to map title -> count.
path_citations = locals().get('var_function-call-7498192109235549923')
# Actually, I used the file directly in the first step.
# I should reload it.
with open(path_citations, 'r') as f:
    citations_list = json.load(f)

citation_map = {c['title']: c['citation_count'] for c in citations_list}

total_citations = 0
chi_papers_count = 0

for doc in docs:
    fname = doc['filename']
    title = fname.replace('.txt', '')
    
    if title in titles:
        text = doc['text']
        # Check for CHI venue
        # Heuristic: Look for "CHI" in the first 1000 chars, usually in header
        # or "Conference on Human Factors in Computing Systems"
        header = text[:2000]
        # Regex for CHI followed by year, e.g. "CHI '15", "CHI 2015", "CHI 15"
        # Or just "CHI" word in lines that look like conference headers.
        
        # Checking for "CHI" as a word.
        if re.search(r'\bCHI\b', header):
             # Double check to avoid false positives (like "CHI" in a name?)
             # Usually in header it's clear.
             # e.g. "CHI '14, April 26 - May 01 2014..."
             total_citations += int(citation_map[title])
             chi_papers_count += 1
        elif "Conference on Human Factors in Computing Systems" in header:
             total_citations += int(citation_map[title])
             chi_papers_count += 1

print(f"Identified {chi_papers_count} CHI papers.")
print(f"Total citations: {total_citations}")
print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_function-call-7498192109235549923': 'file_storage/function-call-7498192109235549923.json', 'var_function-call-1495859486444725251': 'file_storage/function-call-1495859486444725251.json', 'var_function-call-6405304347776267640': 188, 'var_function-call-15965521281973898392': 'file_storage/function-call-15965521281973898392.json', 'var_function-call-6154840779900112772': 'file_storage/function-call-6154840779900112772.json', 'var_function-call-4693824508147823644': 'file_storage/function-call-4693824508147823644.json'}

exec(code, env_args)
