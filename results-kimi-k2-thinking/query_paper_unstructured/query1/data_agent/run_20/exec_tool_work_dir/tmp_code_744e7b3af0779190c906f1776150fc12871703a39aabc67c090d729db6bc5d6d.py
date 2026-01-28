code = """import json

# Load all paper documents from the full query result
paper_docs_path = locals().get('var_functions.query_db:16')
if isinstance(paper_docs_path, str) and paper_docs_path.endswith('.json'):
    with open(paper_docs_path, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = locals().get('var_functions.query_db:16', [])

# Load all citations
citations_path = locals().get('var_functions.query_db:10')
if isinstance(citations_path, str) and citations_path.endswith('.json'):
    with open(citations_path, 'r') as f:
        citations = json.load(f)
else:
    citations = locals().get('var_functions.query_db:10', [])

# Simple keyword matching for food domain papers
food_keywords = ['food', 'eating', 'nutrition', 'diet', 'meal', 'restaurant', 'grocery', 'calorie', 'recipe']

# Collect all unique paper titles
unique_papers = {}
for paper in paper_docs:
    filename = paper.get('filename', '')
    if filename:
        title = filename.replace('.txt', '')
        unique_papers[title.lower()] = title

print(f'Total papers: {len(unique_papers)}')

# Identify food domain papers
food_titles = []
for key, title in unique_papers.items():
    if any(keyword in key for keyword in food_keywords):
        food_titles.append(title)

print(f'Food papers: {len(food_titles)}')
for title in food_titles:
    print(f'- {title}')

# Build citation dictionary (aggregate all years)
citation_totals = {}
for cite in citations:
    cite_title = cite.get('title', '').strip().lower()
    cite_count = int(cite.get('citation_count', 0))
    if cite_title:
        citation_totals[cite_title] = citation_totals.get(cite_title, 0) + cite_count

# Sum citations for food papers
total_citations = 0
matched_papers = []

for title in food_titles:
    title_key = title.lower()
    if title_key in citation_totals:
        count = citation_totals[title_key]
        total_citations += count
        matched_papers.append((title, count))

matched_papers.sort(key=lambda x: x[1], reverse=True)

result = {
    'total_food_papers': len(food_titles),
    'papers_with_data': len(matched_papers),
    'total_citations': total_citations,
    'papers': matched_papers
}

print(f'Total citations for food papers: {total_citations}')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}], 'var_functions.list_db:14': ['paper_docs'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'total_food_papers': 4, 'papers_with_citations': 4, 'total_citation_count': 1328, 'top_papers': [['ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 452], ['A Lived Informatics Model of Personal Informatics', 390], ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 266], ['A Stage-based Model of Personal Informatics Systems', 220]]}, 'var_functions.execute_python:22': {'total_food_domain_papers_identified': 0, 'papers_with_citation_data': 0, 'total_citation_count': 0, 'papers': []}}

exec(code, env_args)
