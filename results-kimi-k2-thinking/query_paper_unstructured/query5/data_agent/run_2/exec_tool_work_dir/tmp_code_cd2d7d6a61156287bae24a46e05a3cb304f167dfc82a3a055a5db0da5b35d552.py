code = """import json

# Load all citations from 2020
with open('/tmp/tmpn2tux2v2.json', 'r') as f:
    citations_2020 = json.load(f)

print('Total citations from 2020:', len(citations_2020))

# Load all paper documents  
with open('/tmp/tmpf_9r5s6n.json', 'r') as f:
    paper_docs = json.load(f)

print('Total paper documents:', len(paper_docs))

# First, let's identify CHI papers by examining the text
chi_paper_titles = []

for paper in paper_docs:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Look for CHI venue indicators
    # Check for various CHI patterns that indicate conference venue
    chi_patterns = [
        'CHI \'1',  # CHI '13, CHI '14, etc.
        'CHI \'2',
        'CHI 20',   # CHI 2013, CHI 2014, etc.
        'Proceedings of CHI',
        'CHI Conference',
        'CHI \u2013',  # CHI – with dash
        'CHI, ',     # CHI, with comma
    ]
    
    full_text = paper.get('text', '')
    is_chi_paper = False
    
    for pattern in chi_patterns:
        if pattern in full_text:
            is_chi_paper = True
            break
    
    if is_chi_paper:
        chi_paper_titles.append(title)

print('Found CHI papers:', len(chi_paper_titles))
print('Sample CHI papers:', chi_paper_titles[:10])

# Now match with citations from 2020
citation_dict = {c['title']: int(c['citation_count']) for c in citations_2020}

# Find citation counts for CHI papers
total_citations_2020 = 0
matched_chi_papers = 0
unmatched_chi_papers = []

for title in chi_paper_titles:
    if title in citation_dict:
        count = citation_dict[title]
        total_citations_2020 += count
        matched_chi_papers += 1
    else:
        unmatched_chi_papers.append(title)

print('\nMatched CHI papers with 2020 citations:', matched_chi_papers)
print('Total citation count for CHI papers in 2020:', total_citations_2020)
print('Unmatched CHI papers:', len(unmatched_chi_papers))
print('Sample unmatched:', unmatched_chi_papers[:5])

result = {
    'total_chi_papers_identified': len(chi_paper_titles),
    'matched_chi_papers_with_2020_citations': matched_chi_papers,
    'total_citation_count_2020': total_citations_2020
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
