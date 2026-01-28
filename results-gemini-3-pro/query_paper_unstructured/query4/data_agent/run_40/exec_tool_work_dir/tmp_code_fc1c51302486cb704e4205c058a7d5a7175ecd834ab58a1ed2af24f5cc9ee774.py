code = """import json
import re

# Load data
with open(locals()['var_function-call-17095788158205138574'], 'r') as f:
    papers = json.load(f)

with open(locals()['var_function-call-7387633955592090896'], 'r') as f:
    citations_list = json.load(f)

# Convert citations list to dict for fast lookup
# Keys are titles. Titles in citations match filename without extension.
citations_dict = {c['title']: int(c['total_citations']) for c in citations_list}

results = []

for p in papers:
    text = p['text']
    filename = p['filename']
    title = filename.replace('.txt', '')
    
    # Check domain: 'physical activity'
    # Use case-insensitive containment as per hint
    if 'physical activity' not in text.lower():
        continue

    # Check year: 2016
    # Look at the first 500 characters which usually contain the header/copyright info
    header = text[:500]
    
    # We look for '2016' or "'16" in the context of a conference or copyright
    # Matches: "CHI '16", "CHI 2016", "Copyright 2016", "September 2016"
    # Avoid: "References... 2016" (unlikely in first 500 chars)
    
    # Patterns for 2016
    regex_2016 = r"(?:2016|'16)"
    
    # Patterns for other years (to avoid false positives if mention is incidental)
    # But usually the header contains the correct year.
    # What if a 2017 paper cites a 2016 paper in the abstract? 
    # Abstract usually doesn't have citations like "Smith 2016".
    # But to be safe, let's look for the year in the conference line.
    
    # Specific Venue check (strongest signal)
    venues = r"(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)"
    venue_match = re.search(f"{venues}.*?{regex_2016}", header, re.IGNORECASE | re.DOTALL)
    
    # Copyright/Date match
    date_match = re.search(r"(?:January|February|March|April|May|June|July|August|September|October|November|December|Copyright|©).*?2016", header, re.IGNORECASE)
    
    if venue_match or date_match:
        # It is a 2016 paper
        count = citations_dict.get(title, 0)
        results.append({"title": title, "citation_count": count})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-16853199496411036361': 'file_storage/function-call-16853199496411036361.json', 'var_function-call-17095788158205138574': 'file_storage/function-call-17095788158205138574.json', 'var_function-call-7387633955592090896': 'file_storage/function-call-7387633955592090896.json'}

exec(code, env_args)
