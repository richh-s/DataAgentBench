code = """import json

# Load citations data from the stored variable
citations_var = var_functions.query_db:26
with open(citations_var, 'r') as f:
    citations_2020 = json.load(f)

# Load papers data from the stored variable
papers_var = var_functions.query_db:10
with open(papers_var, 'r') as f:
    papers = json.load(f)

# Count CHI papers and their citations
citation_dict = {c['title']: int(c['citation_count']) for c in citations_2020}

chi_total = 0
chi_papers_found = 0

for paper in papers:
    text = paper.get('text', '')
    if 'CHI' in text:
        title = paper.get('filename', '').replace('.txt', '')
        if title in citation_dict:
            chi_total += citation_dict[title]
            chi_papers_found += 1

result = {'total_citations': chi_total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
