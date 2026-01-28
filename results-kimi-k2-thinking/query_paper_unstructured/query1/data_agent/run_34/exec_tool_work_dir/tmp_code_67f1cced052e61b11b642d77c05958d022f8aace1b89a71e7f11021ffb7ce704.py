code = """import json

# Load the data
citations_file = locals()['var_functions.query_db:5']
papers_file = locals()['var_functions.query_db:6']

with open(citations_file, 'r') as f:
    all_citations = json.load(f)

with open(papers_file, 'r') as f:
    all_papers = json.load(f)

# Build paper dictionary
papers_dict = {}
for paper in all_papers:
    filename = paper.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    papers_dict[title] = paper

# Find food papers with their text snippets
food_papers_with_snippets = []
for title, paper in papers_dict.items():
    text = paper.get('text', '').lower()
    food_keywords = ['food', 'diet', 'nutrition', 'eating', 'meal', 'calorie']
    if any(keyword in text for keyword in food_keywords):
        # Get a snippet showing the context
        snippet_start = text.find('food')
        if snippet_start == -1:
            snippet_start = text.find('diet')
        if snippet_start == -1:
            snippet_start = text.find('nutrition')
        if snippet_start == -1:
            snippet_start = text.find('eating')
        if snippet_start == -1:
            snippet_start = text.find('meal')
        if snippet_start == -1:
            snippet_start = text.find('calorie')
            
        snippet = text[max(0, snippet_start-100):snippet_start+100]
        food_papers_with_snippets.append({
            'title': title,
            'snippet': snippet.replace('\n', ' ')
        })

print("Found food papers:", len(food_papers_with_snippets))
for paper in food_papers_with_snippets:
    print(f"\n--- {paper['title']} ---")
    print(f"Snippet: ...{paper['snippet']}...")

# Build citation counts
citation_counts = {}
for citation in all_citations:
    title = citation.get('title', '')
    try:
        count = int(citation.get('citation_count', 0))
    except:
        count = 0
    citation_counts[title] = citation_counts.get(title, 0) + count

# Show citations for food papers
print("\n\nFood papers and their citations:")
total = 0
for paper in food_papers_with_snippets:
    title = paper['title']
    if title in citation_counts:
        count = citation_counts[title]
        total += count
        print(f"{title}: {count} citations")
    else:
        print(f"{title}: No citations found")

print(f"\nTotal citations: {total}")

output = {
    "total_citations": total,
    "paper_count": len(food_papers_with_snippets),
    "papers": [p['title'] for p in food_papers_with_snippets]
}
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:16': {'total_citations': 1593, 'food_papers_with_citations': 5, 'total_food_papers': 5}}

exec(code, env_args)
