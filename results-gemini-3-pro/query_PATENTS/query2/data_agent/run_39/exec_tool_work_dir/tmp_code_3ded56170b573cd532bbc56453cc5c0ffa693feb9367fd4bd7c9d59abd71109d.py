code = """import pandas as pd
import json
import re

# Load data
with open(locals()['var_function-call-12461863306711792077'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

def parse_date(date_str):
    if not isinstance(date_str, str):
        return pd.NaT
    s = re.sub(r'(?<=\d)(st|nd|rd|th)\b', '', date_str)
    s = re.sub(r'\b(on|dated|of|the)\b', '', s, flags=re.IGNORECASE)
    s = s.replace(',', ' ')
    s = s.strip()
    try:
        return pd.to_datetime(s, errors='coerce')
    except:
        return pd.NaT

df['grant_dt'] = df['grant_date'].apply(parse_date)

# Filter Grant Date
mask_grant = (df['grant_dt'] >= '2019-07-01') & (df['grant_dt'] <= '2019-12-31')
df = df[mask_grant].copy()

if len(df) > 0:
    def extract_year(date_str):
        if not isinstance(date_str, str):
            return None
        # Simple regex for 4 digits
        match = re.search(r'(19|20)\d{2}', date_str)
        if match:
            return int(match.group(0))
        return None

    df['filing_year'] = df['filing_date'].apply(extract_year)
    df = df[df['filing_year'].notna()]

    def get_cpc_l4(cpc_json):
        try:
            cpc_list = json.loads(cpc_json)
            codes = set()
            for item in cpc_list:
                code = item.get('code', '')
                if len(code) >= 3:
                    codes.add(code[:3])
            return list(codes)
        except:
            return []

    df['cpc_l4'] = df['cpc'].apply(get_cpc_l4)
    df_exploded = df.explode('cpc_l4')
    df_exploded = df_exploded.dropna(subset=['cpc_l4'])

    counts = df_exploded.groupby(['cpc_l4', 'filing_year']).size().reset_index(name='count')
    
    results = []
    smoothing_factor = 0.1
    
    for cpc, group in counts.groupby('cpc_l4'):
        min_year = int(group['filing_year'].min())
        max_year = int(group['filing_year'].max())
        full_range = pd.DataFrame({'filing_year': range(min_year, max_year + 1)})
        
        merged = pd.merge(full_range, group, on='filing_year', how='left').fillna(0)
        merged = merged.sort_values('filing_year')
        
        merged['ema'] = merged['count'].ewm(alpha=smoothing_factor, adjust=False).mean()
        
        best_idx = merged['ema'].idxmax()
        best_row = merged.loc[best_idx]
        
        results.append({
            'cpc_group': str(cpc),
            'max_ema': float(best_row['ema']),
            'best_year': int(best_row['filing_year'])
        })
    
    results_df = pd.DataFrame(results)
    if not results_df.empty:
        results_df = results_df.sort_values('max_ema', ascending=False)
        top_results = results_df.head(50).to_dict(orient='records')
        all_codes = results_df['cpc_group'].unique().tolist()
    else:
        top_results = []
        all_codes = []
else:
    top_results = []
    all_codes = []

print("__RESULT__:")
print(json.dumps({"top_results": top_results, "all_codes": all_codes}))"""

env_args = {'var_function-call-864177832263507867': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-864177832263504362': 'file_storage/function-call-864177832263504362.json', 'var_function-call-4079124224651373343': [{'symbol': 'A', 'level': '2.0', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'A01', 'level': '4.0', 'titleFull': 'AGRICULTURE; FORESTRY; ANIMAL HUSBANDRY; HUNTING; TRAPPING; FISHING'}, {'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'A01B1/00', 'level': '7.0', 'titleFull': 'Hand tools'}], 'var_function-call-4079124224651374308': [{'Patents_info': 'Patent application (number DE-10317286-A) from DE, belonging to NICOLAY VERWALTUNGS GMBH, with publication no. DE-10317286-B3.'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.'}, {'Patents_info': 'In DE, the patent filing (application no. DE-102009032362-A) is owned by MARTOR KG and has pub. number DE-102009032362-B3.'}], 'var_function-call-12461863306711792077': 'file_storage/function-call-12461863306711792077.json', 'var_function-call-8204491127097861937': {'top_results': [], 'all_codes': []}, 'var_function-call-4322196525132722940': 'Debug Info Printed', 'var_function-call-7056566880538965638': {'top_results': [], 'all_codes': []}, 'var_function-call-2967884845563203929': {'debug': {'count_raw': 70, 'sample_raw_grant': ['14th Mar 2019', 'on November 5th, 2019', 'dated 21st November 2019', 'Mar 21st, 2019', '5th of December, 2019'], 'sample_parsed_grant': ['2019-03-14', '2019-11-05', 'NaT', '2019-03-21', '2019-12-05'], 'count_filtered': 27}}, 'var_function-call-1676743229945816130': {'debug': {'count_filtered': 27, 'filing_year_valid': 0, 'sample_filing': ['2013 on Dec 24th', 'dated 14th October 2010', 'July 21st, 2014', 'on August 8th, 2014', 'dated 10th August 2018'], 'sample_filing_parsed': [None, None, None, None, None], 'exploded_count': 50, 'sample_cpc': ['E21', 'F01', 'F04', 'F02', 'F02']}}}

exec(code, env_args)
