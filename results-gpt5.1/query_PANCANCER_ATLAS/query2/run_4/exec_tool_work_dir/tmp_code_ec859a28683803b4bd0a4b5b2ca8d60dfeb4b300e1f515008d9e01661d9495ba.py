code = """import json, pandas as pd
from pathlib import Path

# Load full clinical breast cohort
path = Path(var_call_N5JC1A2SWjyGN93aF6HM0vgV)
clinical = pd.read_json(path)

# Extract patient barcode and vital status from Patient_description text
import re

def extract_barcode(desc):
    m = re.search(r'patient (TCGA-[A-Z0-9-]+)', desc)
    if not m:
        m = re.search(r'barcode (TCGA-[A-Z0-9-]+)', desc)
    return m.group(1) if m else None


def extract_vital(desc):
    m = re.search(r'vital status[:=] ([A-Za-z]+)', desc)
    return m.group(1) if m else None

clinical['ParticipantBarcode'] = clinical['Patient_description'].apply(extract_barcode)
clinical['vital_status'] = clinical['Patient_description'].apply(extract_vital)

# Filter BRCA alive patients
brca_alive = clinical[clinical['vital_status'] == 'Alive'].copy()

# Load CDH1 mutation patients
path_mut = Path(var_call_aZh4kDYwnr1QC0S3vJU29yA9)
mut = pd.read_json(path_mut)
mut_brca = mut.drop_duplicates(subset=['ParticipantBarcode'])

# Merge to flag CDH1 mutation status among BRCA alive
merged = brca_alive.merge(mut_brca[['ParticipantBarcode']], on='ParticipantBarcode', how='left', indicator='mut_flag')
merged['CDH1_mutated'] = merged['mut_flag'] == 'both'

# For each histological_type, compute percentage with CDH1 mutation
summary = merged.groupby('histological_type').agg(
    total_patients=('ParticipantBarcode', 'nunique'),
    mutated_patients=('CDH1_mutated', 'sum')
).reset_index()
summary['mutation_percentage'] = (summary['mutated_patients'] / summary['total_patients']) * 100

# Keep histologies with at least, say, 5 alive patients to avoid noise
summary = summary[summary['total_patients'] >= 5]

# Top 3 by mutation percentage
top3 = summary.sort_values(['mutation_percentage','total_patients'], ascending=[False, False]).head(3)

result = top3.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_aZh4kDYwnr1QC0S3vJU29yA9': 'file_storage/call_aZh4kDYwnr1QC0S3vJU29yA9.json', 'var_call_TygoHs0LcN2Gc0E9566ymvcC': ['clinical_info'], 'var_call_Ba9iNVLnKvpM0EyFlWjCPTcw': 'file_storage/call_Ba9iNVLnKvpM0EyFlWjCPTcw.json', 'var_call_CEwQT0av54FWQVrhjuIdHHLn': [], 'var_call_N5JC1A2SWjyGN93aF6HM0vgV': 'file_storage/call_N5JC1A2SWjyGN93aF6HM0vgV.json'}

exec(code, env_args)
