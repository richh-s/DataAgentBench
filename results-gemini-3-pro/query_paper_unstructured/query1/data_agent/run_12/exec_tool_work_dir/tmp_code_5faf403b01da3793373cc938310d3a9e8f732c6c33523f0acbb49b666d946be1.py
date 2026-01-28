code = """import json

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
        
    lower_text = text.lower()
    
    kw_idx = lower_text.find("author keywords")
    if kw_idx == -1:
        # Check for keywords preceded by newline
        kw_idx = lower_text.find(chr(10) + "keywords")
    
    if kw_idx != -1:
        snippet = lower_text[kw_idx:kw_idx+1000]
        # limit by introduction
        intro_idx = snippet.find("introduction")
        if intro_idx != -1:
            snippet = snippet[:intro_idx]
            
        acm_idx = snippet.find("acm classification")
        if acm_idx != -1:
            snippet = snippet[:acm_idx]
            
        if 'food' in snippet:
            food_titles.append(title)

print("__RESULT__:")
print(json.dumps(food_titles))"""

env_args = {'var_function-call-1852344882916152676': 'file_storage/function-call-1852344882916152676.json', 'var_function-call-1852344882916155297': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-17858895574398346247': 'file_storage/function-call-17858895574398346247.json'}

exec(code, env_args)
