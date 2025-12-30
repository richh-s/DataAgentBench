code = """import json

with open(locals()['var_function-call-5992210223060542077'], 'r') as f:
    papers = json.load(f)

print(f"Total papers: {len(papers)}")

food_in_title = []
food_in_text_snippets = []

for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    text = paper.get('text', '')
    
    if 'food' in title.lower():
        food_in_title.append(title)
    
    idx = text.lower().find('food')
    if idx != -1 and len(food_in_text_snippets) < 5:
        start = max(0, idx - 100)
        end = min(len(text), idx + 100)
        snippet = text[start:end]
        food_in_text_snippets.append({"title": title, "snippet": snippet})

print("__RESULT__:")
print(json.dumps({
    "total_papers": len(papers),
    "titles_with_food": food_in_title,
    "snippets": food_in_text_snippets
}))"""

env_args = {'var_function-call-18115772371800026671': 'file_storage/function-call-18115772371800026671.json', 'var_function-call-5992210223060542077': 'file_storage/function-call-5992210223060542077.json', 'var_function-call-13564221464732274520': 'file_storage/function-call-13564221464732274520.json', 'var_function-call-7850296922984733998': {'food_papers_count': 0, 'total_citations': 0, 'food_paper_titles': []}}

exec(code, env_args)
