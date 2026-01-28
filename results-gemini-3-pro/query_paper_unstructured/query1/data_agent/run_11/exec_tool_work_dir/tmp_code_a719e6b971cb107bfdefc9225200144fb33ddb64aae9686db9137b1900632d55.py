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
# Debug list
found_papers = []

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '').strip()
    
    is_food = False
    text_lower = text.lower()
    
    # Check title
    if 'food' in title.lower():
        is_food = True
        found_papers.append((title, 'title'))
    else:
        # Check keywords
        # Regex: Keywords ... -> ...
        # pattern: (author\s+)?keywords\s*[:\n](.*?)(?:acm\s+classification|introduction|\n\s*\n)
        # We use simple string operations to avoid regex escaping hell in the tool call if possible, 
        # but regex is better. I will double escape.
        
        # pattern: keywords followed by colon or newline
        # matching up to "acm classification" or "introduction" or double newline
        
        # Using 4 backslashes for JSON to result in 2 backslashes in Python string for regex special chars? 
        # No, for \s in regex, I need \\s in Python string? No, r'\s' is fine. 
        # So \\s in JSON -> \s in Python.
        
        pattern = r"(?:author\s+)?keywords\s*[:\n](.*?)(?:acm\s+classification|introduction|\r?\n\s*\r?\n)"
        match = re.search(pattern, text_lower, re.DOTALL | re.IGNORECASE)
        
        if match:
            keywords = match.group(1)
            if 'food' in keywords:
                is_food = True
                found_papers.append((title, 'keywords'))
    
    if is_food:
        food_titles.append(title)

matched_citations = df_citations[df_citations['title'].isin(food_titles)]
total_citations = matched_citations['citation_count'].sum()

print(f"DEBUG: Found {len(food_titles)} papers. List: {found_papers}")
print("__RESULT__:")
print(json.dumps(int(total_citations)))"""

env_args = {'var_function-call-4029809345868206444': 'file_storage/function-call-4029809345868206444.json', 'var_function-call-4029809345868210059': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-17516763971225501651': 'file_storage/function-call-17516763971225501651.json', 'var_function-call-2430846317531582825': 'file_storage/function-call-2430846317531582825.json', 'var_function-call-2430846317531584718': 'file_storage/function-call-2430846317531584718.json'}

exec(code, env_args)
