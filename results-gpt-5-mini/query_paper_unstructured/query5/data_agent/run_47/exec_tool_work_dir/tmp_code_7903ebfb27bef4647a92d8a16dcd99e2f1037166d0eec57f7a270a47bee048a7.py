code = """import json
import pandas as pd

# Load the large citations result from the provided file path variable
with open(var_call_2H7RWpcq9JKwNUeJKnJipnP1, 'r') as f:
    citations = json.load(f)

# DataFrame
df = pd.DataFrame(citations)
# Normalize column name (from SQL query alias)
# Ensure citation count is int
if 'citation_count_2020' in df.columns:
    df['citation_count_2020'] = df['citation_count_2020'].astype(int)
else:
    # try other possible column names
    for col in df.columns:
        if 'citation' in col.lower():
            df['citation_count_2020'] = df[col].astype(int)
            break

# Extract CHI paper titles from the Mongo query result variable
filenames = [d['filename'] for d in var_call_4SGgkMePLE3ABuQeeoQmXCzd]
titles = [fn[:-4] if fn.lower().endswith('.txt') else fn for fn in filenames]

# Filter citations for CHI titles
df_chi = df[df['title'].isin(titles)].copy()

# Prepare output records
records = df_chi[['title', 'citation_count_2020']].to_dict(orient='records')
total = int(df_chi['citation_count_2020'].sum()) if not df_chi.empty else 0

out = {'papers': records, 'total_citations_2020': total}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_2H7RWpcq9JKwNUeJKnJipnP1': 'file_storage/call_2H7RWpcq9JKwNUeJKnJipnP1.json', 'var_call_4SGgkMePLE3ABuQeeoQmXCzd': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}]}

exec(code, env_args)
