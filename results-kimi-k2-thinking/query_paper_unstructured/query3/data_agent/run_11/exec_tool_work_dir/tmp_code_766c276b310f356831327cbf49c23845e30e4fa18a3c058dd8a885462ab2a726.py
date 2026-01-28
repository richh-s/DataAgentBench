code = """import json
import re

# Debug: Load data to understand the structure
papers_file = locals()['var_functions.query_db:5']
citations_file = locals()['var_functions.query_db:12']

print('Papers file: ' + papers_file)
print('Citations file: ' + citations_file)

# Load papers data
with open(papers_file) as f:
    papers = json.load(f)

print('\nTotal papers: ' + str(len(papers)))

# Process a few papers to debug
sample_papers = papers[:5]
for i, paper in enumerate(sample_papers):
    title = paper['filename'].replace('.txt', '')
    print('\nPaper ' + str(i+1) + ': ' + title)
    # Check for years in text
    years = re.findall(r'20\d{2}', paper['text'])
    if years:
        print('Years found: ' + str(years))
    else:
        print('No years found')

# Load citations data
with open(citations_file) as f:
    citations = json.load(f)

print('\nTotal citation records: ' + str(len(citations)))

# Build citation index
citation_counts = {}
for c in citations:
    title = c['title']
    count = int(c['citation_count'])
    citation_counts[title] = citation_counts.get(title, 0) + count

print('Unique papers with citations: ' + str(len(citation_counts)))

# Sample some citation titles
sample_titles = list(citation_counts.keys())[:5]
print('\nSample citation titles:')
for title in sample_titles:
    print('- ' + title)

print('\n---PRINT FORMAT---')
print('__RESULT__:')
print(json.dumps({'debug': 'completed'}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': [], 'var_functions.execute_python:26': [], 'var_functions.query_db:32': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity'}, {'title': 'Why We Use and Abandon Smart Devices'}, {'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App'}, {'title': 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set'}, {'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application"}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'}, {'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization"}]}

exec(code, env_args)
