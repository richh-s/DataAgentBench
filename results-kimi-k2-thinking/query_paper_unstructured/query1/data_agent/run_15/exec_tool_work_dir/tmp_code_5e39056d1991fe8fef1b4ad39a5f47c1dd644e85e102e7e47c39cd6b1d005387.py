code = """import json

# Read citations data
citations_file = locals()['var_functions.query_db:8']
with open(citations_file, 'r') as f:
    citations = json.load(f)

# Read paper docs data
paper_docs_file = locals()['var_functions.query_db:14']
with open(paper_docs_file, 'r') as f:
    papers = json.load(f)

# Extract all titles from both sources
citation_titles = [c['title'] for c in citations]
paper_titles = [p['filename'].replace('.txt', '') for p in papers]

# Check for any exact matches
exact_matches = set(citation_titles) & set(paper_titles)

# Check for partial matches containing food/eating/diet keywords
food_keywords = ['food', 'eating', 'diet', 'meal', 'nutrition', 'calorie', 'dietary']
food_citation_titles = []
food_paper_titles = []

for title in citation_titles:
    if any(keyword.lower() in title.lower() for keyword in food_keywords):
        food_citation_titles.append(title)

for title in paper_titles:
    if any(keyword.lower() in title.lower() for keyword in food_keywords):
        food_paper_titles.append(title)

print('__RESULT__:')
print(json.dumps({
    'total_citations': len(citations),
    'total_papers': len(papers),
    'exact_matches_count': len(exact_matches),
    'food_citation_titles_count': len(food_citation_titles),
    'food_paper_titles_count': len(food_paper_titles),
    'food_citation_titles': food_citation_titles[:10],  # First 10 for preview
    'food_paper_titles': food_paper_titles[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': [], 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_citations': 0, 'food_paper_titles': [], 'citation_count': 0}}

exec(code, env_args)
