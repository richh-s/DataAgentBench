code = """import json
import re

# Get file paths from storage
papers_file = var_functions.query_db:44
citations_file = var_functions.query_db:24

# Load data
with open(papers_file, 'r') as f:
    papers = json.load(f)

with open(citations_file, 'r') as f:
    citations = json.load(f)

# Create citation lookup
citation_lookup = {}
for item in citations:
    title = item['title']
    count = int(item['total_citations'])
    citation_lookup[title] = count

# Process papers
empirical_papers_after_2016 = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    if not title:
        continue
    
    # Extract year from text
    year_match = re.search(r'\b(20[1-9][0-9])\b', text)
    if year_match:
        year = int(year_match.group(1))
    else:
        # Try copyright year
        copyright_match = re.search(r'Copyright[^\d]{0,50}(20[1-9][0-9])', text, re.IGNORECASE)
        if copyright_match:
            year = int(copyright_match.group(1))
        else:
            continue
    
    # Check for empirical contribution
    text_lower = text.lower()
    if 'empirical' in text_lower and year > 2016:
        if title in citation_lookup:
            empirical_papers_after_2016.append({
                'title': title,
                'total_citations': citation_lookup[title],
                'year': year
            })

# Sort by citations descending
result = sorted(empirical_papers_after_2016, key=lambda x: x['total_citations'], reverse=True)

print("__RESULT__:")
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:20': {'available_variables': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', 'var_functions.query_db:6', 'var_functions.query_db:10', 'var_functions.query_db:14', '__builtins__', 'json'], 'var_functions.query_db:14_type': "<class 'str'>", 'var_functions.query_db:14_preview': 'file_storage/functions.query_db:14.json'}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:32': [], 'var_functions.execute_python:34': {'total_processed': 5, 'year_range': 'N/A to N/A', 'papers_with_empirical': 2, 'papers_after_2016': 0, 'empirical_after_2016': 0, 'sample_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'has_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'has_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'has_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'has_empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'has_empirical': False}]}, 'var_functions.execute_python:36': [], 'var_functions.execute_python:38': [], 'var_functions.execute_python:40': {'total_papers': 5, 'sample_title_matches': [{'index': 0, 'title': 'A Lived Informatics Model of Personal Informatics', 'in_citations': True, 'citations': 390}, {'index': 1, 'title': 'A Stage-based Model of Personal Informatics Systems', 'in_citations': True, 'citations': 220}, {'index': 2, 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'in_citations': True, 'citations': 265}, {'index': 3, 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'in_citations': True, 'citations': 266}, {'index': 4, 'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'in_citations': True, 'citations': 452}], 'year_distribution': {}, 'empirical_mentions_in_first_100': 2, 'papers_in_citations': 5}, 'var_functions.execute_python:42': {'paper_count': 5, 'all_titles': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation'], 'first_paper_text_snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characteriz"}, 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
