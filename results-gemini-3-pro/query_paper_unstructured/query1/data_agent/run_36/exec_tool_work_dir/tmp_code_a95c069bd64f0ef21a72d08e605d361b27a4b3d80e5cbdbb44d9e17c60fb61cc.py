code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-13014987171249504047'], 'r') as f:
    papers = json.load(f)

with open(locals()['var_function-call-13014987171249501074'], 'r') as f:
    citations = json.load(f)

# Convert citations to DataFrame
df_citations = pd.DataFrame(citations)
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'])

food_papers = []

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Simple extraction of keywords
    # We look for "Keywords" or "Index Terms"
    # We take a chunk of text after that and look for "food"
    
    text_lower = text.lower()
    
    # Regex to find keywords section
    # Matches "author keywords", "keywords", "index terms" followed by some text
    # We assume keywords are within the first few thousand characters usually, but let's search whole text
    # but usually before Introduction.
    
    # Let's try to find the index of "keywords"
    # Note: "Author Keywords" is common.
    
    keyword_indices = [m.start() for m in re.finditer(r'(author\s+)?keywords|index\s+terms', text_lower)]
    
    is_food = False
    if keyword_indices:
        # Check the context after each keyword occurrence (e.g. next 500 chars)
        for idx in keyword_indices:
            # extract next 500 chars
            snippet = text_lower[idx:idx+500]
            # Check if 'food' is in there
            # We should be careful not to match "food" in "food processing" if that's not the domain, 
            # but usually "food" as a domain is a standalone word or "food tracking".
            # The prompt says common domains include "food".
            # So searching for "food" in the keywords section should be enough.
            if 'food' in snippet:
                is_food = True
                break
    
    # Fallback: if no keywords found, maybe check Abstract?
    # But for now let's stick to keywords as the prompt hints strongly at "extracting domain" which usually implies metadata.
    # The sample paper had keywords that matched the hint's domain list exactly.
    
    if is_food:
        food_papers.append(title)

# Filter citations
# The Citations table has 'title'.
# We need to sum citation_count for rows where title is in food_papers.

food_citations = df_citations[df_citations['title'].isin(food_papers)]
total_citations = food_citations['citation_count'].sum()

print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_function-call-11340871341150089119': ['paper_docs'], 'var_function-call-11340871341150087996': ['Citations', 'sqlite_sequence'], 'var_function-call-6885705562055430499': 'file_storage/function-call-6885705562055430499.json', 'var_function-call-6885705562055430382': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-2249233586870449944': 'file_storage/function-call-2249233586870449944.json', 'var_function-call-13014987171249504047': 'file_storage/function-call-13014987171249504047.json', 'var_function-call-13014987171249501074': 'file_storage/function-call-13014987171249501074.json'}

exec(code, env_args)
