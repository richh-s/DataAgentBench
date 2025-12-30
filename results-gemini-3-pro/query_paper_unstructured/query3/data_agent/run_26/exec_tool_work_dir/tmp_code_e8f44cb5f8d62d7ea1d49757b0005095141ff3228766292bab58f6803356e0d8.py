code = """import json
import re

with open(locals()['var_function-call-1844431421063330575'], 'r') as f:
    paper_docs = json.load(f)

def extract_year(text):
    head = text[:3000]
    years = re.findall(r'\b(20[0-2][0-9])\b', head)
    if years:
        return int(years[0])
    return None

def check_contribution(text):
    return "empirical" in text.lower()

debug_data = []
for doc in paper_docs[:20]:
    title = doc.get('filename', '').replace('.txt', '')
    text = doc.get('text', '')
    year = extract_year(text)
    has_empirical = check_contribution(text)
    debug_data.append({"title": title, "year": year, "has_empirical": has_empirical})

print("__RESULT__:")
print(json.dumps(debug_data))"""

env_args = {'var_function-call-14741953591797828167': ['paper_docs'], 'var_function-call-14741953591797829382': ['Citations', 'sqlite_sequence'], 'var_function-call-2114113704500066494': 'file_storage/function-call-2114113704500066494.json', 'var_function-call-2114113704500064987': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-1844431421063330575': 'file_storage/function-call-1844431421063330575.json', 'var_function-call-11864637065263499194': 'file_storage/function-call-11864637065263499194.json', 'var_function-call-3352296089699517802': []}

exec(code, env_args)
