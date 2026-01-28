code = """import json

# The food papers from the query
food_papers = [
    {"filename": "A Lived Informatics Model of Personal Informatics.txt"},
    {"filename": "A Stage-based Model of Personal Informatics Systems.txt"},
    {"filename": "A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt"},
    {"filename": "A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt"},
    {"filename": "ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt"}
]

# Extract titles
food_titles = []
for paper in food_papers:
    title = paper['filename'].replace('.txt', '')
    food_titles.append(title)

print("Food paper titles:", food_titles)

# Now let's check the citations file path
# The citations path should be available in the environment
import os
print("Current directory:", os.getcwd())
print("Files in directory:", os.listdir('.'))

# Let's try to find the citations file
files = os.listdir('.')
citations_file = None
for f in files:
    if 'citation' in f.lower() or f.endswith('.json'):
        print("Found file:", f)
        if 'query_db_8' in f or 'citations' in f:
            citations_file = f
            break

print("Citations file:", citations_file)

# Load citations
citations_path = './' + citations_file
with open(citations_path, 'r') as f:
    citations = json.load(f)

print("Total citation records:", len(citations))

# Sum citations for food papers
total = 0
for citation in citations:
    if citation['title'] in food_titles:
        total += int(citation['total_citations'])
        print(f"Found: {citation['title']} - {citation['total_citations']} citations")

print("Total citations for food domain:", total)

print("__RESULT__:")
print(str(total))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:5': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}, {'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt'}], 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}]}

exec(code, env_args)
