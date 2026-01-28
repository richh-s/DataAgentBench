code = """import json
import os
import re
from collections import defaultdict

# Load level 5 CPC symbols
level5_file = var_functions.query_db:5
# level5_file is a string path to JSON file
with open(level5_file, 'r') as f:
    level5_data = json.load(f)

level5_symbols = [row['symbol'] for row in level5_data]
# Build a prefix map: for speed, we can group by first char then etc.
# Sort symbols by length descending for matching.
level5_symbols_sorted = sorted(level5_symbols, key=lambda x: -len(x))

# Load publication info data
pub_file = var_functions.query_db:6
with open(pub_file, 'r') as f:
    pub_data = json.load(f)

# Initialize count dict
counts = defaultdict(int)

# Regex to extract year
year_regex = re.compile(r'(\d{4})$')

for row in pub_data:
    date_str = row.get('publication_date', '')
    m = year_regex.search(date_str)
    if not m:
        continue
    year = int(m.group(1))
    # parse CPC codes
    cpc_str = row.get('cpc', '')
    if not cpc_str:
        continue
    try:
        cpc_list = json.loads(cpc_str)
    except Exception as e:
        # ignore malformed
        continue
    for item in cpc_list:
        code = item.get('code')
        if not code:
            continue
        # find matching level5 symbol
        # Because code may be like "C01B33/00" or "C01B" (maybe no slash)
        # We'll check startswith for each level5 symbol.
        # For speed, we can break once found.
        # However a code may match multiple longer symbols? Typically the most specific (longest) match is appropriate.
        # Since sorted by descending length, the first match will be the longest.
        matched = None
        for sym in level5_symbols_sorted:
            if code.startswith(sym):
                # ensure that the next char (if any) is not a letter (to avoid matching partial)
                # e.g., sym "C01" should not match "C01B33"? But level5 symbols are length >= 4 maybe.
                # We'll just accept startswith.
                matched = sym
                break
        if matched:
            counts[(matched, year)] += 1

# Let's see number of distinct groups
groups = set(g for g,_ in counts.keys())
len(groups)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
