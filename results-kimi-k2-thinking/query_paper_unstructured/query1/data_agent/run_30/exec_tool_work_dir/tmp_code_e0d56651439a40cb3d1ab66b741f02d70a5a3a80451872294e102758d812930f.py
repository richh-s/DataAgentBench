code = """import json

# Load paper documents from file
paper_docs_file = locals()['var_functions.query_db:10']
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Load citations from file
citations_file = locals()['var_functions.query_db:11']
with open(citations_file, 'r') as f:
    citations = json.load(f)

# Build dictionary of paper titles to domains
paper_domains = {}
for doc in paper_docs:
    filename = doc.get('filename', '')
    if filename:
        title = filename.replace('.txt', '')
        text = doc.get('text', '').lower()
        
        # Check for food-related terms
        food_terms = ['food', 'nutrition', 'diet', 'eating', 'meal', 'calorie', 'weight']
        is_food = any(term in text for term in food_terms)
        
        if is_food:
            paper_domains[title] = 'food'
        else:
            paper_domains[title] = ''

# Build dictionary of total citations per paper
title_citations = {}
for citation in citations:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    title_citations[title] = title_citations.get(title, 0) + count

# Calculate total citations for food papers
total_food_citations = 0
food_papers_count = 0

for title, domain in paper_domains.items():
    if domain == 'food':
        citations_count = title_citations.get(title, 0)
        total_food_citations += citations_count
        if citations_count > 0:
            food_papers_count += 1

result = {
    "total_citation_count": total_food_citations,
    "food_papers_with_citations": food_papers_count
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:8': {'total_food_citations': 25503, 'food_papers_with_citations': 96}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
