code = """import json

# Read the MongoDB papers data
filepath = var_functions.query_db:14
with open(filepath, 'r') as file:
    papers = json.load(file)

print('Total papers loaded:', len(papers))

# Count papers that have 2016 and physical activity
matched_papers = []
for paper in papers:
    text = paper['text']
    filename = paper['filename']
    
    # Check if published in 2016
    year_check = '2016' in text[:2000]
    
    # Check if about physical activity
    activity_check = 'physical activity' in text.lower()
    
    if year_check and activity_check:
        title = filename.replace('.txt', '')
        matched_papers.append(title)

print('Matched papers:', len(matched_papers))

# Return results
print('__RESULT__:')
print(json.dumps(matched_papers))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:10': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.list_db:12': ['paper_docs'], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:22': [], 'var_functions.query_db:26': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing'}, {'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}]}

exec(code, env_args)
