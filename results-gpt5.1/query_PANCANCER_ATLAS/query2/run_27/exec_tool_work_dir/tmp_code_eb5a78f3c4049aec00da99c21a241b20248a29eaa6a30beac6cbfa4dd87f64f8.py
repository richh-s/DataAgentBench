code = """import json, pandas as pd

# load full CDH1 mutations
path = var_call_cVX3HVYI9d0tndxqW36JBMbH
with open(path) as f:
    cdh1_mut = json.load(f)
cdh1_df = pd.DataFrame(cdh1_mut)

# extract BRCA (Breast invasive carcinoma) alive clinical
path_br = var_call_dGuj8lKA9pnxKYcn9TL5kfz2
with open(path_br) as f:
    br_clin = json.load(f)
br_df = pd.DataFrame(br_clin)

# get patient barcodes from Patient_description
br_df['ParticipantBarcode'] = br_df['Patient_description'].str.extract(r'patient (TCGA-..-....)')[0]

# subset CDH1 mutations to these patients
cdh1_brca = cdh1_df.merge(br_df[['ParticipantBarcode','histological_type']], on='ParticipantBarcode', how='inner')

# for each histological type, compute percent of patients with CDH1 mutation among alive BRCA patients of that type
# first, total alive patients per histological type
alive_counts = br_df.groupby('histological_type')['ParticipantBarcode'].nunique()
mut_counts = cdh1_brca.groupby('histological_type')['ParticipantBarcode'].nunique()

perc = (mut_counts / alive_counts * 100).dropna().sort_values(ascending=False)

top3 = perc.head(3).round(2)
result = [{'histological_type': ht, 'percent_CDH1_mutated_alive_BRCA_patients': float(p)} for ht, p in top3.items()]

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_cVX3HVYI9d0tndxqW36JBMbH': 'file_storage/call_cVX3HVYI9d0tndxqW36JBMbH.json', 'var_call_reGx9r6tpmEzloQPLk5RXaxk': ['clinical_info'], 'var_call_YkxP55koPaDiSN5w9EjXaOhu': 'file_storage/call_YkxP55koPaDiSN5w9EjXaOhu.json', 'var_call_7KXeBq5JOIAMU4uT4SORTs2x': [], 'var_call_TjOeFtNuSDudEpMXZEg5eU1g': [], 'var_call_BGCgsVXwG2DfAqFdQa5wMXlF': 'file_storage/call_BGCgsVXwG2DfAqFdQa5wMXlF.json', 'var_call_dGuj8lKA9pnxKYcn9TL5kfz2': 'file_storage/call_dGuj8lKA9pnxKYcn9TL5kfz2.json'}

exec(code, env_args)
