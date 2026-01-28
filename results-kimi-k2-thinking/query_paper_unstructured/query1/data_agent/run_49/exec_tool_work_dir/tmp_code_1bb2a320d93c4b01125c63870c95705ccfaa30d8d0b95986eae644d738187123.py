code = """import json

# Access the variable using locals() since it has special characters
file_path = locals()['var_functions.query_db:12']

print('File path:', file_path)
print('Type:', type(file_path))

# Check if it's a string (file path) or actual data
if isinstance(file_path, str):
    # It's a file path
    with open(file_path, 'r') as f:
        papers_data = json.load(f)
else:
    # It's already the data
    papers_data = file_path

# Look for food papers
food_papers = []
food_titles = []

for paper in papers_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Get title from filename
    title = filename.replace('.txt', '') if filename else ''
    
    # Check for food domain
    if 'food' in text.lower():
        food_papers.append(paper)
        food_titles.append(title)

print('Total papers:', len(papers_data))
print('Food papers:', len(food_papers))
print('Food paper titles count:', len(food_titles))

# Show first few food titles
print('Sample food papers:')
for i, title in enumerate(food_titles[:5]):
    print(str(i+1) + '. ' + title)

# Prepare result
result = {
    'total_papers': len(papers_data),
    'food_papers_count': len(food_titles),
    'food_titles': food_titles
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}]}

exec(code, env_args)
