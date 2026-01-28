code = """import json

# Get the file path from the storage
file_path = 'var_functions.query_db:2'
print('File path:', file_path)

# Read the full MongoDB result from the file
with open(file_path, 'r') as f:
    papers_data = json.load(f)

print('Number of papers loaded:', len(papers_data))

# Check the first few papers to understand structure
for i, paper in enumerate(papers_data[:3]):
    print(f'Paper {i}: filename={paper.get("filename")}')
    print(f'  Text preview: {paper.get("text", "")[:200]}...')
    print()

# Extract paper titles and domains
papers_info = []
for paper in papers_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title (filename without .txt)
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract domain - look for domain keywords in text
    # Common domains mentioned in the hints
    domain_keywords = [
        'food', 'physical activity', 'sleep', 'mental', 'finances', 
        'productivity', 'screen time', 'social interactions', 'location',
        'chronic', 'diabetes', 'health_behavior'
    ]
    
    domains = []
    text_lower = text.lower()
    for keyword in domain_keywords:
        if keyword in text_lower:
            domains.append(keyword)
    
    papers_info.append({
        'title': title,
        'filename': filename,
        'domains': domains,
        'text_length': len(text)
    })

# Count papers by domain
food_papers = [p for p in papers_info if 'food' in p['domains']]
print(f'Number of papers in food domain: {len(food_papers)}')
print(f'Total papers: {len(papers_info)}')

# Print some food domain papers
print('\nFood domain papers:')
for i, paper in enumerate(food_papers[:5]):
    print(f"{i+1}. {paper['title']}")"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
