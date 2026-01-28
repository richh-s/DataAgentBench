code = """import json
import re

# Get file paths
mongo_file = locals()['var_functions.query_db:2']
citations_file = locals()['var_functions.query_db:22']

# Load MongoDB data
with open(mongo_file, 'r') as f:
    papers_data = json.load(f)

# Load citations data
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Extract physical activity papers from ALL years
physical_activity_papers = []
for doc in papers_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    title = filename.replace('.txt', '') if filename else ''
    
    # Find year in first 2000 chars to avoid reference section
    year_match = re.search(r'\b(20[12][0-9])\b', text[:2000])
    year = int(year_match.group(1)) if year_match else None
    
    # Check for physical activity domain
    text_lower = text.lower()
    is_physical_activity = 'physical activity' in text_lower
    
    if title and year and is_physical_activity:
        physical_activity_papers.append({
            'title': title,
            'year': year
        })

# Count by year
years = {}
for paper in physical_activity_papers:
    year = paper['year']
    years[year] = years.get(year, 0) + 1

# Get 2016 papers specifically
papers_2016 = [p for p in physical_activity_papers if p['year'] == 2016]

# Get citation counts for 2016 papers
for paper in papers_2016:
    total_citations = 0
    for citation in citations_data:
        if citation.get('title', '') == paper['title']:
            total_citations += int(citation.get('citation_count', 0))
    paper['total_citations'] = total_citations

result = {
    'physical_activity_papers_by_year': years,
    'papers_2016': papers_2016,
    'total_2016_papers': len(papers_2016)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'total_papers_found': 0, 'papers_2016': [], 'count_2016': 0}, 'var_functions.list_db:10': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:12': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.execute_python:14': {'year_distribution': {}, 'physical_activity_papers_by_year': {}, 'counts_by_year': {}}, 'var_functions.execute_python:18': {'total_physical_activity_papers': 4, 'papers_2016': [], 'count_2016': 0}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:26': {'papers_2016': [], 'physical_activity_papers_total': 0}}

exec(code, env_args)
