code = """import json
import re

# Load citations
with open(locals()['var_function-call-6342000761403970921'], 'r') as f:
    citations_data = json.load(f)

cit_counts = {}
for c in citations_data:
    t = c['title']
    # citation_count might be string or int. The preview showed string "4".
    # Convert to int.
    try:
        cnt = int(c['citation_count'])
    except:
        cnt = 0
    if t not in cit_counts:
        cit_counts[t] = 0
    cit_counts[t] += cnt

# Load papers
with open(locals()['var_function-call-15772907393576741835'], 'r') as f:
    papers_data = json.load(f)

results = []

for p in papers_data:
    filename = p['filename']
    title = filename.rsplit('.', 1)[0]
    text = p['text']
    
    # Check contribution: "empirical" (case insensitive)
    # Also hint says "values may be part of a list".
    # And "extract contribution".
    # I will assume if the word 'empirical' is present, it counts.
    if 'empirical' not in text.lower():
        continue
        
    # Check year
    # Look for 4-digit years 20xx in first 1000 chars
    header = text[:1000]
    # Regex for 2000-2029
    years = re.findall(r'\b(20[0-2][0-9])\b', header)
    
    pub_year = 0
    if years:
        # Take the first year found
        pub_year = int(years[0])
    
    # Filter: published AFTER 2016 => year > 2016
    if pub_year > 2016:
        # Get citation count
        count = cit_counts.get(title, 0)
        results.append({"title": title, "citation_count": count})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-11810081531988972241': ['paper_docs'], 'var_function-call-10291775221222249891': 'file_storage/function-call-10291775221222249891.json', 'var_function-call-15772907393576741835': 'file_storage/function-call-15772907393576741835.json', 'var_function-call-6342000761403970921': 'file_storage/function-call-6342000761403970921.json'}

exec(code, env_args)
