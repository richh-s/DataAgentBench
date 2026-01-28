code = """import json, re

# Load raw data
papers_file = locals()['var_functions.query_db:5']
citations_file = locals()['var_functions.query_db:12']

with open(papers_file) as f:
    papers = json.load(f)

with open(citations_file) as f:
    citations = json.load(f)

print('Papers: ' + str(len(papers)))
print('Citations: ' + str(len(citations)))

# Check year extraction on sample
sample = papers[0]
text = sample['text']
years = re.findall(r'20\d{2}', text)
print('\nFirst paper: ' + sample['filename'])
print('Years found: ' + str(years))

# Check empirical pattern
has_empirical = re.search(r'(?i)\b(survey|questionnaire|interview|field study|user study|empirical|observation|experiment|case study|participants)\b', text)
print('Has empirical keywords: ' + str(bool(has_empirical)))

# Check overall statistics
year_counts = {}
empirical_by_year = {}

for paper in papers:
    text = paper['text']
    years = re.findall(r'20\d{2}', text)
    
    if years:
        year = max(int(y) for y in years)
        year_counts[year] = year_counts.get(year, 0) + 1
        
        has_empirical = re.search(r'(?i)\b(survey|questionnaire|interview|field study|user study|empirical|observation|experiment|case study|participants)\b', text)
        if has_empirical:
            empirical_by_year[year] = empirical_by_year.get(year, 0) + 1

print('\nYear distribution:')
for year in sorted(year_counts.keys()):
    total = year_counts[year]
    empirical = empirical_by_year.get(year, 0)
    print(str(year) + ': ' + str(total) + ' total, ' + str(empirical) + ' empirical')

# Check citation titles
all_citation_titles = set(c['title'] for c in citations)
print('\nUnique citation titles: ' + str(len(all_citation_titles)))

# Check if any empirical paper titles after 2016 match
all_paper_titles = set(p['filename'].replace('.txt', '') for p in papers)
intersection = all_paper_titles.intersection(all_citation_titles)
print('Matching titles (any year): ' + str(len(intersection)))

# Check for matches specifically after 2016
empirical_after_2016_titles = set()
for paper in papers:
    years = re.findall(r'20\d{2}', paper['text'])
    if years:
        year = max(int(y) for y in years)
        if year > 2016:
            has_empirical = re.search(r'(?i)\\b(survey|questionnaire|interview|field study|user study|empirical|observation|experiment|case study|participants)\\b', paper['text'])
            if has_empirical:
                empirical_after_2016_titles.add(paper['filename'].replace('.txt', ''))

print('Empirical titles after 2016: ' + str(len(empirical_after_2016_titles)))
print('Intersection with citations: ' + str(len(empirical_after_2016_titles.intersection(all_citation_titles))))

if empirical_after_2016_titles:
    print('\nSample empirical titles after 2016:')
    for t in list(empirical_after_2016_titles)[:10]:
        print('  - ' + t)

print('\n---PRINT FORMAT---')
print('__RESULT__:')
print(json.dumps({'completed': True}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': [], 'var_functions.execute_python:26': [], 'var_functions.query_db:32': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity'}, {'title': 'Why We Use and Abandon Smart Devices'}, {'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App'}, {'title': 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set'}, {'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application"}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'}, {'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization"}], 'var_functions.execute_python:38': [], 'var_functions.execute_python:42': []}

exec(code, env_args)
