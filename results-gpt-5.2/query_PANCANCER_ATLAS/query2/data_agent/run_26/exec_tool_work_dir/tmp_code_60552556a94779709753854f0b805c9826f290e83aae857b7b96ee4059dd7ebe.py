code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r') as f:
            return json.load(f)
    return v

clin = pd.DataFrame(load_records(var_call_jDJiJo4toSyvgusVcCI51KFy))
mut = pd.DataFrame(load_records(var_call_dkRjMiN0PxSrA8gbxtsQR7ze))

# extract TCGA barcode from Patient_description
clin['ParticipantBarcode'] = clin['Patient_description'].str.extract(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', expand=False)
clin = clin.dropna(subset=['ParticipantBarcode'])

# alive already filtered; ensure unique patients per histological type
clin = clin[['ParticipantBarcode','histological_type']].drop_duplicates()

# CDH1 mutation status per patient
mut_patients = set(mut['ParticipantBarcode'].dropna().unique().tolist())
clin['CDH1_mut'] = clin['ParticipantBarcode'].isin(mut_patients)

# compute percentages by histological type
agg = clin.groupby('histological_type').agg(n_alive=('ParticipantBarcode','nunique'), n_cdh1=('CDH1_mut','sum'))
agg['pct_cdh1'] = (agg['n_cdh1'] / agg['n_alive'] * 100).round(2)

# require at least 5 alive patients to avoid tiny denominators
agg_f = agg[agg['n_alive']>=5].sort_values(['pct_cdh1','n_alive'], ascending=[False, False]).head(3)

out = []
for hist, row in agg_f.iterrows():
    out.append({
        'histological_type': hist,
        'alive_patients_n': int(row['n_alive']),
        'cdh1_mutated_n': int(row['n_cdh1']),
        'cdh1_mutation_pct': float(row['pct_cdh1'])
    })

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_dkRjMiN0PxSrA8gbxtsQR7ze': 'file_storage/call_dkRjMiN0PxSrA8gbxtsQR7ze.json', 'var_call_QSvvDrFgNQP7iYbDaW2LoHAa': ['clinical_info'], 'var_call_qHnYBN6wxnBnCqpSvETXkfzO': 'file_storage/call_qHnYBN6wxnBnCqpSvETXkfzO.json', 'var_call_lugXjiVRlXYyVa6Tl2aUnJh5': [], 'var_call_6En229Unb3Ywv6hGCF8HHFfr': [{'n': '10761', 'breast_n': '1087'}], 'var_call_GbllptOkq8S80T0vVKB3pjo8': [{'Patient_description': 'Clinical entry D13FB44B-291B-4EA4-920C-142DAA8D1989 identifies patient TCGA-AC-A5EH, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Record 09A5E9FD-D816-4F8C-BAA9-0E40BA607B16 refers to patient TCGA-LL-A7SZ, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': "Patient TCGA-AN-A0FY, registered under UUID de75d0b9-0f47-4732-8df5-05c350cfcd32, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive.", 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Patient TCGA-AC-A2FB (UUID 02BBB632-0F7F-439D-B8F0-C86A06237424) is a FEMALE diagnosed with Breast invasive carcinoma. Current vital status: Alive.', 'histological_type': 'Infiltrating Lobular Carcinoma'}, {'Patient_description': 'The individual with barcode TCGA-AO-A1KR and UUID b7f74ae1-6f58-447c-be50-a7666eb19d9a is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}], 'var_call_jDJiJo4toSyvgusVcCI51KFy': 'file_storage/call_jDJiJo4toSyvgusVcCI51KFy.json'}

exec(code, env_args)
