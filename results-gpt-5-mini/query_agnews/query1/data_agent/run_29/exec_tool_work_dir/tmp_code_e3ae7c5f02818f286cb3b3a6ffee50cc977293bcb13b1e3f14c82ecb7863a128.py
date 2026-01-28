code = """import json
import re

# Load the query result file path variable provided by the previous tool call
file_path = var_call_lcn7jxCQWGyFv4yXVeJJdyXJ

with open(file_path, 'r', encoding='utf-8') as f:
    records = json.load(f)

# Define sports-related keywords
sports_keywords = [
    'soccer','football','goal','goals','match','matches','scored','score','beat','defeated',
    'basketball','baseball','tennis','golf','cricket','innings','tackle','wicket','race','racing',
    'formula','motogp','olympic','olympics','season','league','playoff','playoffs','cup',
    'premier','fifa','uefa','nba','nfl','mlb','nhl','coach','manager','transfer','signed',
    'boxing','fight','knockout','derby','kick','pitch','home run','hat-trick','hat trick'
]

# compile regex for efficiency
keyword_pattern = re.compile(r"\b(" + "|".join(re.escape(k) for k in sports_keywords) + r")\b", flags=re.IGNORECASE)

max_len = -1
max_title = None
max_article = None

for rec in records:
    title = rec.get('title') or ''
    description = rec.get('description') or ''
    # Normalize to string
    if not isinstance(title, str):
        title = str(title)
    if not isinstance(description, str):
        description = str(description)
    # Determine if sports by keyword presence in title or description
    if keyword_pattern.search(title) or keyword_pattern.search(description):
        desc_len = len(description)
        if desc_len > max_len:
            max_len = desc_len
            max_title = title
            max_article = rec

# If none found by keywords, as a fallback attempt to classify by title containing team names or 'match' etc.
if max_title is None:
    # try looser heuristic: titles containing Vs. or ' vs '
    for rec in records:
        title = rec.get('title') or ''
        description = rec.get('description') or ''
        if not isinstance(title, str):
            title = str(title)
        if not isinstance(description, str):
            description = str(description)
        if ' vs ' in title.lower() or ' vs. ' in title.lower() or 'v.' in title.lower() or 'v ' in title.lower():
            desc_len = len(description)
            if desc_len > max_len:
                max_len = desc_len
                max_title = title
                max_article = rec

# Prepare result
result = max_title if max_title is not None else ''

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_YXDAsv9yXq2JZfiieyps2aGi': ['articles'], 'var_call_lcn7jxCQWGyFv4yXVeJJdyXJ': 'file_storage/call_lcn7jxCQWGyFv4yXVeJJdyXJ.json'}

exec(code, env_args)
