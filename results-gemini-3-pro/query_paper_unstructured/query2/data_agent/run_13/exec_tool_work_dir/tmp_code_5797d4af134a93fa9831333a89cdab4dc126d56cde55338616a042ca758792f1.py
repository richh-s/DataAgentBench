code = """import json
import pandas as pd

with open(locals()['var_function-call-12153821661542533629'], 'r') as f:
    citations_data = json.load(f)
citations_df = pd.DataFrame(citations_data)
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])

with open(locals()['var_function-call-12153821661542534380'], 'r') as f:
    papers_data = json.load(f)

acm_strict = []
acm_loose = []
ieee_titles = []

for paper in papers_data:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
        
    if "ACM" in text:
        acm_loose.append(title)
        # stricter check
        if "Copyright" in text and "ACM" in text:
            acm_strict.append(title)
            
    if "IEEE" in text:
        ieee_titles.append(title)

# Calculate averages
avg_loose = citations_df[citations_df['title'].isin(acm_loose)]['citation_count'].mean()
avg_strict = citations_df[citations_df['title'].isin(acm_strict)]['citation_count'].mean()

print("__RESULT__:")
print(json.dumps({"avg_loose": avg_loose, "avg_strict": avg_strict, "count_loose": len(acm_loose), "count_strict": len(acm_strict)}))"""

env_args = {'var_function-call-12153821661542533629': 'file_storage/function-call-12153821661542533629.json', 'var_function-call-12153821661542534380': 'file_storage/function-call-12153821661542534380.json', 'var_function-call-7412265948695005483': 68.5}

exec(code, env_args)
