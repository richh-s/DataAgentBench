code = """import json, re

# Load paper documents from file
paper_file_path = locals()['var_functions.query_db:2']
with open(paper_file_path, 'r') as f:
    paper_docs = json.load(f)

# Load citations data
citations_data = locals()['var_functions.query_db:16']

print("Successfully loaded data")
print("Paper documents count:", len(paper_docs))
print("Citations records count:", len(citations_data))

# Process papers to find 2016 physical activity papers
papers_2016_pa = []

for doc in paper_docs:
    # Extract title
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    if not title:
        continue
    
    # Extract year from text
    year = None
    text = doc.get('text', '')
    year_matches = re.findall(r'\b20\d{2}\b', text[:1000])
    for match in year_matches:
        year_val = int(match)
        if 2010 <= year_val <= 2020:
            year = year_val
            break
    
    # Check if physical activity domain
    is_physical_activity = 'physical activity' in text.lower()
    
    if year == 2016 and is_physical_activity:
        papers_2016_pa.append({
            'title': title,
            'year': year
        })

print("Found 2016 physical activity papers:", len(papers_2016_pa))

# Build citation lookup (title -> list of citation counts)
citation_lookup = {}
for record in citations_data:
    citation_title = record.get('title', '')
    count = int(record.get('citation_count', 0))
    
    if citation_title not in citation_lookup:
        citation_lookup[citation_title] = []
    citation_lookup[citation_title].append(count)

# Calculate total citations for each 2016 PA paper
results = []
for paper in papers_2016_pa:
    paper_title = paper['title']
    total_citations = sum(citation_lookup.get(paper_title, []))
    
    results.append({
        'title': paper_title,
        'total_citation_count': total_citations
    })

# Sort by citation count (descending)
results.sort(key=lambda x: x['total_citation_count'], reverse=True)

print("Results prepared:", len(results))

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': [], 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:22': []}

exec(code, env_args)
