code = """import json

# Load data
with open('/tmp/tmpn2tux2v2.json', 'r') as f:
    citations_2020 = json.load(f)

with open('/tmp/tmpf_9r5s6n.json', 'r') as f:
    paper_docs = json.load(f)

print('Total citations from 2020:', len(citations_2020))
print('Total paper documents:', len(paper_docs))

# Find CHI papers
chi_paper_titles = []
for paper in paper_docs:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check for CHI venue patterns
    full_text = paper.get('text', '')
    if 'CHI' in full_text:
        # Look for specific CHI patterns
        patterns = ['CHI', 'Proceedings of CHI', 'CHI Conference']
        for pattern in patterns:
            if pattern in full_text:
                chi_paper_titles.append(title)
                break

print('Found CHI papers:', len(chi_paper_titles))

# Match citations
citation_dict = {}
for c in citations_2020:
    citation_dict[c.get('title', '')] = int(c.get('citation_count', 0))

total_citations = 0
matched_count = 0

for title in chi_paper_titles:
    if title in citation_dict:
        total_citations += citation_dict[title]
        matched_count += 1

print('Matched CHI papers:', matched_count)
print('Total 2020 citations for CHI papers:', total_citations)

result = {
    'total_citations_2020': total_citations
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
