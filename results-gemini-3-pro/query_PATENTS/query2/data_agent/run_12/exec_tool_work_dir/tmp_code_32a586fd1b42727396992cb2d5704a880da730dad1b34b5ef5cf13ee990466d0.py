code = """import json
import re
import pandas as pd

with open(locals()['var_function-call-6414003164698615798'], 'r') as f:
    data = json.load(f)

months = {
    'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
    'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12,
    'january': 1, 'february': 2, 'march': 3, 'april': 4, 'june': 6,
    'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12
}

def parse_date_manual(date_str):
    if not date_str: return None
    s = date_str.lower()
    # Find year (4 digits)
    y_match = re.search(r'\b(20\d{2})\b', s)
    if not y_match: return None
    year = int(y_match.group(1))
    
    # Find month
    month = None
    for m_name, m_val in months.items():
        if m_name in s:
            month = m_val
            break
    if not month: return None
    
    return year, month

# Filter and Process
filtered_filings = []
debug_dates = []

for row in data:
    p_info = row.get('Patents_info', '')
    # Filter DE
    if not (re.search(r'\bDE[- ]', p_info) or "from DE" in p_info or "In DE" in p_info or "Germany" in p_info):
        continue
        
    g_date_str = row.get('grant_date', '')
    ym = parse_date_manual(g_date_str)
    
    if ym:
        y, m = ym
        debug_dates.append((g_date_str, y, m))
        if y == 2019 and m >= 7:
            # Match!
            # Get Filing Year
            f_date_str = row.get('filing_date', '')
            ym_f = parse_date_manual(f_date_str)
            if ym_f:
                f_year = ym_f[0]
                
                # Extract CPC Level 4 (First 3 chars)
                cpc_json = row.get('cpc', '[]')
                try:
                    cpc_list = json.loads(cpc_json)
                    codes = set()
                    for entry in cpc_list:
                        code = entry.get('code', '')
                        if len(code) >= 3:
                            codes.add(code[:3])
                    
                    for c in codes:
                        filtered_filings.append({'cpc': c, 'year': f_year})
                except:
                    pass

df = pd.DataFrame(filtered_filings)

# EMA and Ranking
results = []
if not df.empty:
    counts = df.groupby(['cpc', 'year']).size().reset_index(name='count')
    all_years = range(counts['year'].min(), counts['year'].max() + 1)
    unique_cpcs = counts['cpc'].unique()
    
    ema_data = []
    
    for cpc in unique_cpcs:
        cpc_counts = counts[counts['cpc'] == cpc].set_index('year')['count']
        cpc_series = cpc_counts.reindex(all_years, fill_value=0)
        
        prev_ema = None
        alpha = 0.1
        
        for y in all_years:
            val = cpc_series[y]
            if prev_ema is None:
                ema = val
            else:
                ema = (val * alpha) + (prev_ema * (1 - alpha))
            ema_vals = {'cpc': cpc, 'year': y, 'ema': ema}
            ema_data.append(ema_vals)
            prev_ema = ema
            
    ema_df = pd.DataFrame(ema_data)
    
    # Winners per year
    winners = {}
    for y in all_years:
        year_data = ema_df[ema_df['year'] == y]
        if not year_data.empty:
            # Get max EMA
            max_ema = year_data['ema'].max()
            # Get all CPCs with this max_ema (ties?)
            top_rows = year_data[year_data['ema'] == max_ema]
            # Just take the first one for now or all
            for _, row in top_rows.iterrows():
                winners[y] = {'cpc': row['cpc'], 'ema': row['ema']}
                break # Take one
                
    # Collect final list
    final_cpcs = {}
    winner_codes = set(v['cpc'] for v in winners.values())
    
    for cpc in winner_codes:
        cpc_stats = ema_df[ema_df['cpc'] == cpc]
        best_stat = cpc_stats.sort_values('ema', ascending=False).iloc[0]
        final_cpcs[cpc] = {
            'cpc': cpc,
            'best_year': int(best_stat['year']),
            'max_ema': float(best_stat['ema'])
        }
    
    print("__RESULT__:")
    print(json.dumps(list(final_cpcs.values())))

else:
    # return debug info
    print("__RESULT__:")
    print(json.dumps({"debug_dates": debug_dates, "msg": "No data after filtering"}))"""

env_args = {'var_function-call-1868465921641692363': 'file_storage/function-call-1868465921641692363.json', 'var_function-call-6414003164698615067': [{'symbol': 'A01K2227/108', 'level': '9.0', 'titleFull': 'Swine'}], 'var_function-call-6414003164698615798': 'file_storage/function-call-6414003164698615798.json', 'var_function-call-4244802832919163477': [{'symbol': 'A', 'level': '2.0', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'A01', 'level': '4.0', 'titleFull': 'AGRICULTURE; FORESTRY; ANIMAL HUSBANDRY; HUNTING; TRAPPING; FISHING'}, {'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'G06F', 'level': '5.0', 'titleFull': 'ELECTRIC DIGITAL DATA PROCESSING'}, {'symbol': 'A01B1/00', 'level': '7.0', 'titleFull': 'Hand tools'}, {'symbol': 'G06F9/00', 'level': '7.0', 'titleFull': 'Arrangements for program control, e.g. control units'}], 'var_function-call-14093412893191991109': [], 'var_function-call-8691657811473980173': [], 'var_function-call-5507538740903062421': {'total_records': 4833, 'de_matches_count': 32, 'sample_de_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'sample_de_grant_date': '14th Mar 2019', 'parsed_sample_date': 'Parse Error', 'de_h2_2019_count': 0}}

exec(code, env_args)
