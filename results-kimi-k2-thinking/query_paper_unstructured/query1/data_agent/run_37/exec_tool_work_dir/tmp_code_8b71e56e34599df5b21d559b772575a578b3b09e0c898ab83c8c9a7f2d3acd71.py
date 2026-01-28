code = """import json

# Load the citation data from the file
citations_file = locals()['var_functions.query_db:8']
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Food domain papers identified earlier
food_papers = [
    "A Lived Informatics Model of Personal Informatics",
    "A Stage-based Model of Personal Informatics Systems"
]

# Filter citations for food domain papers and sum citation counts
food_citations = []
total_citations = 0

for citation in citations_data:
    title = citation['title']
    if title in food_papers:
        count = int(citation['citation_count'])
        year = int(citation['citation_year'])
        food_citations.append({
            'title': title,
            'citation_count': count,
            'citation_year': year
        })
        total_citations += count

# Group by paper to show breakdown
paper_totals = {}
for citation in food_citations:
    title = citation['title']
    count = citation['citation_count']
    if title not in paper_totals:
        paper_totals[title] = 0
    paper_totals[title] += count

print('__RESULT__:')
print(json.dumps({
    'total_citation_count': total_citations,
    'paper_breakdown': paper_totals,
    'total_food_papers': len(food_papers)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:7': {'food_papers_count': 2, 'sample_food_papers': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems']}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
