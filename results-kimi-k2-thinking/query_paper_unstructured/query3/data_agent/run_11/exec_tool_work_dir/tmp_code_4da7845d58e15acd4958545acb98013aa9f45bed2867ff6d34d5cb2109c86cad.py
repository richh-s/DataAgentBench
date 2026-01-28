code = """import json, re

# Load data
papers = json.load(open(locals()['var_functions.query_db:5']))
citations = json.load(open(locals()['var_functions.query_db:12']))

# Build citation index
citation_totals = {}
for c in citations:
    title = c['title']
    citation_totals[title] = citation_totals.get(title, 0) + int(c['citation_count'])

# Process papers
empirical_results = []

for paper in papers:
    title = paper['filename'].replace('.txt', '')
    text = paper['text']
    
    # Extract publication year
    years = re.findall(r'20\d{2}', text)
    year = max([int(y) for y in years]) if years else None
    
    # Check for empirical contribution and year > 2016
    if year and year > 2016:
        # Check if paper has empirical keywords
        if re.search(r'(?i)\b(survey|questionnaire|interview|field study|user study|empirical|observation|experiment|case study|participants)', text):
            # Get total citations
            if title in citation_totals:
                empirical_results.append({
                    'title': title,
                    'year': year,
                    'total_citation_count': citation_totals[title]
                })

# Sort by citation count
def get_citations(x):
    return x['total_citation_count']

empirical_results.sort(key=get_citations, reverse=True)

# Output
print('__RESULT__:')
print(json.dumps(empirical_results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': [], 'var_functions.execute_python:26': [], 'var_functions.query_db:32': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity'}, {'title': 'Why We Use and Abandon Smart Devices'}, {'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App'}, {'title': 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set'}, {'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application"}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'}, {'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization"}], 'var_functions.execute_python:38': [], 'var_functions.execute_python:42': []}

exec(code, env_args)
