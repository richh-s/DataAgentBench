code = """import json

# Get citation data
citation_file_path = locals()['var_functions.query_db:0']
with open(citation_file_path, 'r') as f:
    citations_2020 = json.load(f)

# Extract all titles
titles = [record['title'] for record in citations_2020]
print('__RESULT__:')
print(json.dumps({
    'total_titles': len(titles),
    'titles_sample': titles[:5]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'total_count': 188, 'sample_records': [{'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}], 'titles_sample': ['Sundroid: Solar Radiation Awareness with Smartphones', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'Why We Use and Abandon Smart Devices', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application"]}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json'}

exec(code, env_args)
