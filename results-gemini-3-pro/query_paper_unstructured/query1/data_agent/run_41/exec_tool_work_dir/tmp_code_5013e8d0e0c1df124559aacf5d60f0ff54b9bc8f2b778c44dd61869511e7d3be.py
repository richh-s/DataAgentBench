code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-14859437005275468977'], 'r') as f:
    citations_data = json.load(f)

with open(locals()['var_function-call-9278851709122145007'], 'r') as f:
    papers_data = json.load(f)

df_citations = pd.DataFrame(citations_data)
df_papers = pd.DataFrame(papers_data)

# Process papers to find 'food' domain
def is_food_domain(text):
    # Find Keywords section
    # Patterns to look for
    patterns = [r"Author Keywords", r"Keywords"]
    
    start_idx = -1
    for p in patterns:
        match = re.search(p, text, re.IGNORECASE)
        if match:
            start_idx = match.end()
            break
            
    if start_idx == -1:
        return False
        
    # Extract text after keywords until next section or reasonable length
    # Look for "ACM Classification Keywords" or "INTRODUCTION" or double newline
    # But double newline might happen within keywords.
    # Let's look for "ACM Classification Keywords" or "INTRODUCTION"
    
    sub_text = text[start_idx:]
    
    # End markers
    end_markers = ["ACM Classification Keywords", "INTRODUCTION", "ABSTRACT"]
    end_idx = len(sub_text)
    
    for marker in end_markers:
        marker_match = re.search(marker, sub_text, re.IGNORECASE)
        if marker_match:
            end_idx = min(end_idx, marker_match.start())
            
    # Also limit by length to avoid reading whole paper if markers missing
    if end_idx > 1000:
        end_idx = 1000
        
    keywords_text = sub_text[:end_idx]
    
    # Check for 'food'
    if 'food' in keywords_text.lower():
        return True
    return False

# Normalize filename
df_papers['title_join'] = df_papers['filename'].str.replace('.txt', '', regex=False)

# Identify food papers
df_papers['is_food'] = df_papers['text'].apply(is_food_domain)

food_papers = df_papers[df_papers['is_food']]
print(f"Found {len(food_papers)} papers in food domain.")
print(f"Titles: {food_papers['title_join'].tolist()}")

# Join with citations
# Citations table has 'title', 'citation_count' (int?), 'citation_year'
# Ensure citation_count is numeric
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'])

# Filter citations for food papers
# Inner join
merged = pd.merge(df_citations, food_papers, left_on='title', right_on='title_join')

total_citations = merged['citation_count'].sum()

print("__RESULT__:")
print(json.dumps(int(total_citations)))"""

env_args = {'var_function-call-10309278563115687463': ['paper_docs'], 'var_function-call-17310270331774513134': 'file_storage/function-call-17310270331774513134.json', 'var_function-call-14859437005275468977': 'file_storage/function-call-14859437005275468977.json', 'var_function-call-9278851709122145007': 'file_storage/function-call-9278851709122145007.json'}

exec(code, env_args)
