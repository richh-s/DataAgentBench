code = """import json, re

# Load data files using the storage keys
papers_data = json.load(open(locals()['var_functions.query_db:5']))
citations_data = json.load(open(locals()['var_functions.query_db:12']))

# Process papers to extract info
paper_info = []
for paper in papers_data:
    title = paper['filename'].replace('.txt', '')
    text = paper['text']
    
    # Extract year
    years = re.findall(r'20\d{2}', text)
    year = max(int(y) for y in years) if years else None
    
    # Check if empirical
    is_empirical = bool(re.search(r'(?i)\b(survey|questionnaire|interview|field study|user study|empirical|observation|experiment|case study|participants)\b', text))
    
    paper_info.append({'title': title, 'year': year, 'is_empirical': is_empirical})

# Filter for empirical papers after 2016
empirical_2017plus = [p for p in paper_info if p['is_empirical'] and p['year'] and p['year'] > 2016]

# Build citation totals
citation_totals = {}
for c in citations_data:
    title = c['title']
    citation_totals[title] = citation_totals.get(title, 0) + int(c['citation_count'])

# Join data
result = []
for paper in empirical_2017plus:
    title = paper['title']
    if title in citation_totals:
        result.append({'title': title, 'year': paper['year'], 'total_citation_count': citation_totals[title]})

# Sort by citations descending
result.sort(key=lambda x: x['total_citation_count'], reverse=True)

# Output
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': [], 'var_functions.execute_python:26': [], 'var_functions.query_db:32': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity'}, {'title': 'Why We Use and Abandon Smart Devices'}, {'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App'}, {'title': 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set'}, {'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application"}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'}, {'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization"}]}

exec(code, env_args)
