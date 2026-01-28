code = """import json

# Load the citations data from file
citations_file = 'storage/result/query_Citations_citations_database_11.json'
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Load the papers data from file  
papers_file = 'storage/result/query_paper_docs_paper_docs_database_10.json'
with open(papers_file, 'r') as f:
    papers_data = json.load(f)

print('Total citations records:', len(citations_data))
print('Total papers:', len(papers_data))

# Search for food domain papers using keywords
food_keywords = ['food', 'diet', 'nutrition', 'eating', 'meal', 'dietary', 'calorie', 'cuisine']
food_papers = []

for paper in papers_data:
    text = paper.get('text', '').lower()
    filename = paper.get('filename', '')
    
    # Check if paper is food-related
    if any(keyword in text for keyword in food_keywords):
        # Extract title from filename
        title = filename.replace('.txt', '')
        food_papers.append({
            'title': title,
            'filename': filename
        })

print('Food-related papers found:', len(food_papers))

# Get list of food paper titles for matching
food_titles = [paper['title'] for paper in food_papers]

# Match with citations and sum totals
total_citations = 0
matched_papers = 0
matched_details = []

for citation in citations_data:
    citation_title = citation.get('title', '')
    citation_count = int(citation.get('total_citations', 0))
    
    if citation_title in food_titles:
        total_citations += citation_count
        matched_papers += 1
        matched_details.append({
            'title': citation_title,
            'citations': citation_count
        })

print('Matched food papers with citations:', matched_papers)
print('Total citation count for food domain:', total_citations)

# Show some matched papers
print('\nSample matched papers:')
for detail in matched_details[:10]:
    print(f"  {detail['title']}: {detail['citations']} citations")"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
