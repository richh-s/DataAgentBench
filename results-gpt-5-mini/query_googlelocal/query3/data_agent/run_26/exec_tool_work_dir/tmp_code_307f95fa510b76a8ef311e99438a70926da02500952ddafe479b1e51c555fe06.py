code = """import json
import pandas as pd
import ast
import re

# Load data from storage variables (file paths)
with open(var_call_mfM0RGhOtXfxZPEhumXMRxNT, 'r') as f:
    reviews = json.load(f)
with open(var_call_YZwmggaJMZAQFt97IzsZi6Vh, 'r') as f:
    businesses = json.load(f)

# Create DataFrames
df_rev = pd.DataFrame(reviews)
# Ensure rating numeric
df_rev['rating'] = pd.to_numeric(df_rev['rating'], errors='coerce')

# Compute average rating per gmap_id
avg_ratings = df_rev.groupby('gmap_id', dropna=False)['rating'].mean().reset_index().rename(columns={'rating':'avg_rating'})

# Businesses DataFrame
df_bus = pd.DataFrame(businesses)

# Helper to parse closing time
time_split_re = re.compile(r'[\-\u2013\u2014–—]')
parse_re = re.compile(r"^(\d{1,2})(?::(\d{2}))?\s*([APap][Mm])?$")

def parse_time(t):
    if t is None:
        return None
    s = t.strip()
    # remove spaces
    s = s.replace(' ', '')
    m = parse_re.match(s)
    if not m:
        return None
    hour = int(m.group(1))
    minute = int(m.group(2)) if m.group(2) else 0
    mer = m.group(3)
    if mer:
        mer = mer.upper()
    # Default: if no meridian, return None
    if not mer:
        return None
    if mer == 'PM' and hour != 12:
        hour += 12
    if mer == 'AM' and hour == 12:
        hour = 0
    return hour + minute/60.0

weekdays = set(['Monday','Tuesday','Wednesday','Thursday','Friday'])

results = []

# Merge avg ratings into businesses
df_merged = pd.merge(df_bus, avg_ratings, on='gmap_id', how='left')

for _, row in df_merged.iterrows():
    hours_raw = row.get('hours')
    if hours_raw is None:
        continue
    # treat string "None" as no hours
    if isinstance(hours_raw, str) and hours_raw.strip().lower() == 'none':
        continue
    # try to literal_eval
    try:
        hours_parsed = ast.literal_eval(hours_raw)
    except Exception:
        # fallback: try json loads
        try:
            hours_parsed = json.loads(hours_raw)
        except Exception:
            continue
    # hours_parsed expected to be list of [day, range]
    open_after_6 = False
    if isinstance(hours_parsed, list):
        for entry in hours_parsed:
            if not (isinstance(entry, list) or isinstance(entry, tuple)) or len(entry) < 2:
                continue
            day = entry[0]
            rng = entry[1]
            if day not in weekdays:
                continue
            if isinstance(rng, str):
                if rng.strip().lower() == 'closed':
                    continue
                # split by dash/en-dash
                parts = time_split_re.split(rng)
                if len(parts) < 2:
                    continue
                close_str = parts[-1].strip()
                ct = parse_time(close_str)
                if ct is None:
                    # sometimes format like '11AM–9:30PM' should parse; if not, try to insert space before AM/PM
                    # try regex to extract trailing AM/PM
                    m = re.search(r'([0-9:]+\s*[APap][Mm])$', close_str)
                    if m:
                        ct = parse_time(m.group(1))
                if ct is not None and ct > 18.0:
                    open_after_6 = True
                    break
    if open_after_6:
        avg = row.get('avg_rating')
        if pd.isna(avg):
            continue
        results.append({
            'name': row.get('name'),
            'gmap_id': row.get('gmap_id'),
            'hours': hours_raw,
            'avg_rating': round(float(avg), 2)
        })

# Sort by avg_rating descending and take top 5
results_sorted = sorted(results, key=lambda x: x['avg_rating'], reverse=True)[:5]

import json as _json
print("__RESULT__:")
print(_json.dumps(results_sorted))"""

env_args = {'var_call_wXMoFmPg4W5eZ3A8t1XCPgle': ['review'], 'var_call_BulkPTnseUboUVJ5olWkrPEu': ['business_description'], 'var_call_mfM0RGhOtXfxZPEhumXMRxNT': 'file_storage/call_mfM0RGhOtXfxZPEhumXMRxNT.json', 'var_call_YZwmggaJMZAQFt97IzsZi6Vh': 'file_storage/call_YZwmggaJMZAQFt97IzsZi6Vh.json'}

exec(code, env_args)
