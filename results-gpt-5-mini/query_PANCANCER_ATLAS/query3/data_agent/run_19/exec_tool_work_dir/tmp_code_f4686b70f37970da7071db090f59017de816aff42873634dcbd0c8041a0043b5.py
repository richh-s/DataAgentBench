code = """import json
import pandas as pd

# Load full lists
with open(var_call_2Hbz95VIWvJQczjZECJzyMYV, 'r', encoding='utf-8') as f:
    clinical_list = json.load(f)
with open(var_call_NbI2VMmvh0BNBWFTgNEKYiPB, 'r', encoding='utf-8') as f:
    mut_list = json.load(f)

# Build mapping from patient_id to histological_type for breast females
brca_patients = {}
for rec in clinical_list:
    pdsc = rec.get('Patient_description','')
    if pdsc and ('Breast' in pdsc or 'BRCA' in pdsc or 'Breast invasive carcinoma' in pdsc):
        pid = rec.get('patient_id')
        hist = rec.get('histological_type')
        if pid and hist:
            brca_patients[pid] = hist.strip()

# Filter known histological types
exclude_values = set(['None','[Not Applicable]','Other  specify','Other specify','Unknown','Not Reported','[Not Available]'])
brca_patients = {k:v for k,v in brca_patients.items() if v not in exclude_values}

# Get set of patients with PASS CDH1 mutations
mut_pass_ids = set()
for m in mut_list:
    if m.get('Hugo_Symbol')=='CDH1' and m.get('FILTER')=='PASS':
        pb = m.get('ParticipantBarcode')
        if pb:
            pid = pb.split('-')[-1]
            mut_pass_ids.add(pid)

# Now build contingency counts per hist type
from collections import defaultdict
counts = defaultdict(lambda: {'No':0,'Yes':0})
for pid,hist in brca_patients.items():
    if pid in mut_pass_ids:
        counts[hist]['Yes'] += 1
    else:
        counts[hist]['No'] += 1

# Convert to list and apply exclusion of marginal totals <=10
cont_list = []
for hist,(d) in counts.items():
    total = d['Yes'] + d['No']
    cont_list.append({'histological_type': hist, 'Yes': d['Yes'], 'No': d['No'], 'total': total})

# Create dataframe
df_cont = pd.DataFrame(cont_list)
# Exclude totals <=10
df_included = df_cont[df_cont['total']>10].copy()

# Compute chi-square
grand_total = int(df_included['total'].sum())
col_yes = int(df_included['Yes'].sum())
col_no = int(df_included['No'].sum())
chi2 = 0.0
for idx,row in df_included.iterrows():
    rtot = int(row['total'])
    exp_yes = (rtot * col_yes)/grand_total if grand_total>0 else 0
    exp_no = (rtot * col_no)/grand_total if grand_total>0 else 0
    if exp_yes>0:
        chi2 += (row['Yes'] - exp_yes)**2 / exp_yes
    if exp_no>0:
        chi2 += (row['No'] - exp_no)**2 / exp_no

# Prepare output
contingency_table = []
for idx,row in df_included.iterrows():
    contingency_table.append({'histological_type': row['histological_type'], 'mutation_Yes': int(row['Yes']), 'mutation_No': int(row['No']), 'row_total': int(row['total'])})

excluded = df_cont[df_cont['total']<=10][['histological_type','total']].set_index('histological_type').to_dict()['total']

result = {
    'chi2': float(chi2),
    'grand_total': grand_total,
    'column_totals': {'mutation_No': col_no, 'mutation_Yes': col_yes},
    'included_histological_types': [r['histological_type'] for r in contingency_table],
    'excluded_histological_types': excluded,
    'contingency_table': contingency_table
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_euNu3hqX7o5pimk0JDlcvUZn': ['clinical_info'], 'var_call_TT4YmDFu1feeK1YWDQiVcdcZ': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_c48JMfZf7ddnSH9YptwaPZd0': 'file_storage/call_c48JMfZf7ddnSH9YptwaPZd0.json', 'var_call_2Hbz95VIWvJQczjZECJzyMYV': 'file_storage/call_2Hbz95VIWvJQczjZECJzyMYV.json', 'var_call_NbI2VMmvh0BNBWFTgNEKYiPB': 'file_storage/call_NbI2VMmvh0BNBWFTgNEKYiPB.json', 'var_call_DxXrBq1MATFsl2XFarMAL9Xr': {'var_call_2Hbz95VIWvJQczjZECJzyMYV': {'type': 'str', 'is_file': True, 'list_length': 1076, 'first_keys': ['Patient_description', 'histological_type', 'patient_id']}, 'var_call_NbI2VMmvh0BNBWFTgNEKYiPB': {'type': 'str', 'is_file': True, 'list_length': 261, 'first_keys': ['ParticipantBarcode', 'Hugo_Symbol', 'HGVSp_Short', 'Variant_Classification', 'FILTER']}}, 'var_call_607hVuFkoPzJfzEIwiFGbGSo': {'clinical_count': 1076, 'clinical_type_counts': {'dict': 1076}, 'clinical_keylen_counts_sample': {'3': 20}, 'clinical_sample_keys_first20': [['Patient_description', 'histological_type', 'patient_id'], ['Patient_description', 'histological_type', 'patient_id'], ['Patient_description', 'histological_type', 'patient_id'], ['Patient_description', 'histological_type', 'patient_id'], ['Patient_description', 'histological_type', 'patient_id'], ['Patient_description', 'histological_type', 'patient_id'], ['Patient_description', 'histological_type', 'patient_id'], ['Patient_description', 'histological_type', 'patient_id'], ['Patient_description', 'histological_type', 'patient_id'], ['Patient_description', 'histological_type', 'patient_id'], ['Patient_description', 'histological_type', 'patient_id'], ['Patient_description', 'histological_type', 'patient_id'], ['Patient_description', 'histological_type', 'patient_id'], ['Patient_description', 'histological_type', 'patient_id'], ['Patient_description', 'histological_type', 'patient_id'], ['Patient_description', 'histological_type', 'patient_id'], ['Patient_description', 'histological_type', 'patient_id'], ['Patient_description', 'histological_type', 'patient_id'], ['Patient_description', 'histological_type', 'patient_id'], ['Patient_description', 'histological_type', 'patient_id']], 'mutation_count': 261, 'mutation_type_counts': {'dict': 261}, 'mutation_keylen_counts_sample': {'5': 20}, 'mutation_sample_keys_first20': [['ParticipantBarcode', 'Hugo_Symbol', 'HGVSp_Short', 'Variant_Classification', 'FILTER'], ['ParticipantBarcode', 'Hugo_Symbol', 'HGVSp_Short', 'Variant_Classification', 'FILTER'], ['ParticipantBarcode', 'Hugo_Symbol', 'HGVSp_Short', 'Variant_Classification', 'FILTER'], ['ParticipantBarcode', 'Hugo_Symbol', 'HGVSp_Short', 'Variant_Classification', 'FILTER'], ['ParticipantBarcode', 'Hugo_Symbol', 'HGVSp_Short', 'Variant_Classification', 'FILTER'], ['ParticipantBarcode', 'Hugo_Symbol', 'HGVSp_Short', 'Variant_Classification', 'FILTER'], ['ParticipantBarcode', 'Hugo_Symbol', 'HGVSp_Short', 'Variant_Classification', 'FILTER'], ['ParticipantBarcode', 'Hugo_Symbol', 'HGVSp_Short', 'Variant_Classification', 'FILTER'], ['ParticipantBarcode', 'Hugo_Symbol', 'HGVSp_Short', 'Variant_Classification', 'FILTER'], ['ParticipantBarcode', 'Hugo_Symbol', 'HGVSp_Short', 'Variant_Classification', 'FILTER'], ['ParticipantBarcode', 'Hugo_Symbol', 'HGVSp_Short', 'Variant_Classification', 'FILTER'], ['ParticipantBarcode', 'Hugo_Symbol', 'HGVSp_Short', 'Variant_Classification', 'FILTER'], ['ParticipantBarcode', 'Hugo_Symbol', 'HGVSp_Short', 'Variant_Classification', 'FILTER'], ['ParticipantBarcode', 'Hugo_Symbol', 'HGVSp_Short', 'Variant_Classification', 'FILTER'], ['ParticipantBarcode', 'Hugo_Symbol', 'HGVSp_Short', 'Variant_Classification', 'FILTER'], ['ParticipantBarcode', 'Hugo_Symbol', 'HGVSp_Short', 'Variant_Classification', 'FILTER'], ['ParticipantBarcode', 'Hugo_Symbol', 'HGVSp_Short', 'Variant_Classification', 'FILTER'], ['ParticipantBarcode', 'Hugo_Symbol', 'HGVSp_Short', 'Variant_Classification', 'FILTER'], ['ParticipantBarcode', 'Hugo_Symbol', 'HGVSp_Short', 'Variant_Classification', 'FILTER'], ['ParticipantBarcode', 'Hugo_Symbol', 'HGVSp_Short', 'Variant_Classification', 'FILTER']]}}

exec(code, env_args)
