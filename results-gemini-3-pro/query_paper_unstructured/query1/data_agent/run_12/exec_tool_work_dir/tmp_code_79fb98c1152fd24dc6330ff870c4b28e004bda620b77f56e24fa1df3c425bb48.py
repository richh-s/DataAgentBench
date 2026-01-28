code = """import json
import re

file_path = locals()['var_function-call-17858895574398346247']
with open(file_path, 'r') as f:
    papers = json.load(f)

food_titles = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    if 'food' in title.lower():
        food_titles.append(title)
        continue
    
    # Search for keywords section
    # We look for "Author Keywords" followed by some text until "ACM Classification" or "Introduction"
    # We capture roughly 500 chars after "Author Keywords"
    
    lower_text = text.lower()
    start_idx = lower_text.find("author keywords")
    if start_idx == -1:
        start_idx = lower_text.find("keywords")
        # Ensure it's not in the middle of a sentence
        # Check if preceded by newline or start of file
        if start_idx > 0 and lower_text[start_idx-1] not in ['\n', '\r', ' ']:
             start_idx = -1
             
    if start_idx != -1:
        # Extract substring
        sub = lower_text[start_idx:start_idx+1000]
        # Find end of keywords
        end_idx = 1000
        for marker in ["introduction", "acm classification", "general terms", "abstract"]:
            m_idx = sub.find(marker)
            if m_idx != -1 and m_idx > 10: # ensure it's not the keyword itself
                end_idx = min(end_idx, m_idx)
        
        keywords = sub[:end_idx]
        if 'food' in keywords:
            food_titles.append(title)

print("__RESULT__:")
print(json.dumps(food_titles))"""

env_args = {'var_function-call-1852344882916152676': 'file_storage/function-call-1852344882916152676.json', 'var_function-call-1852344882916155297': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-17858895574398346247': 'file_storage/function-call-17858895574398346247.json'}

exec(code, env_args)
