code = """import json, re

# Load data
papers_file = locals()['var_functions.query_db:5']
citations_file = locals()['var_functions.query_db:12']

with open(papers_file) as f:
    papers = json.load(f)

with open(citations_file) as f:
    citations = json.load(f)

# Build citation index
citation_dict = {}
for c in citations:
    title = c['title']
    citation_dict[title] = citation_dict.get(title, 0) + int(c['citation_count'])

# Process all papers systematically
all_papers = []
for paper in papers:
    title = paper['filename'].replace('.txt', '')
    text = paper['text']
    
    # Extract year - more flexible pattern
    year_match = re.search(r'20[0-3]\d', text)
    year = int(year_match.group()) if year_match else None
    if year:
        # Look for all years and take the most recent one
        years = re.findall(r'20[0-3]\d', text)
        year = max(int(y) for y in years)
    
    # Check for empirical - simplified check
    has_empirical = bool(re.search(r'(?i)(survey|questionnaire|interview|field study|user study|empirical|observation|experiment|case study|participants)', text))
    
    all_papers.append({
        'title': title,
        'year': year,
        'has_empirical': has_empirical,
        'has_citations': title in citation_dict,
        'citation_count': citation_dict.get(title, 0)
    })

# Debug: Check year distribution
year_counts = {}
empirical_by_year = {}
for p in all_papers:
    if p['year']:
        year = p['year']
        year_counts[year] = year_counts.get(year, 0) + 1
        if p['has_empirical']:
            empirical_by_year[year] = empirical_by_year.get(year, 0) + 1

print('Year distribution:')
for year in sorted(year_counts.keys()):
    total = year_counts[year]
    empirical = empirical_by_year.get(year, 0)
    print(f'{year}: {total} total, {empirical} empirical')

# Get empirical papers after 2016
empirical_after_2016 = [p for p in all_papers if p['has_empirical'] and p['year'] and p['year'] > 2016 and p['has_citations']]

# Sort by citation count
result = sorted(empirical_after_2016, key=lambda x: x['citation_count'], reverse=True)

# Format final output
final_result = []
for paper in result:
    final_result.append({
        'title': paper['title'],
        'year': paper['year'],
        'total_citation_count': paper['citation_count']
    })

print('\nFinal results count: ' + str(len(final_result)))

# Output
print('__RESULT__:')
print(json.dumps(final_result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': [], 'var_functions.execute_python:26': [], 'var_functions.query_db:32': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity'}, {'title': 'Why We Use and Abandon Smart Devices'}, {'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App'}, {'title': 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set'}, {'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application"}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'}, {'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization"}], 'var_functions.execute_python:38': [], 'var_functions.execute_python:42': [], 'var_functions.execute_python:46': []}

exec(code, env_args)
