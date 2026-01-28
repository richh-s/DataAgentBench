code = """import json, re
import pandas as pd

clinical_path = var_call_SZWtI8VXZWrjWsr94fvHxDva
mut_path = var_call_7FWy9AkScfQSBbOSiTSaGCcS

with open(clinical_path, 'r') as f:
    clinical = json.load(f)
with open(mut_path, 'r') as f:
    muts = json.load(f)

# Extract TCGA barcode from Patient_description
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
    hist_norm = hist.strip()
    if hist_norm == '' or hist_norm.upper().startswith('[NOT'):
        continue
    if barcode not in patient_hist:
        patient_hist[barcode] = hist_norm

# Build set of mutated participants (use only participant part of barcode)
mutated_participants = set()
for r in muts:
    pb = r.get('ParticipantBarcode')
    if not pb:
        continue
    # ParticipantBarcode may be full TCGA-XX-XXXX or include extra parts; extract core barcode
    m = barcode_re.search(pb)
    if m:
        mutated_participants.add(m.group(1))
    else:
        mutated_participants.add(pb)

# Build dataframe
rows = []
for bc, hist in patient_hist.items():
    rows.append({'barcode': bc, 'histological_type': hist, 'mutated': (bc in mutated_participants)})

df = pd.DataFrame(rows)

if df.empty:
    result = {'error': 'No matching female BRCA patients with histological type found.'}
    print('__RESULT__:')
    print(json.dumps(result))
else:
    # contingency
    ct = pd.crosstab(df['histological_type'], df['mutated'])
    # Ensure columns for False and True
    if True not in ct.columns:
        ct[True] = 0
    if False not in ct.columns:
        ct[False] = 0
    # Keep only these two columns
    ct = ct[[True, False]].copy()
    # Compute row totals
    ct['row_total'] = ct[True] + ct[False]
    # Filter rows with row_total > 10
    included = ct[ct['row_total'] > 10].copy()
    excluded = ct[ct['row_total'] <= 10].copy()

    if included.shape[0] == 0:
        result = {'error': 'No histological categories with total > 10 after filtering.'}
        print('__RESULT__:')
        print(json.dumps(result))
    else:
        # Prepare calculations
        grand_total = int(included[True].sum() + included[False].sum())
        col_totals = { 'mutated': int(included[True].sum()), 'not_mutated': int(included[False].sum()) }
        chi2 = 0.0
        contingency = {}
        for idx, row in included.iterrows():
            mutated_obs = int(row[True])
            not_mut_obs = int(row[False])
            row_total = int(row['row_total'])
            # expected values
            exp_mut = (row_total * col_totals['mutated']) / grand_total if grand_total>0 else 0
            exp_not = (row_total * col_totals['not_mutated']) / grand_total if grand_total>0 else 0
            # accumulate chi2
            if exp_mut > 0:
                chi2 += (mutated_obs - exp_mut) ** 2 / exp_mut
            if exp_not > 0:
                chi2 += (not_mut_obs - exp_not) ** 2 / exp_not
            contingency[idx] = {'mutated': mutated_obs, 'not_mutated': not_mut_obs, 'row_total': row_total}

        excluded_list = []
        for idx, row in excluded.iterrows():
            excluded_list.append({'histological_type': idx, 'mutated': int(row.get(True,0)), 'not_mutated': int(row.get(False,0)), 'row_total': int(row.get('row_total', int(row.get(True,0))+int(row.get(False,0)) ))})

        result = {
            'chi2': round(chi2, 6),
            'grand_total': grand_total,
            'mutated_total': col_totals['mutated'],
            'not_mutated_total': col_totals['not_mutated'],
            'included_histological_types_count': len(contingency),
            'included_contingency': contingency,
            'excluded_histological_types': excluded_list
        }
        print('__RESULT__:')
        print(json.dumps(result))"""

env_args = {'var_call_J8cq91Qkykr7BmOMwRiN41M3': ['clinical_info'], 'var_call_ieTXnMdiVrVRJFhMg9brgKK2': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_TCYUIakYKMmCmy1cTDzmJsFS': 'file_storage/call_TCYUIakYKMmCmy1cTDzmJsFS.json', 'var_call_Ofi87woW9fv2wFDGgz6Tk0LF': [], 'var_call_SZWtI8VXZWrjWsr94fvHxDva': 'file_storage/call_SZWtI8VXZWrjWsr94fvHxDva.json', 'var_call_7FWy9AkScfQSBbOSiTSaGCcS': 'file_storage/call_7FWy9AkScfQSBbOSiTSaGCcS.json'}

exec(code, env_args)
