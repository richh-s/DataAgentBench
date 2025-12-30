code = """import json
import pandas as pd
import re

# Load citations
with open(locals()['var_function-call-4443069208433196148'], 'r') as f:
    citations_data = json.load(f)

df_citations = pd.DataFrame(citations_data)
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
    if not is_food_domain:
        text_lower = text.lower()
        ak_start = text_lower.find('author keywords')
        if ak_start != -1:
            # Extract next 500 chars
            snippet = text_lower[ak_start:ak_start+500]
            
            # Truncate at common next sections
            end_markers = ['acm classification', 'introduction']
            min_end = len(snippet)
            for marker in end_markers:
                idx = snippet.find(marker, len('author keywords'))
                if idx != -1 and idx < min_end:
                    min_end = idx
            
            # Also truncate at double newline if found, as keywords are usually a single paragraph
            dbl_newline = chr(10) + chr(10)
            idx_nl = snippet.find(dbl_newline, len('author keywords'))
            if idx_nl != -1 and idx_nl < min_end:
                 min_end = idx_nl

            keywords_section = snippet[:min_end]
            if 'food' in keywords_section:
                is_food_domain = True
                
    if is_food_domain:
        food_papers_titles.append(title)

# Filter citations
food_citations = df_citations[df_citations['title'].isin(food_papers_titles)]

total_citations = food_citations['citation_count'].sum()

print("__RESULT__:")
print(json.dumps({"total_citation_count": int(total_citations), "paper_count": len(food_papers_titles), "titles": food_papers_titles}))"""

env_args = {'var_function-call-954876731548970456': 'file_storage/function-call-954876731548970456.json', 'var_function-call-13791197239651647544': ['Citations', 'sqlite_sequence'], 'var_function-call-4443069208433196148': 'file_storage/function-call-4443069208433196148.json', 'var_function-call-4410602870318536324': 'file_storage/function-call-4410602870318536324.json'}

exec(code, env_args)
