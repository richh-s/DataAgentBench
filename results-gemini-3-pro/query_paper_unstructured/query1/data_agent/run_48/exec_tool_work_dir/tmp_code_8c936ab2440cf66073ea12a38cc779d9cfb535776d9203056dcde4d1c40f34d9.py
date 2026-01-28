code = """import json
import re
import pandas as pd

# Load citations
with open(locals()['var_function-call-9265765399726123142'], 'r') as f:
    citations = json.load(f)

# Load papers
with open(locals()['var_function-call-5716238485520989105'], 'r') as f:
    papers = json.load(f)

food_titles = set()

for p in papers:
    text = p.get('text', '')
    title = p.get('filename', '').replace('.txt', '')
    
    # Check title
    if 'food' in title.lower():
        food_titles.add(title)
        continue
    
    # Check keywords
    match = re.search(r'Author Keywords\s*(.*?)\s*(?:ACM Classification|INTRODUCTION|General Terms)', text, re.IGNORECASE | re.DOTALL)
    if match:
        keywords = match.group(1).lower()
        if 'food' in keywords:
            food_titles.add(title)

# Filter citations
df_citations = pd.DataFrame(citations)
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'])

# Filter by title
food_citations = df_citations[df_citations['title'].isin(food_titles)]

# Calculate sum
total_citations = food_citations['citation_count'].sum()

print("__RESULT__:")
print(json.dumps({
    "count": int(total_citations),
    "paper_titles": list(food_titles)
}))"""

env_args = {'var_function-call-13370766090165900916': 'file_storage/function-call-13370766090165900916.json', 'var_function-call-9130405135784485262': 'file_storage/function-call-9130405135784485262.json', 'var_function-call-9265765399726123142': 'file_storage/function-call-9265765399726123142.json', 'var_function-call-4672195044827894195': 'file_storage/function-call-4672195044827894195.json', 'var_function-call-6440888066773927974': 876, 'var_function-call-1546429934820446288': {'count': 0, 'titles': []}, 'var_function-call-16718756574261419614': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'], 'var_function-call-3823720206295430091': {'total_papers': 5, 'hits': {'A Lived Informatics Model of Personal Informatics.txt': ['food', 'eating'], 'A Stage-based Model of Personal Informatics Systems.txt': ['food', 'eating'], 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt': ['eating'], 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt': ['food', 'diet'], 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt': ['eating', 'diet']}}, 'var_function-call-5716238485520989105': 'file_storage/function-call-5716238485520989105.json', 'var_function-call-15081243156642599412': {'total_papers': 99, 'text_hits_count': 58, 'keyword_hits_count': 7, 'keyword_hits_titles': ['Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats', "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps", 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'TastyBeats: Designing Palatable Representations of Physical Activity', 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating']}}

exec(code, env_args)
