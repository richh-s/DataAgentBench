code = """import json
import re
import pandas as pd

# Load clinical query result from file
with open(var_call_fO8dvmfFgvNG7fkalMN9y0im, 'r') as f:
    clinical = json.load(f)

# Load mutation list (variable provided directly)
mutation_list = var_call_ulAonLM7JQNB5eBzSkmhi9Dj

# Build mutation set of participant barcodes
mut_set = set()
for d in mutation_list:
    pb = d.get('ParticipantBarcode')
    if pb:
        mut_set.add(pb.strip())

# Extract barcode and histological_type from clinical Patient_description entries
rows = []
for rec in clinical:
    pd_desc = rec.get('Patient_description', '')
    hist = rec.get('histological_type')
    m = re.search(r"(TCGA-[A-Za-z0-9\-]+)", pd_desc)
    if m:
        barcode = m.group(1).strip().strip(',')
        rows.append({'barcode': barcode, 'hist': hist})

df = pd.DataFrame(rows).drop_duplicates(subset='barcode')

# Filter known histological types
bad = set(['None', '[Not Applicable]', 'Unknown', 'Not Reported', '', 'nan', 'NA'])
# Normalize hist
df['hist_clean'] = df['hist'].astype(str).str.strip()
# Remove entries with bad hist values or where hist is empty or contains 'None' etc.
mask_known = ~df['hist_clean'].isin(bad)
# Also exclude entries that literally contain '[Not Applicable]'
mask_known = mask_known & (~df['hist_clean'].str.contains('\[Not Applicable\]', na=False))

df = df[mask_known].copy()

# Determine mutation presence
df['mutated'] = df['barcode'].isin(mut_set).astype(int)

# Build contingency table
ct = df.pivot_table(index='hist_clean', columns='mutated', values='barcode', aggfunc='count', fill_value=0)
for c in [0,1]:
    if c not in ct.columns:
        ct[c] = 0
ct = ct[[0,1]]
ct['row_total'] = ct[0] + ct[1]

# Exclude categories with marginal totals <= 10 (apply to rows)
included = ct[ct['row_total'] > 10].copy()
excluded = ct[ct['row_total'] <= 10].copy()

# Compute chi-square statistic on included table
grand = int(included[[0,1]].values.sum())
col_totals = {0: int(included[0].sum()), 1: int(included[1].sum())}
chi2 = 0.0
if grand > 0:
    for idx, row in included.iterrows():
        row_total = int(row['row_total'])
        for col in [0,1]:
            O = int(row[col])
            E = (row_total * col_totals[col]) / grand if grand > 0 else 0
            if E > 0:
                chi2 += (O - E) ** 2 / E

# Prepare output
contingency = {idx: [int(row[0]), int(row[1])] for idx, row in included.iterrows()}
result = {
    'chi2': chi2,
    'grand_total': grand,
    'col_totals': {'no_mut': col_totals[0], 'mut': col_totals[1]},
    'contingency_table': contingency,
    'included_hist_types': list(included.index),
    'excluded_hist_types': list(excluded.index)
}

print("----BEGIN PRINT FORMAT----")
print("print(\"__RESULT__:\")")
print('print(' + json.dumps(json.dumps(result)) + ')')
print("----END PRINT FORMAT----")"""

