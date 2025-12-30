code = """import json
import pandas as pd
import re

citations_path = locals()['var_function-call-12584433843491866400']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)
citations_df = pd.DataFrame(citations_data)
citations_df['citation_count'] = citations_df['citation_count'].astype(int)

papers_path = locals()['var_function-call-12584433843491866597']
with open(papers_path, 'r') as f:
    paper_docs = json.load(f)

def is_food_paper(doc):
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check title
    if 'food' in title.lower():
        return True, title
        
    # Check Keywords
    # Regex lookahead for various section headers
    # Using simple space matching to avoid literal newline issues in pattern
    pattern = r"Author Keywords(.*?)(?=ACM Classification|INTRODUCTION|General Terms|Index Terms)"
    match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
    if match:
        kw = match.group(1).lower()
        if 'food' in kw:
            return True, title
    
    return False, title

food_titles = []
for doc in paper_docs:
    is_food, title = is_food_paper(doc)
    if is_food:
        food_titles.append(title)

# Filter citations
# Citations title matches paper title
food_citations = citations_df[citations_df['title'].isin(food_titles)]

total_citations = food_citations['citation_count'].sum()

print("__RESULT__:")
print(json.dumps({
    "food_paper_count": len(food_titles),
    "total_citations": int(total_citations),
    "sample_titles": food_titles[:5]
}))"""

env_args = {'var_function-call-3783672913394696319': ['paper_docs'], 'var_function-call-3783672913394696700': ['Citations', 'sqlite_sequence'], 'var_function-call-272073867596597133': 'file_storage/function-call-272073867596597133.json', 'var_function-call-272073867596596742': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-9679994414761045024': 'file_storage/function-call-9679994414761045024.json', 'var_function-call-12584433843491866400': 'file_storage/function-call-12584433843491866400.json', 'var_function-call-12584433843491866597': 'file_storage/function-call-12584433843491866597.json', 'var_function-call-3836062097239578025': {'food_paper_count': 0, 'total_citations': 0, 'sample_titles': []}, 'var_function-call-1933883333484097501': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'keywords_found': 'Lived Informatics; Personal Informatics; Self-Tracking;  Lapsing; Physical Activity; Finances; Locat', 'is_food': False}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'keywords_found': 'Personal informatics, collection, reflection, model, barriers', 'is_food': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'keywords_found': 'Personalization; animation; emotion; engagement; empathy; self-reﬂection.', 'is_food': False}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'keywords_found': 'None', 'is_food': False}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'keywords_found': 'Wearable technology; dashboard; information visualization;  stroke rehabilitation; occupational ther', 'is_food': False}]}

exec(code, env_args)
