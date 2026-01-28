code = """import json

with open('file_storage/functions.query_db:2.json', 'r') as f:
    paper_docs = json.load(f)

with open('file_storage/functions.query_db:0.json', 'r') as f:
    citations = json.load(f)

def is_food_paper(text):
    text_lower = text.lower()
    
    # Count food-related keywords
    food_terms = ['food', 'eating', 'nutrition', 'diet', 'meal', 'calorie', 'dietary', 'nutrition']
    food_count = sum(text_lower.count(term) for term in food_terms)
    
    # If food keywords appear multiple times, likely a food paper
    if food_count >= 3:
        return True
    
    # Also check if it is one of the papers we know discusses food
    if 'food journal' in text_lower or 'food' in text_lower:
        return True
    
    return False

def contains_food_domain(text):
    text_lower = text.lower()
    return 'food' in text_lower

food_papers = []
for doc in paper_docs:
    if contains_food_domain(doc['text']):
        title = doc['filename'].replace('.txt', '')
        food_papers.append(title)

citations_by_title = {}
for citation in citations:
    title = citation['title']
    if title not in citations_by_title:
        citations_by_title[title] = 0
    citations_by_title[title] += int(citation['citation_count'])

total_citations = 0
food_paper_list = []

for paper_title in food_papers:
    if paper_title in citations_by_title:
        paper_cites = citations_by_title[paper_title]
        total_citations += paper_cites
        food_paper_list.append({
            'title': paper_title,
            'citations': paper_cites
        })

result = {
    'food_domain_papers': len(food_papers),
    'total_citation_count': total_citations,
    'papers': food_paper_list
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'path_type': "<class 'str'>", 'path_value': 'file_storage/functions.query_db:2.json'}, 'var_functions.execute_python:8': {'paper_docs_count': 5, 'citations_count': 1405}, 'var_functions.execute_python:12': {'food_papers_found': 5, 'food_papers_with_citations': 5, 'total_citation_count': 1593, 'papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'total_citations': 390}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'total_citations': 220}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': 265}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': 266}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'total_citations': 452}]}, 'var_functions.execute_python:14': {'paper_count': 5, 'first_paper_preview': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characterize  the  integration  of  self-tracking \ninto  everyday  life  by  people  with  varying  goals.  We  build \nupon  prior  work  by  embracing  the  perspective  of  lived \ninformatics to propose a new model of personal informatics. \nWe examine how lived informatics manifests in the habits of \nself-trackers across a variety of domains, first by surveying \n105, 99, and 83 past and present trackers of physical activity, \nfinances, and location and then by interviewing 22 trackers \nregarding their li"}}

exec(code, env_args)
