code = """import json
import pandas as pd

# Load citations
citations_path = locals()['var_function-call-13231219773529852876']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)
df_citations = pd.DataFrame(citations_data)

# Load candidate papers
papers_path = locals()['var_function-call-1470986514462479797']
with open(papers_path, 'r') as f:
    papers_data = json.load(f)

food_papers = []

for paper in papers_data:
    filename = paper['filename']
    title = filename.replace('.txt', '')
    text = paper['text']
    
    is_food = False
    
    # Check title
    if 'food' in title.lower():
        is_food = True
    else:
        # Check Author Keywords
        lower_text = text.lower()
        keyword_idx = lower_text.find('author keywords')
        
        if keyword_idx != -1:
            snippet = lower_text[keyword_idx:keyword_idx+500]
            end_idx = snippet.find('introduction')
            if end_idx == -1:
                end_idx = snippet.find('acm classification')
            if end_idx == -1:
                 end_idx = 300
            
            keywords_section = snippet[:end_idx]
            
            if 'food' in keywords_section:
                is_food = True
    
    if is_food:
        food_papers.append(title)

print("__RESULT__:")
print(json.dumps(food_papers))"""

env_args = {'var_function-call-2303008597307440717': 'file_storage/function-call-2303008597307440717.json', 'var_function-call-13231219773529852876': 'file_storage/function-call-13231219773529852876.json', 'var_function-call-1470986514462479797': 'file_storage/function-call-1470986514462479797.json', 'var_function-call-2063711702066525845': 270}

exec(code, env_args)
