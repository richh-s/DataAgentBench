code = """import json
import re

# Load citations
with open(locals()['var_function-call-16720471753298143428'], 'r') as f:
    citations_data = json.load(f)

# Load papers
with open(locals()['var_function-call-6532184733094038919'], 'r') as f:
    papers_data = json.load(f)

# Helper to normalize title
def normalize_title(t):
    return t.strip().lower()

# Create a map of title -> total citations
citation_map = {}
for entry in citations_data:
    t = normalize_title(entry['title'])
    count = int(entry['citation_count'])
    if t not in citation_map:
        citation_map[t] = 0
    citation_map[t] += count

results = []

for paper in papers_data:
    filename = paper['filename']
    text = paper['text']
    
    # Extract title
    title = filename.replace('.txt', '').strip()
    norm_title = normalize_title(title)
    
    # Extract year
    # Check the first 1000 characters for 2016
    header_text = text[:1000]
    # Check for 2016
    if '2016' in header_text:
        year = 2016
    else:
        year = None
        # Try to find year pattern if not 2016 (maybe 2015?)
        # But we only care about 2016.
        pass
    
    # Check domain
    # We already filtered by "physical activity", but let's double check.
    if 'physical activity' not in text.lower():
        continue

    if year == 2016:
        # Get citations
        total_citations = citation_map.get(norm_title, 0)
        results.append({
            "title": title,
            "total_citations": total_citations
        })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-5019104688225349175': 'file_storage/function-call-5019104688225349175.json', 'var_function-call-4539344191155681833': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-6532184733094038919': 'file_storage/function-call-6532184733094038919.json', 'var_function-call-16720471753298143428': 'file_storage/function-call-16720471753298143428.json'}

exec(code, env_args)