env_args = {'var_call_NaHj9XgGdsswQDR51E0cRArQ': ['clinical_info'], 'var_call_54ZssE9u3MxiSdHOI1YRwGn7': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_eEQQ4yLhb4HJmOl2WlL5Iv8T': 'file_storage/call_eEQQ4yLhb4HJmOl2WlL5Iv8T.json', 'var_call_fO8dvmfFgvNG7fkalMN9y0im': 'file_storage/call_fO8dvmfFgvNG7fkalMN9y0im.json', 'var_call_ulAonLM7JQNB5eBzSkmhi9Dj': [{'ParticipantBarcode': 'TCGA-E2-A1L8'}, {'ParticipantBarcode': 'TCGA-B6-A0X7'}, {'ParticipantBarcode': 'TCGA-LL-A9Q3'}, {'ParticipantBarcode': 'TCGA-A2-A0CK'}, {'ParticipantBarcode': 'TCGA-BH-A0HP'}, {'ParticipantBarcode': 'TCGA-AC-A2FO'}, {'ParticipantBarcode': 'TCGA-D8-A27G'}, {'ParticipantBarcode': 'TCGA-A2-A4S2'}, {'ParticipantBarcode': 'TCGA-A7-A425'}, {'ParticipantBarcode': 'TCGA-BS-A0UV'}, {'ParticipantBarcode': 'TCGA-CD-A4MG'}, {'ParticipantBarcode': 'TCGA-B9-A8YI'}, {'ParticipantBarcode': 'TCGA-A2-A25A'}, {'ParticipantBarcode': 'TCGA-A5-A1OF'}, {'ParticipantBarcode': 'TCGA-B0-5692'}, {'ParticipantBarcode': 'TCGA-BR-A4J9'}, {'ParticipantBarcode': 'TCGA-BR-A453'}, {'ParticipantBarcode': 'TCGA-EE-A29E'}, {'ParticipantBarcode': 'TCGA-BF-A3DL'}, {'ParticipantBarcode': 'TCGA-F1-6874'}, {'ParticipantBarcode': 'TCGA-F5-6814'}, {'ParticipantBarcode': 'TCGA-66-2759'}, {'ParticipantBarcode': 'TCGA-E9-A5FK'}, {'ParticipantBarcode': 'TCGA-CA-6717'}, {'ParticipantBarcode': 'TCGA-CG-4474'}, {'ParticipantBarcode': 'TCGA-E1-A7YJ'}, {'ParticipantBarcode': 'TCGA-BR-8364'}, {'ParticipantBarcode': 'TCGA-77-A5G1'}, {'ParticipantBarcode': 'TCGA-A2-A0T4'}, {'ParticipantBarcode': 'TCGA-B6-A0RQ'}, {'ParticipantBarcode': 'TCGA-G9-6365'}, {'ParticipantBarcode': 'TCGA-WT-AB44'}, {'ParticipantBarcode': 'TCGA-AC-A2FF'}, {'ParticipantBarcode': 'TCGA-AP-A0LM'}, {'ParticipantBarcode': 'TCGA-D7-6518'}, {'ParticipantBarcode': 'TCGA-A6-5661'}, {'ParticipantBarcode': 'TCGA-E9-A2JT'}, {'ParticipantBarcode': 'TCGA-LD-A66U'}, {'ParticipantBarcode': 'TCGA-BR-6803'}, {'ParticipantBarcode': 'TCGA-DD-AAE3'}, {'ParticipantBarcode': 'TCGA-AR-A5QM'}, {'ParticipantBarcode': 'TCGA-GC-A3I6'}, {'ParticipantBarcode': 'TCGA-3M-AB47'}, {'ParticipantBarcode': 'TCGA-A2-A1G0'}, {'ParticipantBarcode': 'TCGA-AC-A2B8'}, {'ParticipantBarcode': 'TCGA-A2-A0SY'}, {'ParticipantBarcode': 'TCGA-D7-8574'}, {'ParticipantBarcode': 'TCGA-BH-A0E9'}, {'ParticipantBarcode': 'TCGA-EE-A2A6'}, {'ParticipantBarcode': 'TCGA-AH-6544'}, {'ParticipantBarcode': 'TCGA-EW-A1J5'}, {'ParticipantBarcode': 'TCGA-VQ-A924'}, {'ParticipantBarcode': 'TCGA-BH-AB28'}, {'ParticipantBarcode': 'TCGA-95-7567'}, {'ParticipantBarcode': 'TCGA-AC-A8OS'}, {'ParticipantBarcode': 'TCGA-R5-A804'}, {'ParticipantBarcode': 'TCGA-BH-A0C1'}, {'ParticipantBarcode': 'TCGA-CC-5260'}, {'ParticipantBarcode': 'TCGA-EO-A22U'}, {'ParticipantBarcode': 'TCGA-BH-A209'}, {'ParticipantBarcode': 'TCGA-BR-4188'}, {'ParticipantBarcode': 'TCGA-D7-A748'}, {'ParticipantBarcode': 'TCGA-50-6590'}, {'ParticipantBarcode': 'TCGA-A2-A0EW'}, {'ParticipantBarcode': 'TCGA-AC-A5XS'}, {'ParticipantBarcode': 'TCGA-F4-6570'}, {'ParticipantBarcode': 'TCGA-VQ-A8PO'}, {'ParticipantBarcode': 'TCGA-DK-A6AW'}, {'ParticipantBarcode': 'TCGA-A2-A0YK'}, {'ParticipantBarcode': 'TCGA-BR-8370'}, {'ParticipantBarcode': 'TCGA-B6-A2IU'}, {'ParticipantBarcode': 'TCGA-C8-A1HO'}, {'ParticipantBarcode': 'TCGA-AO-A128'}, {'ParticipantBarcode': 'TCGA-CN-6024'}, {'ParticipantBarcode': 'TCGA-21-5787'}, {'ParticipantBarcode': 'TCGA-A2-A0CR'}, {'ParticipantBarcode': 'TCGA-DF-A2KV'}, {'ParticipantBarcode': 'TCGA-D8-A1XO'}, {'ParticipantBarcode': 'TCGA-D8-A1Y1'}, {'ParticipantBarcode': 'TCGA-HT-A617'}, {'ParticipantBarcode': 'TCGA-BR-8686'}, {'ParticipantBarcode': 'TCGA-AR-A2LN'}, {'ParticipantBarcode': 'TCGA-E6-A1LX'}, {'ParticipantBarcode': 'TCGA-AC-A2FG'}, {'ParticipantBarcode': 'TCGA-LD-A7W6'}, {'ParticipantBarcode': 'TCGA-OL-A6VQ'}, {'ParticipantBarcode': 'TCGA-B5-A11G'}, {'ParticipantBarcode': 'TCGA-PE-A5DE'}, {'ParticipantBarcode': 'TCGA-4H-AAAK'}, {'ParticipantBarcode': 'TCGA-05-5428'}, {'ParticipantBarcode': 'TCGA-B5-A1MW'}, {'ParticipantBarcode': 'TCGA-XF-A9SX'}, {'ParticipantBarcode': 'TCGA-EW-A423'}, {'ParticipantBarcode': 'TCGA-GM-A4E0'}, {'ParticipantBarcode': 'TCGA-FI-A2D5'}, {'ParticipantBarcode': 'TCGA-BR-8058'}, {'ParticipantBarcode': 'TCGA-C4-A0F0'}, {'ParticipantBarcode': 'TCGA-EY-A5W2'}, {'ParticipantBarcode': 'TCGA-FI-A2D0'}, {'ParticipantBarcode': 'TCGA-S3-A6ZG'}, {'ParticipantBarcode': 'TCGA-BR-8592'}, {'ParticipantBarcode': 'TCGA-BR-A4QM'}, {'ParticipantBarcode': 'TCGA-DD-AADI'}, {'ParticipantBarcode': 'TCGA-77-8009'}, {'ParticipantBarcode': 'TCGA-AX-A1CE'}, {'ParticipantBarcode': 'TCGA-E2-A576'}, {'ParticipantBarcode': 'TCGA-KQ-A41S'}, {'ParticipantBarcode': 'TCGA-LL-A50Y'}, {'ParticipantBarcode': 'TCGA-A2-A1FV'}, {'ParticipantBarcode': 'TCGA-BH-A18P'}, {'ParticipantBarcode': 'TCGA-DU-6392'}, {'ParticipantBarcode': 'TCGA-EB-A5UM'}, {'ParticipantBarcode': 'TCGA-XF-A9T3'}, {'ParticipantBarcode': 'TCGA-AR-A1AT'}, {'ParticipantBarcode': 'TCGA-GM-A2DO'}, {'ParticipantBarcode': 'TCGA-GM-A2DD'}, {'ParticipantBarcode': 'TCGA-CD-5813'}, {'ParticipantBarcode': 'TCGA-D1-A103'}, {'ParticipantBarcode': 'TCGA-Z7-A8R5'}, {'ParticipantBarcode': 'TCGA-BH-A28Q'}, {'ParticipantBarcode': 'TCGA-BR-6452'}, {'ParticipantBarcode': 'TCGA-EW-A6SC'}, {'ParticipantBarcode': 'TCGA-IN-7808'}, {'ParticipantBarcode': 'TCGA-E9-A3X8'}, {'ParticipantBarcode': 'TCGA-PE-A5DD'}, {'ParticipantBarcode': 'TCGA-QF-A5YS'}, {'ParticipantBarcode': 'TCGA-BS-A0U8'}, {'ParticipantBarcode': 'TCGA-OL-A66K'}, {'ParticipantBarcode': 'TCGA-DD-A4NK'}, {'ParticipantBarcode': 'TCGA-42-2590'}, {'ParticipantBarcode': 'TCGA-IR-A3LH'}, {'ParticipantBarcode': 'TCGA-AC-A4ZE'}, {'ParticipantBarcode': 'TCGA-AC-A6IV'}, {'ParticipantBarcode': 'TCGA-AX-A0J0'}, {'ParticipantBarcode': 'TCGA-C8-A3M7'}, {'ParticipantBarcode': 'TCGA-CK-6747'}, {'ParticipantBarcode': 'TCGA-BR-4187'}, {'ParticipantBarcode': 'TCGA-D7-8572'}, {'ParticipantBarcode': 'TCGA-X6-A8C2'}, {'ParticipantBarcode': 'TCGA-EW-A1IZ'}, {'ParticipantBarcode': 'TCGA-G2-A3IE'}, {'ParticipantBarcode': 'TCGA-D8-A3Z6'}, {'ParticipantBarcode': 'TCGA-FS-A1ZK'}, {'ParticipantBarcode': 'TCGA-XX-A89A'}, {'ParticipantBarcode': 'TCGA-EB-A3XC'}, {'ParticipantBarcode': 'TCGA-SJ-A6ZI'}, {'ParticipantBarcode': 'TCGA-A7-A5ZX'}, {'ParticipantBarcode': 'TCGA-E2-A10F'}, {'ParticipantBarcode': 'TCGA-MX-A5UG'}, {'ParticipantBarcode': 'TCGA-AD-6964'}, {'ParticipantBarcode': 'TCGA-63-A5MM'}, {'ParticipantBarcode': 'TCGA-06-0210'}, {'ParticipantBarcode': 'TCGA-D7-A4YU'}, {'ParticipantBarcode': 'TCGA-H4-A2HQ'}, {'ParticipantBarcode': 'TCGA-W8-A86G'}, {'ParticipantBarcode': 'TCGA-BH-A18F'}, {'ParticipantBarcode': 'TCGA-AA-A01R'}, {'ParticipantBarcode': 'TCGA-AR-A2LK'}, {'ParticipantBarcode': 'TCGA-HQ-A2OF'}, {'ParticipantBarcode': 'TCGA-LD-A74U'}, {'ParticipantBarcode': 'TCGA-CD-5799'}, {'ParticipantBarcode': 'TCGA-AR-A2LE'}, {'ParticipantBarcode': 'TCGA-FP-8210'}, {'ParticipantBarcode': 'TCGA-A2-A0YD'}, {'ParticipantBarcode': 'TCGA-A2-A0YL'}, {'ParticipantBarcode': 'TCGA-EJ-7782'}, {'ParticipantBarcode': 'TCGA-G4-6628'}, {'ParticipantBarcode': 'TCGA-B6-A0IH'}, {'ParticipantBarcode': 'TCGA-VQ-A8PX'}, {'ParticipantBarcode': 'TCGA-CV-6937'}, {'ParticipantBarcode': 'TCGA-BB-A5HY'}, {'ParticipantBarcode': 'TCGA-IB-7651'}, {'ParticipantBarcode': 'TCGA-RP-A694'}, {'ParticipantBarcode': 'TCGA-EY-A548'}, {'ParticipantBarcode': 'TCGA-G4-6586'}, {'ParticipantBarcode': 'TCGA-BS-A0TE'}, {'ParticipantBarcode': 'TCGA-DD-AADA'}, {'ParticipantBarcode': 'TCGA-D7-6522'}, {'ParticipantBarcode': 'TCGA-2Y-A9H5'}, {'ParticipantBarcode': 'TCGA-A1-A0SE'}, {'ParticipantBarcode': 'TCGA-E2-A1IJ'}, {'ParticipantBarcode': 'TCGA-B5-A0JY'}, {'ParticipantBarcode': 'TCGA-AC-A6IX'}, {'ParticipantBarcode': 'TCGA-EO-A22R'}, {'ParticipantBarcode': 'TCGA-AC-A3OD'}, {'ParticipantBarcode': 'TCGA-GI-A2C8'}, {'ParticipantBarcode': 'TCGA-B5-A11E'}, {'ParticipantBarcode': 'TCGA-AC-A3QQ'}, {'ParticipantBarcode': 'TCGA-AR-A1AL'}, {'ParticipantBarcode': 'TCGA-BH-A8FY'}, {'ParticipantBarcode': 'TCGA-D8-A27I'}, {'ParticipantBarcode': 'TCGA-F4-6856'}, {'ParticipantBarcode': 'TCGA-OD-A75X'}, {'ParticipantBarcode': 'TCGA-55-A4DF'}, {'ParticipantBarcode': 'TCGA-5L-AAT0'}, {'ParticipantBarcode': 'TCGA-AX-A06L'}, {'ParticipantBarcode': 'TCGA-C8-A274'}, {'ParticipantBarcode': 'TCGA-XX-A899'}, {'ParticipantBarcode': 'TCGA-AX-A2HA'}, {'ParticipantBarcode': 'TCGA-B6-A40C'}, {'ParticipantBarcode': 'TCGA-DK-A1AG'}, {'ParticipantBarcode': 'TCGA-A2-A0T6'}, {'ParticipantBarcode': 'TCGA-GM-A5PV'}, {'ParticipantBarcode': 'TCGA-D5-6928'}, {'ParticipantBarcode': 'TCGA-E9-A6HE'}, {'ParticipantBarcode': 'TCGA-94-7943'}, {'ParticipantBarcode': 'TCGA-E2-A1IH'}, {'ParticipantBarcode': 'TCGA-AC-A3YI'}, {'ParticipantBarcode': 'TCGA-EO-A3AZ'}, {'ParticipantBarcode': 'TCGA-AX-A2HC'}, {'ParticipantBarcode': 'TCGA-B7-A5TI'}, {'ParticipantBarcode': 'TCGA-D7-A6EY'}, {'ParticipantBarcode': 'TCGA-D8-A27V'}, {'ParticipantBarcode': 'TCGA-55-8614'}, {'ParticipantBarcode': 'TCGA-AA-A00N'}, {'ParticipantBarcode': 'TCGA-BR-6566'}, {'ParticipantBarcode': 'TCGA-BR-4292'}, {'ParticipantBarcode': 'TCGA-BR-4279'}, {'ParticipantBarcode': 'TCGA-A5-A0VO'}, {'ParticipantBarcode': 'TCGA-BR-8677'}, {'ParticipantBarcode': 'TCGA-BR-A4IV'}, {'ParticipantBarcode': 'TCGA-CR-7370'}, {'ParticipantBarcode': 'TCGA-OL-A66N'}, {'ParticipantBarcode': 'TCGA-GM-A5PX'}, {'ParticipantBarcode': 'TCGA-XF-AAN0'}, {'ParticipantBarcode': 'TCGA-63-A5MH'}, {'ParticipantBarcode': 'TCGA-AX-A2HD'}, {'ParticipantBarcode': 'TCGA-B5-A11F'}, {'ParticipantBarcode': 'TCGA-PG-A917'}, {'ParticipantBarcode': 'TCGA-AR-A24X'}, {'ParticipantBarcode': 'TCGA-06-5416'}, {'ParticipantBarcode': 'TCGA-DK-AA6Q'}, {'ParticipantBarcode': 'TCGA-B5-A11U'}, {'ParticipantBarcode': 'TCGA-EO-A22X'}, {'ParticipantBarcode': 'TCGA-NC-A5HD'}, {'ParticipantBarcode': 'TCGA-B6-A40B'}, {'ParticipantBarcode': 'TCGA-2W-A8YY'}, {'ParticipantBarcode': 'TCGA-A7-A4SC'}, {'ParticipantBarcode': 'TCGA-VQ-A91K'}, {'ParticipantBarcode': 'TCGA-P6-A5OH'}, {'ParticipantBarcode': 'TCGA-22-1016'}, {'ParticipantBarcode': 'TCGA-FP-A8CX'}, {'ParticipantBarcode': 'TCGA-BR-A44T'}, {'ParticipantBarcode': 'TCGA-FW-A3R5'}, {'ParticipantBarcode': 'TCGA-JX-A3Q0'}, {'ParticipantBarcode': 'TCGA-AC-A2FB'}, {'ParticipantBarcode': 'TCGA-LL-A6FP'}]}

exec(code, env_args)
