code = """import json, math, re

# Load clinical LGG data
data_clinical = None
if isinstance(var_call_uRDZRyxqSDxIhOR55FH4laEi, str):
    with open(var_call_uRDZRyxqSDxIhOR55FH4laEi, 'r') as f:
        data_clinical = json.load(f)
else:
    data_clinical = var_call_uRDZRyxqSDxIhOR55FH4laEi

# Load IGF2 RNA data
data_rna = None
if isinstance(var_call_IxvjvcpWMQuOmfR84OBUeKIA, str):
    with open(var_call_IxvjvcpWMQuOmfR84OBUeKIA, 'r') as f:
        data_rna = json.load(f)
else:
    data_rna = var_call_IxvjvcpWMQuOmfR84OBUeKIA

# Build mapping from ParticipantBarcode -> histological_type using clinical data
barcode_to_hist = {}
pattern = re.compile(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}', re.IGNORECASE)
for rec in data_clinical:
    desc = rec.get('Patient_description','') or ''
    hist = rec.get('histological_type')
    if not hist:
        continue
    # Exclude histologies enclosed in square brackets
    if isinstance(hist, str) and re.match(r'^\[.*\]$', hist.strip()):
        continue
    # find barcode
    m = pattern.search(desc)
    if m:
        barcode = m.group(0).upper()
        barcode_to_hist[barcode] = hist.strip()

# Aggregate log10(normalized_count + 1) by histology
hist_vals = {}
for rec in data_rna:
    p = rec.get('ParticipantBarcode')
    if not p:
        continue
    p_up = p.upper()
    if p_up not in barcode_to_hist:
        continue
    hist = barcode_to_hist[p_up]
    val = rec.get('normalized_count')
    if val is None:
        continue
    try:
        valf = float(val)
    except:
        continue
    # Only include valid numeric
    if math.isnan(valf):
        continue
    logv = math.log10(valf + 1.0)
    hist_vals.setdefault(hist, []).append(logv)

# Compute means with at least 4 decimal places
result = {}
for hist, vals in hist_vals.items():
    if len(vals) == 0:
        continue
    meanv = sum(vals)/len(vals)
    # Round to 4 decimal places
    result[hist] = round(meanv, 4)

# Sort results by histology name for consistency
result_sorted = {k: result[k] for k in sorted(result.keys())}

print("__RESULT__:")
print(json.dumps(result_sorted))"""

env_args = {'var_call_UtQigmJKu9SZyE0EBsCGDf2Q': ['clinical_info'], 'var_call_LyqR2BO1Ll4gbOAPXsHYUNwj': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_Y56AGSNipVAYPT0U3RCcAsBS': 'file_storage/call_Y56AGSNipVAYPT0U3RCcAsBS.json', 'var_call_rRsBnwuP1zXdl1sSMRGXCytY': 'file_storage/call_rRsBnwuP1zXdl1sSMRGXCytY.json', 'var_call_9TEuIvHU5uTgYOHUujy4wWDf': 'file_storage/call_9TEuIvHU5uTgYOHUujy4wWDf.json', 'var_call_IxvjvcpWMQuOmfR84OBUeKIA': 'file_storage/call_IxvjvcpWMQuOmfR84OBUeKIA.json', 'var_call_uRDZRyxqSDxIhOR55FH4laEi': 'file_storage/call_uRDZRyxqSDxIhOR55FH4laEi.json'}

exec(code, env_args)
