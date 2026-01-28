code = """import json
import re
import pandas as pd

# Load results from storage paths
with open(var_call_xgfwqQgmQYB90Agv1Y9V1ATM, 'r', encoding='utf-8') as f:
    docs = json.load(f)
with open(var_call_5QUzNaplD2axIQspTd16liMY, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# DataFrames
df_docs = pd.DataFrame(docs)
# Extract title from filename
df_docs['title'] = df_docs['filename'].str.replace(r"\.txt$", '', regex=True)
# Determine if 'food' appears as a word in the text
df_docs['text_lower'] = df_docs['text'].str.lower().fillna('')
df_docs['food_domain'] = df_docs['text_lower'].apply(lambda t: bool(re.search(r"\bfood\b", t)))

# Citations dataframe
df_cit = pd.DataFrame(citations)
# Ensure numeric
df_cit['total_citations'] = df_cit['total_citations'].astype(int)

# Merge citations for titles present in docs
# Keep only docs with food_domain True
food_titles = df_docs.loc[df_docs['food_domain'], 'title'].unique().tolist()
# Filter citations for these titles
df_food_cit = df_cit[df_cit['title'].isin(food_titles)]

total_citations_food = int(df_food_cit['total_citations'].sum())

# Prepare output as JSON-serializable string
import json
output = json.dumps({"food_domain_total_citations": total_citations_food})
print("__RESULT__:")
print(output)"""

env_args = {'var_call_XjVBNCkepLGgO8Cu2OgcQVth': ['paper_docs'], 'var_call_xgfwqQgmQYB90Agv1Y9V1ATM': 'file_storage/call_xgfwqQgmQYB90Agv1Y9V1ATM.json', 'var_call_qPIPGT34vscwC1oFP3m55bwO': ['Citations', 'sqlite_sequence'], 'var_call_5QUzNaplD2axIQspTd16liMY': 'file_storage/call_5QUzNaplD2axIQspTd16liMY.json'}

exec(code, env_args)
