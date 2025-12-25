code = """import pandas as pd
import json

clinical_data_path = locals()['var_function-call-14341548236009829069']
with open(clinical_data_path, 'r') as f:
    clinical_data = json.load(f)

df_clinical = pd.DataFrame(clinical_data)

# Filter for BRCA patients and vital status 'Alive' using Patient_description
df_brca_alive = df_clinical[
    df_clinical['Patient_description'].str.contains('Bladder urothelial carcinoma') &
    df_clinical['Patient_description'].str.contains('vital status: Alive', na=False)
].copy()

# Extract ParticipantBarcode
df_brca_alive['ParticipantBarcode'] = df_brca_alive['Patient_description'].str.extract(r'patient (TCGA-[\w-]+)')

# Drop rows where ParticipantBarcode could not be extracted
df_brca_alive.dropna(subset=['ParticipantBarcode'], inplace=True)

# Get unique ParticipantBarcodes for the next step
brca_alive_participants = df_brca_alive['ParticipantBarcode'].unique().tolist()

# Prepare data for next step (querying molecular database)
print("__RESULT__:")
print(json.dumps({'participants': brca_alive_participants, 'histological_types': df_brca_alive[['ParticipantBarcode', 'histological_type']].to_dict(orient='records')}))"""

env_args = {'var_function-call-4641508794214492565': ['clinical_info'], 'var_function-call-14341548236009829069': 'file_storage/function-call-14341548236009829069.json'}

exec(code, env_args)
