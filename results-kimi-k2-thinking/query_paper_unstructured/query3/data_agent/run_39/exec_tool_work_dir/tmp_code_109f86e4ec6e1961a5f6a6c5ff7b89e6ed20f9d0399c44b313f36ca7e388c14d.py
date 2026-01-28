code = """import json
import re

# Load citation data
citations_file = locals()['var_functions.query_db:36']
with open(citations_file, 'r') as f:
    citations = json.load(f)

print('Total citation records:', len(citations))
print('Sample citations:', citations[:3])

# Load paper documents (we need to re-extract empirical papers properly)
# Let's also access paper docs again to get full text
paper_docs_file = locals()['var_functions.query_db:22']
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Build a dictionary of paper info by title for fast lookup
paper_info_by_title = {}

for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = doc.get('text', '')
    
    if not title:
        continue
    
    # Extract year
    year = None
    year_matches = re.findall(r"(?:\b|')((?:19|20)\d{2})\b", text)
    if year_matches:
        valid_years = [int(y) for y in year_matches if 1900 <= int(y) <= 2030]
        if valid_years:
            year = max(valid_years)
    
    # Check for empirical contribution using text analysis
    text_lower = text.lower()
    empirical_keywords = [
        'empirical', 'empirically',
        'user study', 'user studies',
        'field study', 'field studies',
        'case study', 'case studies',
        'experiment', 'experiments', 'experimental',
        'evaluation', 'evaluated', 'evaluating',
        'participants', 'subjects',
        'interview', 'interviews', 'interviewed',
        'survey', 'questionnaire',
        'data collection', 'we collected', 'we gathered',
        'we conducted', 'we performed'
    ]
    
    # Also check venue indicators
    venue_indicators = ['chi', 'ubicomp', 'cscw', 'dis', 'pervasivehealth', 'uist', 'iui', 'ozchi', 'tei', 'ah', 'www']
    has_venue = any(venue in text_lower for venue in venue_indicators)
    
    has_empirical_terms = any(term in text_lower for term in empirical_keywords)
    is_empirical = has_empirical_terms and has_venue
    
    paper_info_by_title[title] = {
        'year': year,
        'is_empirical': is_empirical,
        'text_length': len(text)
    }

print('Papers processed:', len(paper_info_by_title))

# Now filter empirical papers after 2016
empirical_papers_after_2016 = []
for title, info in paper_info_by_title.items():
    if info['year'] and info['year'] > 2016 and info['is_empirical']:
        empirical_papers_after_2016.append({
            'title': title,
            'year': info['year']
        })

print(f'Empirical papers after 2016: {len(empirical_papers_after_2016)}')

# Match with citation data
final_results = []
for paper in empirical_papers_after_2016:
    for citation in citations:
        if citation['title'] == paper['title']:
            final_results.append({
                'title': paper['title'],
                'year': paper['year'],
                'total_citations': int(citation['total_citations'])
            })
            break

print('Matched with citations:', len(final_results))

# Sort by citations descending
final_results.sort(key=lambda x: x['total_citations'], reverse=True)

print('__RESULT__:')
print(json.dumps(final_results[:20]))  # Top 20"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:16': {'status': 'info', 'count': 5, 'sample_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:18': [], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:30': [], 'var_functions.execute_python:34': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
