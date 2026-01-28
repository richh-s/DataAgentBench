code = """import json
import pandas as pd
# Load previous tool results from storage
clinical_records_path = var_call_ppat7IwGCsLhXVcHpjKlKZW7
cdh1_list = var_call_BTqWqDdyYzkowV8oBjhNhtru

# read clinical records json file
with open(clinical_records_path, 'r') as f:
    clinical = json.load(f)

# clinical is list of dicts with Patient_description and histological_type
clin_df = pd.DataFrame(clinical)

# Extract TCGA barcodes from Patient_description using simple parsing
import re

def extract_barcode(text):
    m = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4,5})', text)
    if m:
        return m.group(1)
    # sometimes sample codes like TCGA-..-.... with letters; broaden
    m = re.search(r'(TCGA-[A-Z0-9-]+)', text)
    return m.group(1) if m else None

clin_df['ParticipantBarcode'] = clin_df['Patient_description'].apply(extract_barcode)

# normalize histological_type
clin_df['histological_type'] = clin_df['histological_type'].fillna('Unknown')

# Build set of CDH1 mutated participants
cdh1_set = set([d['ParticipantBarcode'] for d in cdh1_list])

# Filter to BRCA cohort: patient_description containing 'Breast' or 'BRCA' already from query
# But ensure ParticipantBarcode exists
clin_df = clin_df[clin_df['ParticipantBarcode'].notnull()].copy()

# Determine female entries by checking 'FEMALE' in Patient_description
clin_df['is_female'] = clin_df['Patient_description'].str.contains('FEMALE', case=False, na=False)
clin_df = clin_df[clin_df['is_female']]

# Only keep entries with known histological types
clin_df = clin_df[clin_df['histological_type'].str.strip().replace('','Unknown')!='Unknown']

# Map mutation presence
clin_df['CDH1_mutation'] = clin_df['ParticipantBarcode'].apply(lambda x: 'Mutated' if x in cdh1_set else 'Wildtype')

# Count by histological_type and mutation
ct = clin_df.groupby(['histological_type','CDH1_mutation']).size().unstack(fill_value=0)
ct = ct.reset_index()

# Exclude categories with marginal totals <= 10
ct['row_total'] = ct['Mutated'] + ct['Wildtype']
ct_filtered = ct[ct['row_total']>10].copy()

# Build contingency table
cont_table = ct_filtered.set_index('histological_type')[['Mutated','Wildtype']]

# Compute chi-square statistic manually
observed = cont_table.values.astype(float)
row_sums = observed.sum(axis=1, keepdims=True)
col_sums = observed.sum(axis=0, keepdims=True)
grand_total = observed.sum()

expected = row_sums.dot(col_sums)/grand_total

chi2 = ((observed - expected)**2 / expected).sum()

# Prepare output
out = {
    'num_histological_categories_used': int(cont_table.shape[0]),
    'categories': [],
    'grand_total': int(grand_total),
    'chi2_statistic': float(chi2)
}
for idx, row in cont_table.iterrows():
    out['categories'].append({
        'histological_type': idx,
        'Mutated': int(row['Mutated']),
        'Wildtype': int(row['Wildtype']),
        'row_total': int(row['Mutated']+row['Wildtype'])
    })

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_YKZFmDyAhCbDreYKMFmPU0nb': ['clinical_info'], 'var_call_XSIlbiyU2SY44Jc6CApc4gQm': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_ya2EgSYyFhC5q6bDbpG2PhJZ': 'file_storage/call_ya2EgSYyFhC5q6bDbpG2PhJZ.json', 'var_call_BTqWqDdyYzkowV8oBjhNhtru': [{'ParticipantBarcode': 'TCGA-AX-A2HD'}, {'ParticipantBarcode': 'TCGA-B5-A11F'}, {'ParticipantBarcode': 'TCGA-PG-A917'}, {'ParticipantBarcode': 'TCGA-P6-A5OH'}, {'ParticipantBarcode': 'TCGA-VQ-A91K'}, {'ParticipantBarcode': 'TCGA-A7-A4SC'}, {'ParticipantBarcode': 'TCGA-FP-A8CX'}, {'ParticipantBarcode': 'TCGA-BR-A44T'}, {'ParticipantBarcode': 'TCGA-FW-A3R5'}, {'ParticipantBarcode': 'TCGA-JX-A3Q0'}, {'ParticipantBarcode': 'TCGA-AC-A2FB'}, {'ParticipantBarcode': 'TCGA-22-1016'}, {'ParticipantBarcode': 'TCGA-DK-AA6Q'}, {'ParticipantBarcode': 'TCGA-06-5416'}, {'ParticipantBarcode': 'TCGA-B5-A11U'}, {'ParticipantBarcode': 'TCGA-EO-A22X'}, {'ParticipantBarcode': 'TCGA-NC-A5HD'}, {'ParticipantBarcode': 'TCGA-B6-A40B'}, {'ParticipantBarcode': 'TCGA-2W-A8YY'}, {'ParticipantBarcode': 'TCGA-AR-A24X'}, {'ParticipantBarcode': 'TCGA-LL-A6FP'}, {'ParticipantBarcode': 'TCGA-AH-6544'}, {'ParticipantBarcode': 'TCGA-R5-A804'}, {'ParticipantBarcode': 'TCGA-EW-A1J5'}, {'ParticipantBarcode': 'TCGA-CC-5260'}, {'ParticipantBarcode': 'TCGA-BH-A0C1'}, {'ParticipantBarcode': 'TCGA-AC-A5XS'}, {'ParticipantBarcode': 'TCGA-BH-A209'}, {'ParticipantBarcode': 'TCGA-BR-4188'}, {'ParticipantBarcode': 'TCGA-D7-A748'}, {'ParticipantBarcode': 'TCGA-50-6590'}, {'ParticipantBarcode': 'TCGA-A2-A0EW'}, {'ParticipantBarcode': 'TCGA-EO-A22U'}, {'ParticipantBarcode': 'TCGA-VQ-A924'}, {'ParticipantBarcode': 'TCGA-BH-AB28'}, {'ParticipantBarcode': 'TCGA-95-7567'}, {'ParticipantBarcode': 'TCGA-AC-A8OS'}, {'ParticipantBarcode': 'TCGA-C8-A1HO'}, {'ParticipantBarcode': 'TCGA-B6-A2IU'}, {'ParticipantBarcode': 'TCGA-21-5787'}, {'ParticipantBarcode': 'TCGA-A2-A0CR'}, {'ParticipantBarcode': 'TCGA-A2-A0YK'}, {'ParticipantBarcode': 'TCGA-BR-8370'}, {'ParticipantBarcode': 'TCGA-CN-6024'}, {'ParticipantBarcode': 'TCGA-AO-A128'}, {'ParticipantBarcode': 'TCGA-VQ-A8PO'}, {'ParticipantBarcode': 'TCGA-DK-A6AW'}, {'ParticipantBarcode': 'TCGA-F4-6570'}, {'ParticipantBarcode': 'TCGA-DF-A2KV'}, {'ParticipantBarcode': 'TCGA-LD-A7W6'}, {'ParticipantBarcode': 'TCGA-05-5428'}, {'ParticipantBarcode': 'TCGA-OL-A6VQ'}, {'ParticipantBarcode': 'TCGA-B5-A11G'}, {'ParticipantBarcode': 'TCGA-PE-A5DE'}, {'ParticipantBarcode': 'TCGA-4H-AAAK'}, {'ParticipantBarcode': 'TCGA-E6-A1LX'}, {'ParticipantBarcode': 'TCGA-D8-A1XO'}, {'ParticipantBarcode': 'TCGA-D8-A1Y1'}, {'ParticipantBarcode': 'TCGA-HT-A617'}, {'ParticipantBarcode': 'TCGA-BR-8686'}, {'ParticipantBarcode': 'TCGA-AR-A2LN'}, {'ParticipantBarcode': 'TCGA-AC-A2FG'}, {'ParticipantBarcode': 'TCGA-OL-A66K'}, {'ParticipantBarcode': 'TCGA-42-2590'}, {'ParticipantBarcode': 'TCGA-AX-A0J0'}, {'ParticipantBarcode': 'TCGA-BS-A0U8'}, {'ParticipantBarcode': 'TCGA-DD-A4NK'}, {'ParticipantBarcode': 'TCGA-IR-A3LH'}, {'ParticipantBarcode': 'TCGA-AC-A4ZE'}, {'ParticipantBarcode': 'TCGA-AC-A6IV'}, {'ParticipantBarcode': 'TCGA-IN-7808'}, {'ParticipantBarcode': 'TCGA-E9-A3X8'}, {'ParticipantBarcode': 'TCGA-PE-A5DD'}, {'ParticipantBarcode': 'TCGA-QF-A5YS'}, {'ParticipantBarcode': 'TCGA-BR-6452'}, {'ParticipantBarcode': 'TCGA-EW-A6SC'}, {'ParticipantBarcode': 'TCGA-B5-A1MW'}, {'ParticipantBarcode': 'TCGA-XF-A9SX'}, {'ParticipantBarcode': 'TCGA-FI-A2D0'}, {'ParticipantBarcode': 'TCGA-S3-A6ZG'}, {'ParticipantBarcode': 'TCGA-BR-8592'}, {'ParticipantBarcode': 'TCGA-77-8009'}, {'ParticipantBarcode': 'TCGA-AX-A1CE'}, {'ParticipantBarcode': 'TCGA-E2-A576'}, {'ParticipantBarcode': 'TCGA-KQ-A41S'}, {'ParticipantBarcode': 'TCGA-LL-A50Y'}, {'ParticipantBarcode': 'TCGA-FI-A2D5'}, {'ParticipantBarcode': 'TCGA-DD-AADI'}, {'ParticipantBarcode': 'TCGA-BR-A4QM'}, {'ParticipantBarcode': 'TCGA-GM-A4E0'}, {'ParticipantBarcode': 'TCGA-BR-8058'}, {'ParticipantBarcode': 'TCGA-C4-A0F0'}, {'ParticipantBarcode': 'TCGA-EY-A5W2'}, {'ParticipantBarcode': 'TCGA-EW-A423'}, {'ParticipantBarcode': 'TCGA-GM-A2DD'}, {'ParticipantBarcode': 'TCGA-BH-A28Q'}, {'ParticipantBarcode': 'TCGA-AR-A1AT'}, {'ParticipantBarcode': 'TCGA-D1-A103'}, {'ParticipantBarcode': 'TCGA-DU-6392'}, {'ParticipantBarcode': 'TCGA-Z7-A8R5'}, {'ParticipantBarcode': 'TCGA-CD-5813'}, {'ParticipantBarcode': 'TCGA-A2-A1FV'}, {'ParticipantBarcode': 'TCGA-BH-A18P'}, {'ParticipantBarcode': 'TCGA-EB-A5UM'}, {'ParticipantBarcode': 'TCGA-XF-A9T3'}, {'ParticipantBarcode': 'TCGA-GM-A2DO'}, {'ParticipantBarcode': 'TCGA-D8-A3Z6'}, {'ParticipantBarcode': 'TCGA-G2-A3IE'}, {'ParticipantBarcode': 'TCGA-X6-A8C2'}, {'ParticipantBarcode': 'TCGA-EW-A1IZ'}, {'ParticipantBarcode': 'TCGA-BR-4187'}, {'ParticipantBarcode': 'TCGA-D7-8572'}, {'ParticipantBarcode': 'TCGA-C8-A3M7'}, {'ParticipantBarcode': 'TCGA-CK-6747'}, {'ParticipantBarcode': 'TCGA-HQ-A2OF'}, {'ParticipantBarcode': 'TCGA-LD-A74U'}, {'ParticipantBarcode': 'TCGA-BB-A5HY'}, {'ParticipantBarcode': 'TCGA-IB-7651'}, {'ParticipantBarcode': 'TCGA-RP-A694'}, {'ParticipantBarcode': 'TCGA-A2-A0YL'}, {'ParticipantBarcode': 'TCGA-EJ-7782'}, {'ParticipantBarcode': 'TCGA-G4-6628'}, {'ParticipantBarcode': 'TCGA-VQ-A8PX'}, {'ParticipantBarcode': 'TCGA-CV-6937'}, {'ParticipantBarcode': 'TCGA-G4-6586'}, {'ParticipantBarcode': 'TCGA-BS-A0TE'}, {'ParticipantBarcode': 'TCGA-DD-AADA'}, {'ParticipantBarcode': 'TCGA-D7-6522'}, {'ParticipantBarcode': 'TCGA-2Y-A9H5'}, {'ParticipantBarcode': 'TCGA-EY-A548'}, {'ParticipantBarcode': 'TCGA-CD-5799'}, {'ParticipantBarcode': 'TCGA-AR-A2LE'}, {'ParticipantBarcode': 'TCGA-FP-8210'}, {'ParticipantBarcode': 'TCGA-A2-A0YD'}, {'ParticipantBarcode': 'TCGA-B6-A0IH'}, {'ParticipantBarcode': 'TCGA-A1-A0SE'}, {'ParticipantBarcode': 'TCGA-FS-A1ZK'}, {'ParticipantBarcode': 'TCGA-XX-A89A'}, {'ParticipantBarcode': 'TCGA-06-0210'}, {'ParticipantBarcode': 'TCGA-D7-A4YU'}, {'ParticipantBarcode': 'TCGA-H4-A2HQ'}, {'ParticipantBarcode': 'TCGA-63-A5MM'}, {'ParticipantBarcode': 'TCGA-BH-A18F'}, {'ParticipantBarcode': 'TCGA-AA-A01R'}, {'ParticipantBarcode': 'TCGA-W8-A86G'}, {'ParticipantBarcode': 'TCGA-SJ-A6ZI'}, {'ParticipantBarcode': 'TCGA-A7-A5ZX'}, {'ParticipantBarcode': 'TCGA-E2-A10F'}, {'ParticipantBarcode': 'TCGA-MX-A5UG'}, {'ParticipantBarcode': 'TCGA-AD-6964'}, {'ParticipantBarcode': 'TCGA-EB-A3XC'}, {'ParticipantBarcode': 'TCGA-AR-A2LK'}, {'ParticipantBarcode': 'TCGA-GM-A5PV'}, {'ParticipantBarcode': 'TCGA-EO-A3AZ'}, {'ParticipantBarcode': 'TCGA-AX-A2HC'}, {'ParticipantBarcode': 'TCGA-B7-A5TI'}, {'ParticipantBarcode': 'TCGA-55-8614'}, {'ParticipantBarcode': 'TCGA-E2-A1IH'}, {'ParticipantBarcode': 'TCGA-D7-A6EY'}, {'ParticipantBarcode': 'TCGA-D8-A27V'}, {'ParticipantBarcode': 'TCGA-D5-6928'}, {'ParticipantBarcode': 'TCGA-E9-A6HE'}, {'ParticipantBarcode': 'TCGA-94-7943'}, {'ParticipantBarcode': 'TCGA-AC-A3YI'}, {'ParticipantBarcode': 'TCGA-AA-A00N'}, {'ParticipantBarcode': 'TCGA-BR-6566'}, {'ParticipantBarcode': 'TCGA-E2-A1IJ'}, {'ParticipantBarcode': 'TCGA-D8-A27I'}, {'ParticipantBarcode': 'TCGA-BH-A8FY'}, {'ParticipantBarcode': 'TCGA-B5-A0JY'}, {'ParticipantBarcode': 'TCGA-B6-A40C'}, {'ParticipantBarcode': 'TCGA-DK-A1AG'}, {'ParticipantBarcode': 'TCGA-GI-A2C8'}, {'ParticipantBarcode': 'TCGA-AC-A3QQ'}, {'ParticipantBarcode': 'TCGA-AR-A1AL'}, {'ParticipantBarcode': 'TCGA-OD-A75X'}, {'ParticipantBarcode': 'TCGA-55-A4DF'}, {'ParticipantBarcode': 'TCGA-5L-AAT0'}, {'ParticipantBarcode': 'TCGA-AX-A06L'}, {'ParticipantBarcode': 'TCGA-C8-A274'}, {'ParticipantBarcode': 'TCGA-XX-A899'}, {'ParticipantBarcode': 'TCGA-AX-A2HA'}, {'ParticipantBarcode': 'TCGA-F4-6856'}, {'ParticipantBarcode': 'TCGA-AC-A6IX'}, {'ParticipantBarcode': 'TCGA-EO-A22R'}, {'ParticipantBarcode': 'TCGA-AC-A3OD'}, {'ParticipantBarcode': 'TCGA-B5-A11E'}, {'ParticipantBarcode': 'TCGA-A2-A0T6'}, {'ParticipantBarcode': 'TCGA-BR-4292'}, {'ParticipantBarcode': 'TCGA-CR-7370'}, {'ParticipantBarcode': 'TCGA-OL-A66N'}, {'ParticipantBarcode': 'TCGA-BR-A4IV'}, {'ParticipantBarcode': 'TCGA-GM-A5PX'}, {'ParticipantBarcode': 'TCGA-XF-AAN0'}, {'ParticipantBarcode': 'TCGA-BR-4279'}, {'ParticipantBarcode': 'TCGA-A5-A0VO'}, {'ParticipantBarcode': 'TCGA-BR-8677'}, {'ParticipantBarcode': 'TCGA-63-A5MH'}, {'ParticipantBarcode': 'TCGA-E2-A1L8'}, {'ParticipantBarcode': 'TCGA-D8-A27G'}, {'ParticipantBarcode': 'TCGA-B9-A8YI'}, {'ParticipantBarcode': 'TCGA-LL-A9Q3'}, {'ParticipantBarcode': 'TCGA-A2-A0CK'}, {'ParticipantBarcode': 'TCGA-BH-A0HP'}, {'ParticipantBarcode': 'TCGA-AC-A2FO'}, {'ParticipantBarcode': 'TCGA-A2-A4S2'}, {'ParticipantBarcode': 'TCGA-A7-A425'}, {'ParticipantBarcode': 'TCGA-BS-A0UV'}, {'ParticipantBarcode': 'TCGA-CD-A4MG'}, {'ParticipantBarcode': 'TCGA-B6-A0X7'}, {'ParticipantBarcode': 'TCGA-A2-A25A'}, {'ParticipantBarcode': 'TCGA-A6-5661'}, {'ParticipantBarcode': 'TCGA-AR-A5QM'}, {'ParticipantBarcode': 'TCGA-A2-A0SY'}, {'ParticipantBarcode': 'TCGA-D7-8574'}, {'ParticipantBarcode': 'TCGA-GC-A3I6'}, {'ParticipantBarcode': 'TCGA-3M-AB47'}, {'ParticipantBarcode': 'TCGA-A2-A1G0'}, {'ParticipantBarcode': 'TCGA-AC-A2B8'}, {'ParticipantBarcode': 'TCGA-BR-6803'}, {'ParticipantBarcode': 'TCGA-DD-AAE3'}, {'ParticipantBarcode': 'TCGA-E9-A2JT'}, {'ParticipantBarcode': 'TCGA-LD-A66U'}, {'ParticipantBarcode': 'TCGA-BH-A0E9'}, {'ParticipantBarcode': 'TCGA-EE-A2A6'}, {'ParticipantBarcode': 'TCGA-A5-A1OF'}, {'ParticipantBarcode': 'TCGA-E1-A7YJ'}, {'ParticipantBarcode': 'TCGA-CA-6717'}, {'ParticipantBarcode': 'TCGA-CG-4474'}, {'ParticipantBarcode': 'TCGA-AC-A2FF'}, {'ParticipantBarcode': 'TCGA-AP-A0LM'}, {'ParticipantBarcode': 'TCGA-D7-6518'}, {'ParticipantBarcode': 'TCGA-77-A5G1'}, {'ParticipantBarcode': 'TCGA-A2-A0T4'}, {'ParticipantBarcode': 'TCGA-B6-A0RQ'}, {'ParticipantBarcode': 'TCGA-G9-6365'}, {'ParticipantBarcode': 'TCGA-WT-AB44'}, {'ParticipantBarcode': 'TCGA-BR-8364'}, {'ParticipantBarcode': 'TCGA-BR-A453'}, {'ParticipantBarcode': 'TCGA-EE-A29E'}, {'ParticipantBarcode': 'TCGA-BF-A3DL'}, {'ParticipantBarcode': 'TCGA-F1-6874'}, {'ParticipantBarcode': 'TCGA-F5-6814'}, {'ParticipantBarcode': 'TCGA-66-2759'}, {'ParticipantBarcode': 'TCGA-E9-A5FK'}, {'ParticipantBarcode': 'TCGA-B0-5692'}, {'ParticipantBarcode': 'TCGA-BR-A4J9'}], 'var_call_685AF1mmtVzEeAxLNMWULAQi': 'file_storage/call_685AF1mmtVzEeAxLNMWULAQi.json', 'var_call_XCfqRKUIdt9kRAmceUtJIU9U': 'file_storage/call_XCfqRKUIdt9kRAmceUtJIU9U.json', 'var_call_ppat7IwGCsLhXVcHpjKlKZW7': 'file_storage/call_ppat7IwGCsLhXVcHpjKlKZW7.json'}

exec(code, env_args)
