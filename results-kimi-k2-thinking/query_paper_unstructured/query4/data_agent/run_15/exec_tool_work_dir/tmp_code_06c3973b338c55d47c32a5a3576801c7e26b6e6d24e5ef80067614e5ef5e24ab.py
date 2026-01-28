code = """import json, re

# Load citations data
cit_file = locals()['var_functions.query_db:34']
with open(cit_file, 'r') as f:
    citations = json.load(f)

# Load paper documents
paper_file = locals()['var_functions.query_db:2']
with open(paper_file, 'r') as f:
    papers = json.load(f)

print("Data loaded successfully")
print("Citations:", len(citations))
print("Papers:", len(papers))

# Find physical activity papers
pa_papers_all = []
for doc in papers:
    title = doc.get('filename', '').replace('.txt', '')
    if not title:
        continue
    
    text = doc.get('text', '')
    
    # Check for physical activity in text or title
    has_pa = 'physical activity' in text.lower() or 'physical activity' in title.lower()
    
    if not has_pa:
        continue
    
    # Extract year
    year = None
    
    # Try copyright
    copyright_match = re.search(r'Copyright\s+(?:\d{4}\s+[-–]?\s*)?(20\d{2})', text[:2000])
    if copyright_match:
        year = int(copyright_match.group(1))
    
    # Try conference
    if not year:
        conf_match = re.search(r"(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s+'?(\d{2})\b", text[:1000])
        if conf_match:
            year_num = int(conf_match.group(1))
            if year_num < 50:
                year = 2000 + year_num
    
    # Fallback
    if not year:
        year_matches = re.findall(r'\b20\d{2}\b', text[:2000])
        for match in year_matches:
            y = int(match)
            if 2010 <= y <= 2025:
                year = y
                break
    
    if year:
        pa_papers_all.append({'title': title, 'year': year})

print("Physical activity papers found:", len(pa_papers_all))

# Filter for 2016
papers_2016 = [p for p in pa_papers_all if p['year'] == 2016]
print("2016 physical activity papers:", len(papers_2016))

# Build citation map
citation_map = {}
for rec in citations:
    title = rec.get('title', '')
    count = int(rec.get('total_citations', 0))
    citation_map[title] = count

# Combine results
results = []
for paper in papers_2016:
    title = paper['title']
    citations = citation_map.get(title, 0)
    results.append({'title': title, 'total_citation_count': citations})

# Sort by citations
results.sort(key=lambda x: x['total_citation_count'], reverse=True)

print("Final results count:", len(results))
for r in results:
    print(r['title'], ':', r['total_citation_count'])

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': [], 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': [], 'var_functions.execute_python:28': {'total_papers': 5, 'papers_2016': 0}, 'var_functions.execute_python:32': {'papers_count': 0, 'papers': []}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json'}

exec(code, env_args)
