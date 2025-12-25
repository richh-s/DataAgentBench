code = """import json
import pandas as pd
import re
import datetime

# Load data
file_path = locals()['var_function-call-824216202442530492']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Date cleaning function
def clean_date(d_str):
    if not isinstance(d_str, str):
        return None
    # Remove ordinal suffixes and filler words
    d_str = d_str.lower()
    for word in ['dated', 'on', 'the', 'of', 'st', 'nd', 'rd', 'th', ',']:
        d_str = d_str.replace(word, ' ')
    # Normalize whitespace
    d_str = ' '.join(d_str.split())
    try:
        return pd.to_datetime(d_str)
    except:
        return None

# Apply date cleaning
df['grant_date_dt'] = df['grant_date'].apply(clean_date)
df['filing_date_dt'] = df['filing_date'].apply(clean_date)

# Filter for H2 2019 grants (2019-07-01 to 2019-12-31)
start_date = pd.Timestamp('2019-07-01')
end_date = pd.Timestamp('2019-12-31')
df_filtered = df[(df['grant_date_dt'] >= start_date) & (df['grant_date_dt'] <= end_date)].copy()

print(f"Filtered patents count: {len(df_filtered)}")

# Extract CPC Level 4 codes and Filing Year
cpc_list = []
for idx, row in df_filtered.iterrows():
    f_date = row['filing_date_dt']
    if pd.isna(f_date):
        continue
    year = f_date.year
    cpc_json = row['cpc']
    try:
        cpcs = json.loads(cpc_json)
        # Extract unique Level 4 codes (first 3 chars)
        codes = set()
        for c in cpcs:
            if 'code' in c and c['code']:
                # Level 4 is usually Class (3 chars) e.g., H01
                code_l4 = c['code'][:3]
                codes.add(code_l4)
        
        for code in codes:
            cpc_list.append({'code': code, 'year': year})
    except:
        continue

df_cpc = pd.DataFrame(cpc_list)

if df_cpc.empty:
    print("__RESULT__:")
    print("[]")
else:
    # Count filings per Code per Year
    counts = df_cpc.groupby(['code', 'year']).size().reset_index(name='count')
    
    # Calculate EMA for each code
    results = []
    codes = counts['code'].unique()
    
    for code in codes:
        sub = counts[counts['code'] == code].sort_values('year')
        min_year = int(sub['year'].min())
        max_year = int(sub['year'].max())
        
        # Create full range
        full_range = pd.DataFrame({'year': range(min_year, max_year + 1)})
        merged = pd.merge(full_range, sub, on='year', how='left').fillna({'count': 0})
        
        # EMA
        # Pandas ewm: span? com? halflife? alpha?
        # User specified "smoothing factor 0.1". This is alpha.
        # adjust=False usually matches the recursive formula: y_t = alpha*x_t + (1-alpha)*y_{t-1}
        # But pandas initialization might differ.
        # Let's do manual loop to be safe and exact.
        
        ema = 0
        ema_values = []
        alpha = 0.1
        
        # Initial EMA: usually the first value, or 0? 
        # "Exponential moving average". Often initialized with the first observation.
        # Let's assume EMA_0 = count_0
        
        counts_series = merged['count'].values
        years_series = merged['year'].values
        
        current_ema = counts_series[0]
        ema_values.append(current_ema)
        
        for i in range(1, len(counts_series)):
            current_ema = (counts_series[i] * alpha) + (current_ema * (1 - alpha))
            ema_values.append(current_ema)
            
        merged['ema'] = ema_values
        
        # Find best year
        best_idx = merged['ema'].idxmax()
        best_year = merged.loc[best_idx, 'year']
        max_ema = merged.loc[best_idx, 'ema']
        
        results.append({'code': code, 'best_year': int(best_year), 'max_ema': max_ema})
        
    # Sort by max_ema descending
    results_df = pd.DataFrame(results).sort_values('max_ema', ascending=False)
    
    # Keep top 20 or so? Or all? User said "Find the CPC technology areas ...".
    # I'll output top 100 json keys to be safe, then fetch titles for them.
    # Actually, the user wants the list. I'll print the list of codes first to fetch titles in next step.
    
    top_results = results_df.head(20).to_dict(orient='records') # limit to top 20 to avoid huge query
    
    print("__RESULT__:")
    print(json.dumps(top_results))"""

env_args = {'var_function-call-7712572374435619726': 'file_storage/function-call-7712572374435619726.json', 'var_function-call-9207544012969803277': [{'Patents_info': 'Patent application (number DE-10317286-A) from DE, belonging to NICOLAY VERWALTUNGS GMBH, with publication no. DE-10317286-B3.', 'grant_date': 'dated 7th October 2004', 'filing_date': 'dated 9th April 2003'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.', 'grant_date': '2006 on Apr 27th', 'filing_date': '18th of April, 2005'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.', 'grant_date': 'Nov 29th, 2007', 'filing_date': '2006, May 11th'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.', 'grant_date': '2009, January 29th', 'filing_date': '30th June 2007'}, {'Patents_info': 'In DE, the patent filing (application no. DE-102009032362-A) is owned by MARTOR KG and has pub. number DE-102009032362-B3.', 'grant_date': '17th Jun 2010', 'filing_date': '2009, July 8th'}], 'var_function-call-9207544012969800986': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}], 'var_function-call-12829125581804936989': [{'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}, {'symbol': 'B99', 'level': '4.0', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION'}, {'symbol': 'B29', 'level': '4.0', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL'}, {'symbol': 'B33', 'level': '4.0', 'titleFull': 'ADDITIVE MANUFACTURING TECHNOLOGY'}], 'var_function-call-606694554395787070': [{'symbol': 'C01', 'level': '4.0', 'titleFull': 'INORGANIC CHEMISTRY'}, {'symbol': 'C01B', 'level': '5.0', 'titleFull': 'NON-METALLIC ELEMENTS; COMPOUNDS THEREOF; METALLOIDS OR COMPOUNDS THEREOF NOT COVERED BY SUBCLASS C01C'}], 'var_function-call-13685583688298079669': [{'count(*)': '11644'}], 'var_function-call-824216202442530492': 'file_storage/function-call-824216202442530492.json'}

exec(code, env_args)
