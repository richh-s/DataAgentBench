code = """import json, re, math
import pandas as pd

# Load the query results from storage files
with open(var_call_akv90jxyyJ4YzHvBNkCTwukR, 'r') as f:
    clinical = json.load(f)
with open(var_call_4IFT8P1AmEnv34arRCpBHoT3, 'r') as f:
    expr = json.load(f)

# Create DataFrames
df_clin = pd.DataFrame(clinical)
df_expr = pd.DataFrame(expr)

# Ensure columns exist
# Extract TCGA barcode from Patient_description
pattern = re.compile(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', re.IGNORECASE)

def extract_barcode(desc):
    if not isinstance(desc, str):
        return None
    m = pattern.search(desc)
    return m.group(1).upper() if m else None

# Apply extraction
if 'Patient_description' in df_clin.columns:
    df_clin['TCGA_barcode'] = df_clin['Patient_description'].apply(extract_barcode)
else:
    df_clin['TCGA_barcode'] = df_clin.get('Patient_description', []).apply(extract_barcode)

# Filter clinical rows that likely correspond to LGG: we used a query that selected '%lower%'
# But to be safe, also ensure TCGA_barcode is not null
df_clin = df_clin[df_clin['TCGA_barcode'].notna()].copy()

# Exclude histological_type values enclosed in square brackets
# Consider histological_type missing as exclusion

def valid_hist(h):
    if not isinstance(h, str):
        return False
    return ('[' not in h) and (']' not in h) and (h.strip() != '')

if 'histological_type' in df_clin.columns:
    df_clin = df_clin[df_clin['histological_type'].apply(valid_hist)].copy()
else:
    df_clin = df_clin[[]]  # empty if no histology

# Prepare expression dataframe: ParticipantBarcode and normalized_count
# Convert normalized_count to float, drop invalid

def to_float(x):
    try:
        return float(x)
    except:
        return float('nan')

if 'ParticipantBarcode' not in df_expr.columns:
    df_expr['ParticipantBarcode'] = df_expr.get('ParticipantBarcode', [])

if 'normalized_count' in df_expr.columns:
    df_expr['normalized_count_f'] = df_expr['normalized_count'].apply(to_float)
else:
    df_expr['normalized_count_f'] = float('nan')

# Keep only IGF2 rows already filtered by earlier query
# Drop NaN normalized_count
df_expr = df_expr[df_expr['normalized_count_f'].notna()].copy()

# Standardize ParticipantBarcode to upper
df_expr['ParticipantBarcode'] = df_expr['ParticipantBarcode'].str.upper()

# Merge clinical and expression on barcode
merged = pd.merge(df_clin, df_expr, left_on='TCGA_barcode', right_on='ParticipantBarcode', how='inner')

# Compute log10(normalized_count + 1)
merged['log10_expr'] = merged['normalized_count_f'].apply(lambda x: math.log10(x + 1))

# Group by histological_type and compute mean
result = merged.groupby('histological_type')['log10_expr'].mean().reset_index()

# Format results with at least four decimal places
out = {}
for _, row in result.iterrows():
    hist = row['histological_type']
    val = row['log10_expr']
    out[hist] = '{:.4f}'.format(val)

# Print in required format
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_iCh3WUhqp3jn8iqO1bs4p06I': ['clinical_info'], 'var_call_XXCm1gBRLVWfOJ60pLUezii9': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_zgPG4OUEJgXm4cTDAAY6iobO': 'file_storage/call_zgPG4OUEJgXm4cTDAAY6iobO.json', 'var_call_s9HKUpyZfafxqEF3raOb0Dys': 'file_storage/call_s9HKUpyZfafxqEF3raOb0Dys.json', 'var_call_WHIRGCvCqkeO5LAM6aIZgcD4': [], 'var_call_akv90jxyyJ4YzHvBNkCTwukR': 'file_storage/call_akv90jxyyJ4YzHvBNkCTwukR.json', 'var_call_4IFT8P1AmEnv34arRCpBHoT3': 'file_storage/call_4IFT8P1AmEnv34arRCpBHoT3.json'}

exec(code, env_args)
