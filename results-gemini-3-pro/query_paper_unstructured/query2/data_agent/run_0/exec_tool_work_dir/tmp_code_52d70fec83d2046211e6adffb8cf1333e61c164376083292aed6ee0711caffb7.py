code = """import json
import re

# Load citations
with open(locals()['var_function-call-2762186927541110364'], 'r') as f:
    citations_data = json.load(f)

# Load papers
with open(locals()['var_function-call-11744135755181896625'], 'r') as f:
    papers_data = json.load(f)

# Create a lookup for citations
# key: title, value: citation_count
citation_lookup = {item['title']: int(item['citation_count']) for item in citations_data}

acm_citations = []
acm_papers_count = 0
matched_papers_count = 0

for paper in papers_data:
    text = paper['text']
    filename = paper['filename']
    title = filename.replace('.txt', '')
    
    # Check if paper is ACM
    # Heuristic: Look for "ACM" in the first 2000 chars or last 2000 chars
    # or look for "Copyright ... ACM" pattern
    # The preview showed "Copyright 2015 © ACM" and "ACM Classification Keywords"
    
    is_acm = False
    if "ACM" in text:
        # Refine check to avoid references
        # Check for specific phrases common in ACM papers headers/footers
        if "Copyright" in text and "ACM" in text:
            # Check if they are close?
            # Let's simple check: if "ACM" is in the first 1000 characters (header) 
            # or in a line with "Copyright"
            if "ACM" in text[:3000]: 
                is_acm = True
            else:
                # Check for copyright line
                lines = text.split('\n')
                for line in lines:
                    if "Copyright" in line and "ACM" in line:
                        is_acm = True
                        break
                    if "Permission" in line and "ACM" in line:
                        is_acm = True
                        break
        # Also check for "ACM Classification Keywords" which is very specific
        if "ACM Classification Keywords" in text:
            is_acm = True
            
    if is_acm:
        acm_papers_count += 1
        if title in citation_lookup:
            count = citation_lookup[title]
            acm_citations.append(count)
            matched_papers_count += 1

if acm_citations:
    avg_citations = sum(acm_citations) / len(acm_citations)
else:
    avg_citations = 0

print(f"Total papers processed: {len(papers_data)}")
print(f"ACM papers found: {acm_papers_count}")
print(f"ACM papers with citations in 2018: {matched_papers_count}")
print(f"Average citations: {avg_citations}")

print("__RESULT__:")
print(json.dumps(avg_citations))"""

