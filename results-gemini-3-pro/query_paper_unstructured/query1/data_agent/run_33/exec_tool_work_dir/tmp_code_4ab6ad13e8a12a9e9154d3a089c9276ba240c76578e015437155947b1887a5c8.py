code = """import json
import pandas as pd
import re

# Load Citations
citations_path = locals()['var_function-call-1373040785545021376']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)
df_citations = pd.DataFrame(citations_data)

# Load Paper Docs
docs_path = locals()['var_function-call-6365592025106147893']
with open(docs_path, 'r') as f:
    docs_data = json.load(f)
df_docs = pd.DataFrame(docs_data)

# Extract title from filename
df_docs['title'] = df_docs['filename'].str.replace(r'\.txt$', '', regex=True)

# Function to check for 'food' domain
def is_food_domain(row):
    text = row['text']
    title = row['title']
    
    # 1. Check Title
    if 'food' in title.lower():
        return True
        
    # 2. Check Keywords section
    # Look for "Author Keywords", "Keywords", "General Terms"
    # Capture the text following it until a double newline or a section header (usually UPPERCASE)
    # This is heuristic.
    match = re.search(r'(?:Author Keywords|Keywords|General Terms)([\s\S]{0,1000})', text, re.IGNORECASE)
    if match:
        keywords_block = match.group(1).lower()
        # Cut off at next section usually indicated by \n\n[A-Z]
        # But simply searching in the next 1000 chars is likely safe enough if we look for the word "food"
        # However, "food" might be part of "non-food".
        # Use word boundary
        if re.search(r'\bfood\b', keywords_block):
            return True
            
    # 3. Fallback: Check Abstract or early text
    # Assuming Abstract is in the first 3000 chars.
    # Searching for "food" in the abstract is risky if it's just mentioned.
    # But usually "food" domain papers will mention it in Abstract.
    # Let's check first 3000 chars for "\bfood\b"
    head_text = text[:3000].lower()
    if re.search(r'\bfood\b', head_text):
        # To be safer, maybe ensure it's not just "food for thought" (rare in technical papers).
        return True
        
    return False

df_docs['is_food'] = df_docs.apply(is_food_domain, axis=1)

# Filter food papers
food_papers = df_docs[df_docs['is_food']]
food_titles = food_papers['title'].unique()

# Filter citations
# Merge or filter
# Ensure we match titles exactly
total_citations = df_citations[df_citations['title'].isin(food_titles)]['citation_count'].sum()

print("__RESULT__:")
print(total_citations)"""

env_args = {'var_function-call-4548718859833522719': 'file_storage/function-call-4548718859833522719.json', 'var_function-call-1373040785545021376': 'file_storage/function-call-1373040785545021376.json', 'var_function-call-14795720345132237503': 'file_storage/function-call-14795720345132237503.json', 'var_function-call-6365592025106147893': 'file_storage/function-call-6365592025106147893.json'}

exec(code, env_args)
