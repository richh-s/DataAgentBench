code = """import json

# Access the stored file path
paper_docs_file = locals()['var_functions.query_db:2']

# Load all paper documents
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Better food domain detection - look for more specific patterns
food_papers = []
food_keywords = ['food', 'eating', 'nutrition', 'diet', 'meal', 'calorie', 'dietary', 'nutrition tracking', 'food journal', 'food logging']

for doc in paper_docs:
    filename = doc['filename']
    text = doc.get('text', '').lower()
    
    # Extract title
    title = filename.replace('.txt', '')
    
    # Check for food-specific mentions with context
    food_score = 0
    for keyword in food_keywords:
        if keyword in text:
            food_score += 1
    
    # Require at least 2 food mentions to be more confident
    if food_score >= 2:
        # Count occurrences of each keyword
        occurrences = sum(text.count(keyword) for keyword in food_keywords)
        if occurrences >= 3:  # At least 3 mentions total
            food_papers.append(title)

print(f"Found {len(food_papers)} papers that appear to be food-related:")
for i, title in enumerate(food_papers, 1):
    print(f"{i}. {title}")

print('__RESULT__:')
print(json.dumps({'food_paper_titles': food_papers, 'count': len(food_papers)}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:10': {'food_papers_count': 5, 'food_paper_titles': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation']}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'total_food_papers': 5, 'food_papers_with_citations': 5, 'total_citation_count': 1593, 'food_citation_details': [{'title': 'A Lived Informatics Model of Personal Informatics', 'citations': 390}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'citations': 220}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citations': 265}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citations': 266}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citations': 452}]}}

exec(code, env_args)
