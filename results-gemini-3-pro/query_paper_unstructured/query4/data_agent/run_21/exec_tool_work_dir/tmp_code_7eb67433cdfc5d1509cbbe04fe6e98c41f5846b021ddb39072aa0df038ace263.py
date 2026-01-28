code = """import json
import re

file_papers = locals()['var_function-call-16262289729118297755']
file_citations = locals()['var_function-call-16262289729118296254']

with open(file_papers, 'r') as f:
    papers = json.load(f)

with open(file_citations, 'r') as f:
    citations = json.load(f)

citation_map = {}
for c in citations:
    t = c['title']
    try:
        count = int(c['citation_count'])
    except:
        count = 0
    if t not in citation_map:
        citation_map[t] = 0
    citation_map[t] += count

results = []
domain_keyword = "physical activity"

for p in papers:
    text = p['text']
    filename = p['filename']
    title = filename.replace('.txt', '')
    
    # Check domain explicitly (case insensitive)
    if domain_keyword.lower() not in text.lower():
        continue
    
    header = text[:1000]
    is_2016 = False
    
    # Check for Copyright 2016
    if "Copyright 2016" in header or "© 2016" in header or "©2016" in header:
        is_2016 = True
    elif "2016" in header:
        first_line = text[:200]
        years_found = re.findall(r'20\d{2}', first_line)
        
        # If 2016 is in the first line years
        if '2016' in years_found:
            # Check if a later year is in the copyright
            if re.search(r'Copyright (20(1[7-9]|2[0-9]))', header) or re.search(r'© (20(1[7-9]|2[0-9]))', header):
                is_2016 = False
            # Check if an earlier year is in the copyright
            elif re.search(r'Copyright (20(0[0-9]|1[0-5]))', header) or re.search(r'© (20(0[0-9]|1[0-5]))', header):
                is_2016 = False
            else:
                 is_2016 = True
        
        # If not in first line, but "2016" is in header?
        # Maybe "Ubicomp '16"
        elif re.search(r"[A-Z]+\s?'16", first_line):
             is_2016 = True
             
    # One more check: "CHI '16" etc
    if not is_2016:
        if re.search(r"[A-Z]+\s?'16", header[:300]):
             is_2016 = True

    if is_2016:
        count = citation_map.get(title, 0)
        results.append({"title": title, "total_citation_count": count})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-3509049514350352642': 'file_storage/function-call-3509049514350352642.json', 'var_function-call-3509049514350351227': ['Citations', 'sqlite_sequence'], 'var_function-call-16262289729118297755': 'file_storage/function-call-16262289729118297755.json', 'var_function-call-16262289729118296254': 'file_storage/function-call-16262289729118296254.json'}

exec(code, env_args)