env_args = {'var_function-call-2762186927541110364': 'file_storage/function-call-2762186927541110364.json', 'var_function-call-633366278914912942': 'file_storage/function-call-633366278914912942.json', 'var_function-call-4289778566380079256': {'citations_count': 158, 'papers_count': 5}, 'var_function-call-11284583893576344510': 'file_storage/function-call-11284583893576344510.json', 'var_function-call-6632607513572008990': [{'_id': '694f5530284b10b11dc0a869'}, {'_id': '694f5530284b10b11dc0a86a'}, {'_id': '694f5530284b10b11dc0a86b'}, {'_id': '694f5530284b10b11dc0a86c'}, {'_id': '694f5530284b10b11dc0a86d'}], 'var_function-call-9662563948370855485': ['paper_docs'], 'var_function-call-15927959577128233410': [{'_id': '694f5530284b10b11dc0a869'}, {'_id': '694f5530284b10b11dc0a86a'}, {'_id': '694f5530284b10b11dc0a86b'}, {'_id': '694f5530284b10b11dc0a86c'}, {'_id': '694f5530284b10b11dc0a86d'}, {'_id': '694f5530284b10b11dc0a86e'}, {'_id': '694f5530284b10b11dc0a86f'}, {'_id': '694f5530284b10b11dc0a870'}, {'_id': '694f5530284b10b11dc0a871'}, {'_id': '694f5530284b10b11dc0a872'}, {'_id': '694f5530284b10b11dc0a873'}, {'_id': '694f5530284b10b11dc0a874'}, {'_id': '694f5530284b10b11dc0a875'}, {'_id': '694f5530284b10b11dc0a876'}, {'_id': '694f5530284b10b11dc0a877'}, {'_id': '694f5530284b10b11dc0a878'}, {'_id': '694f5530284b10b11dc0a879'}, {'_id': '694f5530284b10b11dc0a87a'}, {'_id': '694f5530284b10b11dc0a87b'}, {'_id': '694f5530284b10b11dc0a87c'}, {'_id': '694f5530284b10b11dc0a87d'}, {'_id': '694f5530284b10b11dc0a87e'}, {'_id': '694f5530284b10b11dc0a87f'}, {'_id': '694f5530284b10b11dc0a880'}, {'_id': '694f5530284b10b11dc0a881'}, {'_id': '694f5530284b10b11dc0a882'}, {'_id': '694f5530284b10b11dc0a883'}, {'_id': '694f5530284b10b11dc0a884'}, {'_id': '694f5530284b10b11dc0a885'}, {'_id': '694f5530284b10b11dc0a886'}, {'_id': '694f5530284b10b11dc0a887'}, {'_id': '694f5530284b10b11dc0a888'}, {'_id': '694f5530284b10b11dc0a889'}, {'_id': '694f5530284b10b11dc0a88a'}, {'_id': '694f5530284b10b11dc0a88b'}, {'_id': '694f5530284b10b11dc0a88c'}, {'_id': '694f5530284b10b11dc0a88d'}, {'_id': '694f5530284b10b11dc0a88e'}, {'_id': '694f5530284b10b11dc0a88f'}, {'_id': '694f5530284b10b11dc0a890'}, {'_id': '694f5530284b10b11dc0a891'}, {'_id': '694f5530284b10b11dc0a892'}, {'_id': '694f5530284b10b11dc0a893'}, {'_id': '694f5530284b10b11dc0a894'}, {'_id': '694f5530284b10b11dc0a895'}, {'_id': '694f5530284b10b11dc0a896'}, {'_id': '694f5530284b10b11dc0a897'}, {'_id': '694f5530284b10b11dc0a898'}, {'_id': '694f5530284b10b11dc0a899'}, {'_id': '694f5530284b10b11dc0a89a'}, {'_id': '694f5530284b10b11dc0a89b'}, {'_id': '694f5530284b10b11dc0a89c'}, {'_id': '694f5530284b10b11dc0a89d'}, {'_id': '694f5530284b10b11dc0a89e'}, {'_id': '694f5530284b10b11dc0a89f'}, {'_id': '694f5530284b10b11dc0a8a0'}, {'_id': '694f5530284b10b11dc0a8a1'}, {'_id': '694f5530284b10b11dc0a8a2'}, {'_id': '694f5530284b10b11dc0a8a3'}, {'_id': '694f5530284b10b11dc0a8a4'}, {'_id': '694f5530284b10b11dc0a8a5'}, {'_id': '694f5530284b10b11dc0a8a6'}, {'_id': '694f5530284b10b11dc0a8a7'}, {'_id': '694f5530284b10b11dc0a8a8'}, {'_id': '694f5530284b10b11dc0a8a9'}, {'_id': '694f5530284b10b11dc0a8aa'}, {'_id': '694f5530284b10b11dc0a8ab'}, {'_id': '694f5530284b10b11dc0a8ac'}, {'_id': '694f5530284b10b11dc0a8ad'}, {'_id': '694f5530284b10b11dc0a8ae'}, {'_id': '694f5530284b10b11dc0a8af'}, {'_id': '694f5530284b10b11dc0a8b0'}, {'_id': '694f5530284b10b11dc0a8b1'}, {'_id': '694f5530284b10b11dc0a8b2'}, {'_id': '694f5530284b10b11dc0a8b3'}, {'_id': '694f5530284b10b11dc0a8b4'}, {'_id': '694f5530284b10b11dc0a8b5'}, {'_id': '694f5530284b10b11dc0a8b6'}, {'_id': '694f5530284b10b11dc0a8b7'}, {'_id': '694f5530284b10b11dc0a8b8'}, {'_id': '694f5530284b10b11dc0a8b9'}, {'_id': '694f5530284b10b11dc0a8ba'}, {'_id': '694f5530284b10b11dc0a8bb'}, {'_id': '694f5530284b10b11dc0a8bc'}, {'_id': '694f5530284b10b11dc0a8bd'}, {'_id': '694f5530284b10b11dc0a8be'}, {'_id': '694f5530284b10b11dc0a8bf'}, {'_id': '694f5530284b10b11dc0a8c0'}, {'_id': '694f5530284b10b11dc0a8c1'}, {'_id': '694f5530284b10b11dc0a8c2'}, {'_id': '694f5530284b10b11dc0a8c3'}, {'_id': '694f5530284b10b11dc0a8c4'}, {'_id': '694f5530284b10b11dc0a8c5'}, {'_id': '694f5530284b10b11dc0a8c6'}, {'_id': '694f5530284b10b11dc0a8c7'}, {'_id': '694f5530284b10b11dc0a8c8'}, {'_id': '694f5530284b10b11dc0a8c9'}, {'_id': '694f5530284b10b11dc0a8ca'}, {'_id': '694f5530284b10b11dc0a8cb'}], 'var_function-call-13924013320174006094': 99, 'var_function-call-11744135755181896625': 'file_storage/function-call-11744135755181896625.json'}

exec(code, env_args)
