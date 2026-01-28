code = """import json

# Load paper documents
paper_docs_path = locals().get('var_functions.query_db:16', None)
if paper_docs_path and isinstance(paper_docs_path, str) and paper_docs_path.endswith('.json'):
    with open(paper_docs_path, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = locals().get('var_functions.query_db:16', [])

# Load citations
citations_path = locals().get('var_functions.query_db:10', None)
if citations_path and isinstance(citations_path, str) and citations_path.endswith('.json'):
    with open(citations_path, 'r') as f:
        citations = json.load(f)
else:
    citations = locals().get('var_functions.query_db:10', [])

# Extract all titles
all_titles = []
food_related_titles = []

# Keywords that indicate food/nutrition/eating focus
food_keywords = ['food', 'eating', 'nutrition', 'diet', 'meal', 'restaurant', 'grocery', 'calorie', 'weight loss', 'weight management', 'hunger', 'cooking', 'recipe', 'kitchen', 'dietary']

for paper in paper_docs:
    filename = paper.get('filename', '')
    if filename:
        title = filename.replace('.txt', '')
        all_titles.append(title)
        
        # Check if any food keyword appears in title (case-insensitive)
        title_lower = title.lower()
        if any(keyword in title_lower for keyword in food_keywords):
            food_related_titles.append(title)

print(f"Total papers: {len(all_titles)}")
print(f"Food-related titles found: {len(food_related_titles)}")
print("\nAll food-related titles:")
for title in food_related_titles:
    print(f"  - {title}")

# Check total citations
all_citation_counts = {}
for cite in citations:
    title = cite.get('title', '').strip()
    count = int(cite.get('citation_count', 0))
    if title:
        key = title.lower()
        all_citation_counts[key] = all_citation_counts.get(key, 0) + count

total_all_citations = sum(all_citation_counts.values())
print(f"\nTotal citations across all papers: {total_all_citations}")
print(f"Unique papers with citations: {len(all_citation_counts)}")

# Count citations for food papers
food_citations = 0
food_papers_with_cites = []

for title in food_related_titles:
    key = title.lower()
    if key in all_citation_counts:
        count = all_citation_counts[key]
        food_citations += count
        food_papers_with_cites.append((title, count))

food_papers_with_cites.sort(key=lambda x: x[1], reverse=True)

print(f"\nTotal citations for food papers: {food_citations}")
print(f"Food papers with citation data: {len(food_papers_with_cites)}")
print("\nTop food papers by citations:")
for title, count in food_papers_with_cites[:10]:
    print(f"  - {title}: {count} citations")

result = {
    'total_food_papers': len(food_related_titles),
    'food_papers_with_citations': len(food_papers_with_cites),
    'total_citation_count': food_citations
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}], 'var_functions.list_db:14': ['paper_docs'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'total_food_papers': 4, 'papers_with_citations': 4, 'total_citation_count': 1328, 'top_papers': [['ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 452], ['A Lived Informatics Model of Personal Informatics', 390], ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 266], ['A Stage-based Model of Personal Informatics Systems', 220]]}, 'var_functions.execute_python:22': {'total_food_domain_papers_identified': 0, 'papers_with_citation_data': 0, 'total_citation_count': 0, 'papers': []}}

exec(code, env_args)
