code = """import json, re

# Load aggregated citations
citations_file = locals()['var_functions.query_db:14']
with open(citations_file, 'r') as f:
    aggregated_citations = json.load(f)

# Create a dict mapping title to total_citations (int)
citation_map = {}
for entry in aggregated_citations:
    title = entry['title']
    total = entry.get('total_citations')
    if total is not None:
        # total may be string
        citation_map[title] = int(total)

# Load paper documents
paper_docs_file = locals()['var_functions.query_db:2']
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Extract relevant info for each paper: title, year, domains
paper_info = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    title = filename.replace('.txt', '')
    # Extract year (first 4-digit year appearing)
    year_match = re.search(r'(\b(20|19)\d{2})\b', text)
    year = int(year_match.group(1)) if year_match else None
    # Determine domains by substring search
    domains = []
    domain_keywords = ['physical activity', 'food', 'sleep', 'mental', 'finances', 'productivity', 'screen time', 'social interactions', 'location', 'chronic', 'diabetes', 'health_behavior']
    for keyword in domain_keywords:
        if keyword in text.lower():
            domains.append(keyword)
    paper_info.append({'title': title, 'year': year, 'domains': domains})

# Filter papers from 2016 belonging to physical activity domain
papers_2016 = [p for p in paper_info if p['year'] == 2016 and 'physical activity' in p['domains']]

# Build result list with total citations per paper
result = []
for paper in papers_2016:
    title = paper['title']
    total_citations = citation_map.get(title, 0)
    result.append({'title': title, 'total_citations': total_citations})

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:10': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
