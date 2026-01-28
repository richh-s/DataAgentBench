code = """import json

# Load paper documents
paper_docs_file = locals()['var_functions.query_db:0']
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Load citations
citations_file = locals()['var_functions.query_db:3']
with open(citations_file, 'r') as f:
    citations = json.load(f)

# Extract paper information
def extract_domains(text):
    text_lower = text.lower()
    domains = []
    
    # Check for food-related terms
    food_terms = ['food', 'nutrition', 'diet', 'eating', 'meal', 'calorie', 'weight']
    if any(term in text_lower for term in food_terms):
        domains.append('food')
    
    # Check other domains for completeness
    if 'physical activity' in text_lower or 'exercise' in text_lower:
        domains.append('physical activity')
    if 'sleep' in text_lower:
        domains.append('sleep')
    if 'mental' in text_lower:
        domains.append('mental')
    
    return ','.join(domains)

# Build paper dictionary with domains
paper_domains = {}
for doc in paper_docs:
    filename = doc.get('filename', '')
    if filename:
        title = filename.replace('.txt', '')
        text = doc.get('text', '')
        domain = extract_domains(text)
        paper_domains[title] = domain

# Sum citations by title
title_citations = {}
for citation in citations:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    title_citations[title] = title_citations.get(title, 0) + count

# Find food papers and sum their citations
food_total = 0
food_papers = []

for title, domain in paper_domains.items():
    if 'food' in domain:
        citations_count = title_citations.get(title, 0)
        if citations_count > 0:
            food_papers.append(title)
            food_total += citations_count

result = {
    'total_food_citations': food_total,
    'food_papers_with_citations': len(food_papers)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json'}

exec(code, env_args)
