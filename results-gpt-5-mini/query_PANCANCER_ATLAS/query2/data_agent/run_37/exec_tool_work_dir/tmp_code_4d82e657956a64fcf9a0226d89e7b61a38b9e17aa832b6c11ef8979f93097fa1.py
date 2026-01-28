code = """import json
import pandas as pd

# Load the clinical_info preview file
with open(var_call_ysZTmiZFslLAwz5xuT5bLsP9, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# get columns and some unique Patient_description samples
cols = df.columns.tolist()

# find rows containing 'BRCA' or 'Breast' or 'Breast Invasive' in Patient_description
mask_brca = df['Patient_description'].str.contains('BRCA', case=False, na=False)
mask_breast = df['Patient_description'].str.contains('Breast', case=False, na=False)

sample_brca = df[mask_brca].head(10).to_dict(orient='records')
sample_breast = df[mask_breast].head(10).to_dict(orient='records')

result = {
    'columns': cols,
    'num_rows_preview': len(df),
    'breast_matches_count_preview': int(mask_breast.sum()),
    'brca_matches_count_preview': int(mask_brca.sum()),
    'breast_samples_preview': sample_breast,
    'brca_samples_preview': sample_brca
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_xLGvMiQkGuR9NeCE9sfREf7q': ['clinical_info'], 'var_call_X7I7sxtKpzs4csfdvFBqSgk4': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_ysZTmiZFslLAwz5xuT5bLsP9': 'file_storage/call_ysZTmiZFslLAwz5xuT5bLsP9.json', 'var_call_GwccanqqWFT3gIsqtMJ7j6PT': []}

exec(code, env_args)
