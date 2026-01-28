code = """import json

# Load paper documents
paper_docs_file = locals()['var_functions.query_db:10']
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Load citations
citations_file = locals()['var_functions.query_db:11']
with open(citations_file, 'r') as f:
    citations = json.load(f)

print(f"Total papers: {len(paper_docs)}")
print(f"Total citation records: {len(citations)}")

# Check for food-related papers
food_papers = []

for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    if filename and text:
        text_lower = text.lower()
        if 'food' in text_lower or 'nutrition' in text_lower or 'diet' in text_lower or 'eating' in text_lower or 'meal' in text_lower or 'calorie' in text_lower or 'weight' in text_lower:
            title = filename.replace('.txt', '')
            food_papers.append(title)

print(f"Found {len(food_papers)} food-related papers")
print("Sample food papers:", food_papers[:5] if food_papers else "None")

# Check citations for food papers
title_to_citations = {}
for citation in citations:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    title_to_citations[title] = title_to_citations.get(title, 0) + count

print(f"Unique papers with citations: {len(title_to_citations)}")

# Find citations for food papers
total_food_citations = 0
matched_food_papers = []

for title in food_papers:
    citations_count = title_to_citations.get(title, 0)
    if citations_count > 0:
        total_food_citations += citations_count
        matched_food_papers.append((title, citations_count))

print(f"\nFood papers with citations: {len(matched_food_papers)}")
print(f"Total citation count: {total_food_citations}")

# Show top food papers by citations if any
if matched_food_papers:
    print("\nTop food papers by citations:")
    sorted_papers = sorted(matched_food_papers, key=lambda x: x[1], reverse=True)
    for title, count in sorted_papers[:10]:
        print(f"  - {title[:60]}...: {count} citations")

result = {
    'total_food_citations': total_food_citations,
    'food_papers_count': len(matched_food_papers)
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:8': {'total_food_citations': 25503, 'food_papers_with_citations': 96}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
