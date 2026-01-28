code = """import json

# Load the data files
citations_file = locals()['var_functions.query_db:5']
papers_file = locals()['var_functions.query_db:6']

with open(citations_file) as f:
    citations = json.load(f)

with open(papers_file) as f:
    papers = json.load(f)

print("Documents loaded:", len(citations), "citations", len(papers), "papers")

# Build paper lookup by title
paper_lookup = {}
for p in papers:
    fn = p.get('filename', '')
    title = fn[:-4] if fn.endswith('.txt') else fn
    paper_lookup[title] = p

print("Unique papers:", len(paper_lookup))

# Identify food domain papers
food_papers = []
for title, paper in paper_lookup.items():
    txt = paper.get('text', '').lower()
    keywords = ['food', 'diet', 'nutrition', 'eating', 'meal', 'calorie']
    if any(k in txt for k in keywords):
        food_papers.append(title)

print("Food papers identified:", len(food_papers))

# Aggregate citations per title
cite_counts = {}
for c in citations:
    t = c.get('title', '')
    try:
        cnt = int(c.get('citation_count', 0))
    except:
        cnt = 0
    cite_counts[t] = cite_counts.get(t, 0) + cnt

print("Papers with citation data:", len(cite_counts))

# Calculate total for food papers
total = 0
matches = 0
for p in food_papers:
    if p in cite_counts:
        total += cite_counts[p]
        matches += 1

print("Food papers in citation data:", matches)
print("Total citations:", total)

result = {"total_citations": total, "papers_matched": matches, "food_papers": len(food_papers)}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:16': {'total_citations': 1593, 'food_papers_with_citations': 5, 'total_food_papers': 5}}

exec(code, env_args)
