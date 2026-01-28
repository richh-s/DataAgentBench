code = """import json

# Read files
with open('/tmp/tmp_z5f1h1u.json', 'r') as f:
    citations = json.load(f)

with open('/tmp/tmp1_jn5t0d.json', 'r') as f:
    papers = json.load(f)

# Find CHI papers
chi_titles = []
for p in papers:
    text = p.get('text', '')
    if 'CHI' in text:
        title = p.get('filename', '').replace('.txt', '')
        chi_titles.append(title)

# Sum citations
total = 0
for c in citations:
    if c['title'] in chi_titles:
        total += int(c['citation_count'])

# Output
print('__RESULT__:')
print(json.dumps({'total': total}))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
