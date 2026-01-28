code = """import json

with open(locals()['var_function-call-8131891965155681043'], 'r') as f:
    paper_docs = json.load(f)

results = []
newline = chr(10)

for paper in paper_docs[:20]: # Check first 20 papers
    filename = paper.get('filename', '')
    text = paper.get('text', '').lower()
    
    if 'food' in text:
        # Find context
        idx = text.find('food')
        context = text[max(0, idx-50):min(len(text), idx+50)].replace(newline, ' ')
        results.append({"title": filename, "context": context})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-8528399130518209876': ['paper_docs'], 'var_function-call-8528399130518209403': ['Citations', 'sqlite_sequence'], 'var_function-call-5911009850598284906': 'file_storage/function-call-5911009850598284906.json', 'var_function-call-5911009850598284323': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-8131891965155681043': 'file_storage/function-call-8131891965155681043.json', 'var_function-call-9545123832461402324': 'file_storage/function-call-9545123832461402324.json', 'var_function-call-16177678008665017919': {'food_papers_count': 0, 'food_papers_titles': [], 'total_citations': 0}}

exec(code, env_args)
