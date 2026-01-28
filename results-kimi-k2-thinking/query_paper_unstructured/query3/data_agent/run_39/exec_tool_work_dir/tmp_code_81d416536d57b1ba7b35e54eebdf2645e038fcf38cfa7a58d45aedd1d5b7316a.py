code = """import json
import re

# Load citations
citations_file = locals()['var_functions.query_db:36']
with open(citations_file, 'r') as f:
    citations = json.load(f)

# Load paper documents
paper_docs_file = locals()['var_functions.query_db:22']
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Create citation lookup by title
citation_lookup = {c['title']: int(c['total_citations']) for c in citations}

print('Total citations loaded:', len(citation_lookup))
print('Sample citation titles:', list(citation_lookup.keys())[:5])

# Process papers
results = []

for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    if not title:
        continue
    
    text = doc.get('text', '')
    
    # Extract year
    year_matches = re.findall(r'((?:19|20)\d{2})', text)
    year = None
    if year_matches:
        valid_years = [int(y) for y in year_matches if 1900 <= int(y) <= 2030]
        if valid_years:
            year = max(valid_years)
    
    # Check if after 2016
    if not year or year <= 2016:
        continue
    
    # Check for empirical contribution
    text_lower = text.lower()
    empirical_terms = ['empirical','user study','field study','case study','experiment','evaluation','participants','interview','survey','data collection','we conducted','we studied']
    has_empirical = any(term in text_lower for term in empirical_terms)
    
    # Also check venue
    venue_terms = ['chi','ubicomp','cscw','dis','pervasivehealth','uist','iui','www','ozchi','tei']
    has_venue = any(venue in text_lower for venue in venue_terms)
    
    if has_empirical and has_venue:
        # Get citation count
        citations = citation_lookup.get(title, 0)
        if citations > 0:  # Only include papers with citations
            results.append({
                'title': title,
                'year': year,
                'total_citations': citations
            })

print('Found papers:', len(results))

# Sort by citations
results.sort(key=lambda x: x['total_citations'], reverse=True)

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:16': {'status': 'info', 'count': 5, 'sample_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:18': [], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:30': [], 'var_functions.execute_python:34': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:38': []}

exec(code, env_args)
