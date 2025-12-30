code = """import json
import re

# Load papers
with open(locals()['var_function-call-9106356078782033053'], 'r') as f:
    papers = json.load(f)

# Load citations
with open(locals()['var_function-call-7203993170122994378'], 'r') as f:
    citations = json.load(f)

# Create a dictionary for citations: title -> total_count
citation_sums = {}
for c in citations:
    t = c['title']
    count = int(c['citation_count'])
    citation_sums[t] = citation_sums.get(t, 0) + count

results = []

for p in papers:
    text = p['text']
    filename = p['filename']
    title = filename.replace('.txt', '')
    
    # Extract Year
    # Look in the first 1000 characters
    header = text[:1000]
    
    # Regex for 20xx
    match_year = re.search(r'20[0-2][0-9]', header)
    year = None
    if match_year:
        year = int(match_year.group(0))
    else:
        # Try to find 'xx e.g. '17
        # This is risky, but let's try to match " '1[0-9] " or " '2[0-5] "
        # preceded by a capital letter or space
        # e.g. "CHI '18"
        match_short = re.search(r"[A-Z]+ '[0-9]{2}", header)
        if match_short:
             # extract the last 2 digits
             yy = int(match_short.group(0).split("'")[1])
             year = 2000 + yy
    
    # Extract Contribution
    # Check for "empirical" (case insensitive)
    # The hint says "values may be part of a list", suggesting we might look for specific phrases.
    # But usually finding "empirical" is a good proxy if we lack structured data.
    # I'll check if "empirical" is in the text.
    is_empirical = "empirical" in text.lower()
    
    if year and year > 2016 and is_empirical:
        total_c = citation_sums.get(title, 0)
        results.append({"title": title, "total_citation_count": total_c})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-1382832429316452546': ['paper_docs'], 'var_function-call-1382832429316454187': ['Citations', 'sqlite_sequence'], 'var_function-call-12576902616845472384': 'file_storage/function-call-12576902616845472384.json', 'var_function-call-9106356078782033053': 'file_storage/function-call-9106356078782033053.json', 'var_function-call-7203993170122994378': 'file_storage/function-call-7203993170122994378.json'}

exec(code, env_args)
