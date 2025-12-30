code = """import json

papers_path = locals()['var_function-call-15077613833019679981']
with open(papers_path, 'r') as f:
    papers = json.load(f)

results = []
count = 0
for p in papers:
    text_lower = p['text'].lower()
    if "food" in text_lower:
        idx = text_lower.find("food")
        snippet = p['text'][max(0, idx-50):min(len(p['text']), idx+50)]
        
        # Try to find keywords
        kw_idx = text_lower.find("author keywords")
        kw_snippet = ""
        if kw_idx != -1:
            kw_snippet = p['text'][kw_idx:kw_idx+200]
            
        results.append({
            "title": p['filename'],
            "context": snippet,
            "keywords": kw_snippet
        })
        count += 1
        if count >= 5: break

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-14405582414403684106': ['paper_docs'], 'var_function-call-14405582414403686195': ['Citations', 'sqlite_sequence'], 'var_function-call-1273577479453038261': 'file_storage/function-call-1273577479453038261.json', 'var_function-call-1273577479453039900': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-15077613833019679981': 'file_storage/function-call-15077613833019679981.json', 'var_function-call-15077613833019680274': 'file_storage/function-call-15077613833019680274.json', 'var_function-call-3637328086309733464': 0}

exec(code, env_args)
