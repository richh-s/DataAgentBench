code = """import json

# Load the MongoDB documents from the file
with open('/tmp/tmpj7j1t4q6.json', 'r') as f:
    mongo_docs = json.load(f)

# Extract paper information from MongoDB documents
paper_info = []
for doc in mongo_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename (remove .txt)
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract domain from text - look for keywords related to food
    # Common food-related terms to search for
    food_keywords = [
        'food', 'diet', 'nutrition', 'eating', 'meal', 'calorie', 
        'weight loss', 'weight gain', 'restaurant', 'dietary'
    ]
    
    # Convert text to lowercase for case-insensitive matching
    text_lower = text.lower()
    
    # Check if any food keywords are in the text
    domain = None
    for keyword in food_keywords:
        if keyword in text_lower:
            domain = 'food'
            break
    
    # Also check for food in specific context markers
    if not domain:
        # Look for explicit domain mentions in the text
        if 'food' in text_lower:
            # Check if it's not just a casual mention but part of research domain
            # Look for patterns like "food [domain/topic/tracking]"
            import re
            if re.search(r'food (domain|topic|tracking|journal|intake|habits|consumption)', text_lower):
                domain = 'food'
    
    if domain == 'food':
        paper_info.append({
            'title': title,
            'domain': domain
        })

print(f"Found {len(paper_info)} papers in food domain")
print(paper_info[:5])  # Show first 5"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
