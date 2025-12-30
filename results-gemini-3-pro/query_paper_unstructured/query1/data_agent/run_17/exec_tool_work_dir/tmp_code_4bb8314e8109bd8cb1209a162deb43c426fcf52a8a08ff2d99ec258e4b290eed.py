code = """import json
import pandas as pd
import re

# Load citations
with open(locals()['var_function-call-7751700414245967410'], 'r') as f:
    citations_data = json.load(f)
citations_df = pd.DataFrame(citations_data)
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])

# Load papers
with open(locals()['var_function-call-6242695006040143543'], 'r') as f:
    papers_data = json.load(f)

def is_food_domain(paper):
    text_lower = paper['text'].lower()
    filename_lower = paper['filename'].lower()
    
    # 1. Check Keywords
    # Regex to find "Author Keywords" or "Keywords" block
    # We grab text until a double newline or "Introduction" or "ACM Classification"
    # Note: Regex dot matches newline? No.
    match = re.search(r"(author keywords|keywords|index terms)[:\s]*(.*?)(?:\n\n|\n[A-Z]|\n\s*introduction|\n\s*acm classification)", text_lower, re.DOTALL)
    if match:
        keywords_block = match.group(2)
        if "food" in keywords_block:
            return True
            
    # 2. Check Title (filename)
    if "food" in filename_lower:
        return True
        
    return False

food_papers = []
for p in papers_data:
    if is_food_domain(p):
        title = p['filename'].replace('.txt', '')
        food_papers.append(title)

# Join and sum
food_citations = citations_df[citations_df['title'].isin(food_papers)]
total_citations = food_citations['citation_count'].sum()

print("__RESULT__:")
print(json.dumps({
    "food_papers_count": len(food_papers),
    "food_papers_titles": food_papers,
    "total_citations": int(total_citations)
}))"""

env_args = {'var_function-call-8429523015460398318': 'file_storage/function-call-8429523015460398318.json', 'var_function-call-495826835805715086': 'file_storage/function-call-495826835805715086.json', 'var_function-call-7751700414245967410': 'file_storage/function-call-7751700414245967410.json', 'var_function-call-6242695006040143543': 'file_storage/function-call-6242695006040143543.json'}

exec(code, env_args)
