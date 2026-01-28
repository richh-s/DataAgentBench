code = """import json

# Read the MongoDB query result - paper documents
with open('file_storage/functions.query_db:2.json', 'r') as f:
    paper_docs = json.load(f)

# Read the SQLite citations query result
with open('file_storage/functions.query_db:0.json', 'r') as f:
    citations = json.load(f)

# Function to extract domain from paper text
def extract_domains(text):
    """Extract domains from paper text based on keywords"""
    text_lower = text.lower()
    domains = []
    
    # Check for various domains
    if 'food' in text_lower or 'eating' in text_lower or 'nutrition' in text_lower or 'diet' in text_lower:
        domains.append('food')
    if 'physical activity' in text_lower or 'exercise' in text_lower or 'fitness' in text_lower:
        domains.append('physical activity')
    if 'sleep' in text_lower:
        domains.append('sleep')
    if 'mental' in text_lower or 'mood' in text_lower:
        domains.append('mental')
    if 'finances' in text_lower or 'financial' in text_lower or 'money' in text_lower:
        domains.append('finances')
    if 'location' in text_lower:
        domains.append('location')
        
    return domains

# Extract paper information including domains
paper_info = []
for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    domains = extract_domains(doc['text'])
    paper_info.append({
        'title': title,
        'domains': domains,
        'text': doc['text'][:500]  # First 500 chars for debugging
    })

# Create a dictionary of citations by title for easier lookup
citations_by_title = {}
for citation in citations:
    title = citation['title']
    if title not in citations_by_title:
        citations_by_title[title] = []
    citations_by_title[title].append({
        'citation_count': int(citation['citation_count']),
        'citation_year': int(citation['citation_year'])
    })

# Find food domain papers and their citations
food_papers_with_citations = []
total_citations = 0
food_papers_count = 0

for paper in paper_info:
    if 'food' in paper['domains']:
        food_papers_count += 1
        title = paper['title']
        
        # Get citations for this paper
        if title in citations_by_title:
            paper_citations = citations_by_title[title]
            paper_total_citations = sum(c['citation_count'] for c in paper_citations)
            total_citations += paper_total_citations
            
            food_papers_with_citations.append({
                'title': title,
                'total_citations': paper_total_citations,
                'citation_records': paper_citations
            })

result = {
    'food_papers_found': food_papers_count,
    'food_papers_with_citations': len(food_papers_with_citations),
    'total_citation_count': total_citations,
    'paper_details': food_papers_with_citations
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'path_type': "<class 'str'>", 'path_value': 'file_storage/functions.query_db:2.json'}, 'var_functions.execute_python:8': {'paper_docs_count': 5, 'citations_count': 1405}}

exec(code, env_args)
