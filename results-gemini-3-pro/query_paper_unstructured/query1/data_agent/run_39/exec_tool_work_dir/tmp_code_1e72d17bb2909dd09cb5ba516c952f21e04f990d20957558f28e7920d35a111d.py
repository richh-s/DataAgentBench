code = """import json
import re

# Load paper_docs
with open(locals()['var_function-call-8131891965155681043'], 'r') as f:
    paper_docs = json.load(f)

# Load citations
with open(locals()['var_function-call-9545123832461402324'], 'r') as f:
    citations = json.load(f)

food_papers = []

for paper in paper_docs:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    text = paper.get('text', '')
    
    # Check title
    if 'food' in title.lower():
        food_papers.append(title)
        continue
    
    # Check keywords
    # Regex for keywords section
    # Using explicit newlines and double backslashes for JSON compatibility
    pattern = r"(?:Author Keywords|Index Terms|Keywords)\s*[:\n]\s*(.*?)(?:\n\n|\Z)"
    keywords_match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
    
    if keywords_match:
        keywords = keywords_match.group(1).lower()
        if 'food' in keywords:
            food_papers.append(title)
            continue
            
    # Check abstract
    pattern_abstract = r"ABSTRACT\s*\n(.*?)(?:\n\n|INTRODUCTION)"
    abstract_match = re.search(pattern_abstract, text, re.IGNORECASE | re.DOTALL)
    
    if abstract_match:
        abstract = abstract_match.group(1).lower()
        if 'food' in abstract:
             food_papers.append(title)
             continue

# Filter citations
total_citations = 0
food_papers_set = set(food_papers)

for cit in citations:
    if cit['title'] in food_papers_set:
        try:
            total_citations += int(cit['citation_count'])
        except:
            pass

print("__RESULT__:")
print(json.dumps({"food_papers_count": len(food_papers), "food_papers_titles": food_papers, "total_citations": total_citations}))"""

env_args = {'var_function-call-8528399130518209876': ['paper_docs'], 'var_function-call-8528399130518209403': ['Citations', 'sqlite_sequence'], 'var_function-call-5911009850598284906': 'file_storage/function-call-5911009850598284906.json', 'var_function-call-5911009850598284323': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-8131891965155681043': 'file_storage/function-call-8131891965155681043.json', 'var_function-call-9545123832461402324': 'file_storage/function-call-9545123832461402324.json'}

exec(code, env_args)
