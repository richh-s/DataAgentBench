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
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    title = filename.replace('.txt', '')
    
    if 'food' in title.lower():
        return True, title
        
    # Regex to find Author Keywords
    # using single quotes for the pattern
    pattern = r'Author Keywords[\s\S]*?(?=ACM Classification|INTRODUCTION|General Terms)'
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        keywords = match.group(0).lower()
        if 'food' in keywords:
            return True, title
            
    return False, title

food_titles = []
for doc in paper_docs:
    is_food, title = is_food_paper(doc)
    if is_food:
        food_titles.append(title)

food_citations = citations_df[citations_df['title'].isin(food_titles)]
total_citations = food_citations['citation_count'].sum()

print("__RESULT__:")
print(json.dumps({
    "food_paper_count": len(food_titles),
    "total_citations": int(total_citations),
    "sample_titles": food_titles[:5]
}))"""

env_args = {'var_function-call-3783672913394696319': ['paper_docs'], 'var_function-call-3783672913394696700': ['Citations', 'sqlite_sequence'], 'var_function-call-272073867596597133': 'file_storage/function-call-272073867596597133.json', 'var_function-call-272073867596596742': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-9679994414761045024': 'file_storage/function-call-9679994414761045024.json', 'var_function-call-12584433843491866400': 'file_storage/function-call-12584433843491866400.json', 'var_function-call-12584433843491866597': 'file_storage/function-call-12584433843491866597.json'}

exec(code, env_args)
