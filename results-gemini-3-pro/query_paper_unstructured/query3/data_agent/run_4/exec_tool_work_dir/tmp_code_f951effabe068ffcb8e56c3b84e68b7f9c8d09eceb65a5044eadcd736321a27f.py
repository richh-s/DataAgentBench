code = """import json
import re

# Get file paths from storage
docs_path = locals()['var_function-call-11712304195294590657']
citations_path = locals()['var_function-call-1716571983847186930']

# Load data
with open(docs_path, 'r') as f:
    docs = json.load(f)

with open(citations_path, 'r') as f:
    citations_list = json.load(f)

# Create citation map
citation_map = {}
for item in citations_list:
    # Handle case where total_citations might be None (though sum usually 0 or null)
    # and convert to int
    val = item['total_citations']
    if val is None:
        val = 0
    citation_map[item['title']] = int(val)

results = []
# Regex for year 20xx
year_pattern = re.compile(r'\b(20\d{2})\b')

for doc in docs:
    title = doc['filename'].replace('.txt', '')
    text = doc.get('text', '')
    
    # Extract year from first 1000 chars
    head = text[:1000]
    matches = year_pattern.findall(head)
    
    # Filter valid years (e.g. 2000-2025)
    valid_years = [int(y) for y in matches if 2000 <= int(y) <= 2025]
    
    if not valid_years:
        continue
        
    # Assume first valid year is publication year
    pub_year = valid_years[0]
    
    # Check if published after 2016 (i.e., >= 2017)
    if pub_year > 2016:
        # Check for 'empirical' contribution
        if 'empirical' in text.lower():
            count = citation_map.get(title, 0)
            results.append({"title": title, "citation_count": count})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-2488897031636296364': 'file_storage/function-call-2488897031636296364.json', 'var_function-call-2488897031636298801': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-13084840739219341064': 'file_storage/function-call-13084840739219341064.json', 'var_function-call-11712304195294590657': 'file_storage/function-call-11712304195294590657.json', 'var_function-call-14759133979912557114': [{'count(*)': '1405'}], 'var_function-call-1716571983847186930': 'file_storage/function-call-1716571983847186930.json'}

exec(code, env_args)
