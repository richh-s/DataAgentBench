code = """import json
import pandas as pd

file_path = locals()['var_function-call-824216202442530492']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

def clean_date(d_str):
    if not isinstance(d_str, str):
        return None
    d_str = d_str.lower()
    for word in ['dated', 'on', 'the', 'of', 'st', 'nd', 'rd', 'th', ',']:
        d_str = d_str.replace(word, ' ')
    d_str = ' '.join(d_str.split())
    try:
        return pd.to_datetime(d_str)
    except:
        return None

df['grant_date_dt'] = df['grant_date'].apply(clean_date)
df['filing_date_dt'] = df['filing_date'].apply(clean_date)

start_date = pd.Timestamp('2019-07-01')
end_date = pd.Timestamp('2019-12-31')
df_filtered = df[(df['grant_date_dt'] >= start_date) & (df['grant_date_dt'] <= end_date)]

cpc_list = []
for idx, row in df_filtered.iterrows():
    f_date = row['filing_date_dt']
    if pd.isna(f_date):
        continue
    year = f_date.year
    cpc_json = row['cpc']
    try:
        cpcs = json.loads(cpc_json)
        codes_in_patent = set()
        for c in cpcs:
            if 'code' in c and c['code']:
                codes_in_patent.add(c['code'][:3])
        for code in codes_in_patent:
            cpc_list.append({'code': code, 'year': year})
    except:
        continue

df_cpc = pd.DataFrame(cpc_list)

if df_cpc.empty:
    print("__RESULT__:")
    print("[]")
else:
    counts = df_cpc.groupby(['code', 'year']).size().reset_index(name='count')
    results = []
    codes = counts['code'].unique()
    
    for code in codes:
        sub = counts[counts['code'] == code].sort_values('year')
        min_year = int(sub['year'].min())
        max_year = int(sub['year'].max())
        
        full_range = pd.DataFrame({'year': range(min_year, max_year + 1)})
        merged = pd.merge(full_range, sub, on='year', how='left').fillna({'count': 0})
        
        counts_series = merged['count'].values
        years_series = merged['year'].values
        
        alpha = 0.1
        current_ema = counts_series[0]
        ema_values = [current_ema]
        
        for i in range(1, len(counts_series)):
            current_ema = (counts_series[i] * alpha) + (current_ema * (1 - alpha))
            ema_values.append(current_ema)
            
        merged['ema'] = ema_values
        
        best_idx = merged['ema'].idxmax()
        best_year = merged.loc[best_idx, 'year']
        max_ema = merged.loc[best_idx, 'ema']
        
        results.append({'code': code, 'best_year': int(best_year), 'max_ema': max_ema})
        
    results_df = pd.DataFrame(results).sort_values('max_ema', ascending=False)
    print("__RESULT__:")
    print(json.dumps(results_df.to_dict(orient='records')))"""

env_args = {'var_function-call-7712572374435619726': 'file_storage/function-call-7712572374435619726.json', 'var_function-call-9207544012969803277': [{'Patents_info': 'Patent application (number DE-10317286-A) from DE, belonging to NICOLAY VERWALTUNGS GMBH, with publication no. DE-10317286-B3.', 'grant_date': 'dated 7th October 2004', 'filing_date': 'dated 9th April 2003'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.', 'grant_date': '2006 on Apr 27th', 'filing_date': '18th of April, 2005'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.', 'grant_date': 'Nov 29th, 2007', 'filing_date': '2006, May 11th'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.', 'grant_date': '2009, January 29th', 'filing_date': '30th June 2007'}, {'Patents_info': 'In DE, the patent filing (application no. DE-102009032362-A) is owned by MARTOR KG and has pub. number DE-102009032362-B3.', 'grant_date': '17th Jun 2010', 'filing_date': '2009, July 8th'}], 'var_function-call-9207544012969800986': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}], 'var_function-call-12829125581804936989': [{'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}, {'symbol': 'B99', 'level': '4.0', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION'}, {'symbol': 'B29', 'level': '4.0', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL'}, {'symbol': 'B33', 'level': '4.0', 'titleFull': 'ADDITIVE MANUFACTURING TECHNOLOGY'}], 'var_function-call-606694554395787070': [{'symbol': 'C01', 'level': '4.0', 'titleFull': 'INORGANIC CHEMISTRY'}, {'symbol': 'C01B', 'level': '5.0', 'titleFull': 'NON-METALLIC ELEMENTS; COMPOUNDS THEREOF; METALLOIDS OR COMPOUNDS THEREOF NOT COVERED BY SUBCLASS C01C'}], 'var_function-call-13685583688298079669': [{'count(*)': '11644'}], 'var_function-call-824216202442530492': 'file_storage/function-call-824216202442530492.json', 'var_function-call-10104036999913047761': [{'code': 'A61', 'best_year': 2016, 'max_ema': 2.0}, {'code': 'A21', 'best_year': 2015, 'max_ema': 1.0}, {'code': 'A43', 'best_year': 2016, 'max_ema': 1.0}, {'code': 'A47', 'best_year': 2015, 'max_ema': 1.0}, {'code': 'B23', 'best_year': 2015, 'max_ema': 1.0}, {'code': 'B29', 'best_year': 2012, 'max_ema': 1.0}, {'code': 'B41', 'best_year': 2007, 'max_ema': 1.0}, {'code': 'B60', 'best_year': 2009, 'max_ema': 1.0}, {'code': 'B62', 'best_year': 2010, 'max_ema': 1.0}, {'code': 'B64', 'best_year': 2018, 'max_ema': 1.0}, {'code': 'B66', 'best_year': 2016, 'max_ema': 1.0}, {'code': 'E02', 'best_year': 2012, 'max_ema': 1.0}, {'code': 'E05', 'best_year': 2012, 'max_ema': 1.0}, {'code': 'F01', 'best_year': 2018, 'max_ema': 1.0}, {'code': 'F02', 'best_year': 2010, 'max_ema': 1.0}, {'code': 'F04', 'best_year': 2018, 'max_ema': 1.0}, {'code': 'F05', 'best_year': 2018, 'max_ema': 1.0}, {'code': 'F16', 'best_year': 2009, 'max_ema': 1.0}, {'code': 'F41', 'best_year': 2012, 'max_ema': 1.0}, {'code': 'F42', 'best_year': 2012, 'max_ema': 1.0}], 'var_function-call-7319816257142469515': {'count': 30, 'years': [2019]}}

exec(code, env_args)
