code = """import json
import pandas as pd

# Load data from previous tool results
with open(var_call_8BM1t2i9tHyr2VlKoQgkV7sJ, 'r') as f:
    clinical = json.load(f)
with open(var_call_k4wdRgBzWMAqo5yWj0XJZZBW, 'r') as f:
    mutations = json.load(f)

df_clin = pd.DataFrame(clinical)
df_mut = pd.DataFrame(mutations)

# Standardize barcodes
df_clin['participant_barcode'] = df_clin['participant_barcode'].astype(str).str.strip().str.upper()
df_mut['ParticipantBarcode'] = df_mut['ParticipantBarcode'].astype(str).str.strip().str.upper()

# Keep unique clinical patients (first occurrence)
df_clin_unique = df_clin.drop_duplicates(subset=['participant_barcode']).copy()

# Set of participants with CDH1 PASS mutations
mutated_set = set(df_mut['ParticipantBarcode'].unique())

# Focus only on clinical patients (female BRCA cohort extracted earlier)
df_clin_unique = df_clin_unique[df_clin_unique['participant_barcode'].notna()]

# Create mutation presence column
df_clin_unique['CDH1_mut'] = df_clin_unique['participant_barcode'].isin(mutated_set)

# Compute counts by histological type
group = df_clin_unique.groupby('histological_type').agg(
    mutated_count=('CDH1_mut', lambda x: int(x.sum())),
    total_count=('CDH1_mut', 'size')
).reset_index()
group['nonmutated_count'] = group['total_count'] - group['mutated_count']

# Exclude categories with marginal totals <= 10
included = group[group['total_count'] > 10].copy()

# If no categories left, result cannot be computed
if included.empty:
    result = {
        'error': 'No histological categories remain after excluding marginal totals <= 10.'
    }
else:
    # Build contingency table
    included = included.sort_values('histological_type')
    rows = included['histological_type'].tolist()
    observed = included[['mutated_count','nonmutated_count']].values.astype(float)
    # compute grand totals
    row_totals = observed.sum(axis=1)
    col_totals = observed.sum(axis=0)
    grand_total = row_totals.sum()
    # Expected counts and chi-square
    expected = (row_totals.reshape(-1,1) * col_totals.reshape(1,-1)) / grand_total
    # Avoid division by zero; only include cells with expected>0
    chi_sq = float(((observed - expected)**2 / expected).sum())

    # Prepare output structure
    contingency = []
    for i, rt in enumerate(rows):
        contingency.append({'histological_type': rt,
                            'mutated_count': int(observed[i,0]),
                            'nonmutated_count': int(observed[i,1]),
                            'total_count': int(row_totals[i])})
    result = {
        'chi_square': chi_sq,
        'grand_total': int(grand_total),
        'col_totals': {'mutated': int(col_totals[0]), 'nonmutated': int(col_totals[1])},
        'included_histological_types': contingency
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_xOsvUDMVOujDrw467HkcJPQ5': ['clinical_info'], 'var_call_UQP1za2q6llQK0JY9mJbc5Gj': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_zMMglcU8pczHPOyZwDqXlKz8': 'file_storage/call_zMMglcU8pczHPOyZwDqXlKz8.json', 'var_call_8BM1t2i9tHyr2VlKoQgkV7sJ': 'file_storage/call_8BM1t2i9tHyr2VlKoQgkV7sJ.json', 'var_call_k4wdRgBzWMAqo5yWj0XJZZBW': 'file_storage/call_k4wdRgBzWMAqo5yWj0XJZZBW.json'}

exec(code, env_args)
