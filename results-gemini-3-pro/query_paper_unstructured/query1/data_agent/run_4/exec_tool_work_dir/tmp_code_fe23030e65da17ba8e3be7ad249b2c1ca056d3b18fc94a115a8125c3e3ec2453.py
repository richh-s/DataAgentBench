code = """import json
import pandas as pd
import re

with open(locals()['var_function-call-1057251804069707820'], 'r') as f:
    papers = json.load(f)
with open(locals()['var_function-call-6501009897595543018'], 'r') as f:
    citations = json.load(f)

df_citations = pd.DataFrame(citations)
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'])

def is_food_domain(row):
    filename = row.get('filename', '')
    text = row.get('text', '')
    if not text:
        return False
    
    title = filename.replace('.txt', '')
    text_lower = text.lower()
    
    # 1. Check Title
    if 'food' in title.lower():
        return True
    
    # 2. Check Keywords
    # Regex to find "Author Keywords" or "Keywords" or "CCS Concepts" etc.
    # We look for the word "keywords" and check the context.
    keyword_matches = list(re.finditer(r'keywords', text_lower))
    for m in keyword_matches:
        start = m.start()
        # Check window of 500 chars
        window = text_lower[start:start+500]
        if 'food' in window:
            return True
            
    # 3. Check Abstract
    # Find "ABSTRACT"
    abstract_match = re.search(r'abstract', text_lower)
    if abstract_match:
        start = abstract_match.end()
        # Abstract is usually before Introduction.
        intro_match = re.search(r'introduction', text_lower[start:])
        end = start + intro_match.start() if intro_match else start + 2000
        abstract_text = text_lower[start:end]
        
        # Check if "food" appears in abstract
        # Be careful of "food for thought" etc. but for this domain it's likely "food consumption", "food waste", etc.
        # But wait, looking at the sample paper, "food [11]" was in Introduction.
        # The prompt says: "Common domains include: 'food'... Fields like domain ... may contain multiple values".
        # This implies it's a classification task.
        # If I can't find it in Keywords or Title, should I trust Abstract?
        # Let's trust Keywords and Title first.
        # If I add Abstract, I might get false positives.
        pass

    return False

food_papers = []
for p in papers:
    if is_food_domain(p):
        title = p['filename'].replace('.txt', '')
        food_papers.append(title)

# Filter citations
food_citations = df_citations[df_citations['title'].isin(food_papers)]
total_citations = food_citations['citation_count'].sum()

print("__RESULT__:")
print(json.dumps({"total_citations": int(total_citations), "food_paper_titles": food_papers, "count_papers": len(papers)}))"""

env_args = {'var_function-call-4282369109293305518': ['paper_docs'], 'var_function-call-17210862545939823160': 'file_storage/function-call-17210862545939823160.json', 'var_function-call-6501009897595543018': 'file_storage/function-call-6501009897595543018.json', 'var_function-call-343981584432704958': 'file_storage/function-call-343981584432704958.json', 'var_function-call-17966795539395450339': 0, 'var_function-call-17399558695385330668': {'total_papers': 5, 'total_citations': 1405, 'sample_citation_titles': ['Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'], 'sample_paper_filenames': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'], 'food_in_title': [], 'food_in_keywords': []}, 'var_function-call-12410144699501629173': 'file_storage/function-call-12410144699501629173.json', 'var_function-call-1057251804069707820': 'file_storage/function-call-1057251804069707820.json'}

exec(code, env_args)
