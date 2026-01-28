code = """import json

citations_file = locals()['var_function-call-15343742255672940442']
papers_file = locals()['var_function-call-15343742255672942069']

with open(citations_file, 'r') as f:
    citations = json.load(f)

with open(papers_file, 'r') as f:
    papers = json.load(f)

food_titles = set()
count_food_papers = 0
found_titles = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    text_lower = text.lower()
    
    # robust keyword extraction
    keyword_start = text_lower.find('author keywords')
    if keyword_start == -1:
        keyword_start = text_lower.find('index terms')
    
    is_food = False
    if keyword_start != -1:
        # Take a chunk after the keywords header
        snippet = text_lower[keyword_start:keyword_start+1000] 
        # Stop at the next major section if possible to avoid reading too much
        # Common next sections: "introduction", "acm classification", "abstract" (unlikely after), "categories and subject descriptors"
        end_markers = ['introduction', 'acm classification', 'categories and subject descriptors', 'general terms']
        min_end = 1000
        for marker in end_markers:
            idx = snippet.find(marker)
            if idx != -1 and idx < min_end:
                min_end = idx
        
        keywords_text = snippet[:min_end]
        
        if 'food' in keywords_text:
            is_food = True
    
    if is_food:
        food_titles.add(title)
        found_titles.append(title)
        count_food_papers += 1

total_citations = 0
for cit in citations:
    cit_title = cit.get('title')
    count = cit.get('citation_count')
    try:
        count = int(count)
    except:
        count = 0
        
    if cit_title in food_titles:
        total_citations += count

print("__RESULT__:")
print(json.dumps({"food_papers_count": count_food_papers, "food_paper_titles": found_titles, "total_citations": total_citations}))"""

env_args = {'var_function-call-9331785913232115953': 'file_storage/function-call-9331785913232115953.json', 'var_function-call-2738688620942147002': 'file_storage/function-call-2738688620942147002.json', 'var_function-call-2738688620942145205': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-15343742255672940442': 'file_storage/function-call-15343742255672940442.json', 'var_function-call-15343742255672942069': 'file_storage/function-call-15343742255672942069.json'}

exec(code, env_args)
