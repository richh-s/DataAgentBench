code = """import json
import re

# Get the file paths from locals
citations_var_name = 'var_functions.query_db:26'
papers_var_name = 'var_functions.query_db:10'

citations_path = locals()[citations_var_name]
papers_path = locals()[papers_var_name]

# Load all 2020 citations
with open(citations_path, 'r') as f:
    citations_2020 = json.load(f)

# Load all papers
with open(papers_path, 'r') as f:
    papers = json.load(f)

print(f'Loaded {len(citations_2020)} citations from 2020')
print(f'Loaded {len(papers)} papers from database')

# Build title to citation count map
citation_map = {}
for cit in citations_2020:
    citation_map[cit['title']] = int(cit['citation_count'])

# Find CHI papers and sum their 2020 citations
total_citations = 0
chi_papers_count = 0
chi_papers_with_citations = 0

chi_pattern = re.compile(r'CHI\s*\'?\d{2}', re.I)

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Check if paper is from CHI conference
    if chi_pattern.search(text):
        chi_papers_count += 1
        if title in citation_map:
            total_citations += citation_map[title]
            chi_papers_with_citations += 1

result = {
    'total_2020_citations_for_chi_papers': total_citations,
    'total_chi_papers_found': chi_papers_count,
    'chi_papers_with_2020_citations': chi_papers_with_citations
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
