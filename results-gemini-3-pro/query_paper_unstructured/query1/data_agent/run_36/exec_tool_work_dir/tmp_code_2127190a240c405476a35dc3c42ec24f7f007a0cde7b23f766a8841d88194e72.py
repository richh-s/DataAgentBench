code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-13014987171249504047'], 'r') as f:
    papers = json.load(f)

with open(locals()['var_function-call-13014987171249501074'], 'r') as f:
    citations = json.load(f)

# Convert citations to DataFrame
df_citations = pd.DataFrame(citations)
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'])

food_papers = []

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    text_lower = text.lower()
    
    # Check for keywords sections
    keyword_indices = [m.start() for m in re.finditer(r'(author\s+)?keywords|index\s+terms', text_lower)]
    
    is_food = False
    if keyword_indices:
        for idx in keyword_indices:
            # extract next 1000 chars to be safe, but stop at next section if possible
            # Just taking 500 chars is a good heuristic for keywords block
            snippet = text_lower[idx:idx+500]
            if 'food' in snippet:
                is_food = True
                break
    
    if is_food:
        food_papers.append(title)

# Filter citations
food_citations = df_citations[df_citations['title'].isin(food_papers)]
total_citations = int(food_citations['citation_count'].sum())

print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_function-call-11340871341150089119': ['paper_docs'], 'var_function-call-11340871341150087996': ['Citations', 'sqlite_sequence'], 'var_function-call-6885705562055430499': 'file_storage/function-call-6885705562055430499.json', 'var_function-call-6885705562055430382': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-2249233586870449944': 'file_storage/function-call-2249233586870449944.json', 'var_function-call-13014987171249504047': 'file_storage/function-call-13014987171249504047.json', 'var_function-call-13014987171249501074': 'file_storage/function-call-13014987171249501074.json'}

exec(code, env_args)
