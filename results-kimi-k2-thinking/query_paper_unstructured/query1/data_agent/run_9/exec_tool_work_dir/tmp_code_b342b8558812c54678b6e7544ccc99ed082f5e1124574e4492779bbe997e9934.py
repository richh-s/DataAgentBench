code = """import os
import json

print('Files in current directory:')
files = os.listdir('.')
for f in sorted(files):
    if f.endswith('.json'):
        print('JSON file: ' + f)

# Check all json files
json_files = [f for f in files if f.endswith('.json')]

for f in json_files:
    print('\nChecking: ' + f)
    size = os.path.getsize(f)
    print('Size: ' + str(size) + ' bytes')
    
    with open(f, 'r') as file:
        data = json.load(file)
    
    print('Records: ' + str(len(data)))
    if len(data) > 0:
        keys = list(data[0].keys())
        print('Keys: ' + str(keys))
        if 'filename' in keys:
            print('This appears to be paper docs data')
        elif 'title' in keys and 'total_citations' in keys:
            print('This appears to be citations data')

# Now we'll extract the food papers and sum citations
food_file = None
cite_file = None

for f in json_files:
    with open(f, 'r') as file:
        data = json.load(file)
    if len(data) > 0:
        if 'filename' in data[0]:
            food_file = f
        elif 'title' in data[0] and 'total_citations' in data[0]:
            cite_file = f

print('\nUsing food file: ' + str(food_file))
print('Using citations file: ' + str(cite_file))

# Process data
with open(food_file, 'r') as f:
    food_data = json.load(f)

with open(cite_file, 'r') as f:
    cite_data = json.load(f)

# Get food titles
food_titles = []
for item in food_data:
    title = item['filename'].replace('.txt', '')
    food_titles.append(title)

# Sum citations
total = 0
for citation in cite_data:
    if citation['title'] in food_titles:
        total += int(citation['total_citations'])

print('Total citations for food domain: ' + str(total))
print('__RESULT__:')
print(str(total))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:5': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}, {'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt'}], 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}]}

exec(code, env_args)
