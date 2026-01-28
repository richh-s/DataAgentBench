code = """import json

# Load the citations data
citations_path = locals().get('var_functions.query_db:10')
citations = []
if citations_path and isinstance(citations_path, str) and citations_path.endswith('.json'):
    with open(citations_path, 'r') as f:
        citations = json.load(f)
else:
    citations = locals().get('var_functions.query_db:10', [])

# Load the papers data
papers_path = locals().get('var_functions.query_db:16')
papers = []
if papers_path and isinstance(papers_path, str) and papers_path.endswith('.json'):
    with open(papers_path, 'r') as f:
        papers = json.load(f)
else:
    papers = locals().get('var_functions.query_db:16', [])

print(f'Loaded {len(citations)} citation records')
print(f'Loaded {len(papers)} paper documents')

# Create citation dictionary - sum all years for each title
citation_totals = {}
for record in citations:
    title = record.get('title', '').strip().lower()
    count = int(record.get('citation_count', 0))
    if title:
        citation_totals[title] = citation_totals.get(title, 0) + count

print(f'Total unique papers with citations: {len(citation_totals)}')

# Identify food-related papers and calculate citations
food_keywords = ['food', 'eating', 'nutrition', 'diet', 'meal', 'restaurant', 'grocery', 'calorie', 'weight loss', 'weight management']
food_papers = []
food_citation_total = 0

for paper in papers:
    filename = paper.get('filename', '')
    if not filename:
        continue
        
    title = filename.replace('.txt', '')
    title_lower = title.lower()
    
    # Check if title contains food-related keywords
    if any(keyword in title_lower for keyword in food_keywords):
        citations = citation_totals.get(title_lower, 0)
        if citations > 0:
            food_papers.append((title, citations))
            food_citation_total += citations

print(f'Found {len(food_papers)} food papers with citations')
print(f'Total citations for food papers: {food_citation_total}')

# Sort by citation count
food_papers.sort(key=lambda x: x[1], reverse=True)

result = {
    'food_papers_count': len(food_papers),
    'total_citation_count': food_citation_total,
    'top_food_papers': food_papers[:5]
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}], 'var_functions.list_db:14': ['paper_docs'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'total_food_papers': 4, 'papers_with_citations': 4, 'total_citation_count': 1328, 'top_papers': [['ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 452], ['A Lived Informatics Model of Personal Informatics', 390], ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 266], ['A Stage-based Model of Personal Informatics Systems', 220]]}, 'var_functions.execute_python:22': {'total_food_domain_papers_identified': 0, 'papers_with_citation_data': 0, 'total_citation_count': 0, 'papers': []}, 'var_functions.execute_python:26': {'total_food_papers': 0, 'papers_with_data': 0, 'total_citations': 0, 'papers': []}, 'var_functions.execute_python:30': {'status': 'debug_complete'}}

exec(code, env_args)
