code = """import pandas as pd
import json
import re

# Load data
with open(locals()['var_function-call-12461863306711792077'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Helper to parse dates
def parse_date(date_str):
    if not isinstance(date_str, str):
        return pd.NaT
    # Clean string
    s = re.sub(r'(st|nd|rd|th|on|dated|of|the|,)', '', date_str)
    s = s.strip()
    try:
        return pd.to_datetime(s, errors='coerce')
    except:
        return pd.NaT

def extract_year(date_str):
    if not isinstance(date_str, str):
        return None
    match = re.search(r'\b(19|20)\d{2}\b', date_str)
    if match:
        return int(match.group(0))
    return None

# Filter Grant Date: 2019 H2 (July - Dec)
# Parse grant_date fully to check range
df['grant_dt'] = df['grant_date'].apply(parse_date)
df = df[df['grant_dt'].notna()]
df = df[(df['grant_dt'] >= '2019-07-01') & (df['grant_dt'] <= '2019-12-31')]

# Filter Country: Check Patents_info for DE
# The SQL query already filtered loosely. Let's strictly check if "DE" or "Germany" is involved.
# The examples showed "from DE", "In DE", "DE-..."
# We keep all as the SQL filter was reasonably specific.

# Extract Filing Year
df['filing_year'] = df['filing_date'].apply(extract_year)
df = df[df['filing_year'].notna()]

# Extract CPC Level 4
# Level 4 is Class, e.g., C01 (3 chars)
def get_cpc_l4(cpc_json):
    try:
        cpc_list = json.loads(cpc_json)
        codes = set()
        for item in cpc_list:
            code = item.get('code', '')
            # Extract first 3 chars if valid
            if len(code) >= 3:
                codes.add(code[:3])
        return list(codes)
    except:
        return []

df['cpc_l4'] = df['cpc'].apply(get_cpc_l4)
df_exploded = df.explode('cpc_l4')
df_exploded = df_exploded.dropna(subset=['cpc_l4'])

# Count filings per year per CPC
counts = df_exploded.groupby(['cpc_l4', 'filing_year']).size().reset_index(name='count')

# Calculate EMA
results = []
smoothing_factor = 0.1

for cpc, group in counts.groupby('cpc_l4'):
    # Create full range of years
    min_year = group['filing_year'].min()
    max_year = group['filing_year'].max()
    full_range = pd.DataFrame({'filing_year': range(min_year, max_year + 1)})
    
    merged = pd.merge(full_range, group, on='filing_year', how='left').fillna(0)
    merged = merged.sort_values('filing_year')
    
    # Calculate EMA
    # pandas ewm: alpha=0.1, adjust=False corresponds to recursive formula starting with mean?
    # recursive: y_t = alpha * x_t + (1-alpha) * y_{t-1}
    # pandas ewm(alpha=0.1, adjust=False).mean() implements this.
    merged['ema'] = merged['count'].ewm(alpha=smoothing_factor, adjust=False).mean()
    
    # Find max EMA
    best_idx = merged['ema'].idxmax()
    best_row = merged.loc[best_idx]
    
    results.append({
        'cpc_group': cpc,
        'max_ema': best_row['ema'],
        'best_year': int(best_row['filing_year'])
    })

results_df = pd.DataFrame(results)
# Sort by max_ema descending
results_df = results_df.sort_values('max_ema', ascending=False)

# Keep top 20 for brevity if many, or all if reasonable
top_results = results_df.head(20).to_dict(orient='records')
all_codes = results_df['cpc_group'].tolist()

print("__RESULT__:")
print(json.dumps({"top_results": top_results, "all_codes": all_codes}))"""

env_args = {'var_function-call-864177832263507867': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-864177832263504362': 'file_storage/function-call-864177832263504362.json', 'var_function-call-4079124224651373343': [{'symbol': 'A', 'level': '2.0', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'A01', 'level': '4.0', 'titleFull': 'AGRICULTURE; FORESTRY; ANIMAL HUSBANDRY; HUNTING; TRAPPING; FISHING'}, {'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'A01B1/00', 'level': '7.0', 'titleFull': 'Hand tools'}], 'var_function-call-4079124224651374308': [{'Patents_info': 'Patent application (number DE-10317286-A) from DE, belonging to NICOLAY VERWALTUNGS GMBH, with publication no. DE-10317286-B3.'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.'}, {'Patents_info': 'In DE, the patent filing (application no. DE-102009032362-A) is owned by MARTOR KG and has pub. number DE-102009032362-B3.'}], 'var_function-call-12461863306711792077': 'file_storage/function-call-12461863306711792077.json'}

exec(code, env_args)
