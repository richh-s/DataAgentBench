code = """import json, re

# Load citation data
cit_data = json.load(open(locals()['var_functions.query_db:34']))
paper_data = json.load(open(locals()['var_functions.query_db:2']))

print('Data loaded')
print('Citations:', len(cit_data))
print('Papers:', len(paper_data))

# Build citation lookup
citation_lookup = {}
for item in cit_data:
    citation_lookup[item['title']] = int(item['total_citations'])

# Find papers with physical activity from 2016
results = []

for doc in paper_data:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    if not title:
        continue
    
    text = doc.get('text', '')
    
    # Check for physical activity domain
    if 'physical activity' not in text.lower() and 'physical activity' not in title.lower():
        continue
    
    # Extract year from text
    year = None
    
    # Try copyright line
    copyright_match = re.search(r'Copyright\s+(?:\d{4}\s+[-–]?\s*)?(20\d{2})', text[:3000])
    if copyright_match:
        year = int(copyright_match.group(1))
    
    # Try conference header
    if not year:
        conf_match = re.search(r"(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s+'?(\d{2})\b", text[:2000])
        if conf_match:
            yr = int(conf_match.group(1))
            if yr < 50:
                year = 2000 + yr
    
    # Fallback to reasonable year range
    if not year:
        year_matches = re.findall(r'\b20\d{2}\b', text[:3000])
        for match in year_matches:
            y = int(match)
            if 2010 <= y <= 2025:
                year = y
                break
    
    if year == 2016:
        total_citations = citation_lookup.get(title, 0)
        results.append({'title': title, 'total_citation_count': total_citations})

# Sort by citation count
count = len(results)
print('Found 2016 physical activity papers:', count)

sorted_results = sorted(results, key=lambda x: x['total_citation_count'], reverse=True)

# Print results
for item in sorted_results:
    print('Title:', item['title'])
    print('Citations:', item['total_citation_count'])
    print()

print('__RESULT__:')
print(json.dumps(sorted_results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': [], 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': [], 'var_functions.execute_python:28': {'total_papers': 5, 'papers_2016': 0}, 'var_functions.execute_python:32': {'papers_count': 0, 'papers': []}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:38': []}

exec(code, env_args)
