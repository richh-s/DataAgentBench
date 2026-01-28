code = """import json

# Read the query results from MongoDB
with open('/tmp/tmp0fht6t2l.json', 'r') as f:
    paper_docs = json.load(f)

# Read the citation data
with open('/tmp/tmp3q8m8q2r.json', 'r') as f:
    citations_data = f.read()
    # Parse the JSON string
    citations = json.loads(citations_data)

print('Number of papers in MongoDB:', len(paper_docs))
print('Number of citations records:', len(citations))

# Look for CHI mentions in papers
chi_papers = []
for i, paper in enumerate(paper_docs):
    text = paper.get('text', '').lower()
    filename = paper.get('filename', 'Unknown')
    # Check for CHI venue patterns
    if 'chi' in text:
        # More specific pattern matching
        text_upper = paper.get('text', '')
        patterns = ['CHI ', 'CHI \'', 'CHI 20', 'CHI \'1', 'CHI \'0','Proceedings of CHI', 'CHI Conference']
        for pattern in patterns:
            if pattern in text_upper:
                chi_papers.append({
                    'index': i,
                    'filename': filename,
                    'title': filename.replace('.txt', '')
                })
                if len(chi_papers) <= 3:
                    print('CHI paper found:', filename)
                break

print('\nTotal papers with CHI venue patterns:', len(chi_papers))

# Look at citations from 2020
citations_2020 = []
for c in citations:
    if str(c.get('citation_year')) == '2020':
        citations_2020.append(c)

print('\nTotal citations from 2020:', len(citations_2020))
if citations_2020:
    print('Sample 2020 citations:')
    for i, c in enumerate(citations_2020[:5]):
        print(f"  {c.get('title')}: {c.get('citation_count')} citations")"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}]}

exec(code, env_args)
