code = """import json
import pandas as pd
import re
import ast

# Load data from storage-provided file paths
with open(var_call_Vc58INWhVzo9NGpYAGxYB2VT, 'r', encoding='utf-8') as f:
    biz = json.load(f)
with open(var_call_JZJmfDFs5jRvmzrSKIn4E5p5, 'r', encoding='utf-8') as f:
    rev = json.load(f)

dfb = pd.DataFrame(biz)
dfr = pd.DataFrame(rev)

# Normalize types
if 'rating' in dfr.columns:
    dfr['rating'] = pd.to_numeric(dfr['rating'], errors='coerce')

# Compute average rating per business
avg_rating = dfr.groupby('gmap_id', dropna=True)['rating'].mean().reset_index().rename(columns={'rating':'avg_rating'})

# Merge with business data
df = pd.merge(dfb, avg_rating, on='gmap_id', how='inner')

# Helper to parse time strings into minutes since midnight
def parse_time_token(tok):
    tok = tok.strip()
    # Handle cases like 'Closed' or empty
    if not tok or tok.lower() == 'closed':
        return None
    # Remove periods/spaces
    tok = tok.replace('.', '').upper()
    # Regex to capture hour[:minute] and AM/PM
    m = re.match(r"^(\d{1,2})(:(\d{2}))?\s*(AM|PM)?$", tok)
    if not m:
        return None
    hour = int(m.group(1))
    minute = int(m.group(3)) if m.group(3) else 0
    period = m.group(4)
    if period == 'AM':
        if hour == 12:
            hour = 0
    elif period == 'PM':
        if hour != 12:
            hour += 12
    else:
        # If no AM/PM, assume 24-hour? but here unlikely. Try to infer: if hour==24 -> 0
        if hour == 24:
            hour = 0
    return hour*60 + minute

# Parse hours field which is a string representation of a list
weekday_names = set(['Monday','Tuesday','Wednesday','Thursday','Friday'])

def opens_after_6pm(hours_str):
    if not hours_str or hours_str == 'None':
        return False
    # Try to parse JSON first
    hours_list = None
    try:
        hours_list = json.loads(hours_str)
    except Exception:
        try:
            hours_list = ast.literal_eval(hours_str)
        except Exception:
            # fallback: find day-time pairs with regex
            hours_list = []
            parts = re.findall(r"\[?\s*'?(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)'?\s*,\s*'([^']+)'\s*\]", hours_str)
            hours_list = [[d,t] for d,t in parts]
    if not isinstance(hours_list, list):
        return False
    for entry in hours_list:
        if not isinstance(entry, (list, tuple)) or len(entry) < 2:
            continue
        day = entry[0]
        times = entry[1]
        if day not in weekday_names:
            continue
        if not times or times.lower() == 'closed':
            continue
        # Some entries may have multiple ranges separated by commas
        ranges = re.split(r"\s*,\s*", times)
        for r in ranges:
            # Split on dash variants
            parts = re.split(r"[-–—]", r)
            if len(parts) < 2:
                continue
            start_tok = parts[0].strip()
            end_tok = parts[1].strip()
            start_min = parse_time_token(start_tok)
            end_min = parse_time_token(end_tok)
            if end_min is None:
                continue
            # If end_min <= start_min, assume it goes past midnight: add 24*60
            if start_min is not None and end_min <= start_min:
                end_min += 24*60
            # Check if closing strictly after 6:00 PM (18:00 -> 1080 minutes)
            if end_min > 18*60:
                return True
    return False

# Apply filter
df['opens_after_6pm_weekday'] = df['hours'].apply(opens_after_6pm)
filtered = df[df['opens_after_6pm_weekday'] & df['avg_rating'].notna()].copy()

# Sort by avg_rating desc and take top 5
filtered['avg_rating'] = filtered['avg_rating'].astype(float)
top5 = filtered.sort_values(by=['avg_rating','num_of_reviews'], ascending=[False, False]).head(5)

# Prepare output
out = []
for _, row in top5.iterrows():
    out.append({
        'name': row.get('name'),
        'hours': row.get('hours'),
        'average_rating': round(float(row.get('avg_rating')), 2)
    })

result_json = json.dumps(out)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_ES0DfPMgOPb2uwij2wEvKoq1': ['business_description'], 'var_call_Vc58INWhVzo9NGpYAGxYB2VT': 'file_storage/call_Vc58INWhVzo9NGpYAGxYB2VT.json', 'var_call_JZJmfDFs5jRvmzrSKIn4E5p5': 'file_storage/call_JZJmfDFs5jRvmzrSKIn4E5p5.json'}

exec(code, env_args)
