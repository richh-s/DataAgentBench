code = """import json
import re

# Load datasets
cit_file = locals()['var_functions.query_db:34']
paper_file = locals()['var_functions.query_db:2']

with open(cit_file) as f:
    citations = json.load(f)
with open(paper_file) as f:
    papers = json.load(f)

# Create citation lookup
citation_lookup = {}
for rec in citations:
    citation_lookup[rec['title']] = int(rec['total_citations'])

# Process all papers to extract years and check for physical activity
all_papers_info = []
pa_keyword_counts = {}

for doc in papers:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    if not title:
        continue
    
    text = doc.get('text', '')
    
    # Extract publication year
    year = None
    
    # Try copyright line
    copyright_match = re.search(r'Copyright\s+(?:\d{4}\s+[-–]?\s*)?(20\d{2})', text[:3000])
    if copyright_match:
        year = int(copyright_match.group(1))
    
    # Fallback to other methods
    if not year:
        conf_match = re.search(r"(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s+'?(\d{2})\b", text[:1500])
        if conf_match:
            yr = int(conf_match.group(1))
            if yr < 50:
                year = 2000 + yr
    
    if not year:
        year_matches = re.findall(r'\b20\d{2}\b', text[:2000])
        for match in year_matches:
            y = int(match)
            if 2010 <= y <= 2025:
                year = y
                break
    
    if year:
        all_papers_info.append({'title': title, 'year': year, 'text': text})

# Check year distribution
from collections import Counter
year_counts = Counter([p['year'] for p in all_papers_info])

print('Year distribution:')
print(json.dumps(dict(sorted(year_counts.items()))))

# Check 2016 papers
papers_2016 = [p for p in all_papers_info if p['year'] == 2016]
print('\n2016 papers count: ' + str(len(papers_2016)))

# Find physical activity papers from 2016
physical_activity_keywords = ['physical activity', 'fitness', 'exercise', 'workout', 'sedentary', 'step', 'running', 'walking', 'sports', 'active']

results = []
for paper in papers_2016:
    text_lower = paper['text'].lower()
    title_lower = paper['title'].lower()
    
    in_pa_domain = any(keyword in text_lower or keyword in title_lower for keyword in physical_activity_keywords)
    
    if in_pa_domain:
        citations = citation_lookup.get(paper['title'], 0)
        results.append({'title': paper['title'], 'total_citation_count': citations})

# Sort by citation count
def get_citation_count(item):
    return item['total_citation_count']

results.sort(key=get_citation_count, reverse=True)

print('\n2016 physical activity papers:')
print(json.dumps(results))

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': [], 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': [], 'var_functions.execute_python:28': {'total_papers': 5, 'papers_2016': 0}, 'var_functions.execute_python:32': {'papers_count': 0, 'papers': []}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:38': [], 'var_functions.execute_python:46': [], 'var_functions.execute_python:50': [], 'var_functions.execute_python:56': [], 'var_functions.execute_python:64': [], 'var_functions.execute_python:68': []}

exec(code, env_args)
