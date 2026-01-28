code = """import json
import re

# Get file paths
citations_path = var_functions.query_db:6
papers_path = var_functions.query_db:10

# Load data
citations_2020 = json.load(open(citations_path))
papers = json.load(open(papers_path))

chi_titles = []
chi_count = 0

for p in papers:
    txt = p.get('text', '')
    if 'CHI' in txt:
        # More specific check
        if re.search(r'CHI\s*\'\d{2}|CHI\s*20\d{2}', txt, re.I):
            title = p.get('filename', '').replace('.txt', '')
            chi_titles.append(title)
            chi_count += 1

citation_df = {}
for c in citations_2020:
    citation_df[c['title']] = int(c['citation_count'])

total = 0
found = 0
for title in chi_titles:
    if title in citation_df:
        total += citation_df[title]
        found += 1

result = {
    'total_citations_2020': total,
    'chi_papers_total': chi_count,
    'chi_papers_cited': found
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
