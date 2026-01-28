code = """import json

# Read the MongoDB papers data from the file
papers_file = var_functions.query_db:6  # This is the file path

with open(papers_file, 'r') as f:
    papers_data = json.load(f)

print(f"Total papers loaded: {len(papers_data)}")

# Let's preview the first paper to see the structure
first_paper = papers_data[0]
print("\nFirst paper preview:")
print(f"Filename: {first_paper.get('filename')}")
print(f"Text preview (first 500 chars): {first_paper.get('text', '')[:500]}")
print("\n")

# Extract titles and domains from papers
# The domain information is embedded in the text, we need to parse it
# Based on the hints, the domain field may contain values like "food", "physical activity", etc.
paper_info = []

for paper in papers_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title from filename (without .txt)
    title = filename.replace('.txt', '') if filename else ''
    
    # Look for domain mentions in the text
    # Common domains include: "food", "physical activity", "sleep", "mental", "finances", 
    # "productivity", "screen time", "social interactions", "location", "chronic", "diabetes", "health_behavior"
    domains = []
    text_lower = text.lower()
    
    if 'food' in text_lower:
        domains.append('food')
    if 'physical activity' in text_lower or 'fitness' in text_lower or 'exercise' in text_lower:
        domains.append('physical activity')
    if 'sleep' in text_lower:
        domains.append('sleep')
    if 'mental' in text_lower or 'psychology' in text_lower:
        domains.append('mental')
    if 'finances' in text_lower or 'financial' in text_lower or 'money' in text_lower:
        domains.append('finances')
    if 'productivity' in text_lower:
        domains.append('productivity')
    if 'screen time' in text_lower or 'digital wellbeing' in text_lower:
        domains.append('screen time')
    if 'social interactions' in text_lower or 'social media' in text_lower:
        domains.append('social interactions')
    if 'location' in text_lower or 'gps' in text_lower:
        domains.append('location')
    if 'chronic' in text_lower:
        domains.append('chronic')
    if 'diabetes' in text_lower:
        domains.append('diabetes')
    if 'health behavior' in text_lower:
        domains.append('health_behavior')
    
    paper_info.append({
        'title': title,
        'domains': domains
    })

# Count papers in food domain
food_papers = [p for p in paper_info if 'food' in p['domains']]
print(f"Papers in 'food' domain: {len(food_papers)}")

# Store paper_info for later use
print("__RESULT__:")
print(json.dumps({
    'total_papers': len(paper_info),
    'food_papers_count': len(food_papers),
    'paper_info': paper_info[:10]  # Return first 10 as preview
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:1': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
