code = """import json, re, math
import pandas as pd

# Load data files from previous query results
clinical_path = var_call_SZWtI8VXZWrjWsr94fvHxDva
mut_path = var_call_7FWy9AkScfQSBbOSiTSaGCcS

with open(clinical_path, 'r') as f:
    clinical = json.load(f)
with open(mut_path, 'r') as f:
    muts = json.load(f)

# Extract TCGA barcode from Patient_description using regex
barcode_re = re.compile(r'(TCGA-[A-Za-z0-9]{2}-[A-Za-z0-9]{3,6})')

patient_hist = {}
for r in clinical:
    desc = r.get('Patient_description', '')
    m = barcode_re.search(desc)
    if not m:
        continue
    barcode = m.group(1)
    hist = r.get('histological_type')
    if hist is None:
        continue
    # Normalize hist string
    hist_norm = hist.strip()
    if hist_norm == '' or hist_norm.upper().startswith('[NOT'):
        continue
    # Use first observed histology for barcode
    if barcode not in patient_hist:
        patient_hist[barcode] = hist_norm

# Build set of participants with PASS CDH1 mutations
mutated_participants = set()
for r in muts:
    pb = r.get('ParticipantBarcode')
    if pb:
        mutated_participants.add(pb)

# Build dataframe of clinical BRCA female patients with known hist types
rows = []
for bc, hist in patient_hist.items():
    rows.append({'barcode': bc, 'histological_type': hist, 'mutated': (bc in mutated_participants)})

df = pd.DataFrame(rows)

# If df empty, return
if df.empty:
    result = {'error': 'No matching female BRCA patients with histological type found.'}
    print('__RESULT__:')
    print(json.dumps(result))
else:
    # Contingency table
    ct = pd.crosstab(df['histological_type'], df['mutated'])
    # Ensure both columns True/False exist
    for col in [False, True]:
        if col not in ct.columns:
            ct[col] = 0
    ct = ct[[True, False]] if True in ct.columns else ct[[False, True]]
    # Compute row totals
    ct['row_total'] = ct.sum(axis=1)
    # Exclude hist types with marginal totals <= 10
    included = ct[ct['row_total'] > 10].copy()
    excluded = ct[ct['row_total'] <= 10].copy()

    # Prepare contingency table for included types
    if included.shape[0] == 0:
        result = {'error': 'No histological categories with total > 10 after filtering.'}
        print('__RESULT__:')
        print(json.dumps(result))
    else:
        # Columns: True (mutated), False (not mutated)
        included = included[[True, False]]
        grand_total = int(included.values.sum())
        col_totals = included.sum(axis=0)
        chi2 = 0.0
        for i, row in included.iterrows():
            row_total = int(row.sum())
            for col in [True, False]:
                obs = int(row[col])
                expected = (row_total * int(col_totals[col])) / grand_total if grand_total>0 else 0
                if expected > 0:
                    chi2 += (obs - expected) ** 2 / expected
        # Prepare outputs
        contingency = {}
        for idx, row in included.iterrows():
            contingency[idx] = {'mutated': int(row[True]), 'not_mutated': int(row[False]), 'row_total': int(row.sum())}
        excluded_list = []
        for idx, row in excluded.iterrows():
            excluded_list.append({'histological_type': idx, 'mutated': int(row.get(True,0)), 'not_mutated': int(row.get(False,0)), 'row_total': int(row.sum())})

        result = {
            'chi2': round(chi2, 6),
            'grand_total': grand_total,
            'mutated_total': int(col_totals.get(True,0)),
            'not_mutated_total': int(col_totals.get(False,0)),
            'included_histological_types_count': len(contingency),
            'included_contingency': contingency,
            'excluded_histological_types': excluded_list
        }
        print('__RESULT__:')
        print(json.dumps(result))"""

env_args = {'var_call_J8cq91Qkykr7BmOMwRiN41M3': ['clinical_info'], 'var_call_ieTXnMdiVrVRJFhMg9brgKK2': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_TCYUIakYKMmCmy1cTDzmJsFS': 'file_storage/call_TCYUIakYKMmCmy1cTDzmJsFS.json', 'var_call_Ofi87woW9fv2wFDGgz6Tk0LF': [], 'var_call_SZWtI8VXZWrjWsr94fvHxDva': 'file_storage/call_SZWtI8VXZWrjWsr94fvHxDva.json', 'var_call_7FWy9AkScfQSBbOSiTSaGCcS': 'file_storage/call_7FWy9AkScfQSBbOSiTSaGCcS.json'}

exec(code, env_args)
