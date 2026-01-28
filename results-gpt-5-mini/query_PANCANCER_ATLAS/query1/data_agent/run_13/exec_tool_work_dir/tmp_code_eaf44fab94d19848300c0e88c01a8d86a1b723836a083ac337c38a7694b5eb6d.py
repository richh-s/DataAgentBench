code = """import json, re, math

# Load clinical LGG entries
with open(var_call_UW0rCoSMeoIaDXfSy2vRms2U, 'r') as f:
    clinical = json.load(f)

# Load IGF2 expression rows
with open(var_call_BA8rP6MwaAIgVDnRCEno7LK3, 'r') as f:
    expr = json.load(f)

# Build mapping from ParticipantBarcode (extracted from Patient_description) to histological_type
barcode_to_hist = {}
pattern = re.compile(r'(TCGA[-A-Z0-9]+)', re.IGNORECASE)
for rec in clinical:
    desc = rec.get('Patient_description', '')
    hist = rec.get('histological_type')
    if not hist:
        continue
    hist_str = hist.strip()
    # exclude histologies enclosed in square brackets entirely
    if re.match(r'^\[.*\]$', hist_str):
        continue
    m = pattern.search(desc)
    if not m:
        # try to construct from patient_id if present (some entries show patient_id like A4XH)
        pid = rec.get('patient_id')
        if pid:
            # find prefix in description like 'TCGA-' followed by something ending with patient_id
            m2 = re.search(r'(TCGA[-A-Z0-9]+{}\b)'.format(re.escape(pid)), desc, re.IGNORECASE)
            if m2:
                barcode = m2.group(1).upper()
            else:
                continue
        else:
            continue
    else:
        barcode = m.group(1).upper()
    barcode_to_hist[barcode] = hist_str

# Now aggregate log10(normalized_count + 1) for IGF2 for participants in barcode_to_hist
hist_values = {}
for r in expr:
    pb = r.get('ParticipantBarcode')
    if not pb:
        continue
    pb_up = pb.upper()
    if pb_up not in barcode_to_hist:
        continue
    nc = r.get('normalized_count')
    try:
        count = float(nc)
    except Exception:
        continue
    # skip invalid (NaN, negative?) normalized_count - negative shouldn't happen but guard
    if math.isnan(count):
        continue
    if count < 0:
        continue
    logv = math.log10(count + 1.0)
    hist = barcode_to_hist[pb_up]
    hist_values.setdefault(hist, []).append(logv)

# Compute mean per histology
hist_means = {}
for hist, vals in hist_values.items():
    if len(vals) == 0:
        continue
    meanv = sum(vals) / len(vals)
    # format with at least four decimal places; keep 6 for safety
    hist_means[hist] = round(meanv, 6)

# Prepare JSON serializable string
result_json = json.dumps(hist_means, ensure_ascii=False)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_jsC6Q7AngeAbejVzafXMsSId': 'file_storage/call_jsC6Q7AngeAbejVzafXMsSId.json', 'var_call_LMftCnOLplk9HTdxTwbXmfMw': 'file_storage/call_LMftCnOLplk9HTdxTwbXmfMw.json', 'var_call_UW0rCoSMeoIaDXfSy2vRms2U': 'file_storage/call_UW0rCoSMeoIaDXfSy2vRms2U.json', 'var_call_BA8rP6MwaAIgVDnRCEno7LK3': 'file_storage/call_BA8rP6MwaAIgVDnRCEno7LK3.json'}

exec(code, env_args)
