code = """import json
import re

# Load data
# Using the variables provided in the previous turn
citations_file = locals()['var_function-call-332096647494284469']
papers_file = locals()['var_function-call-9719230712903826217']

with open(citations_file, 'r') as f:
    citations_data = json.load(f)

with open(papers_file, 'r') as f:
    papers_data = json.load(f)

# Create citation map: Title -> Total Citations
# The SQL query result keys are 'title' and 'total_citations'
# Note: total_citations might be a string in the JSON
citation_map = {}
for item in citations_data:
    try:
        count = int(item['total_citations'])
    except:
        count = 0
    citation_map[item['title']] = count

results = []

for paper in papers_data:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Extract Year
    # Look in first 2000 chars for metadata
    header_text = text[:2000]
    
    # Logic: Search for 2016
    # Or specific conference abbreviations followed by '16
    is_2016 = False
    
    # Check for explicitly 2016
    if re.search(r'\b2016\b', header_text):
        is_2016 = True
    else:
        # Check for '16 with conference names
        # Venues: CHI, Ubicomp, CSCW, DIS, PervasiveHealth, WWW, IUI, OzCHI, TEI, AH
        venues = ["CHI", "Ubicomp", "CSCW", "DIS", "PervasiveHealth", "WWW", "IUI", "OzCHI", "TEI", "AH"]
        pattern = r"(" + "|".join(venues) + r").*?'16"
        if re.search(pattern, header_text, re.IGNORECASE):
            is_2016 = True
            
    # Extract Domain
    # Check for "physical activity" in full text
    # Hint: "values may be part of a list", "substring/contains matching"
    domain_match = "physical activity" in text.lower()
    
    if is_2016 and domain_match:
        count = citation_map.get(title, 0)
        results.append({"title": title, "citation_count": count})

# Sort results by title for consistency
results.sort(key=lambda x: x['title'])

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-332096647494284469': 'file_storage/function-call-332096647494284469.json', 'var_function-call-332096647494285302': 'file_storage/function-call-332096647494285302.json', 'var_function-call-9719230712903826217': 'file_storage/function-call-9719230712903826217.json'}

exec(code, env_args)
