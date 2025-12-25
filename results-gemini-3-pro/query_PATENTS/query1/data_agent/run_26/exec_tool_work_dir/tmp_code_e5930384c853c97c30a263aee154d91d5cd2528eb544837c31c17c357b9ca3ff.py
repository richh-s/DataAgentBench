code = """import json
import re

# Get file paths from local variables
path_level5 = locals()['var_function-call-8552121385304934685']
path_patents = locals()['var_function-call-12122079112080214207']

# Load level 5 symbols
with open(path_level5, 'r') as f:
    level5_list = json.load(f)
level5_symbols = set(item['symbol'] for item in level5_list)

# Load patent data
with open(path_patents, 'r') as f:
    patent_data = json.load(f)

# Regex for year
year_pattern = re.compile(r'\b(19|20)\d{2}\b')

counts = {} # {symbol: {year: count}}

for row in patent_data:
    f_date = row.get('filing_date')
    if not f_date:
        continue
    
    match = year_pattern.search(f_date)
    if not match:
        continue
    year = int(match.group(0))
    
    cpc_str = row.get('cpc')
    if not cpc_str:
        continue
    
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
    
    current_patent_symbols = set()
    for item in cpc_list:
        code = item.get('code', '')
        # Check against level 5 symbols
        # Assumption: Level 5 symbols are 4 characters (Subclass)
        if len(code) >= 4:
            prefix = code[:4]
            if prefix in level5_symbols:
                current_patent_symbols.add(prefix)
            
    for s in current_patent_symbols:
        if s not in counts:
            counts[s] = {}
        counts[s][year] = counts[s].get(year, 0) + 1

# Calculate EMA and find best year
alpha = 0.2
selected_symbols = []

for sym, year_counts in counts.items():
    years = sorted(year_counts.keys())
    if not years:
        continue
        
    start_year = years[0]
    end_year = years[-1]
    
    if end_year < 2022:
        continue
        
    ema = 0
    max_ema = -1
    best_year = -1
    
    current_ema = None
    
    for y in range(start_year, end_year + 1):
        c = year_counts.get(y, 0)
        if current_ema is None:
            current_ema = c
        else:
            current_ema = alpha * c + (1 - alpha) * current_ema
        
        # Check if this year is the best so far.
        # Note: If multiple years have same max_ema, we usually take the first or last?
        # Float comparison might be tricky, but exact equality is rare.
        if current_ema > max_ema:
            max_ema = current_ema
            best_year = y
        elif current_ema == max_ema:
             # Tie-breaking? Let's stick with the first one or update?
             # If the EMA is flat, the "best year" is ambiguous.
             # But strictly "highest".
             pass
            
    if best_year == 2022:
        selected_symbols.append(sym)

print("__RESULT__:")
print(json.dumps(selected_symbols))"""

env_args = {'var_function-call-1397089811542180174': ['publicationinfo'], 'var_function-call-1397089811542180177': ['cpc_definition'], 'var_function-call-3017323399836205737': 'file_storage/function-call-3017323399836205737.json', 'var_function-call-3017323399836208786': [{'count': '677'}], 'var_function-call-16375230660246420135': [{'count(*)': '277813'}], 'var_function-call-8552121385304934685': 'file_storage/function-call-8552121385304934685.json', 'var_function-call-12122079112080214207': 'file_storage/function-call-12122079112080214207.json'}

exec(code, env_args)
