code = """import json
import pandas as pd

# Load the clinical BRCA alive patients data
with open(var_call_BeTzlQA4cbDS1MOGfNvY58oG) as f:
    clinical = json.load(f)

# Load the list of participants with CDH1 mutations
with open(var_call_MqVb9x9wpRIG5AbnM3GztzIs) as f:
    muts = json.load(f)

# DataFrames
df_clin = pd.DataFrame(clinical)
df_muts = pd.DataFrame(muts)

# normalize column names to lower case
df_clin.columns = [c.lower() for c in df_clin.columns]
df_muts.columns = [c.lower() for c in df_muts.columns]

# expected column names
pcol = 'participantbarcode'
hcol_candidates = ['histological_type', 'histologicaltype', 'histological_type']
# find hist column
hcol = None
for c in df_clin.columns:
    if 'histologic' in c or 'histological' in c or 'histology' in c:
        hcol = c
        break
if hcol is None:
    # fallback
    hcol = 'histological_type'

# keep relevant columns and drop rows without participant barcode
df_clin = df_clin[[pcol, hcol]].dropna(subset=[pcol])
# uppercase barcodes
df_clin[pcol] = df_clin[pcol].str.upper().str.strip()
# fill missing hist types
df_clin[hcol] = df_clin[hcol].fillna('Unknown')

# Deduplicate patients (unique participants)
df_clin_unique = df_clin.drop_duplicates(subset=[pcol])

# total counts per histological type
total_by_hist = df_clin_unique.groupby(hcol)[pcol].nunique().rename('total').reset_index()

# mutated participants set
mut_set = set(df_muts[df_muts.columns[0]].astype(str).str.upper().str.strip().unique())

# compute mutated counts per hist
mutated_counts = (
    df_clin_unique[df_clin_unique[pcol].isin(mut_set)]
    .groupby(hcol)[pcol]
    .nunique()
    .rename('mutated')
    .reset_index()
)

# merge
df_stats = pd.merge(total_by_hist, mutated_counts, on=hcol, how='left')
 df_stats['mutated'] = df_stats['mutated'].fillna(0).astype(int)

# compute percentage
df_stats['percent'] = (df_stats['mutated'] / df_stats['total']) * 100

# sort and pick top 3
df_stats_sorted = df_stats.sort_values(by=['percent', 'mutated', hcol], ascending=[False, False, True]).head(3)

# prepare result list
result_list = []
for _, row in df_stats_sorted.iterrows():
    result_list.append({
        'histological_type': row[hcol],
        'total_alive_patients': int(row['total']),
        'mutated_patients': int(row['mutated']),
        'percent_mutated': round(float(row['percent']), 2)
    })

import json
print("__RESULT__:")
print(json.dumps(result_list))"""

env_args = {'var_call_BoKPAucPC0dfAgrOfK3xikrw': ['clinical_info'], 'var_call_c2Mt4k1g4FCgPfVRXCoCmoQ9': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_AKcAUiLEZgFVy7sGGP7gTnaf': 'file_storage/call_AKcAUiLEZgFVy7sGGP7gTnaf.json', 'var_call_BeTzlQA4cbDS1MOGfNvY58oG': 'file_storage/call_BeTzlQA4cbDS1MOGfNvY58oG.json', 'var_call_MqVb9x9wpRIG5AbnM3GztzIs': 'file_storage/call_MqVb9x9wpRIG5AbnM3GztzIs.json'}

exec(code, env_args)
