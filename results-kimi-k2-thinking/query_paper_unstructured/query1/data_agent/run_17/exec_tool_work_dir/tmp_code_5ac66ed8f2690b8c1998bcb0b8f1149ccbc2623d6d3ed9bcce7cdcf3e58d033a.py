code = """import json
import os

# Load the paper documents from the stored file
paper_docs_file = var_functions.query_db:2
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Initialize list to store papers with extracted info
papers_with_info = []

for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '')
    
    # Extract domain from text - look for domain-related keywords
    # The description says common domains include: "food", "physical activity", "sleep", "mental", etc.
    # We'll search for "food" related keywords in the text
    
    # Normalize text to lowercase for searching
    lower_text = text.lower()
    
    # Check if this is a food domain paper
    # Look for mentions of food-related terms
    food_keywords = ['food', 'eating', 'nutrition', 'diet', 'meal', 'calorie', 'dietary']
    is_food = any(keyword in lower_text for keyword in food_keywords)
    
    if is_food:
        # Extract more context around food mentions if needed
        domain = 'food'
        papers_with_info.append({
            'title': title,
            'filename': filename,
            'domain': domain
        })

print('__RESULT__:')
print(json.dumps({
    'food_papers_count': len(papers_with_info),
    'sample_food_papers': papers_with_info[:5]
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}]}

exec(code, env_args)
