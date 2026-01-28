code = """import json

# Load citations data
citations_file = locals()['var_functions.query_db:5']
with open(citations_file, 'r') as f:
    all_citations = json.load(f)

print("Total citation records:", len(all_citations))

# Load paper documents  
papers_file = locals()['var_functions.query_db:6']
with open(papers_file, 'r') as f:
    all_papers = json.load(f)

print("Total paper documents:", len(all_papers))

# Build paper dictionary by title
papers_dict = {}
for paper in all_papers:
    filename = paper.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    papers_dict[title] = paper

print("Unique papers extracted:", len(papers_dict))

# Identify food domain papers
food_papers = []
for title, paper in papers_dict.items():
    text = paper.get('text', '').lower()
    food_keywords = ['food', 'diet', 'nutrition', 'eating', 'meal', 'calorie']
    if any(keyword in text for keyword in food_keywords):
        food_papers.append(title)

print("Papers in food domain:", len(food_papers))

if food_papers:
    print("Sample food papers:", food_papers[:3])

# Aggregate citations by paper title
citation_counts = {}
for citation in all_citations:
    title = citation.get('title', '')
    try:
        count = int(citation.get('citation_count', 0))
    except (ValueError, TypeError):
        count = 0
    citation_counts[title] = citation_counts.get(title, 0) + count

print("Unique papers with citation data:", len(citation_counts))

# Calculate total citations for food papers
total_citations = 0
matching_papers = 0
for paper_title in food_papers:
    if paper_title in citation_counts:
        total_citations += citation_counts[paper_title]
        matching_papers += 1

print("Food papers with citation data:", matching_papers)
print("Total citations for food papers:", total_citations)

# Format output
output = {
    "total_citations": total_citations,
    "food_papers_with_citations": matching_papers,
    "total_food_papers": len(food_papers)
}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
