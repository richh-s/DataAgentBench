code = """import json
import re

# Load papers
# The variable name is var_function-call-16262289729118297755 (from context)
# Python variable mapping usually replaces dashes with underscores in some environments, 
# but here I should use locals()[key] or just the key string if I am opening a file.
# The tool description says: "the storage entry will be the .json file path (a string)".
# So I can access it via the variable name provided in the previous message.
# The variable name was `var_function-call-16262289729118297755`. 
# Wait, I cannot use dashes in variable names in Python directly.
# The system instruction says: "Inside execute_python code you may read storage entries using the provided key names, e.g., if the tool call id is 'call-1', you can access its result via `locals()['var_call-1']` in your code."
# So I will use `locals()['var_function-call-16262289729118297755']`.

file_papers = locals()['var_function-call-16262289729118297755']
file_citations = locals()['var_function-call-16262289729118296254']

with open(file_papers, 'r') as f:
    papers = json.load(f)

with open(file_citations, 'r') as f:
    citations = json.load(f)

# Build citation map
citation_map = {}
for c in citations:
    t = c['title']
    count = c['citation_count']
    if t not in citation_map:
        citation_map[t] = 0
    citation_map[t] += count

results = []
domain_keyword = "physical activity"

for p in papers:
    text = p['text']
    filename = p['filename']
    title = filename.replace('.txt', '')
    
    # Check domain explicitly
    if domain_keyword.lower() not in text.lower():
        continue
    
    # Extract year
    # Look at the first 1000 characters
    header = text[:1000]
    
    # Check for Copyright 2016
    is_2016 = False
    if "Copyright 2016" in header or "© 2016" in header or "©2016" in header:
        is_2016 = True
    elif "2016" in header:
        # Heuristic: if 2016 is present, and no other year (2015, 2017, 2018) is present in the first 200 chars.
        # Often the first line is the conference line.
        first_line = text[:200]
        years_found = re.findall(r'20\d{2}', first_line)
        years_found = [y for y in years_found]
        
        if '2016' in years_found:
            # If 2016 is the only year, or the most prominent?
            # If '2015' and '2016' are there? e.g. "Review of 2015... Published 2016"
            # If '2016' and '2017' are there? e.g. "Copyright 2016... Conference 2017" (unlikely)
            # Let's verify no "2017" or "2018" or "2019" etc in the copyright notice.
            
            # Check for other copyright years
            if re.search(r'Copyright (20(?!16)\d{2})', header) or re.search(r'© (20(?!16)\d{2})', header):
                is_2016 = False
            else:
                 # If we see "2016" and no competing copyright year, assume 2016.
                 is_2016 = True
    
    # Also check for '16 suffix in conference names in first 200 chars
    # e.g. "CHI '16", "Ubicomp '16"
    if not is_2016:
        if re.search(r"[A-Z]+\s?'16", header[:200]):
            is_2016 = True

    if is_2016:
        count = citation_map.get(title, 0)
        results.append({"title": title, "total_citation_count": count})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-3509049514350352642': 'file_storage/function-call-3509049514350352642.json', 'var_function-call-3509049514350351227': ['Citations', 'sqlite_sequence'], 'var_function-call-16262289729118297755': 'file_storage/function-call-16262289729118297755.json', 'var_function-call-16262289729118296254': 'file_storage/function-call-16262289729118296254.json'}

exec(code, env_args)
