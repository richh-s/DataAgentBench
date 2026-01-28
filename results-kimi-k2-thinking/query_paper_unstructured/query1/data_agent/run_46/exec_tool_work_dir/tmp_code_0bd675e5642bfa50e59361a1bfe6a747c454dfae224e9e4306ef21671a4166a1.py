code = """import json
import re

# Read the JSON file with all documents
with open('/home/user/database/d1d0b7e8-4b2a-4f7d-8b2b-8a3d3e9f4c1c.json', 'r') as f:
    documents = json.load(f)

print(f"Total documents: {len(documents)}")

# Function to extract paper information from text
food_papers = []

for doc in documents:
    filename = doc['filename']
    text = doc['text'].lower()
    title = filename.replace('.txt', '')
    
    # Look for domain indicators in the text
    # Common patterns for domain mentions
    domain_indicators = [
        r'\bfood\b',
        r'food\s+track',
        r'track\s+food',
        r'food\s+journal',
        r'eat\w+',
        r'diet\w+',
        r'nutri\w+',
        r'meal\w+'
    ]
    
    # Check if this is a food domain paper
    is_food = False
    for indicator in domain_indicators:
        if re.search(indicator, text):
            # Additional check to ensure it's not just a mention but a domain focus
            # Look for patterns like "food [" which is common for domain citations
            if 'food [' in doc['text'].lower() or 'food,' in doc['text'].lower() or text.count('food') > 3:
                is_food = True
                break
    
    if is_food:
        # Check if it's a primary focus vs just a mention
        # Count occurrences and context
        food_count = text.count('food')
        if food_count >= 3:  # At least 3 mentions suggests it's a domain focus
            food_papers.append({
                'title': title,
                'filename': filename,
                'food_mentions': food_count
            })

print(f"Found {len(food_papers)} potential food domain papers")

# Show some examples
for i, paper in enumerate(food_papers[:5]):
    print(f"{i+1}. {paper['title']} (food mentions: {paper['food_mentions']})")

__RESULT__: 
{"food_papers_count": len(food_papers), "papers": food_papers[:10]}"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}]}

exec(code, env_args)
