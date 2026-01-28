code = """import json

# Load data from file paths
paper_file_path = locals()['var_functions.query_db:2']
citation_file_path = locals()['var_functions.query_db:10']

with open(paper_file_path, 'r') as f:
    papers_data = json.load(f)

with open(citation_file_path, 'r') as f:
    citations_data = json.load(f)

# Create dictionary mapping paper titles to their data
papers_dict = {}
for paper in papers_data:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    if title:
        papers_dict[title] = paper

# Find papers in food domain
food_paper_titles = []
for title, paper in papers_dict.items():
    text = paper.get('text', '').lower()
    
    # Check for various food domain indicators
    food_keywords = ['food domain', 'domain: food', 'tracking food', 'food tracking', 
                     'food intake', 'diet tracking', 'food and']
    
    domain_section = text.split('domain:')
    if len(domain_section) > 1:
        domain_part = domain_section[1].split()[0:10]  # Get first few words after 'domain:'
        domain_text = ' '.join(domain_part)
        if 'food' in domain_text:
            food_paper_titles.append(title)
            continue
    
    if any(keyword in text for keyword in food_keywords):
        food_paper_titles.append(title)

# Get citations for food papers
food_citations = {title: [] for title in food_paper_titles}
for citation in citations_data:
    citation_title = citation.get('title', '')
    if citation_title in food_paper_titles:
        food_citations[citation_title].append(citation)

# Calculate total citation count
total_citations = 0
for title, citations in food_citations.items():
    for citation in citations:
        count = int(citation.get('citation_count', 0))
        total_citations += count

result = {
    'food_papers_count': len(food_paper_titles),
    'total_citation_count': total_citations,
    'food_paper_titles': food_paper_titles,
    'papers_with_citations': sum(1 for citations in food_citations.values() if citations)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:18': {'papers_type': "<class 'str'>", 'citations_type': "<class 'str'>"}}

exec(code, env_args)
