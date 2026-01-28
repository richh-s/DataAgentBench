code = """import json
import pandas as pd

# Load papers data  
papers = var_functions.query_db_2
if isinstance(papers, str):
    with open(papers, 'r') as f:
        papers_data = json.load(f)
else:
    papers_data = papers

# Load citations data
citations = var_functions.query_db_10
if isinstance(citations, str):
    with open(citations, 'r') as f:
        citations_data = json.load(f)
else:
    citations_data = citations

food_paper_titles = []

# Extract papers in 'food' domain
for paper in papers_data:
    text = paper.get('text', '').lower()
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Check if 'food' is mentioned in the text
    if 'food' in text:
        # Look for clear domain indicators
        domain_indicators = [
            'food domain',
            'domain: food', 
            'tracking food',
            'food tracking',
            'food intake',
            'diet tracking'
        ]
        
        if any(indicator in text for indicator in domain_indicators):
            food_paper_titles.append(title)

print('__RESULT__:')
print(json.dumps({
    'food_papers_found': len(food_paper_titles),
    'food_paper_titles': food_paper_titles[:10],
    'total_papers': len(papers_data)
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
