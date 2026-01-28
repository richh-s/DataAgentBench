code = """import json

# Load all citations from SQLite
citations_file = locals()['var_functions.query_db:5']
citations = []
with open(citations_file, 'r') as f:
    citations = json.load(f)

# Food papers identified from previous analysis
food_papers = [
    "A Lived Informatics Model of Personal Informatics",
    "A Stage-based Model of Personal Informatics Systems",
    "A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App"
]

# Create a set for faster lookup (case-insensitive matching)
food_papers_set = {paper.lower() for paper in food_papers}

# Filter citations for food papers and sum citation counts
total_citations = 0
food_citations = []

for citation in citations:
    citation_title = citation.get('title', '').lower()
    citation_count = int(citation.get('citation_count', 0))
    
    # Check if this citation belongs to a food paper
    for food_title in food_papers_set:
        if food_title == citation_title:
            total_citations += citation_count
            food_citations.append({
                'title': citation.get('title'),
                'citation_count': citation_count,
                'citation_year': citation.get('citation_year')
            })

# Debug: see the breakdown
print('__RESULT__:')
print(json.dumps({
    "food_papers": food_papers,
    "total_food_citations": total_citations,
    "citation_records_found": len(food_citations)
}))"""

env_args = {'var_functions.query_db:0': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'citations_count': 1405, 'papers_count': 5}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'total_papers': 5, 'total_citations': 1405}, 'var_functions.execute_python:14': {'total_papers_loaded': 5, 'papers_with_titles': 5, 'food_papers_found': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'], 'food_papers_count': 3}}

exec(code, env_args)
