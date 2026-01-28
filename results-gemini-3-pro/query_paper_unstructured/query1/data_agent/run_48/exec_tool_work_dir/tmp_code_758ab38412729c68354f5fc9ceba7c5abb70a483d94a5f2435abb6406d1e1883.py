code = """import json
import re

# Load citations (using previous key, it was full table)
with open(locals()['var_function-call-9265765399726123142'], 'r') as f:
    citations = json.load(f)

# Load papers (new key)
with open(locals()['var_function-call-5716238485520989105'], 'r') as f:
    papers = json.load(f)

text_hits = []
keyword_hits = []

for p in papers:
    text = p.get('text', '')
    title = p.get('filename', '').replace('.txt', '')
    
    # Check text
    if 'food' in text.lower():
        text_hits.append(title)
        
    # Check keywords
    # Regex to find Author Keywords block
    match = re.search(r'Author Keywords\s*(.*?)\s*(?:ACM Classification|INTRODUCTION|General Terms)', text, re.IGNORECASE | re.DOTALL)
    if match:
        keywords = match.group(1).lower()
        if 'food' in keywords:
            keyword_hits.append(title)

print("__RESULT__:")
print(json.dumps({
    "total_papers": len(papers),
    "text_hits_count": len(text_hits),
    "keyword_hits_count": len(keyword_hits),
    "keyword_hits_titles": keyword_hits
}))"""

env_args = {'var_function-call-13370766090165900916': 'file_storage/function-call-13370766090165900916.json', 'var_function-call-9130405135784485262': 'file_storage/function-call-9130405135784485262.json', 'var_function-call-9265765399726123142': 'file_storage/function-call-9265765399726123142.json', 'var_function-call-4672195044827894195': 'file_storage/function-call-4672195044827894195.json', 'var_function-call-6440888066773927974': 876, 'var_function-call-1546429934820446288': {'count': 0, 'titles': []}, 'var_function-call-16718756574261419614': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'], 'var_function-call-3823720206295430091': {'total_papers': 5, 'hits': {'A Lived Informatics Model of Personal Informatics.txt': ['food', 'eating'], 'A Stage-based Model of Personal Informatics Systems.txt': ['food', 'eating'], 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt': ['eating'], 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt': ['food', 'diet'], 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt': ['eating', 'diet']}}, 'var_function-call-5716238485520989105': 'file_storage/function-call-5716238485520989105.json'}

exec(code, env_args)
