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
    # Try to find "Author Keywords" or "Keywords" block
    # Regex to capture text after "Author Keywords" until next double newline
    keywords_match = re.search(r'(?:Author Keywords|Index Terms|Keywords)\s*[:\n]\s*(.*?)(?:\n\n|\Z)', text, re.IGNORECASE | re.DOTALL)
    if keywords_match:
        keywords = keywords_match.group(1).lower()
        if 'food' in keywords:
            food_papers.append(title)
            continue
            
    # Check abstract (heuristic: first 2000 chars, look for 'food' related context?)
    # But let's stick to title and keywords first as they are most reliable.
    # If the user prompt implies extracted "domain", and lists "food", it's likely a keyword.
    
    # As a fallback, let's check if 'food' appears frequently or is in the abstract.
    # Extract Abstract
    abstract_match = re.search(r'ABSTRACT\s*\n(.*?)(?:\n\n|INTRODUCTION)', text, re.IGNORECASE | re.DOTALL)
    if abstract_match:
        abstract = abstract_match.group(1).lower()
        # If "food" is in abstract, it MIGHT be a food paper.
        # But in the sample, "food [11]" was in Introduction.
        # Let's check abstract.
        if 'food' in abstract:
             # To be safe, maybe check context? e.g. "food tracking", "food journal", "eating", "diet"
             # But "food" is the domain name.
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
