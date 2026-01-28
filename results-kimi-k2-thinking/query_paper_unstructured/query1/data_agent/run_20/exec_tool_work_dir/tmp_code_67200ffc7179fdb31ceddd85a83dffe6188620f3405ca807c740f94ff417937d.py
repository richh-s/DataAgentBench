code = """import json

# Access the original query results directly
citations_res = locals().get('var_functions.query_db:10')
papers_res = locals().get('var_functions.query_db:16')

print(f'citations_res type: {type(citations_res)}')
print(f'papers_res type: {type(papers_res)}')

# Check if the first attempt at loading citations worked
citations_file = locals().get('var_functions.query_db:10')
if isinstance(citations_file, str) and citations_file.endswith('.json'):
    with open(citations_file, 'r') as f:
        all_citations = json.load(f)
    print(f'Loaded citations from file: {len(all_citations)} records')
else:
    all_citations = locals().get('var_functions.query_db:10', [])
    print(f'Citations already in memory: {len(all_citations)} records')

# Check if the first attempt at loading papers worked
papers_file = locals().get('var_functions.query_db:16')
if isinstance(papers_file, str) and papers_file.endswith('.json'):
    with open(papers_file, 'r') as f:
        all_papers = json.load(f)
    print(f'Loaded papers from file: {len(all_papers)} records')
else:
    all_papers = locals().get('var_functions.query_db:16', [])
    print(f'Papers already in memory: {len(all_papers)} records')

# Build citation dict
citation_dict = {}
for cite in all_citations:
    title = cite.get('title', '').strip().lower()
    count = int(cite.get('citation_count', 0))
    if title:
        citation_dict[title] = citation_dict.get(title, 0) + count

print(f'Unique papers with citations: {len(citation_dict)}')

# Extract paper titles and look for food ones
food_related = []

for paper in all_papers:
    filename = paper.get('filename', '')
    if filename:
        title = filename.replace('.txt', '')
        title_lower = title.lower()
        
        # Simple check for food-related terms
        if 'food' in title_lower:
            count = citation_dict.get(title_lower, 0)
            food_related.append((title, count))
            print(f'Found food paper: {title} - {count} citations')

# Sum them
total_citations = sum(count for _, count in food_related)

result = {
    'total_food_papers': len(food_related),
    'total_citations': total_citations,
    'papers': food_related
}

print('\nFinal result:')
print(f'Food papers: {len(food_related)}')
print(f'Total citations: {total_citations}')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}], 'var_functions.list_db:14': ['paper_docs'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'total_food_papers': 4, 'papers_with_citations': 4, 'total_citation_count': 1328, 'top_papers': [['ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 452], ['A Lived Informatics Model of Personal Informatics', 390], ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 266], ['A Stage-based Model of Personal Informatics Systems', 220]]}, 'var_functions.execute_python:22': {'total_food_domain_papers_identified': 0, 'papers_with_citation_data': 0, 'total_citation_count': 0, 'papers': []}, 'var_functions.execute_python:26': {'total_food_papers': 0, 'papers_with_data': 0, 'total_citations': 0, 'papers': []}}

exec(code, env_args)
