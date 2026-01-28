code = """import json
import re

# Get file paths from stored variables
mongo_file_path = var_functions.query_db:5
citations_file_path = var_functions.query_db:14

# Load data
with open(mongo_file_path, 'r') as f:
    mongo_docs = json.load(f)

with open(citations_file_path, 'r') as f:
    citations_data = json.load(f)

print(f"Total papers in MongoDB: {len(mongo_docs)}")
print(f"Total citation records: {len(citations_data)}")

# Extract food domain papers
food_papers = []
food_keywords = [
    'food', 'diet', 'nutrition', 'eating', 'meal', 'calorie', 
    'weight loss', 'weight gain', 'restaurant', 'dietary', 
    'nutrition tracking', 'food journal', 'food intake', 'diet tracking'
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
    
    # Count occurrences of food-related terms
    food_term_count = sum(1 for keyword in food_keywords if keyword in text_lower)
    
    # If we have multiple food-related terms, it's likely a food domain paper
    if food_term_count >= 3:
        is_food_paper = True
    else:
        # Look for explicit research context
        food_context_patterns = [
            r'food (tracking|journal|intake|logging|monitoring|habits|consumption)',
            r'nutrition (tracking|monitoring|logging|intake)',
            r'diet (tracking|monitoring|logging)',
            r'calorie (tracking|counting|monitoring)',
            r'eating (habits|behaviors|patterns|monitoring)',
            r'meal (tracking|logging|planning)',
            r'self.?tracking.*food',
            r'food.*self.?tracking'
        ]
        
        for pattern in food_context_patterns:
            if re.search(pattern, text_lower):
                is_food_paper = True
                break
    
    if is_food_paper:
        food_papers.append(title)

print(f"Found {len(food_papers)} papers in food domain")
print("First 15 food papers:", food_papers[:15])

# Create a set for faster lookup
food_papers_set = set(food_papers)

# Match with citations and calculate total citations for food domain
food_citations_total = 0
food_citation_records = []

for citation in citations_data:
    citation_title = citation.get('title', '')
    citation_count = int(citation.get('citation_count', 0))
    
    if citation_title in food_papers_set:
        food_citations_total += citation_count
        food_citation_records.append({
            'title': citation_title,
            'citation_count': citation_count,
            'citation_year': citation.get('citation_year', '')
        })

print(f"Total citations for food domain papers: {food_citations_total}")
print(f"Number of citation records for food papers: {len(food_citation_records)}")

# Save result
result = {
    'food_paper_count': len(food_papers),
    'total_food_citations': food_citations_total,
    'food_citation_records_count': len(food_citation_records),
    'food_papers': food_papers[:20],  # First 20 titles
    'sample_citation_records': food_citation_records[:10]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:12': [{'total_citations': '1405'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:18': {'total_citation_records': 1405, 'sample_records': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}], 'total_citations_all': 70977}}

exec(code, env_args)
