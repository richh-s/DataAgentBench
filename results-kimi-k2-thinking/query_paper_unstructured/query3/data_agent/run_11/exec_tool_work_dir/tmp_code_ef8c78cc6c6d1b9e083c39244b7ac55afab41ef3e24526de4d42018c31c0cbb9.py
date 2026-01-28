code = """import json
import re

# Load the paper documents from storage
papers_file = locals()['var_functions.query_db:5']
with open(papers_file, 'r') as f:
    papers = json.load(f)

print('Loaded ' + str(len(papers)) + ' papers')

# Load citation titles for comparison
citation_titles_file = locals()['var_functions.query_db:32']
with open(citation_titles_file, 'r') as f:
    citation_titles_list = json.load(f)

citation_titles = set(c['title'] for c in citation_titles_list)
print('Available citation titles: ' + str(len(citation_titles)))

# Process all papers to extract year and check for empirical contribution
paper_info = []
empirical_papers = []

for paper in papers:
    title = paper['filename'].replace('.txt', '')
    text = paper['text']
    
    # Extract year - look for 4-digit years from 2000-2030
    year_matches = re.findall(r'20[0-3]\d', text)
    year = None
    if year_matches:
        # Use the most recent year (max)
        year = max(int(y) for y in year_matches)
    
    # Check for empirical contribution - broad pattern
    has_empirical = re.search(r'(?i)\b(survey|questionnaire|interview|field study|field research|user study|empirical|observation|data collection|experiment|case study|participants|study|investigation|evaluation|assessment|methodology|methods|results|findings|data analysis|statistical|hypothesis)\b', text)
    
    contribution = []
    if has_empirical:
        contribution.append('empirical')
        empirical_papers.append({'title': title, 'year': year})
    
    paper_info.append({'title': title, 'year': year, 'contribution': contribution})

print('\nTotal papers processed: ' + str(len(paper_info)))
print('Total empirical papers: ' + str(len(empirical_papers)))

# Filter for empirical papers after 2016
empirical_after_2016 = [p for p in empirical_papers if p['year'] and p['year'] > 2016]
print('Empirical papers after 2016: ' + str(len(empirical_after_2016)))

# Load full citations data
citations_file = locals()['var_functions.query_db:12']
with open(citations_file, 'r') as f:
    all_citations = json.load(f)

print('\nTotal citation records: ' + str(len(all_citations)))

# Build citation dictionary with totals per title
citation_dict = {}
for citation in all_citations:
    title = citation['title']
    count = int(citation['citation_count'])
    citation_dict[title] = citation_dict.get(title, 0) + count

print('Unique papers with citations: ' + str(len(citation_dict)))

# Create final results by joining empirical papers with their citations
result = []
for paper in empirical_after_2016:
    title = paper['title']
    if title in citation_dict:
        result.append({
            'title': title,
            'year': paper['year'],
            'total_citation_count': citation_dict[title]
        })

# Sort by citation count descending
result.sort(key=lambda x: x['total_citation_count'], reverse=True)

print('\nFinal results with citations: ' + str(len(result)))

# Output
output = json.dumps(result, indent=2)
print('---PRINT FORMAT---')
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': [], 'var_functions.execute_python:26': [], 'var_functions.query_db:32': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity'}, {'title': 'Why We Use and Abandon Smart Devices'}, {'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App'}, {'title': 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set'}, {'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application"}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'}, {'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization"}]}

exec(code, env_args)
