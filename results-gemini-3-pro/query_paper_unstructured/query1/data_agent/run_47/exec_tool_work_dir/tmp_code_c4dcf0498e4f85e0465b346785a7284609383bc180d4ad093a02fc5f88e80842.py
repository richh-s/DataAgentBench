code = """import json
import re

# Load paper docs
with open('var_function-call-15077613833019679981.json', 'r') as f:
    papers = json.load(f)

# Load citations
with open('var_function-call-15077613833019680274.json', 'r') as f:
    citations = json.load(f)

food_titles = set()

for p in papers:
    filename = p.get('filename', '')
    text = p.get('text', '')
    title = filename.replace('.txt', '')
    
    # Check title
    if re.search(r'\bfood\b', title, re.IGNORECASE):
        food_titles.add(title)
        continue
        
    # Check Keywords section
    # Look for "Author Keywords" or "Keywords"
    # We take a chunk of text starting from the keyword label
    match = re.search(r'(?:Author Keywords|Index Terms|Keywords)\s*[:\r\n]+(.*?)(?:INTRODUCTION|ABSTRACT|ACM Classification|\Z)', text, re.IGNORECASE | re.DOTALL)
    if match:
        keywords_block = match.group(1)
        if re.search(r'\bfood\b', keywords_block, re.IGNORECASE):
            food_titles.add(title)
            continue
            
    # Fallback: Check for "food" in the first 5000 characters if no specific keyword section was found?
    # Or strict adherence? 
    # The hint says "For each paper, you may need to extract: ... domain". 
    # This implies the domain is there. 
    # If the regex fails, we might miss papers. 
    # Let's try to search in the whole text but check if it matches a specific context?
    # No, simple search for "food" in the whole text might be too noisy.
    # However, if the paper is in the food domain, "food" should appear frequently?
    # Let's stick to Title and Keywords for now. 
    # If the count is 0, I might broaden the search.

# Calculate total citations
total_citations = 0
for c in citations:
    c_title = c.get('title', '')
    # The citation title matches the paper title (filename without extension)
    if c_title in food_titles:
        try:
            count = int(c.get('citation_count', 0))
            total_citations += count
        except:
            pass

print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_function-call-14405582414403684106': ['paper_docs'], 'var_function-call-14405582414403686195': ['Citations', 'sqlite_sequence'], 'var_function-call-1273577479453038261': 'file_storage/function-call-1273577479453038261.json', 'var_function-call-1273577479453039900': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-15077613833019679981': 'file_storage/function-call-15077613833019679981.json', 'var_function-call-15077613833019680274': 'file_storage/function-call-15077613833019680274.json'}

exec(code, env_args)
