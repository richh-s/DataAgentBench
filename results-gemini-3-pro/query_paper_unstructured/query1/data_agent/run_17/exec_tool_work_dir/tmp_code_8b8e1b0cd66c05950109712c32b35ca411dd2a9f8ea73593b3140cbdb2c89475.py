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

# Function to extract domain
def is_food_domain(text):
    # Normalize text
    text_lower = text.lower()
    
    # Look for keywords section
    # Common headers: "Author Keywords", "Keywords", "Index Terms"
    # We want to match "food" within that section.
    
    # Simple heuristic: find "Author Keywords" or "Keywords" and look at the next ~200 chars or until next newline block
    # Note: text formatting can be messy.
    
    patterns = [r"author keywords", r"keywords", r"index terms"]
    
    for pattern in patterns:
        match = re.search(pattern, text_lower)
        if match:
            # Extract next chunk of text
            start = match.end()
            # Look for next section header or double newline?
            # Papers often have "ACM Classification Keywords" or "INTRODUCTION" after.
            # Let's take next 500 chars
            chunk = text_lower[start:start+500]
            
            # Stop at "introduction" or "acm classification" or "abstract" if they appear (keywords usually before or after abstract)
            # Actually abstract is usually before keywords.
            
            # Let's clean the chunk up to the next big header
            end_match = re.search(r"\n\s*(introduction|acm classification|abstract)", chunk)
            if end_match:
                chunk = chunk[:end_match.start()]
                
            # Check for "food" in chunk
            if "food" in chunk:
                return True
                
    # Fallback: check title? (filename)
    # But filtering by keywords is safer for "domain".
    return False

# Filter papers
food_papers = []
for p in papers_data:
    if is_food_domain(p['text']):
        title = p['filename'].replace('.txt', '')
        food_papers.append(title)

# Join and sum
# Filter citations where title is in food_papers
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
