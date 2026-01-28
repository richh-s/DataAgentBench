code = """import json

# Read the query results from MongoDB
with open('/tmp/tmp0fht6t2l.json', 'r') as f:
    paper_docs = json.load(f)

# Read the citation data
with open('/tmp/tmp3q8m8q2r.json', 'r') as f:
    citations_data = f.read()
    citations = json.loads(citations_data)

print('Number of papers in MongoDB:', len(paper_docs))
print('Number of citations records:', len(citations))

chi_papers = []
for paper in paper_docs:
    text = paper.get('text', '').lower()
    filename = paper.get('filename', '')
    # Look for CHI patterns
    if 'chi' in text:
        # Check if it's likely a venue marker by looking for common conference patterns
        text_full = paper.get('text', '')
        if ('CHI ' in text_full or 'Proceedings of CHI' in text_full or 
            'CHI conference' in text_full.lower() or 'CHI \'' in text_full):
            chi_papers.append({
                'filename': filename,
                'title': filename.replace('.txt', '')
            })

print('Found papers with CHI venue patterns:', len(chi_papers))

# Check citations from 2020
citations_2020 = [c for c in citations if str(c.get('citation_year')) == '2020']
print('Citations from 2020:', len(citations_2020))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}]}

exec(code, env_args)
