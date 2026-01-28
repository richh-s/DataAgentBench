code = """import json
import re

# Load the result from the previous tool call which contains all paper documents
# The variable name is var_function_call_2784456045421474973 (replacing hyphens with underscores if needed, but usually the key is a string)
# Actually, the instructions say: "access its result via locals()['var_call-1']". The key provided was 'var_function-call-2784456045421474973'.
# Python variables cannot have hyphens. The system usually provides the key as is. I should access it using the string key in locals().

file_path = locals()['var_function-call-2784456045421474973']

with open(file_path, 'r') as f:
    papers = json.load(f)

food_titles = []
for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Extract Author Keywords
    # Pattern: "Author Keywords" followed by text until "ACM Classification Keywords" or "INTRODUCTION" or other headers.
    # We can be a bit flexible.
    
    # Normalize text for searching
    text_lower = text.lower()
    
    # Find start
    start_idx = text_lower.find('author keywords')
    if start_idx == -1:
        # Try "Index Terms"
        start_idx = text_lower.find('index terms')
    
    keywords = ""
    if start_idx != -1:
        # Find end. Common next headers.
        end_candidates = ['acm classification keywords', 'introduction', 'general terms', 'abstract']
        # We start searching for end after the start keyword line.
        # Let's just take a chunk and split by lines?
        # Or find the nearest next header.
        
        # Approximate extraction: take next 500 chars and look for terminators
        chunk = text_lower[start_idx:start_idx+1000]
        
        # Find the earliest occurrence of any end candidate
        min_end = 1000
        for cand in end_candidates:
            end_idx = chunk.find(cand, 15) # skip the "author keywords" itself
            if end_idx != -1 and end_idx < min_end:
                min_end = end_idx
        
        keywords = chunk[:min_end]
        
    # Check if 'food' is in keywords
    if 'food' in keywords:
        food_titles.append(title)
        
print("__RESULT__:")
print(json.dumps(food_titles))"""

env_args = {'var_function-call-16691690145892377259': 'file_storage/function-call-16691690145892377259.json', 'var_function-call-2784456045421474973': 'file_storage/function-call-2784456045421474973.json'}

exec(code, env_args)
