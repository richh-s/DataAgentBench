code = """import json
import pandas as pd
import re

with open(locals()['var_function-call-343981584432704958'], 'r') as f:
    papers = json.load(f)
with open(locals()['var_function-call-6501009897595543018'], 'r') as f:
    citations = json.load(f)

df_papers = pd.DataFrame(papers)
df_citations = pd.DataFrame(citations)

debug_info = {}
debug_info["total_papers"] = len(papers)
debug_info["total_citations"] = len(df_citations)
debug_info["sample_citation_titles"] = df_citations['title'].head(5).tolist()
debug_info["sample_paper_filenames"] = df_papers['filename'].head(5).tolist()

def get_keywords_window(text):
    text_lower = text.lower()
    keyword_indices = [m.start() for m in re.finditer(r'keywords', text_lower)]
    windows = []
    for idx in keyword_indices:
        windows.append(text_lower[idx:idx+300]) 
    return windows

food_in_title = [p['filename'] for p in papers if 'food' in p['filename'].lower()]
debug_info["food_in_title"] = food_in_title

food_in_keywords = []
for p in papers:
    kw_windows = get_keywords_window(p['text'])
    for w in kw_windows:
        if 'food' in w:
            food_in_keywords.append(p['filename'])
            break

debug_info["food_in_keywords"] = food_in_keywords

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-4282369109293305518': ['paper_docs'], 'var_function-call-17210862545939823160': 'file_storage/function-call-17210862545939823160.json', 'var_function-call-6501009897595543018': 'file_storage/function-call-6501009897595543018.json', 'var_function-call-343981584432704958': 'file_storage/function-call-343981584432704958.json', 'var_function-call-17966795539395450339': 0}

exec(code, env_args)
