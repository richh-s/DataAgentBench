code = """import json
import re

# Load the papers
with open(locals()['var_function-call-17858895574398346247'], 'r') as f:
    papers = json.load(f)

food_papers = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check title
    if 'food' in title.lower():
        food_papers.append(title)
        continue
        
    # Check keywords
    # heuristic to find keywords
    # Look for "Author Keywords" or "Keywords"
    # Take the text until the next empty line or "INTRODUCTION" or "ACM Classification"
    
    lower_text = text.lower()
    keywords_start = -1
    
    if "author keywords" in lower_text:
        keywords_start = lower_text.find("author keywords") + len("author keywords")
    elif "keywords" in lower_text:
        # Be careful with just "keywords", might be "Keywords" as a header
        # Check for "\nKeywords" or similar
        keywords_start = lower_text.find("\nkeywords")
        if keywords_start != -1:
            keywords_start += len("\nkeywords")
            
    if keywords_start != -1:
        # Extract a chunk after keywords
        chunk = lower_text[keywords_start:keywords_start+500] 
        # Truncate at next section
        end_markers = ["introduction", "acm classification", "abstract", "general terms", "\n\n\n"]
        min_end = len(chunk)
        for marker in end_markers:
            idx = chunk.find(marker)
            if idx != -1 and idx < min_end:
                min_end = idx
        
        keywords_text = chunk[:min_end]
        
        if "food" in keywords_text:
            food_papers.append(title)

print("__RESULT__:")
print(json.dumps(food_papers))"""

env_args = {'var_function-call-1852344882916152676': 'file_storage/function-call-1852344882916152676.json', 'var_function-call-1852344882916155297': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-17858895574398346247': 'file_storage/function-call-17858895574398346247.json'}

exec(code, env_args)
