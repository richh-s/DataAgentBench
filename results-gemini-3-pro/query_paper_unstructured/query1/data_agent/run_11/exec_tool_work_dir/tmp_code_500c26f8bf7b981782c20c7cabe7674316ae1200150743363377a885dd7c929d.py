code = """import json
import pandas as pd

# Load papers
with open(locals()['var_function-call-2430846317531582825'], 'r') as f:
    papers = json.load(f)

# Load citations
with open(locals()['var_function-call-2430846317531584718'], 'r') as f:
    citations = json.load(f)

df_citations = pd.DataFrame(citations)
df_citations['citation_count'] = df_citations['citation_count'].astype(int)

food_titles = []
debug_titles = []

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '').strip()
    
    is_food = False
    text_lower = text.lower()
    
    if 'food' in title.lower():
        is_food = True
    else:
        # heuristic extraction
        idx = text_lower.find('author keywords')
        if idx == -1:
            idx = text_lower.find('keywords')
            
        if idx != -1:
            # Look ahead for markers
            end_idx = idx + 300 # default
            
            # Find closest marker
            for marker in ['introduction', 'acm classification', 'general terms']:
                e = text_lower.find(marker, idx + 20)
                if e != -1 and e < end_idx:
                    end_idx = e
            
            keywords_text = text_lower[idx:end_idx]
            if 'food' in keywords_text:
                is_food = True
                debug_titles.append(title)
    
    if is_food:
        food_titles.append(title)

matched_citations = df_citations[df_citations['title'].isin(food_titles)]
total_citations = matched_citations['citation_count'].sum()

print(f"DEBUG: Found {len(food_titles)} papers. Titles: {debug_titles}")
print("__RESULT__:")
print(json.dumps(int(total_citations)))"""

env_args = {'var_function-call-4029809345868206444': 'file_storage/function-call-4029809345868206444.json', 'var_function-call-4029809345868210059': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-17516763971225501651': 'file_storage/function-call-17516763971225501651.json', 'var_function-call-2430846317531582825': 'file_storage/function-call-2430846317531582825.json', 'var_function-call-2430846317531584718': 'file_storage/function-call-2430846317531584718.json'}

exec(code, env_args)
