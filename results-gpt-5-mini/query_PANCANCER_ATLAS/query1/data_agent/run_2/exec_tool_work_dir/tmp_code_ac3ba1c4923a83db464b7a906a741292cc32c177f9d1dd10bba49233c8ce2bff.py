code = """import json, re
# var_call_KJVqY154j6lyEW1kCxYgJfDS is the storage key containing the clinical query result file path
path = var_call_KJVqY154j6lyEW1kCxYgJfDS
with open(path, 'r') as f:
    data = json.load(f)

barcode_hist = {}
barcodes = []
pattern = re.compile(r'TCGA-[A-Z0-9]{2}-[A-Za-z0-9]{4}')
for rec in data:
    desc = rec.get('Patient_description','')
    hist = rec.get('histological_type', None)
    if not desc:
        continue
    m = pattern.search(desc)
    if not m:
        continue
    barcode = m.group(0)
    if hist is None:
        continue
    hist_str = hist.strip()
    # Exclude histology annotations enclosed in square brackets (starting with '[')
    if hist_str.startswith('['):
        continue
    barcode_hist[barcode] = hist_str
    barcodes.append(barcode)

# ensure unique
barcodes = sorted(list(set(barcodes)))

out = {'barcodes': barcodes, 'barcode_histology': barcode_hist, 'count': len(barcodes)}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_fVUg1ESSxCeIbmVdPzMpKAFp': ['clinical_info'], 'var_call_8o2sYAglsRp5YoKFlvGlezXD': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_cG2ZfbXIdax07gqSUvs6mi6d': 'file_storage/call_cG2ZfbXIdax07gqSUvs6mi6d.json', 'var_call_TxCOCTzUgijRtJqc3JxcGFco': 'file_storage/call_TxCOCTzUgijRtJqc3JxcGFco.json', 'var_call_KJVqY154j6lyEW1kCxYgJfDS': 'file_storage/call_KJVqY154j6lyEW1kCxYgJfDS.json'}

exec(code, env_args)
