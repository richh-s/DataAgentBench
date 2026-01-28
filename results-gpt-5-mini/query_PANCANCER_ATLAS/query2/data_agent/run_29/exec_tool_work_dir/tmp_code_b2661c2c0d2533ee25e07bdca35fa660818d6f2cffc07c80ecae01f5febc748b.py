code = """import json
import pandas as pd
import os

# Load stored results from previous tool calls
# var_call_YFJyy1NfkG6x4moekPx9zSjV : clinical alive BRCA patients (may be filepath or list)
# var_call_K1lkjBb1USWvz2xfxN6g9bwg : ParticipantBarcodes with CDH1 mutation (may be filepath or list)

def load_var(v):
    if isinstance(v, str):
        with open(v, 'r') as f:
            return json.load(f)
    return v

clin = load_var(var_call_YFJyy1NfkG6x4moekPx9zSjV)
mut = load_var(var_call_K1lkjBb1USWvz2xfxN6g9bwg)

# Create DataFrames
dfc = pd.DataFrame(clin)
dfm = pd.DataFrame(mut)

# Ensure column names
if 'barcode' not in dfc.columns:
    # Try alternate key
    if 'ParticipantBarcode' in dfc.columns:
        dfc = dfc.rename(columns={'ParticipantBarcode':'barcode'})

# Totals per histological_type among alive BRCA patients
group = dfc.groupby('histological_type').agg(total=('barcode','nunique')).reset_index()

# Mutated patients: join on barcode == ParticipantBarcode
if 'ParticipantBarcode' not in dfm.columns:
    # If mutation table used different key name, try to detect
    pass

joined = dfc.merge(dfm, left_on='barcode', right_on='ParticipantBarcode', how='left')

# Count unique mutated barcodes per histological_type
mut_counts = joined[joined['ParticipantBarcode'].notnull()].groupby('histological_type').agg(mutated=('barcode','nunique')).reset_index()

merge = group.merge(mut_counts, on='histological_type', how='left').fillna(0)
merge['mutated'] = merge['mutated'].astype(int)
merge['percent'] = (merge['mutated']/merge['total']*100).round(2)

# Sort and get top 3 by percent, then mutated, then total
res = merge.sort_values(['percent','mutated','total'], ascending=[False,False,True]).head(3)

out = res[['histological_type','total','mutated','percent']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_BJIbV4gVEYV4l8VvJtnPhCtP': ['clinical_info'], 'var_call_2UuqXemXZlW4uTaiOkcnBfo7': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_tjT3G2hZ8n85Ne2MCykgUkRX': 'file_storage/call_tjT3G2hZ8n85Ne2MCykgUkRX.json', 'var_call_FwxggJzMMRtGwTSDQWnBKcG9': 'file_storage/call_FwxggJzMMRtGwTSDQWnBKcG9.json', 'var_call_YFJyy1NfkG6x4moekPx9zSjV': 'file_storage/call_YFJyy1NfkG6x4moekPx9zSjV.json', 'var_call_K1lkjBb1USWvz2xfxN6g9bwg': 'file_storage/call_K1lkjBb1USWvz2xfxN6g9bwg.json'}

exec(code, env_args)
