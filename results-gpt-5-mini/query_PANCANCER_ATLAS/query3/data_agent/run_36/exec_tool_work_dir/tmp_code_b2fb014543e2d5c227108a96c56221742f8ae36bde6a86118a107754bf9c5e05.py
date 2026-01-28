code = """import json, re
import pandas as pd

clinical_path = var_call_SZWtI8VXZWrjWsr94fvHxDva
mut_path = var_call_7FWy9AkScfQSBbOSiTSaGCcS

with open(clinical_path, 'r') as f:
    clinical = json.load(f)
with open(mut_path, 'r') as f:
    muts = json.load(f)

barcode_re = re.compile(r'(TCGA-[A-Za-z0-9]{2}-[A-Za-z0-9]{3,6})')

patient_hist = {}
processed = 0
for r in clinical:
    processed += 1
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

mutated_participants = set()
for r in muts:
    pb = r.get('ParticipantBarcode')
    if not pb:
        continue
    m = barcode_re.search(pb)
    if m:
        mutated_participants.add(m.group(1))
    else:
        mutated_participants.add(pb)

rows = []
for bc, hist in patient_hist.items():
    rows.append({'barcode': bc, 'histological_type': hist, 'mutated': (bc in mutated_participants)})

# gather diagnostics
try:
    df = pd.DataFrame(rows)
    df_sample = df.head(10).to_dict(orient='records')
    unique_hists = list(df['histological_type'].value_counts().head(20).to_dict().items())
    diag = {
        'clinical_records_processed': processed,
        'patient_hist_count': len(patient_hist),
        'mutated_participants_count': len(mutated_participants),
        'df_rows': len(df),
        'unique_hist_top20': unique_hists,
        'df_sample': df_sample
    }
except Exception as e:
    diag = {'error': str(e), 'clinical_records_processed': processed, 'patient_hist_count': len(patient_hist), 'mutated_participants_count': len(mutated_participants), 'rows_built': len(rows)}

print('__RESULT__:')
print(json.dumps(diag))"""

env_args = {'var_call_J8cq91Qkykr7BmOMwRiN41M3': ['clinical_info'], 'var_call_ieTXnMdiVrVRJFhMg9brgKK2': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_TCYUIakYKMmCmy1cTDzmJsFS': 'file_storage/call_TCYUIakYKMmCmy1cTDzmJsFS.json', 'var_call_Ofi87woW9fv2wFDGgz6Tk0LF': [], 'var_call_SZWtI8VXZWrjWsr94fvHxDva': 'file_storage/call_SZWtI8VXZWrjWsr94fvHxDva.json', 'var_call_7FWy9AkScfQSBbOSiTSaGCcS': 'file_storage/call_7FWy9AkScfQSBbOSiTSaGCcS.json'}

exec(code, env_args)
