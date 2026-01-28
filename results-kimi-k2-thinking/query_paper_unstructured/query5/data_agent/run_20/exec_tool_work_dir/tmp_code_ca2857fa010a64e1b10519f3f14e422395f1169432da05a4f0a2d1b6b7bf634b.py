code = """import json

# Load citations data from 2020
citation_file_path = locals()['var_functions.query_db:0']
with open(citation_file_path, 'r') as f:
    citations_2020 = json.load(f)

# Load CHI papers data
chi_file_path = locals()['var_functions.query_db:14']
with open(chi_file_path, 'r') as f:
    all_papers = json.load(f)

print('__RESULT__:')
print(json.dumps({
    'citations_2020_count': len(citations_2020),
    'all_papers_count': len(all_papers),
    'citation_titles_sample': [c['title'] for c in citations_2020[:3]],
    'paper_filenames_sample': [p['filename'] for p in all_papers[:3]]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'total_count': 188, 'sample_records': [{'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}], 'titles_sample': ['Sundroid: Solar Radiation Awareness with Smartphones', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'Why We Use and Abandon Smart Devices', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application"]}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.execute_python:12': {'total_titles': 188, 'titles_sample': ['Sundroid: Solar Radiation Awareness with Smartphones', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'Why We Use and Abandon Smart Devices', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application"]}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
