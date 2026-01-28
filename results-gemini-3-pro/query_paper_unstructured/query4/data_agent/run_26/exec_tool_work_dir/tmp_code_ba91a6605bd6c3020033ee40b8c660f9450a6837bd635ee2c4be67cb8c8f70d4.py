code = """import json
import re

# Get file path from storage
file_path = locals()['var_function-call-11196622143221928567']

# Load the papers
with open(file_path, 'r') as f:
    papers = json.load(f)

matching_titles = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check for Year 2016
    # Look in the first 1000 characters
    header = text[:1000]
    # Simple check for 2016. The user query is specific to 2016.
    # Note: '16 might match other things, but usually headers like "CHI '16" represent year.
    # To be safer, maybe look for "2016" or " '16 " or "’16".
    # Let's try searching for 2016 primarily.
    is_2016 = '2016' in header
    
    # Check for Domain 'physical activity'
    # Case insensitive
    has_domain = 'physical activity' in text.lower()
    
    if is_2016 and has_domain:
        matching_titles.append(title)

print("__RESULT__:")
print(json.dumps(matching_titles))"""

env_args = {'var_function-call-16083049299143672043': 'file_storage/function-call-16083049299143672043.json', 'var_function-call-6689175005249734094': ['Citations', 'sqlite_sequence'], 'var_function-call-11808017164042867885': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-11196622143221928567': 'file_storage/function-call-11196622143221928567.json'}

exec(code, env_args)
