code = """import json
import re

with open(locals()['var_function-call-13014987171249504047'], 'r') as f:
    papers = json.load(f)

debug_info = []

for p in papers:
    text = p.get('text', '')
    title = p.get('filename', '')
    text_lower = text.lower()
    
    if 'food' in text_lower:
        # Check my regex
        keyword_indices = [m.start() for m in re.finditer(r'(author\s+)?keywords|index\s+terms', text_lower)]
        snippets = []
        for idx in keyword_indices:
            snippets.append(text_lower[idx:idx+200]) # shorter snippet for view
        
        debug_info.append({
            "title": title,
            "has_food_in_text": True,
            "keyword_matches": len(keyword_indices),
            "snippets": snippets
        })
        if len(debug_info) >= 5:
            break

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-11340871341150089119': ['paper_docs'], 'var_function-call-11340871341150087996': ['Citations', 'sqlite_sequence'], 'var_function-call-6885705562055430499': 'file_storage/function-call-6885705562055430499.json', 'var_function-call-6885705562055430382': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-2249233586870449944': 'file_storage/function-call-2249233586870449944.json', 'var_function-call-13014987171249504047': 'file_storage/function-call-13014987171249504047.json', 'var_function-call-13014987171249501074': 'file_storage/function-call-13014987171249501074.json', 'var_function-call-1951529117087221933': 0}

exec(code, env_args)
