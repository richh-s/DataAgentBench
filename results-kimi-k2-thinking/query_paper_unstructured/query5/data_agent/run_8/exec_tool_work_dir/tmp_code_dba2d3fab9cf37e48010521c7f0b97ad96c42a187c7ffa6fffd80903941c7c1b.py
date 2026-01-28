code = """import json
import re

# Load the data from the stored file paths
citations_file = locals()['var_functions.query_db:6']
papers_file = locals()['var_functions.query_db:10']

with open(citations_file, 'r') as f:
    citations_2020 = json.load(f)

with open(papers_file, 'r') as f:
    papers = json.load(f)

chi_paper_titles = []
chi_count = 0

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Look for CHI patterns in the paper text
    chi_patterns = ['CHI', "CHI '", 'CHI 20', 'CHI Conference', 'Proceedings of CHI', 'ACM CHI']
    
    is_chi = any(pattern in text for pattern in chi_patterns)
    
    # More specific regex check
    if not is_chi:
        if re.search(r'CHI\s*\'\d{2}', text) or re.search(r'CHI\s*20\d{2}', text):
            is_chi = True
    
    if is_chi:
        chi_paper_titles.append(title)
        chi_count += 1

total_citations = 0
chi_papers_cited = 0

for citation in citations_2020:
    cit_title = citation.get('title', '')
    if cit_title in chi_paper_titles:
        total_citations += int(citation.get('citation_count', 0))
        chi_papers_cited += 1

result = {
    'total_citations_2020_chi_papers': total_citations,
    'total_chi_papers': chi_count,
    'chi_papers_cited_in_2020': chi_papers_cited
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
