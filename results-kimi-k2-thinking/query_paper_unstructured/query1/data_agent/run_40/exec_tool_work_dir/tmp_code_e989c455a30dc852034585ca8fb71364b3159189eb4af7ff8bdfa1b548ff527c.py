code = """import json
import pandas as pd
import re

# Load paper documents from the file
paper_docs_file = locals()['var_functions.query_db:14']
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Load citation data from the file
citations_file = locals()['var_functions.query_db:2']
with open(citations_file, 'r') as f:
    citations = json.load(f)

# Extract title and domain from each paper document
paper_info = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']
    
    # Look for food domain indicators - more specific patterns
    # We'll search for papers that focus on food tracking, food systems, etc.
    food_indicators = [
        r'food tracking',
        r'food journal',
        r'food intake',
        r'dietary',
        r'eating habits',
        r'nutrition',
        r'meal logging',
        r'food [Dd]omain',
        r'food\b(?! (journal|tracking|intake|logging))'  # just 'food' word
    ]
    
    text_lower = text.lower()
    has_food_domain = False
    
    # Check each indicator
    for indicator in food_indicators:
        if re.search(indicator, text_lower):
            has_food_domain = True
            break
    
    # Also check if food is mentioned in context of domains being studied
    if 'food' in text_lower:
        # Check if it's in a list of domains or in a research context
        domain_context_patterns = [
            r'domain[^.]{0,50}food',
            r'food[^.]{0,30}domain',
            r'tracking[^.]{0,30}food',
            r'food[^.]{0,30}tracking'
        ]
        
        for pattern in domain_context_patterns:
            if re.search(pattern, text_lower):
                has_food_domain = True
                break
    
    paper_info.append({
        'title': title,
        'text': text[:500],  # First 500 chars for preview
        'is_food_domain': has_food_domain
    })

# Create DataFrames
papers_df = pd.DataFrame(paper_info)
citations_df = pd.DataFrame(citations)

# Convert citation_count to int
citations_df['citation_count'] = citations_df['citation_count'].astype(int)

# Join with citation data
food_papers = papers_df[papers_df['is_food_domain']]['title'].tolist()

# Get citations for food papers
food_citations = citations_df[citations_df['title'].isin(food_papers)]

total_citations_food = food_citations['citation_count'].sum()

print('__RESULT__:')
print(json.dumps({
    "food_paper_titles": food_papers,
    "num_food_papers": len(food_papers),
    "total_citation_count": int(total_citations_food),
    "num_citation_records": len(food_citations)
}))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_citations': 1405, 'sample_titles': ['Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies']}, 'var_functions.list_db:8': ['paper_docs'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'paper_docs_count': 5, 'citations_count': 1405, 'sample_paper': 'A Lived Informatics Model of Personal Informatics.txt'}, 'var_functions.execute_python:18': {'total_papers': 5, 'food_papers': 3, 'food_paper_titles': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'], 'sample_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'domains': ['finances', 'location', 'chronic', 'physical activity', 'food', 'mental'], 'is_food': True}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'domains': ['finances', 'location', 'productivity', 'sleep', 'physical activity', 'food', 'diabetes'], 'is_food': True}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'domains': ['sleep', 'physical activity', 'mental', 'social interactions'], 'is_food': False}]}}

exec(code, env_args)
