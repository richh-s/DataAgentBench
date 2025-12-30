code = """import json
import re

# Load the papers
with open('11196622143221928567.json', 'r') as f:
    papers = json.load(f)

matching_titles = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check for Year 2016
    # Look in the first 1000 characters for conference headers
    header = text[:1000]
    # Patterns: "2016", "'16"
    # Be careful with phone numbers or other digits. But usually header has the year.
    # Pattern for conference year: "CHI '16", "UbiComp '16", "2016"
    if '2016' in header or "'16" in header:
        year_match = True
    else:
        year_match = False
        
    # Check for Domain 'physical activity'
    # Case insensitive search in the whole text (or headers/keywords if possible)
    if 'physical activity' in text.lower():
        domain_match = True
    else:
        domain_match = False
        
    if year_match and domain_match:
        matching_titles.append(title)

print("__RESULT__:")
print(json.dumps(matching_titles))"""

env_args = {'var_function-call-16083049299143672043': 'file_storage/function-call-16083049299143672043.json', 'var_function-call-6689175005249734094': ['Citations', 'sqlite_sequence'], 'var_function-call-11808017164042867885': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-11196622143221928567': 'file_storage/function-call-11196622143221928567.json'}

exec(code, env_args)
