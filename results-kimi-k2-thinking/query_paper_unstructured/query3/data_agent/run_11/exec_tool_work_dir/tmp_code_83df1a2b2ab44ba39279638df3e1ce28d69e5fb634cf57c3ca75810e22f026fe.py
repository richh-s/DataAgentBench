code = """import json, re

# Load data
papers_file = locals()['var_functions.query_db:5']
citations_file = locals()['var_functions.query_db:12']

with open(papers_file) as f:
    papers = json.load(f)

with open(citations_file) as f:
    citations = json.load(f)

# Build citation index
citation_titles = set()
citation_dict = {}
for c in citations:
    title = c['title']
    citation_titles.add(title)
    citation_dict[title] = citation_dict.get(title, 0) + int(c['citation_count'])

# Process papers
paper_titles = set()
empirical_papers = []
papers_with_years = []

for paper in papers:
    title = paper['filename'].replace('.txt', '')
    paper_titles.add(title)
    text = paper['text']
    
    # Extract year
    years = re.findall(r'20\d{2}', text)
    year = max(int(y) for y in years) if years else None
    if year:
        papers_with_years.append((title, year))
    
    # Check empirical
    is_empirical = bool(re.search(r'(?i)\b(survey|questionnaire|interview|field study|user study|empirical|observation|experiment|case study|participants)\b', text))
    
    if is_empirical and year and year > 2016:
        empirical_papers.append({'title': title, 'year': year})

# Find matches
matching_titles = paper_titles.intersection(citation_titles)
empirical_with_citations = [p for p in empirical_papers if p['title'] in citation_dict]

# Build final results
result = []
for paper in empirical_with_citations:
    result.append({
        'title': paper['title'],
        'year': paper['year'],
        'total_citation_count': citation_dict[paper['title']]
    })

result.sort(key=lambda x: x['total_citation_count'], reverse=True)

# Debug info
debug_info = {
    'total_papers': len(papers),
    'total_citations': len(citations),
    'unique_citation_titles': len(citation_titles),
    'papers_with_years': len(papers_with_years),
    'empirical_after_2016': len(empirical_papers),
    'matching_titles': len(matching_titles),
    'empirical_with_citations': len(empirical_with_citations),
    'final_results': len(result)
}

print('Debug:')
for k, v in debug_info.items():
    print(k + ': ' + str(v))

print('\nSample papers with years:')
for i, (title, year) in enumerate(papers_with_years[:10]):
    print(str(i+1) + '. ' + title + ' (' + str(year) + ')')

if result:
    print('\nFinal results (top 10):')
    for i, paper in enumerate(result[:10]):
        print(str(i+1) + '. ' + paper['title'] + ' (' + str(paper['year']) + ') - ' + str(paper['total_citation_count']) + ' citations')

print('\n---PRINT FORMAT---')
print('__RESULT__:')
print(json.dumps(debug_info))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': [], 'var_functions.execute_python:26': [], 'var_functions.query_db:32': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity'}, {'title': 'Why We Use and Abandon Smart Devices'}, {'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App'}, {'title': 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set'}, {'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application"}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'}, {'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization"}], 'var_functions.execute_python:38': []}

exec(code, env_args)
