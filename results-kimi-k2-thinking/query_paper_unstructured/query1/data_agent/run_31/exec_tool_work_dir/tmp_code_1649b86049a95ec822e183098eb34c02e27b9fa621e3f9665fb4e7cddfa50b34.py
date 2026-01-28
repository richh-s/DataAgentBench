code = """import json

# Load both datasets with known paths
citations_file = 'storage/result/query_Citations_citations_database_12.json'
papers_file = 'storage/result/query_paper_docs_paper_docs_database_11.json'

# Load citations
citations = json.load(open(citations_file))
print('CITATIONS SAMPLE (first 5):')
for i, c in enumerate(citations[:5]):
    print(f"  {i+1}. '{c['title']}' - {c['total_citations']} citations")

print(f"\nTotal citations records: {len(citations)}")

# Load papers  
papers = json.load(open(papers_file))
print('\nPAPERS SAMPLE (first 5):')
for i, p in enumerate(papers[:5]):
    print(f"  {i+1}. '{p['filename']}'")

# Check some specific food-related papers in citations
print('\nFOOD-RELATED CITATIONS:')
food_citation_titles = []
for c in citations:
    title = c['title'].lower()
    if 'food' in title or 'diet' in title or 'nutrition' in title or 'eating' in title:
        print(f"  '{c['title']}' - {c['total_citations']} citations")
        food_citation_titles.append(c['title'])

print(f"\nFood citations found: {len(food_citation_titles)}")

# Search food keywords in paper texts
print('\nSEARCHING FOR FOOD KEYWORDS IN PAPERS:')
food_keywords = ['food', 'diet', 'nutrition', 'eating', 'meal', 'dietary', 'calorie', 'cuisine']
food_paper_matches = []

for paper in papers:
    text = paper.get('text', '').lower()
    filename = paper.get('filename', '')
    
    # Count how many food keywords appear
    keyword_matches = []
    for kw in food_keywords:
        if kw in text:
            # Count occurrences
            count = text.count(kw)
            keyword_matches.append((kw, count))
    
    if keyword_matches:
        title = filename.replace('.txt', '')
        food_paper_matches.append({
            'title': title,
            'filename': filename,
            'keyword_matches': keyword_matches
        })
        print(f"  '{title}' matches: {keyword_matches}")

print(f"\nFood papers found: {len(food_paper_matches)}")"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:52': {'total_citations': 0}}

exec(code, env_args)
