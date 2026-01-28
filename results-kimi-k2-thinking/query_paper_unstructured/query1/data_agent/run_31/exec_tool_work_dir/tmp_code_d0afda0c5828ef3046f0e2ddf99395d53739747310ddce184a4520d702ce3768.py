code = """import json

# Access the file path stored in the previous result
citations_file = var_functions.query_db:9
papers_file = var_functions.query_db:10

print('Citations file:', citations_file)
print('Papers file:', papers_file)

# Load both datasets
with open(citations_file, 'r') as f:
    citations = json.load(f)

with open(papers_file, 'r') as f:
    papers = json.load(f)

print('Loaded citations count:', len(citations))
print('Loaded papers count:', len(papers))

# Search for food-related papers
food_keywords = ['food', 'diet', 'nutrition', 'eating', 'meal', 'culinary', 'calorie']
food_paper_titles = []

for paper in papers:
    text = paper.get('text', '').lower()
    filename = paper.get('filename', '')
    
    # Check if the paper is food-related
    if any(keyword in text for keyword in food_keywords):
        # Extract title from filename
        title = filename.replace('.txt', '')
        food_paper_titles.append(title)

print('Food paper titles found:', len(food_paper_titles))
print('Sample titles:', food_paper_titles[:10])

# Now find citations for these food papers
food_citations_total = 0
food_citations_count = 0

for citation in citations:
    citation_title = citation.get('title', '')
    total_citations = int(citation.get('total_citations', 0))
    
    # Check if this citation matches any of our food papers
    if citation_title in food_paper_titles:
        food_citations_total += total_citations
        food_citations_count += 1
        print(f"Match found: {citation_title} - {total_citations} citations")

print('\nTotal food papers with citations:', food_citations_count)
print('Total citation count for food domain:', food_citations_total)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
