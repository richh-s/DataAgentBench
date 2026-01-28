code = """import json, re

# Load papers from MongoDB
mongo_path = var_functions.query_db:2
with open(mongo_path, 'r') as f:
    papers = json.load(f)

# Extract empirical papers published after 2016
empirical_papers = []

for paper in papers:
    filename = paper.get('filename', '')
    if not filename:
        continue
    
    # Get title from filename
    title = filename[:-4] if filename.endswith('.txt') else filename
    text = paper.get('text', '')
    
    # Extract year - look for 4-digit year starting with 20 or 201
    year_match = re.search(r'20[0-9]{2}', text[:3000])
    year = int(year_match.group()) if year_match else 0
    
    # Check for empirical in first 8000 chars
    has_empirical = 'empirical' in text[:8000].lower()
    
    if year > 2016 and has_empirical:
        empirical_papers.append(title)

print('__RESULT__:')
result = {'empirical_papers_after_2016': len(empirical_papers), 'sample_titles': empirical_papers[:5]}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.list_db:22': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
