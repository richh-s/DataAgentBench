code = """import json

with open(locals()['var_function-call-17235522576117083875'], 'r') as f:
    papers = json.load(f)

food_in_text_count = 0
examples = []

for p in papers:
    text = p.get('text', '').lower()
    if 'food' in text:
        food_in_text_count += 1
        # extract a snippet around "food"
        idx = text.find('food')
        snippet = text[max(0, idx-50):min(len(text), idx+50)]
        
        # extract keywords section if possible to debug
        kwd_idx = text.find('keywords')
        kwd_snippet = ""
        if kwd_idx != -1:
            kwd_snippet = text[kwd_idx:kwd_idx+200]
        
        if len(examples) < 5:
            examples.append({
                "title": p.get('filename'),
                "food_snippet": snippet,
                "keywords_snippet": kwd_snippet
            })

print("__RESULT__:")
print(json.dumps({
    "count_food_in_text": food_in_text_count,
    "examples": examples
}))"""

env_args = {'var_function-call-5786904885440834537': 'file_storage/function-call-5786904885440834537.json', 'var_function-call-5786904885440834028': ['Citations', 'sqlite_sequence'], 'var_function-call-17235522576117083875': 'file_storage/function-call-17235522576117083875.json', 'var_function-call-17235522576117081446': 'file_storage/function-call-17235522576117081446.json', 'var_function-call-10431991474880319321': {'food_paper_count': 0, 'total_citations': 0, 'matched_citation_records': 0, 'sample_food_titles': []}}

exec(code, env_args)
