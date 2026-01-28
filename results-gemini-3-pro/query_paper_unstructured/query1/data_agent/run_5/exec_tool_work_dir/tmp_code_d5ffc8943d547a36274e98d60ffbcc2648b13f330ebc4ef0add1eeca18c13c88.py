code = """import json
import re

# Load data
with open(locals()['var_function-call-17959813920400142644'], 'r') as f:
    paper_docs = json.load(f)

with open(locals()['var_function-call-14824333924694724411'], 'r') as f:
    citations = json.load(f)

food_papers = []
debug_info = []

for doc in paper_docs:
    text = doc['text']
    filename = doc['filename']
    title = filename.replace('.txt', '')
    
    # Normalize text
    lower_text = text.lower()
    
    # Try to find the keyword section
    # Search for "Author Keywords" or "Index Terms" or just "Keywords"
    # We look for the label, then capture text until we hit another known section header like "INTRODUCTION" or "ACM CLASSIFICATION"
    
    # Pattern: label followed by some text, then a lookahead for a section header or end of file
    # Note: Regex can be tricky with newlines.
    
    # Let's find the start
    match = re.search(r'(author\s+keywords|index\s+terms|keywords)', lower_text)
    
    if match:
        start_pos = match.end()
        # Take a chunk of text after the header
        chunk = lower_text[start_pos:start_pos+1000]
        
        # Stop at "introduction" or "abstract" or "acm classification" or "general terms"
        # Be careful with "abstract" since it usually comes BEFORE keywords.
        # Usually: Abstract -> Keywords -> Introduction
        
        stop_match = re.search(r'(introduction|acm classification|general terms)', chunk)
        if stop_match:
            keywords_text = chunk[:stop_match.start()]
        else:
            keywords_text = chunk
            
        # Check for 'food' as a whole word
        if re.search(r'\bfood\b', keywords_text):
            food_papers.append(title)
            debug_info.append(title)
            
# Calculate citations
total_citations = 0
for cit in citations:
    if cit['title'] in food_papers:
        try:
            total_citations += int(cit['citation_count'])
        except:
            pass

print("__RESULT__:")
print(json.dumps({
    "food_papers_count": len(food_papers),
    "food_papers": food_papers,
    "total_citations": total_citations
}))"""

env_args = {'var_function-call-12772568682444921532': 'file_storage/function-call-12772568682444921532.json', 'var_function-call-268740664748096753': 'file_storage/function-call-268740664748096753.json', 'var_function-call-17959813920400142644': 'file_storage/function-call-17959813920400142644.json', 'var_function-call-14824333924694724411': 'file_storage/function-call-14824333924694724411.json'}

exec(code, env_args)
