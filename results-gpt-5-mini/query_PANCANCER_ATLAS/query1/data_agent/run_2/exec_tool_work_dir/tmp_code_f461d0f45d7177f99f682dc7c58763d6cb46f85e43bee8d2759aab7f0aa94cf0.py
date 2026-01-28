code = """import json
# load clinical barcode->histology mapping from previous step
clinical_path = var_call_Qd40VIsDMsMVf7OX1aObGxPF
with open(clinical_path,'r') as f:
    clinical = json.load(f)
barcode_hist = clinical['barcode_histology']
# load IGF2 expression data
expr_path = var_call_1tC2u5aEGupn1UqDPC0xilt6
with open(expr_path,'r') as f:
    expr = json.load(f)

# Build mapping from patient barcode (first 12 chars) to normalized_count
expr_map = {}
for rec in expr:
    pb = rec.get('ParticipantBarcode')
    val = rec.get('normalized_count')
    try:
        num = float(val)
    except:
        continue
    # Standardize barcode to first 12 chars (TCGA-XX-XXXX)
    key = pb
    if len(pb) > 12:
        key = pb[:12]
    expr_map.setdefault(key, []).append(num)

# For each clinical barcode, find matching expression using first 12 chars
import math
from collections import defaultdict
hist_values = defaultdict(list)
missing_count = 0
for full_barcode, hist in barcode_hist.items():
    key = full_barcode[:12]
    if key in expr_map:
        # if multiple entries per participant, use mean of them
        vals = expr_map[key]
        mean_val = sum(vals)/len(vals)
        # exclude invalid IGF2 expression values: consider NaN or negative? only include valid floats
        if mean_val is None or (isinstance(mean_val,float) and (math.isnan(mean_val))):
            missing_count += 1
            continue
        log10_val = math.log10(mean_val + 1)
        hist_values[hist].append(log10_val)
    else:
        missing_count += 1

# Compute averages per histology with at least four decimal places
results = {}
for hist, vals in hist_values.items():
    if len(vals) == 0:
        continue
    avg = sum(vals)/len(vals)
    results[hist] = round(avg, 6)  # keep extra precision

out = {'per_histology_avg_log10_IGF2': results, 'num_histologies': len(results), 'samples_used_total': sum(len(v) for v in hist_values.values()), 'missing_matches': missing_count}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_fVUg1ESSxCeIbmVdPzMpKAFp': ['clinical_info'], 'var_call_8o2sYAglsRp5YoKFlvGlezXD': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_cG2ZfbXIdax07gqSUvs6mi6d': 'file_storage/call_cG2ZfbXIdax07gqSUvs6mi6d.json', 'var_call_TxCOCTzUgijRtJqc3JxcGFco': 'file_storage/call_TxCOCTzUgijRtJqc3JxcGFco.json', 'var_call_KJVqY154j6lyEW1kCxYgJfDS': 'file_storage/call_KJVqY154j6lyEW1kCxYgJfDS.json', 'var_call_Qd40VIsDMsMVf7OX1aObGxPF': 'file_storage/call_Qd40VIsDMsMVf7OX1aObGxPF.json', 'var_call_1tC2u5aEGupn1UqDPC0xilt6': 'file_storage/call_1tC2u5aEGupn1UqDPC0xilt6.json'}

exec(code, env_args)
