code = """import json

# Read the full MongoDB results
file_path = var_functions.query_db:2
with open(file_path, 'r') as f:
    papers_data = json.load(f)

print(f"Total papers in database: {len(papers_data)}")
print("\nFirst paper structure:")
print(json.dumps(papers_data[0], indent=2)[:2000] + "...")

# Extract papers in 'food' domain
food_papers = []
for paper in papers_data:
    text = paper.get('text', '').lower()
    filename = paper.get('filename', '')
    
    # Check if 'food' is mentioned as a domain in the text
    # Look for domain indicators in the text
    if 'domain: food' in text or 'food domain' in text or 'tracking food' in text:
        # Extract title from filename (remove .txt extension)
        title = filename.replace('.txt', '') if filename else ''
        food_papers.append({
            'title': title,
            'filename': filename,
            '_id': paper.get('_id')
        })

print(f"\nFound {len(food_papers)} potential food domain papers")
if food_papers:
    print("\nSample food papers:")
    for i, paper in enumerate(food_papers[:5]):
        print(f"{i+1}. {paper['title']}")"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
