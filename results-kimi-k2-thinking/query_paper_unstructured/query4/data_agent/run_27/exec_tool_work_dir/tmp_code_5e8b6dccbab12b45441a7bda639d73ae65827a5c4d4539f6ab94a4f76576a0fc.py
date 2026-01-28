code = """import json
import re

# Load both datasets
mongo_file = locals()['var_functions.query_db:2']
citations_file = locals()['var_functions.query_db:22']

with open(mongo_file, 'r') as f:
    papers_data = json.load(f)

with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Build citation totals
citation_totals = {}
for citation in citations_data:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    citation_totals[title] = citation_totals.get(title, 0) + count

# Extract papers with physical activity domain and year
physical_activity_2016 = []

for doc in papers_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Check for physical activity domain
    text_lower = text.lower()
    has_physical_activity = 'physical activity' in text_lower
    
    # Extract year - try multiple patterns
    year = None
    patterns = [
        (r'\b(2016)\b', lambda m: int(m.group(1))),  # Explicit 2016
        (r"[A-Z]['’](16)\b", lambda m: 2016),  # CHI '16 format
        (r'\b(20[12][0-9])\b', lambda m: int(m.group(1))),  # Any year
    ]
    
    for pattern, extractor in patterns:
        match = re.search(pattern, text)
        if match:
            year = extractor(match)
            break
    
    if has_physical_activity and year == 2016:
        total_cites = citation_totals.get(title, 0)
        physical_activity_2016.append({
            'title': title,
            'total_citations': total_cites
        })

# Format result
result = {
    'papers': physical_activity_2016,
    'total_papers': len(physical_activity_2016)
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'total_papers_found': 0, 'papers_2016': [], 'count_2016': 0}, 'var_functions.list_db:10': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:12': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.execute_python:14': {'year_distribution': {}, 'physical_activity_papers_by_year': {}, 'counts_by_year': {}}, 'var_functions.execute_python:18': {'total_physical_activity_papers': 4, 'papers_2016': [], 'count_2016': 0}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:26': {'papers_2016': [], 'physical_activity_papers_total': 0}, 'var_functions.execute_python:28': {'physical_activity_papers_by_year': {}, 'papers_2016': [], 'total_2016_papers': 0}, 'var_functions.execute_python:32': {'papers_2016_physical_activity': [], 'count': 0}}

exec(code, env_args)
