code = """import json
import os

# Let's access the storage key directly
storage_key = 'var_functions.query_db:16'
result = locals()[storage_key]
print(f"Result type: {type(result)}")
print(f"Result value: {result}")

# If it's a file path, read it
if isinstance(result, str) and 'paper_docs' in result:
    with open(result, 'r') as f:
        papers = json.load(f)
    print(f"Loaded {len(papers)} papers")
    
    # Now look for 2016 physical activity papers
    physical_activity_2016 = []
    
    for paper in papers:
        text = paper.get('text', '').lower()
        
        # Check for year 2016
        has_2016 = '2016' in text
        
        # Check for physical activity
        has_physical_activity = 'physical activity' in text
        
        if has_2016 and has_physical_activity:
            title = paper.get('filename', '').replace('.txt', '')
            physical_activity_2016.append({
                'title': title,
                '_id': paper.get('_id')
            })
    
    print(f"Found {len(physical_activity_2016)} papers from 2016 in physical activity domain:")
    for p in physical_activity_2016:
        print(f"- {p['title']}")
    
    final_result = physical_activity_2016
else:
    final_result = []

print('__RESULT__:')
print(json.dumps(final_result))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': 'test', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
