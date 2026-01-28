code = """import json
import os

# Find and load the data files from the results
# Based on the tool call history, the files should be in storage/result/

# Load citations data
citations_path = None
papers_path = None

print("Looking for data files...")
for root, dirs, files in os.walk("storage/result"):
    for file in files:
        if file.startswith("query_") and file.endswith(".json"):
            filepath = os.path.join(root, file)
            print(f"Found: {filepath}")
            if "Citations" in filepath:
                citations_path = filepath
            elif "paper_docs" in filepath:
                papers_path = filepath

print(f"\nCitations file: {citations_path}")
print(f"Papers file: {papers_path}")

# Load both datasets
with open(citations_path, 'r') as f:
    citations = json.load(f)
    print(f"Loaded {len(citations)} citation records")

with open(papers_path, 'r') as f:
    papers = json.load(f)
    print(f"Loaded {len(papers)} papers")

# Find food-related papers
food_keywords = ['food', 'diet', 'nutrition', 'eating', 'meal', 'dietary', 'calorie', 'cuisine']
food_titles = []

for paper in papers:
    text = paper.get('text', '').lower()
    filename = paper.get('filename', '')
    
    if any(keyword in text for keyword in food_keywords):
        title = filename.replace('.txt', '')
        food_titles.append(title)

print(f"Found {len(food_titles)} food-related papers")

# Create a lookup dictionary for citations
citation_lookup = {item['title']: int(item.get('total_citations', 0)) for item in citations}

# Calculate total citations for food papers
total_citations = 0
matched = 0

for title in food_titles:
    if title in citation_lookup:
        total_citations += citation_lookup[title]
        matched += 1

result = {
    'food_papers_count': len(food_titles),
    'matched_with_citations': matched,
    'total_citation_count': total_citations
}

print("\\n=== FINAL RESULT ===")
print(f"Total citation count for food domain: {total_citations}")

__RESULT__ = str(total_citations)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
