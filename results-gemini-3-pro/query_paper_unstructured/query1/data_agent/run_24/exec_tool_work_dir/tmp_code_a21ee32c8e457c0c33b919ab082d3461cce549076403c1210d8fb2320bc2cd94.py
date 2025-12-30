code = """import json
import re

# Get file paths from local variables
papers_path = locals()['var_function-call-1444485295091662967']
citations_path = locals()['var_function-call-1444485295091665344']

# Load papers
with open(papers_path, 'r') as f:
    papers = json.load(f)

# Load citations
with open(citations_path, 'r') as f:
    citations = json.load(f)

food_titles = set()
# Regex to find keywords section. 
keyword_pattern = re.compile(r"(?:Author\s+|Index\s+)?Keywords(?:\s*|:)\s*(.*?)(?:ACM Classification|INTRODUCTION|General Terms|Categories and Subject|ABSTRACT|\Z)", re.IGNORECASE | re.DOTALL)

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    is_food = False
    
    # Check Keywords section
    match = keyword_pattern.search(text)
    if match:
        keywords_text = match.group(1)
        if 'food' in keywords_text.lower():
            is_food = True
    
    # Check Title
    if 'food' in title.lower():
        is_food = True
        
    if is_food:
        food_titles.add(title)

# Sum citations
total_citations = 0
found_citations_count = 0
for cit in citations:
    # Title in citations table matches filename without extension (already handled above)
    if cit['title'] in food_titles:
        try:
            total_citations += int(cit['citation_count'])
            found_citations_count += 1
        except ValueError:
            pass

print(f"DEBUG: Found {len(food_titles)} food papers.")
print(f"DEBUG: Found {found_citations_count} citation records for these papers.")

print("__RESULT__:")
print(total_citations)"""

env_args = {'var_function-call-11821534155231291682': ['paper_docs'], 'var_function-call-11821534155231291545': ['Citations', 'sqlite_sequence'], 'var_function-call-4442982415428092656': 'file_storage/function-call-4442982415428092656.json', 'var_function-call-4442982415428092529': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-6202574896160599785': 'file_storage/function-call-6202574896160599785.json', 'var_function-call-938146018632188602': 'file_storage/function-call-938146018632188602.json', 'var_function-call-938146018632191415': [{'count(*)': '1405'}], 'var_function-call-1444485295091662967': 'file_storage/function-call-1444485295091662967.json', 'var_function-call-1444485295091665344': 'file_storage/function-call-1444485295091665344.json'}

exec(code, env_args)
