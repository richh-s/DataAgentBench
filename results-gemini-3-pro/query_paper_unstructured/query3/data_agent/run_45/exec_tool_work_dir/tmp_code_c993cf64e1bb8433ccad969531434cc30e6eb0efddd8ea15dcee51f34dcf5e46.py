code = """import json
import re

with open(locals()['var_function-call-6342000761403970921'], 'r') as f:
    citations_data = json.load(f)

cit_titles = set()
for c in citations_data:
    cit_titles.add(c['title'])

with open(locals()['var_function-call-15772907393576741835'], 'r') as f:
    papers_data = json.load(f)

debug_info = {
    "total_papers": len(papers_data),
    "papers_with_empirical": 0,
    "papers_post_2016": 0,
    "matched_titles": 0,
    "sample_years": []
}

for i, p in enumerate(papers_data):
    filename = p['filename']
    title = filename.rsplit('.', 1)[0]
    text = p['text']
    
    # Check empirical
    has_empirical = 'empirical' in text.lower()
    if has_empirical:
        debug_info["papers_with_empirical"] += 1
    
    # Check year
    header = text[:1000]
    years = re.findall(r'\b(20[0-2][0-9])\b', header)
    pub_year = int(years[0]) if years else 0
    
    if pub_year > 2016:
        debug_info["papers_post_2016"] += 1
        
    if title in cit_titles:
        debug_info["matched_titles"] += 1
        
    if i < 10:
        debug_info["sample_years"].append({"title": title, "year": pub_year, "has_empirical": has_empirical})

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-11810081531988972241': ['paper_docs'], 'var_function-call-10291775221222249891': 'file_storage/function-call-10291775221222249891.json', 'var_function-call-15772907393576741835': 'file_storage/function-call-15772907393576741835.json', 'var_function-call-6342000761403970921': 'file_storage/function-call-6342000761403970921.json', 'var_function-call-809378135484135581': []}

exec(code, env_args)
