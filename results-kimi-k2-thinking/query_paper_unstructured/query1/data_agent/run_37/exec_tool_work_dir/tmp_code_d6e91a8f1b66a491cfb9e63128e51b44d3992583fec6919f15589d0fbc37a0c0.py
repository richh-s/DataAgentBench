code = """import json

# Read the paper documents from the file
paper_docs_file = locals()['var_functions.query_db:3']
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Read citations data from the file
citations_file = locals()['var_functions.query_db:8']
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Combined food patterns that indicate food domain (looking for primary focus)
import re

def is_food_paper(text, filename):
    text_lower = text.lower()
    filename_lower = filename.lower()
    
    # Check if filename contains food
    if 'food' in filename_lower:
        return True
    
    # More targeted patterns for actual food papers (not just papers that mention food)
    primary_food_patterns = [
        r'food\s+journal',  # food journal
        r'food\s+tracking',  # food tracking
        r'food\s+consumption',  # food consumption
        r'mobile\s+food',  # mobile food
        r'food\s+intake',  # food intake
        r'food\s+logging',  # food logging
        r'food\s+photo',  # food photo
        r'food\s+entry',  # food entry
    ]
    
    secondary_patterns = [
        r'eating\s+habits',
        r'calorie\s+counting',
        r'nutrition\s+tracking',
        r'weight\s+loss',  # often food-focused but not always
        r'diet\s+tracking',
        r'meal\s+logging',
        r'restaurant.*?food',
    ]
    
    # Check for primary patterns (strong indicator)
    for pattern in primary_food_patterns:
        if re.search(pattern, text_lower):
            return True
    
    # For secondary patterns, need at least 2+ mentions to be confident
    secondary_count = 0
    for pattern in secondary_patterns:
        matches = re.findall(pattern, text_lower)
        secondary_count += len(matches)
    
    # If we see 3+ secondary pattern matches, it's likely food-focused
    if secondary_count >= 3:
        return True
    
    return False

# Extract ALL food domain papers from the full database
all_food_papers = []
for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']
    
    title = filename.replace('.txt', '')
    
    if is_food_paper(text, filename):
        all_food_papers.append(title)

# Load the papers we already found from the food filename search
existing_food_papers = [
    "Barriers and Negative Nudges: Exploring Challenges in Food Journaling", 
    "Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness", 
    "Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers", 
    "Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture"
]

# Combine and deduplicate
combined_food_papers = list(set(all_food_papers + existing_food_papers))

# Now find all citations for these papers
citations_file = locals()['var_functions.query_db:8']
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Filter citations for food domain papers
food_citations = []
total_citations = 0

for citation in citations_data:
    title = citation['title']
    if title in combined_food_papers:
        count = int(citation['citation_count'])
        food_citations.append({
            'title': title,
            'citation_count': count,
            'citation_year': int(citation['citation_year'])
        })
        total_citations += count

# Group by paper
paper_totals = {}
for citation in food_citations:
    title = citation['title']
    count = citation['citation_count']
    if title not in paper_totals:
        paper_totals[title] = 0
    paper_totals[title] += count

print('__RESULT__:')
print(json.dumps({
    'total_citation_count': total_citations,
    'food_papers_count': len(combined_food_papers),
    'paper_breakdown': paper_totals,
    'all_food_papers': combined_food_papers
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:7': {'food_papers_count': 2, 'sample_food_papers': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems']}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'total_citation_count': 610, 'paper_breakdown': {'A Lived Informatics Model of Personal Informatics': 390, 'A Stage-based Model of Personal Informatics Systems': 220}, 'total_food_papers': 2}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'food_papers_count': 4, 'food_papers': ['Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture']}}

exec(code, env_args)
