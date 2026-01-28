code = """import json, re

# Load data
papers = json.load(open(locals()['var_functions.query_db:5']))
citations = json.load(open(locals()['var_functions.query_db:12']))

# Build citation dictionary
citation_dict = {}
for c in citations:
    title = c['title']
    citation_dict[title] = citation_dict.get(title, 0) + int(c['citation_count'])

# Find empirical papers published after 2016
empirical_papers = []
for paper in papers:
    title = paper['filename'].replace('.txt', '')
    text = paper['text']
    
    # Extract year
    years = re.findall(r'20\d{2}', text)
    if not years:
        continue
    year = max(int(y) for y in years)
    
    # Check if after 2016 and empirical
    if year > 2016:
        if re.search(r'(?i)(survey|questionnaire|interview|field study|user study|empirical|observation|experiment|case study|participants)', text):
            empirical_papers.append({'title': title, 'year': year})

# Join with citations
result = []
for paper in empirical_papers:
    title = paper['title']
    if title in citation_dict:
        result.append({
            'title': title,
            'year': paper['year'],
            'total_citation_count': citation_dict[title]
        })

# Sort by citation count
result.sort(key=lambda x: x['total_citation_count'], reverse=True)

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': [], 'var_functions.execute_python:26': [], 'var_functions.query_db:32': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity'}, {'title': 'Why We Use and Abandon Smart Devices'}, {'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App'}, {'title': 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set'}, {'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application"}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'}, {'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization"}], 'var_functions.execute_python:38': [], 'var_functions.execute_python:42': [], 'var_functions.execute_python:46': []}

exec(code, env_args)
