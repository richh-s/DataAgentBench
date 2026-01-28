code = """import json

with open(locals()['var_function-call-10209984453905821604'], 'r') as f:
    paper_docs = json.load(f)

with open(locals()['var_function-call-10209984453905818035'], 'r') as f:
    citations = json.load(f)

food_titles = set()

for doc in paper_docs:
    text = doc['text']
    title = doc['filename'].replace('.txt', '')
    
    # Check title
    if 'food' in title.lower():
        food_titles.add(title)
        continue
    
    # Check Keywords in first 5000 chars
    head = text[:5000]
    
    found_kw = False
    for kw_header in ["Author Keywords", "Keywords", "Index Terms"]:
        if kw_header in head:
            idx = head.find(kw_header)
            # Extract roughly the line or block
            # Assume keywords are within the next 500 chars
            snippet = head[idx:idx+500]
            # Check for 'food'
            if 'food' in snippet.lower():
                food_titles.add(title)
                found_kw = True
                break
    
    # If not found in keywords, check abstract specifically? 
    # Or just check if "food" appears in the text frequently?
    # Let's stick to keywords + title as primary. 
    # But let's check if we missed any obvious ones by printing a debug if 'food' is in text but not classified.
    if not found_kw and 'food' in text.lower():
        # Heuristic: if 'food' appears in the first 1000 chars (Introduction/Abstract) it might be relevant
        if 'food' in head.lower()[:1000]:
             # We might want to include it? 
             # For now, let's just log it in the result to see.
             pass

total_citations = 0
for cit in citations:
    if cit['title'] in food_titles:
        total_citations += int(cit['citation_count'])

print("__RESULT__:")
print(json.dumps({"total_citations": total_citations, "food_papers": list(food_titles)}))"""

env_args = {'var_function-call-15020890105501723075': ['paper_docs'], 'var_function-call-15020890105501724646': ['Citations', 'sqlite_sequence'], 'var_function-call-10118985144780459012': 'file_storage/function-call-10118985144780459012.json', 'var_function-call-10118985144780458999': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-10209984453905821604': 'file_storage/function-call-10209984453905821604.json', 'var_function-call-10209984453905818035': 'file_storage/function-call-10209984453905818035.json'}

exec(code, env_args)
