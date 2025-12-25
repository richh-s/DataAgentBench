code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-3206621542987617848'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Date Parsing Helpers
month_map = {
    'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
    'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
}

def parse_grant_date_check_h2_2019(date_str):
    if not isinstance(date_str, str): return False
    # Check year 2019
    if '2019' not in date_str:
        return False
    
    # Extract month
    # Regex for month name
    match = re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*', date_str, re.IGNORECASE)
    if match:
        m_str = match.group(1).lower()
        m_num = month_map.get(m_str, 0)
        return m_num >= 7
    return False

def parse_filing_year(date_str):
    if not isinstance(date_str, str): return None
    match = re.search(r'(\d{4})', date_str)
    if match:
        return int(match.group(1))
    return None

# Filter Grant Date
df['is_h2_2019'] = df['grant_date'].apply(parse_grant_date_check_h2_2019)
df_filtered = df[df['is_h2_2019']].copy()

# Parse Filing Year
df_filtered['filing_year'] = df_filtered['filing_date'].apply(parse_filing_year)
df_filtered = df_filtered.dropna(subset=['filing_year'])
df_filtered['filing_year'] = df_filtered['filing_year'].astype(int)

# Extract CPCs
# cpc field is a JSON string
import json
def extract_level4_cpcs(cpc_json_str):
    try:
        cpc_list = json.loads(cpc_json_str)
        codes = set()
        for item in cpc_list:
            code = item.get('code', '')
            # Level 4 in DB seems to be Class (3 chars, e.g. A01)
            # Standard code format: A01B...
            if len(code) >= 3:
                codes.add(code[:3])
        return list(codes)
    except:
        return []

df_filtered['cpc_codes'] = df_filtered['cpc'].apply(extract_level4_cpcs)
df_exploded = df_filtered.explode('cpc_codes')
df_exploded = df_exploded.dropna(subset=['cpc_codes'])

# Count filings per CPC per Year
counts = df_exploded.groupby(['cpc_codes', 'filing_year']).size().reset_index(name='count')

# Calculate EMA
# Get range of years
min_year = counts['filing_year'].min()
max_year = counts['filing_year'].max()
all_years = range(min_year, max_year + 1)

results = []

for cpc, group in counts.groupby('cpc_codes'):
    # Reindex to full year range
    g = group.set_index('filing_year').reindex(all_years, fill_value=0)
    # Calculate EMA
    # smooth factor 0.1
    # pandas ewm: alpha=0.1, adjust=False (usually recursive: y_t = alpha*x_t + (1-alpha)*y_{t-1})
    g['ema'] = g['count'].ewm(alpha=0.1, adjust=False).mean()
    
    # Find best year
    best_idx = g['ema'].idxmax()
    max_ema = g.loc[best_idx, 'ema']
    
    results.append({
        'cpc_code': cpc,
        'best_year': int(best_idx),
        'max_ema': float(max_ema)
    })

results_df = pd.DataFrame(results)

# Prepare to fetch titles
cpc_codes = results_df['cpc_code'].unique().tolist()
print("__RESULT__:")
print(json.dumps(cpc_codes))"""

env_args = {'var_function-call-4649531244037871347': 'file_storage/function-call-4649531244037871347.json', 'var_function-call-4649531244037872868': [{'symbol': 'A01K2227/108', 'level': '9.0', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'level': '9.0', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'level': '9.0', 'titleFull': 'Bovine'}], 'var_function-call-485676876898493978': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-485676876898493815': [{'Patents_info': 'In AT, the patent filing (application no. AT-52022-U) is assigned to ST Extruded Products Germany GmbH and has publication no. AT-17758-U1.'}, {'Patents_info': 'Application (no. AU-2006246481-A) from AU, belonging to KAO GERMANY GMBH, with pub. number AU-2006246481-B2.'}, {'Patents_info': 'TRELLEBORG AUTOMOTIVE GERMANY holds the PL patent application (number PL-07728345-T), with publication no. PL-2010798-T3.'}, {'Patents_info': 'The DE application (number DE-102008034343-A) is assigned to CONTINENTAL MECH COMPONENTS GERMANY GMBH and has pub. number DE-102008034343-B4.'}, {'Patents_info': 'In EP, the application (ID EP-18829350-A) is belonging to MEYER BURGER GERMANY GMBH and has pub. number EP-3729486-C0.'}], 'var_function-call-1173670379374644714': [{'symbol': 'A', 'level': '2.0', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'A01', 'level': '4.0', 'titleFull': 'AGRICULTURE; FORESTRY; ANIMAL HUSBANDRY; HUNTING; TRAPPING; FISHING'}, {'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'A01B1/00', 'level': '7.0', 'titleFull': 'Hand tools'}], 'var_function-call-1173670379374644669': [], 'var_function-call-12085292487298471941': [{'count(*)': '4833'}], 'var_function-call-12085292487298470532': [{'count(*)': '68'}], 'var_function-call-12085292487298473219': [{'count(*)': '5'}], 'var_function-call-3206621542987617848': 'file_storage/function-call-3206621542987617848.json'}

exec(code, env_args)
