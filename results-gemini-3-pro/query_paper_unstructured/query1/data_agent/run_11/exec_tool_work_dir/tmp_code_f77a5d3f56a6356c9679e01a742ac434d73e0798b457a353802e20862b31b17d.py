code = """import json
import pandas as pd
import re

# Load papers
with open(locals()['var_function-call-2430846317531582825'], 'r') as f:
    papers = json.load(f)

# Load citations
with open(locals()['var_function-call-2430846317531584718'], 'r') as f:
    citations = json.load(f)

df_citations = pd.DataFrame(citations)
df_citations['citation_count'] = df_citations['citation_count'].astype(int)

food_titles = []
debug_info = []

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '').strip()
    
    is_food = False
    text_lower = text.lower()
    
    # Check title
    if 'food' in title.lower():
        is_food = True
        debug_info.append(f"Found via title: {title}")
    else:
        # Check keywords
        # Regex to find keywords section. 
        # Look for "Author Keywords" or just "Keywords", followed by text, ending at "ACM Classification", "Introduction", or multiple newlines.
        # Note: pattern should be non-greedy for the content.
        match = re.search(r'(?:author\s+)?keywords\s*[:\n](.*?)(?:acm\s+classification|introduction|\n\s*\n)', text_lower, re.DOTALL | re.IGNORECASE)
        if match:
            keywords = match.group(1)
            if 'food' in keywords:
                is_food = True
                debug_info.append(f"Found via keywords: {title} | KW: {keywords[:50]}...")
        else:
             # Fallback: check Abstract? 
             # If "food" is mentioned in Abstract, it might be relevant. 
             # But "food" is a common word.
             # Let's stick to keywords/title as primary indicators for "domain".
             pass
    
    if is_food:
        food_titles.append(title)

# Filter citations
# Ensure titles match
# df_citations['title'] match food_titles
matched_citations = df_citations[df_citations['title'].isin(food_titles)]
total_citations = matched_citations['citation_count'].sum()

print(f"Debug: Found {len(food_titles)} papers in food domain.")
print(f"Debug: Titles: {food_titles}")

print("__RESULT__:")
print(json.dumps(int(total_citations)))"""

env_args = {'var_function-call-4029809345868206444': 'file_storage/function-call-4029809345868206444.json', 'var_function-call-4029809345868210059': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-17516763971225501651': 'file_storage/function-call-17516763971225501651.json', 'var_function-call-2430846317531582825': 'file_storage/function-call-2430846317531582825.json', 'var_function-call-2430846317531584718': 'file_storage/function-call-2430846317531584718.json'}

exec(code, env_args)
