code = """import json

# Load citations data
citations_file_path = "storage/result/query_Citations_citations_database_12.json"
with open(citations_file_path, 'r') as f:
    citations_data = json.load(f)

# Load papers data  
papers_file_path = "storage/result/query_paper_docs_paper_docs_database_11.json"
with open(papers_file_path, 'r') as f:
    papers_data = json.load(f)

print("=== DATA SUMMARY ===")
print(f"Total citation records: {len(citations_data)}")
print(f"Total papers in database: {len(papers_data)}")

# Find food domain papers
food_keywords = ['food', 'diet', 'nutrition', 'eating', 'meal', 'dietary', 'calorie', 'cuisine']
food_paper_titles = []

for paper in papers_data:
    text = paper.get('text', '').lower()
    filename = paper.get('filename', '')
    
    if any(keyword in text for keyword in food_keywords):
        title = filename.replace('.txt', '')
        food_paper_titles.append(title)

print(f"Food-related papers identified: {len(food_paper_titles)}")

# Calculate total citations for food papers
food_papers_dict = {title: 0 for title in food_paper_titles}
matched_papers = 0
total_citations = 0

for citation in citations_data:
    citation_title = citation.get('title', '')
    citation_count = int(citation.get('total_citations', 0))
    
    if citation_title in food_papers_dict:
        food_papers_dict[citation_title] = citation_count
        matched_papers += 1
        total_citations += citation_count

print(f"Paper-citation matches found: {matched_papers}")
print(f"=== TOTAL CITATION COUNT FOR FOOD DOMAIN: {total_citations} ===")

# Show sample matches
print("\nSample matched papers:")
for title, count in list(food_papers_dict.items())[:5]:
    if count > 0:
        print(f"  {title}: {count} citations")

__RESULT__ = str(total_citations)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
