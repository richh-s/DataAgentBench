code = """import json

# Load the citations data
citations_file = locals()['var_functions.query_db:14']
with open(citations_file, 'r') as f:
    citations = json.load(f)

# Load the papers analysis result
papers_result = locals()['var_functions.execute_python:32']

# Extract food paper titles
food_titles = papers_result['food_paper_titles']

# Calculate total citations for food papers
total_citations = 0
detailed_breakdown = {}

for title in food_titles:
    title_citations = [int(c['citation_count']) for c in citations if c['title'] == title]
    title_total = sum(title_citations)
    total_citations += title_total
    detailed_breakdown[title] = {
        'citation_records': len(title_citations),
        'total_citations': title_total,
        'yearly_breakdown': title_citations
    }

print('__RESULT__:')
print(json.dumps({
    'total_food_domain_citations': total_citations,
    'detailed_breakdown': detailed_breakdown,
    'verification': total_citations == 610
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:5': [], 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': 'file_storage/functions.execute_python:16.json', 'var_functions.execute_python:20': {'total_papers': 5, 'food_domain_papers': [], 'food_papers_count': 0}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:32': {'total_food_domain_citations': 610, 'food_domain_papers_count': 2, 'food_paper_titles': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems']}, 'var_functions.query_db:34': [{'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '77'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '9'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '50'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '49'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '77'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '60'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '68'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'citation_count': '88'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'citation_count': '32'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'citation_count': '86'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'citation_count': '14'}]}

exec(code, env_args)
