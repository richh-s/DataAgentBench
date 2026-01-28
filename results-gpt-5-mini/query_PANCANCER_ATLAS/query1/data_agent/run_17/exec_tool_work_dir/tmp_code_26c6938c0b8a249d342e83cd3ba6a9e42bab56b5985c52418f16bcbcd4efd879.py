code = """import json
import re

# Load clinical query result file
with open(var_call_3BdZADeMn017QPPTKqRsgZQD, 'r') as f:
    clinical = json.load(f)

# Extract TCGA barcode from Patient_description
barcode_re = re.compile(r'TCGA[-][0-9A-Z]{2,}-[0-9A-Z]{2,4}', re.IGNORECASE)

barcode_to_hist = {}
for row in clinical:
    desc = row.get('Patient_description','')
    hist = row.get('histological_type', '')
    if hist is None:
        continue
    hs = str(hist)
    # skip histologies with square brackets
    if '[' in hs or ']' in hs:
        continue
    m = barcode_re.search(desc)
    if m:
        barcode = m.group(0)
        # normalize barcode to uppercase
        barcode = barcode.upper()
        barcode_to_hist[barcode] = hs

barcodes = sorted(list(barcode_to_hist.keys()))

out = {'num_clinical_rows': len(clinical), 'num_barcodes_extracted': len(barcodes), 'barcodes': barcodes, 'barcode_to_hist': barcode_to_hist}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_CTiuVYQ0GzbevuBkPuuokkjQ': ['clinical_info'], 'var_call_HmLQhigU0Pu3WEKpxZ5We0HE': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_Aqx3og4knI7XgSyuA3gd75Lf': 'file_storage/call_Aqx3og4knI7XgSyuA3gd75Lf.json', 'var_call_qwlEvjfagCOisqlBUmRH2FPF': 'file_storage/call_qwlEvjfagCOisqlBUmRH2FPF.json', 'var_call_YQVTzrXK8Axnm8KDXDZKAgqk': {'num_lgg_matches_raw': 0, 'num_matches_after_hist_filter': 0, 'participant_barcodes': [], 'barcode_to_hist': {}}, 'var_call_0eWGehozTZ9q7pSljkAcAha6': 'file_storage/call_0eWGehozTZ9q7pSljkAcAha6.json', 'var_call_lNLHdfhJLZZN9Kscj9Ybxtgx': 'file_storage/call_lNLHdfhJLZZN9Kscj9Ybxtgx.json', 'var_call_3BdZADeMn017QPPTKqRsgZQD': 'file_storage/call_3BdZADeMn017QPPTKqRsgZQD.json'}

exec(code, env_args)
