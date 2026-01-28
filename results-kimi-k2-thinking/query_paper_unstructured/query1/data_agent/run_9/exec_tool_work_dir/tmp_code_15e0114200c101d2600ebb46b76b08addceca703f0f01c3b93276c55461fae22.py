code = """import os
import json

print('Listing files:')
files = os.listdir('.')
for f in sorted(files):
    print('  ' + f)

# Get all JSON files and their sizes
json_info = []
for f in files:
    if f.endswith('.json'):
        size = os.path.getsize(f)
        json_info.append((f, size))

print('\nJSON files with sizes:')
for f, size in sorted(json_info, key=lambda x: x[1], reverse=True):
    print('  ' + f + ': ' + str(size) + ' bytes')

# Try to identify which is which
food_file = None
citations_file = None

for f, size in json_info:
    if 'food' in f.lower():
        food_file = f
    elif size > 50000:  # Likely citations file
        citations_file = f

print('\nFood file identified: ' + str(food_file))
print('Citations file identified: ' + str(citations_file))

# Load them
if food_file and citations_file:
    with open(food_file, 'r') as f:
        food_data = json.load(f)
    
    with open(citations_file, 'r') as f:
        citations_data = json.load(f)
    
    print('\nFood records: ' + str(len(food_data)))
    print('Citation records: ' + str(len(citations_data)))
    
    # Extract food paper titles
    food_titles = set()
    for item in food_data:
        if 'filename' in item:
            title = item['filename'].replace('.txt', '')
            food_titles.add(title)
    
    print('Food titles count: ' + str(len(food_titles)))
    
    # Sum citations
    total = 0
    for citation in citations_data:
        if 'title' in citation and citation['title'] in food_titles:
            total += int(citation['total_citations'])
    
    print('__RESULT__:')
    print(str(total))
else:
    print('Could not identify files')"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:5': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}, {'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt'}], 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}]}

exec(code, env_args)
