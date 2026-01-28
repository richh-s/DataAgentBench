code = """import json
import re
from pathlib import Path

# Load the query_db result file path variable provided by the tool call
file_path = var_call_nNa0aD0cyur9MIIFtUHym88v

# Read JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    records = json.load(f)

titles_2016 = []

# Helper to extract year from text
year_re = re.compile(r"(?<!\d)(19|20)\d{2}(?!\d)")
for rec in records:
    filename = rec.get('filename', '')
    text = rec.get('text', '')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    # find all years in the text and pick a reasonable candidate
    years = year_re.findall(text)
    # year_re.findall returns tuples because of group; better to use finditer
    years_iter = [m.group(0) for m in year_re.finditer(text)]
    year = None
    # Try to find 2016 specifically
    if '2016' in years_iter:
        year = 2016
    else:
        # otherwise, try to find earliest 20xx after the title header (first 2000s year)
        for y in years_iter:
            yint = int(y)
            if 2000 <= yint <= 2024:
                year = yint
                break
    if year == 2016:
        titles_2016.append(title)

# Deduplicate
titles_2016 = sorted(list(dict.fromkeys(titles_2016)))

import json
print("__RESULT__:")
print(json.dumps(titles_2016))"""

env_args = {'var_call_nNa0aD0cyur9MIIFtUHym88v': 'file_storage/call_nNa0aD0cyur9MIIFtUHym88v.json'}

exec(code, env_args)
