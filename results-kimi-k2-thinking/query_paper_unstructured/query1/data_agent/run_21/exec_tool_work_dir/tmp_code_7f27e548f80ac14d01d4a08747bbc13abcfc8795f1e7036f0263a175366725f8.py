code = """import json

# Load all paper documents from MongoDB
with open('/tmp/tmp_result_20.json', 'r') as f:
    papers = json.load(f)

# Extract paper titles and look for food domain
food_paper_titles = []
paper_info = {}

for paper in papers:
    filename = paper['filename']
    title = filename.replace('.txt', '')
    text = paper['text'].lower()
    
    # Store paper info
    paper_info[title] = paper
    
    # Check if this is a food domain paper
    # Look for 'food' in domain context
    if ' food ' in text:
        # Look for surrounding context that suggests it's a domain
        # Check sections that mention domains/tracking areas
        lines = text.split('\n')
        for line in lines:
            if 'food' in line and ('domain' in line or 'tracking' in line or 'track' in line):
                food_paper_titles.append(title)
                break
        # Also check if mentioned in multiple contexts
        elif text.count(' food ') > 3:  # Multiple mentions likely means it's a domain
            food_paper_titles.append(title)

# Remove duplicates
food_paper_titles = list(set(food_paper_titles))

print('Total papers: ' + str(len(papers)))
print('Food papers found: ' + str(len(food_paper_titles)))
print('Sample food papers: ' + str(food_paper_titles[:10]))

result = {
    'food_paper_titles': food_paper_titles,
    'total_papers': len(papers)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.list_db:10': ['paper_docs'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
