code = """import json
import pandas as pd
import re

# Load citations
with open(locals()['var_function-call-4443069208433196148'], 'r') as f:
    citations_data = json.load(f)

df_citations = pd.DataFrame(citations_data)
# Convert citation_count to int
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'])

# Load papers
with open(locals()['var_function-call-4410602870318536324'], 'r') as f:
    papers_data = json.load(f)

food_papers_titles = []

for paper in papers_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    title = filename.replace('.txt', '')
    
    is_food_domain = False
    
    # Check Title
    if 'food' in title.lower():
        is_food_domain = True
    
    # Check Author Keywords
    # Regex to find Author Keywords section
    # Usually "Author Keywords" followed by text until "ACM Classification Keywords" or "INTRODUCTION" or double newline
    # Using a simple heuristic
    if not is_food_domain:
        # Find "Author Keywords" (case insensitive)
        match = re.search(r'Author Keywords\s*(.*?)\s*(?:ACM Classification Keywords|INTRODUCTION|ABSTRACT|\n\n)', text, re.IGNORECASE | re.DOTALL)
        if match:
            keywords = match.group(1).lower()
            if 'food' in keywords:
                is_food_domain = True
    
    # If still not found, check if "food" is in the Abstract? 
    # The description says "extract: ... domain". And "Common domains include: 'food'".
    # If the regex found the paper, it has "food".
    # But as we saw, "food" can be mentioned in body text.
    # If it's in the domain, it should be in keywords or title.
    # Let's trust keywords and title.
    
    if is_food_domain:
        food_papers_titles.append(title)

# Filter citations
# Find citations where title is in food_papers_titles
food_citations = df_citations[df_citations['title'].isin(food_papers_titles)]

total_citations = food_citations['citation_count'].sum()

print("__RESULT__:")
print(json.dumps({"total_citation_count": int(total_citations), "paper_count": len(food_papers_titles)}))"""

env_args = {'var_function-call-954876731548970456': 'file_storage/function-call-954876731548970456.json', 'var_function-call-13791197239651647544': ['Citations', 'sqlite_sequence'], 'var_function-call-4443069208433196148': 'file_storage/function-call-4443069208433196148.json', 'var_function-call-4410602870318536324': 'file_storage/function-call-4410602870318536324.json'}

exec(code, env_args)
