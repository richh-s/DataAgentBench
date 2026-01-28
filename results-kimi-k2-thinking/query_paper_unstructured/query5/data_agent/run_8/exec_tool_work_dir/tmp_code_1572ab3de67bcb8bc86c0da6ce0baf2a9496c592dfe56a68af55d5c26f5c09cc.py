code = """import json
import re

# Load all 2020 citations
citations_path = locals()['var_functions.query_db:44']
papers_path = locals()['var_functions.query_db:10']

with open(citations_path, 'r') as f:
    citations_2020 = json.load(f)

with open(papers_path, 'r') as f:
    papers = json.load(f)

# Build citation dictionary
citation_dict = {}
for cit in citations_2020:
    citation_dict[cit['title']] = int(cit['citation_count'])

# Find CHI papers and sum citations
total_citations = 0
chi_paper_count = 0
chi_papers_with_citations = 0

# CHI patterns to search for
chi_patterns = [
    r'CHI\s*\'\d{2}',
    r'CHI\s*20\d{2}',
    r'Proceedings of the CHI',
    r'ACM Conference on Human Factors',
    r'Conference on Human Factors in Computing Systems'
]

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Check if this is a CHI paper
    is_chi = False
    for pattern in chi_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            is_chi = True
            break
    
    if is_chi:
        chi_paper_count += 1
        if title in citation_dict:
            total_citations += citation_dict[title]
            chi_papers_with_citations += 1

result = {
    'total_citation_count': total_citations,
    'chi_papers_identified': chi_paper_count,
    'chi_papers_with_2020_citations': chi_papers_with_citations,
    'total_2020_citations_processed': len(citations_2020)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
