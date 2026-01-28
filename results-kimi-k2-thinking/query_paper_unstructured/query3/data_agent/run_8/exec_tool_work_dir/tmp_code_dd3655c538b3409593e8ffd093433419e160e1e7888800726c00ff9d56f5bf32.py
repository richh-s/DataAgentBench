code = """import json

# Get the file paths from storage
papers_file_path = globals()['var_functions.query_db:26']

# Read papers data
with open(papers_file_path, 'r') as f:
    papers = json.load(f)

# Just look at all papers and their titles
all_titles = []
for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    all_titles.append(title)

print("__RESULT__:")
print(json.dumps({
    "paper_count": len(papers),
    "all_titles": all_titles,
    "first_paper_text_snippet": papers[0].get('text', '')[:500] if papers else "no text"
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:20': {'available_variables': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', 'var_functions.query_db:6', 'var_functions.query_db:10', 'var_functions.query_db:14', '__builtins__', 'json'], 'var_functions.query_db:14_type': "<class 'str'>", 'var_functions.query_db:14_preview': 'file_storage/functions.query_db:14.json'}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:32': [], 'var_functions.execute_python:34': {'total_processed': 5, 'year_range': 'N/A to N/A', 'papers_with_empirical': 2, 'papers_after_2016': 0, 'empirical_after_2016': 0, 'sample_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'has_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'has_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'has_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'has_empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'has_empirical': False}]}, 'var_functions.execute_python:36': [], 'var_functions.execute_python:38': [], 'var_functions.execute_python:40': {'total_papers': 5, 'sample_title_matches': [{'index': 0, 'title': 'A Lived Informatics Model of Personal Informatics', 'in_citations': True, 'citations': 390}, {'index': 1, 'title': 'A Stage-based Model of Personal Informatics Systems', 'in_citations': True, 'citations': 220}, {'index': 2, 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'in_citations': True, 'citations': 265}, {'index': 3, 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'in_citations': True, 'citations': 266}, {'index': 4, 'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'in_citations': True, 'citations': 452}], 'year_distribution': {}, 'empirical_mentions_in_first_100': 2, 'papers_in_citations': 5}}

exec(code, env_args)
