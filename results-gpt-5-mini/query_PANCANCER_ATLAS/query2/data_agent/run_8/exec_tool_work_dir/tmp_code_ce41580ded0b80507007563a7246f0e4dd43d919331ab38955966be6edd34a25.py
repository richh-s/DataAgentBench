code = """import json
import pandas as pd

# Load stored results which may be file paths or lists
def load_var(var):
    # If it's a string pointing to a .json file, open it
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return var

clinical_records = load_var(var_call_0fbi9yzq4LAHHybexOxuRTTA)
mutation_records = load_var(var_call_vCU0uKFlk2XMKZO8Qa8dY6vl)

# Create DataFrames
df_clin = pd.DataFrame(clinical_records)
# Normalize column names to lowercase for safety
df_clin.columns = [c.lower() for c in df_clin.columns]
# Expected columns: participantbarcode, histological_type
if 'participantbarcode' not in df_clin.columns:
    # try other key names
    possible_pb = [c for c in df_clin.columns if 'participant' in c]
    if possible_pb:
        df_clin = df_clin.rename(columns={possible_pb[0]: 'participantbarcode'})

if 'histological_type' not in df_clin.columns:
    possible_ht = [c for c in df_clin.columns if 'histolog' in c]
    if possible_ht:
        df_clin = df_clin.rename(columns={possible_ht[0]: 'histological_type'})

# Keep only necessary columns
df_clin = df_clin[['participantbarcode', 'histological_type']].dropna()
# strip whitespace
df_clin['participantbarcode'] = df_clin['participantbarcode'].str.strip()

df_mut = pd.DataFrame(mutation_records)
# Normalize
df_mut.columns = [c for c in df_mut.columns]
# Ensure ParticipantBarcode and Hugo_Symbol exist (case-insensitive)
cols_lower = {c.lower(): c for c in df_mut.columns}
if 'participantbarcode' in cols_lower:
    pb_col = cols_lower['participantbarcode']
else:
    # try variants
    pb_col = None
    for c in df_mut.columns:
        if 'participant' in c.lower():
            pb_col = c
            break

if 'hugo_symbol' in cols_lower:
    hugo_col = cols_lower['hugo_symbol']
else:
    hugo_col = None
    for c in df_mut.columns:
        if 'hugo' in c.lower():
            hugo_col = c
            break

if pb_col is None or hugo_col is None:
    raise ValueError('Mutation data missing expected columns')

# Filter mutations for CDH1
mask = df_mut[hugo_col].astype(str).str.upper() == 'CDH1'
cdh1_df = df_mut.loc[mask, [pb_col]].dropna()
# Standardize participant barcodes
cdh1_df = cdh1_df.rename(columns={pb_col: 'participantbarcode'})
cdh1_df['participantbarcode'] = cdh1_df['participantbarcode'].astype(str).str.strip()
# Unique mutated participants
mutated_set = set(cdh1_df['participantbarcode'].unique())

# Determine mutation status among clinical alive BRCA patients
# clinical dataframe contains alive BRCA participants from previous query
# Add mutated flag
df_clin['mutated'] = df_clin['participantbarcode'].apply(lambda x: x in mutated_set)

# Group by histological_type
group = df_clin.groupby('histological_type').agg(
    total_patients=('participantbarcode', 'nunique'),
    mutated_patients=('mutated', 'sum')
).reset_index()
# Compute percentage
group['percent_mutated'] = (group['mutated_patients'] / group['total_patients']) * 100
# Remove histological types with zero total (shouldn't happen) or NaN
group = group.dropna(subset=['histological_type'])

# Sort by percent desc, then mutated_patients desc, then total
group_sorted = group.sort_values(by=['percent_mutated', 'mutated_patients', 'total_patients'], ascending=[False, False, False])

# Take top 3
top3 = group_sorted.head(3)

# Prepare JSON-serializable output
result_list = []
for _, row in top3.iterrows():
    result_list.append({
        'histological_type': str(row['histological_type']),
        'total_patients': int(row['total_patients']),
        'mutated_patients': int(row['mutated_patients']),
        'percent_mutated': round(float(row['percent_mutated']), 2)
    })

import json
print("__RESULT__:")
print(json.dumps(result_list))"""

env_args = {'var_call_omyrWWxQ2iugAshRW9tDzeKo': ['clinical_info'], 'var_call_Fx7Ml25nTnvShnEQUFJ3BFex': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_HYmWS8a38qRwHqlfX3D0pcri': 'file_storage/call_HYmWS8a38qRwHqlfX3D0pcri.json', 'var_call_Wcft27pCPoguBFgEkTiFMNNf': [{'cnt': '1087'}], 'var_call_0fbi9yzq4LAHHybexOxuRTTA': 'file_storage/call_0fbi9yzq4LAHHybexOxuRTTA.json', 'var_call_vCU0uKFlk2XMKZO8Qa8dY6vl': 'file_storage/call_vCU0uKFlk2XMKZO8Qa8dY6vl.json'}

exec(code, env_args)
