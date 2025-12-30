code = """import pandas as pd
import json

with open(locals()['var_function-call-2842283538054183407'], 'r') as f:
    citation_data = json.load(f)

citation_df = pd.DataFrame(citation_data)
paper_titles = citation_df['title'].tolist()

__RESULT__:
print(json.dumps(paper_titles))"""

env_args = {'var_function-call-2842283538054183407': 'file_storage/function-call-2842283538054183407.json'}

exec(code, env_args)
