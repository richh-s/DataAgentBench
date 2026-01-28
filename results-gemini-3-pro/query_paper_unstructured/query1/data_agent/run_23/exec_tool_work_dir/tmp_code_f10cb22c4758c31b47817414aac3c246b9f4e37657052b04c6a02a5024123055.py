code = """import json
import re

citations_file = locals()['var_function-call-15343742255672940442']
papers_file = locals()['var_function-call-15343742255672942069']

with open(citations_file, 'r') as f:
    citations = json.load(f)

with open(papers_file, 'r') as f:
    papers = json.load(f)

food_titles = set()
count_food_papers = 0

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Extract Author Keywords
    # Look for "Author Keywords" followed by text until "ACM Classification" or other section
    # Use regex
    keywords_match = re.search(r'Author Keywords\s*[\r\n]+(.*?)(?:\n\n|\r\n\r\n|ACM Classification)', text, re.IGNORECASE | re.DOTALL)
    
    is_food = False
    if keywords_match:
        keywords = keywords_match.group(1).lower()
        if 'food' in keywords:
            is_food = True
    else:
        # Fallback: check if "Index Terms" exists
        index_terms_match = re.search(r'Index Terms\s*[:\-]?\s*(.*?)(?:\n\n|\r\n\r\n)', text, re.IGNORECASE | re.DOTALL)
        if index_terms_match:
             keywords = index_terms_match.group(1).lower()
             if 'food' in keywords:
                 is_food = True
    
    if is_food:
        food_titles.add(title)
        count_food_papers += 1

total_citations = 0
for cit in citations:
    cit_title = cit.get('title')
    count = cit.get('citation_count')
    # Handle possible string format
    try:
        count = int(count)
    except:
        count = 0
        
    if cit_title in food_titles:
        total_citations += count

print("__RESULT__:")
print(json.dumps({"food_papers_count": count_food_papers, "total_citations": total_citations}))"""

env_args = {'var_function-call-9331785913232115953': 'file_storage/function-call-9331785913232115953.json', 'var_function-call-2738688620942147002': 'file_storage/function-call-2738688620942147002.json', 'var_function-call-2738688620942145205': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-15343742255672940442': 'file_storage/function-call-15343742255672940442.json', 'var_function-call-15343742255672942069': 'file_storage/function-call-15343742255672942069.json'}

exec(code, env_args)
