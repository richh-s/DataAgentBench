code = """import json

with open('file_storage/functions.query_db:2.json', 'r') as f:
    paper_docs = json.load(f)

with open('file_storage/functions.query_db:0.json', 'r') as f:
    citations = json.load(f)

import re

# Extract domains from paper text by looking for domain mentions
def extract_domains_from_text(text):
    """Extract domains from paper text"""
    text_lower = text.lower()
    domains = set()
    
    # Look for domain mentions in context
    # Pattern 1: Direct mention in abstract/introduction
    if 'food' in text_lower:
        domains.add('food')
    if 'physical activity' in text_lower or 'fitness' in text_lower or 'exercise' in text_lower:
        domains.add('physical activity')
    if 'sleep' in text_lower:
        domains.add('sleep')
    if 'mental' in text_lower or 'mood' in text_lower:
        domains.add('mental')
    if 'finances' in text_lower or 'financial' in text_lower or 'money' in text_lower:
        domains.add('finances')
    if 'location' in text_lower:
        domains.add('location')
        
    # Pattern 2: Look for phrases like "trackers of X, Y, and Z"
    tracker_pattern = r'trackers of ([^,.]+)(?:, ([^,.]+))?(?:,? and ([^,.]+))?'
    matches = re.findall(tracker_pattern, text_lower)
    for match in matches:
        for domain in match:
            if domain and domain.strip():
                domains.add(domain.strip())
    
    # Pattern 3: Look for "tracking [domain]" patterns
    tracking_pattern = r'tracking ([a-zA-Z]+(?: [a-zA-Z]+)?)'
    matches = re.findall(tracking_pattern, text_lower)
    for domain in matches:
        if domain in ['food', 'sleep', 'location', 'weight', 'finances', 'physical activity', 'mental']:
            domains.add(domain)
    
    return list(domains)

# Process all papers
papers_with_domains = []
for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    domains = extract_domains_from_text(doc['text'])
    papers_with_domains.append({
        'title': title,
        'domains': domains,
        'is_food': 'food' in domains
    })

# Count citations by title
citations_by_title = {}
for citation in citations:
    title = citation['title']
    citations_by_title[title] = citations_by_title.get(title, 0) + int(citation['citation_count'])

# Calculate total citations for food domain papers
food_papers = []
total_food_citations = 0
food_paper_count = 0

for paper in papers_with_domains:
    if paper['is_food']:
        food_paper_count += 1
        title = paper['title']
        paper_citations = citations_by_title.get(title, 0)
        total_food_citations += paper_citations
        food_papers.append({
            'title': title,
            'domains': paper['domains'],
            'citations': paper_citations
        })

result = {
    'total_food_domain_papers': food_paper_count,
    'total_citation_count': total_food_citations,
    'papers': food_papers
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'path_type': "<class 'str'>", 'path_value': 'file_storage/functions.query_db:2.json'}, 'var_functions.execute_python:8': {'paper_docs_count': 5, 'citations_count': 1405}, 'var_functions.execute_python:12': {'food_papers_found': 5, 'food_papers_with_citations': 5, 'total_citation_count': 1593, 'papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'total_citations': 390}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'total_citations': 220}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': 265}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': 266}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'total_citations': 452}]}, 'var_functions.execute_python:14': {'paper_count': 5, 'first_paper_preview': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characterize  the  integration  of  self-tracking \ninto  everyday  life  by  people  with  varying  goals.  We  build \nupon  prior  work  by  embracing  the  perspective  of  lived \ninformatics to propose a new model of personal informatics. \nWe examine how lived informatics manifests in the habits of \nself-trackers across a variety of domains, first by surveying \n105, 99, and 83 past and present trackers of physical activity, \nfinances, and location and then by interviewing 22 trackers \nregarding their li"}, 'var_functions.execute_python:18': {'food_domain_papers': 3, 'total_citation_count': 876, 'papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'citations': 390}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'citations': 220}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citations': 266}]}}

exec(code, env_args)
