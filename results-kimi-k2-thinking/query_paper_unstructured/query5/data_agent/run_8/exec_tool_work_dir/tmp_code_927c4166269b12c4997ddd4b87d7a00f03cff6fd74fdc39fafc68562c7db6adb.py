code = """import json
import re

# Load 2020 citations
citations_file = locals()['var_functions.query_db:44']
with open(citations_file, 'r') as f:
    citations = json.load(f)

# Load papers
papers_file = locals()['var_functions.query_db:10']
with open(papers_file, 'r') as f:
    papers = json.load(f)

# Build citation map
citation_counts = {}
for c in citations:
    citation_counts[c['title']] = int(c['citation_count'])

# Find CHI papers and sum citations
total = 0
found = 0
chi_count = 0

for p in papers:
    text = p.get('text', '')
    if re.search('CHI', text):
        chi_count += 1
        title = p.get('filename', '').replace('.txt', '')
        if title in citation_counts:
            total += citation_counts[title]
            found += 1

result = {'total': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
