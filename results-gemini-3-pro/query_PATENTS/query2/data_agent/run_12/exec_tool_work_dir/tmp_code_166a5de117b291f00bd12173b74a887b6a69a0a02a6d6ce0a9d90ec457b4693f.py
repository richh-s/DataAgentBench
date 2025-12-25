code = """import json
import re
import pandas as pd

with open(locals()['var_function-call-6414003164698615798'], 'r') as f:
    data = json.load(f)

months = {
    'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6,
    'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12,
    'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'jun': 6,
    'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
}

def parse_date_robust(date_str):
    if not date_str: return None
    s = date_str.lower().replace(',', ' ').replace('.', ' ').replace('of', ' ').replace('the', ' ')
    
    # Year
    y_match = re.search(r'\b(20\d{2})\b', s)
    if not y_match: return None
    year = int(y_match.group(1))
    
    # Month
    month = None
    # Sort months by length desc to match 'january' before 'jan'
    for m_name in sorted(months.keys(), key=len, reverse=True):
        if m_name in s:
            month = months[m_name]
            break
    if not month: return None
    return year, month

filings = []

for row in data:
    # Filter DE
    p_info = row.get('Patents_info', '')
    if not (re.search(r'\bDE[- ]', p_info) or "from DE" in p_info or "In DE" in p_info or "Germany" in p_info):
        continue
        
    # Grant Date H2 2019
    g_str = row.get('grant_date', '')
    gym = parse_date_robust(g_str)
    if not gym: continue
    gy, gm = gym
    if not (gy == 2019 and gm >= 7):
        continue
        
    # Filing Date Year
    f_str = row.get('filing_date', '')
    fym = parse_date_robust(f_str)
    if not fym: continue
    f_year = fym[0]
    
    # CPC Level 4
    cpc_json = row.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_json)
        codes = set()
        for entry in cpc_list:
            code = entry.get('code', '')
            if len(code) >= 3:
                codes.add(code[:3])
        
        for c in codes:
            filings.append({'cpc': c, 'year': f_year})
    except:
        pass

df = pd.DataFrame(filings)

final_list = []

if not df.empty:
    # Count per CPC/Year
    counts = df.groupby(['cpc', 'year']).size().reset_index(name='count')
    all_years = range(counts['year'].min(), counts['year'].max() + 1)
    unique_cpcs = counts['cpc'].unique()
    
    ema_rows = []
    
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
            ema_rows.append({'cpc': cpc, 'year': y, 'ema': ema})
            prev_ema = ema
            
    ema_df = pd.DataFrame(ema_rows)
    
    # Identify winners per year
    winners = {}
    for y in all_years:
        yd = ema_df[ema_df['year'] == y]
        if not yd.empty:
            best = yd.sort_values('ema', ascending=False).iloc[0]
            winners[y] = best['cpc']
            
    unique_winners = set(winners.values())
    
    # Prepare result for these winners
    for cpc in unique_winners:
        stats = ema_df[ema_df['cpc'] == cpc]
        best_stat = stats.sort_values('ema', ascending=False).iloc[0]
        final_list.append({
            'cpc': cpc,
            'best_year': int(best_stat['year']),
            'max_ema': float(best_stat['ema'])
        })

print("__RESULT__:")
print(json.dumps(final_list))"""

env_args = {'var_function-call-1868465921641692363': 'file_storage/function-call-1868465921641692363.json', 'var_function-call-6414003164698615067': [{'symbol': 'A01K2227/108', 'level': '9.0', 'titleFull': 'Swine'}], 'var_function-call-6414003164698615798': 'file_storage/function-call-6414003164698615798.json', 'var_function-call-4244802832919163477': [{'symbol': 'A', 'level': '2.0', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'A01', 'level': '4.0', 'titleFull': 'AGRICULTURE; FORESTRY; ANIMAL HUSBANDRY; HUNTING; TRAPPING; FISHING'}, {'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'G06F', 'level': '5.0', 'titleFull': 'ELECTRIC DIGITAL DATA PROCESSING'}, {'symbol': 'A01B1/00', 'level': '7.0', 'titleFull': 'Hand tools'}, {'symbol': 'G06F9/00', 'level': '7.0', 'titleFull': 'Arrangements for program control, e.g. control units'}], 'var_function-call-14093412893191991109': [], 'var_function-call-8691657811473980173': [], 'var_function-call-5507538740903062421': {'total_records': 4833, 'de_matches_count': 32, 'sample_de_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'sample_de_grant_date': '14th Mar 2019', 'parsed_sample_date': 'Parse Error', 'de_h2_2019_count': 0}, 'var_function-call-1410127800540734811': {'debug_dates': [], 'msg': 'No data after filtering'}, 'var_function-call-14949167756059639455': ['14th Mar 2019', 'dated 21st November 2019', '22nd of August, 2019', 'September the 19th, 2019', 'on March 21st, 2019', 'August the 29th, 2019', '2019 on Mar 28th', '2019, December 24th', 'December 24th, 2019', 'dated 9th May 2019']}

exec(code, env_args)
