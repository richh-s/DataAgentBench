code = """import json

with open('file_storage/functions.query_db:2.json', 'r') as f:
    paper_docs = json.load(f)

with open('file_storage/functions.query_db:0.json', 'r') as f:
    citations = json.load(f)

def extract_domains(text):
    text_lower = text.lower()
    domains = []
    
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

paper_info = []
for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    domains = extract_domains(doc['text'])
    paper_info.append({
        'title': title,
        'domains': domains
    })

citations_by_title = {}
for citation in citations:
    title = citation['title']
    if title not in citations_by_title:
        citations_by_title[title] = []
    citations_by_title[title].append({
        'citation_count': int(citation['citation_count']),
        'citation_year': int(citation['citation_year'])
    })

total_citations = 0
food_papers_count = 0
food_papers_with_citations = []

for paper in paper_info:
    if 'food' in paper['domains']:
        food_papers_count += 1
        title = paper['title']
        
        if title in citations_by_title:
            paper_citations = citations_by_title[title]
            paper_total = sum(c['citation_count'] for c in paper_citations)
            total_citations += paper_total
            food_papers_with_citations.append({
                'title': title,
                'total_citations': paper_total
            })

result = {
    'food_papers_found': food_papers_count,
    'food_papers_with_citations': len(food_papers_with_citations),
    'total_citation_count': total_citations,
    'papers': food_papers_with_citations
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'path_type': "<class 'str'>", 'path_value': 'file_storage/functions.query_db:2.json'}, 'var_functions.execute_python:8': {'paper_docs_count': 5, 'citations_count': 1405}}

exec(code, env_args)
