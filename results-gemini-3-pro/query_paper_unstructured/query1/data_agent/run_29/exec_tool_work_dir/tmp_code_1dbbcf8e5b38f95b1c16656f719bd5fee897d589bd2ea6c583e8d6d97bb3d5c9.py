code = """import json
import pandas as pd

# Load papers
with open(locals()['var_function-call-4410602870318536324'], 'r') as f:
    papers_data = json.load(f)

dropped_titles = []
kept_titles = []

for paper in papers_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    title = filename.replace('.txt', '')
    
    is_food_domain = False
    
    if 'food' in title.lower():
        is_food_domain = True
    
    if not is_food_domain:
        text_lower = text.lower()
        ak_start = text_lower.find('author keywords')
        if ak_start != -1:
            snippet = text_lower[ak_start:ak_start+500]
            end_markers = ['acm classification', 'introduction']
            min_end = len(snippet)
            for marker in end_markers:
                idx = snippet.find(marker, len('author keywords'))
                if idx != -1 and idx < min_end:
                    min_end = idx
            
            dbl_newline = chr(10) + chr(10)
            idx_nl = snippet.find(dbl_newline, len('author keywords'))
            if idx_nl != -1 and idx_nl < min_end:
                 min_end = idx_nl

            keywords_section = snippet[:min_end]
            if 'food' in keywords_section:
                is_food_domain = True
    
    if is_food_domain:
        kept_titles.append(title)
    else:
        dropped_titles.append(title)

print("__RESULT__:")
print(json.dumps({"kept": kept_titles, "dropped_sample": dropped_titles[:10]}))"""

env_args = {'var_function-call-954876731548970456': 'file_storage/function-call-954876731548970456.json', 'var_function-call-13791197239651647544': ['Citations', 'sqlite_sequence'], 'var_function-call-4443069208433196148': 'file_storage/function-call-4443069208433196148.json', 'var_function-call-4410602870318536324': 'file_storage/function-call-4410602870318536324.json', 'var_function-call-6127820780696900910': {'total_citation_count': 270, 'paper_count': 1, 'titles': ['Barriers and Negative Nudges: Exploring Challenges in Food Journaling']}}

exec(code, env_args)
