code = """import json
import re

# Load MongoDB data from the file path stored in the variable
mongo_file_path = var_functions.query_db:5

with open(mongo_file_path, 'r') as f:
    mongo_docs = json.load(f)

print(f"Total papers in MongoDB: {len(mongo_docs)}")

# Extract paper information and identify food domain papers
food_papers = []
food_keywords = [
    'food', 'diet', 'nutrition', 'eating', 'meal', 'calorie', 
    'weight loss', 'weight gain', 'restaurant', 'dietary', 
    'nutrition tracking', 'food journal', 'food intake'
]

for doc in mongo_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else ''
    
    if not title:
        continue
    
    # Check if paper is in food domain
    text_lower = text.lower()
    is_food_paper = False
    
    # Look for explicit domain mentions
    for keyword in food_keywords:
        if keyword in text_lower:
            # Verify it's not just a casual mention
            # Look for patterns indicating research focus
            patterns = [
                rf'{keyword} (tracking|journal|intake|habits|consumption|monitoring|logging)',
                rf'{keyword} (domain|topic|area|research)',
                rf'self.?tracking.*{keyword}',
                rf'{keyword}.*self.?tracking'
            ]
            
            for pattern in patterns:
                if re.search(pattern, text_lower):
                    is_food_paper = True
                    break
            
            if is_food_paper:
                break
    
    # Additional check for food-related research context
    if not is_food_paper:
        food_context_terms = ['weight management', 'dietary intake', 'food logging', 
                             'nutrition monitoring', 'calorie tracking', 'meal tracking']
        for term in food_context_terms:
            if term in text_lower:
                is_food_paper = True
                break
    
    if is_food_paper:
        food_papers.append(title)

print(f"Found {len(food_papers)} papers in food domain")
print("Sample food papers:", food_papers[:10])

# Save food paper titles for later use
result = {
    'food_paper_titles': food_papers,
    'count': len(food_papers)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:12': [{'total_citations': '1405'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
