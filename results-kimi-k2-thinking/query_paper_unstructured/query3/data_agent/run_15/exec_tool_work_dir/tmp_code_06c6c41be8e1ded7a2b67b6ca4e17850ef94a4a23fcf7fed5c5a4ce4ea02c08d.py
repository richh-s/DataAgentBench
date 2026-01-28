code = """import json

# Load the citations data from the file
citations_file = locals()['var_functions.query_db:14']
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Load the empirical papers after 2016 from previous result
empirical_papers = [
    {"title": "A Trip to the Moon: Personalized Animated Movies for Self-reflection", "year": 2018},
    {"title": "A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App", "year": 2019}
]

# Calculate total citations for each empirical paper
result = []

for paper in empirical_papers:
    title = paper['title']
    total_citations = 0
    
    # Sum citation counts for this title
    for citation in citations_data:
        if citation['title'] == title:
            total_citations += int(citation['citation_count'])
    
    result.append({
        'title': title,
        'year': paper['year'],
        'total_citations': total_citations
    })

# Return the result
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018, 'total_citations': 0}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019, 'total_citations': 0}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
