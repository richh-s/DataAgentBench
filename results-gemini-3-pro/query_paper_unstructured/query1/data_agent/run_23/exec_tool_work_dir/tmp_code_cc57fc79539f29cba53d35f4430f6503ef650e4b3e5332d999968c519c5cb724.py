code = """import json

papers_file = locals()['var_function-call-15343742255672942069']

with open(papers_file, 'r') as f:
    papers = json.load(f)

debug_info = []

for i, paper in enumerate(papers[:5]):
    text = paper.get('text', '')
    text_lower = text.lower()
    
    keyword_start = text_lower.find('author keywords')
    snippet = ""
    if keyword_start != -1:
        snippet = text[keyword_start:keyword_start+200]
    
    debug_info.append({
        "title": paper.get('filename'),
        "has_food_in_text": "food" in text_lower,
        "keyword_snippet": snippet
    })

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-9331785913232115953': 'file_storage/function-call-9331785913232115953.json', 'var_function-call-2738688620942147002': 'file_storage/function-call-2738688620942147002.json', 'var_function-call-2738688620942145205': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-15343742255672940442': 'file_storage/function-call-15343742255672940442.json', 'var_function-call-15343742255672942069': 'file_storage/function-call-15343742255672942069.json', 'var_function-call-1326459099851093110': {'food_papers_count': 0, 'food_paper_titles': [], 'total_citations': 0}}

exec(code, env_args)
