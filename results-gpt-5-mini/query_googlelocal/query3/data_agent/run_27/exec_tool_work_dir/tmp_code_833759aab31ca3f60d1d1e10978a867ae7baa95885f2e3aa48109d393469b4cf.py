code = """import json
import pandas as pd
from datetime import datetime

# Load data from previous tool results
ratings = var_call_8QgOAtlXUWStwHo7ZiV3gh2O  # list of dicts

# Read business query result from file
path = var_call_C4BLxMC08IKryIBmJy9Z3GWV
with open(path, 'r', encoding='utf-8') as f:
    businesses = json.load(f)

# Convert to DataFrame
df_bus = pd.DataFrame(businesses)
df_ratings = pd.DataFrame(ratings)

# Normalize ratings types
df_ratings['avg_rating'] = df_ratings['avg_rating'].astype(float)
if 'n_reviews' in df_ratings.columns:
    df_ratings['n_reviews'] = df_ratings['n_reviews'].astype(int)

# Merge on gmap_id
df = pd.merge(df_bus, df_ratings, on='gmap_id', how='inner')

# Helper to parse hours string into list
import re

def parse_hours_str(s):
    if s is None:
        return []
    try:
        # The hours field appears to be a JSON-encoded string; try json.loads
        hours = json.loads(s)
        return hours
    except Exception:
        try:
            # Fallback: literal eval
            import ast
            return ast.literal_eval(s)
        except Exception:
            return []

# Helper to parse time like '9:30AM' or '6PM' to minutes since midnight

def time_to_minutes(tstr):
    t = tstr.strip().upper().replace(' ', '').replace('.', '')
    # Replace unicode variants of colon/dash if any
    # Try formats
    for fmt in ('%I:%M%p', '%I%p'):
        try:
            dt = datetime.strptime(t, fmt)
            return dt.hour * 60 + dt.minute
        except Exception:
            continue
    # If failed, try to insert minutes if missing
    m = re.match(r"^(\d{1,2})[:](\d{2})(AM|PM)$", t)
    if m:
        hh = int(m.group(1)); mm = int(m.group(2)); ampm = m.group(3)
        if ampm == 'PM' and hh != 12:
            hh += 12
        if ampm == 'AM' and hh == 12:
            hh = 0
        return hh*60+mm
    # If still failed, return None
    return None

# Weekdays to consider
weekdays = set(['Monday','Tuesday','Wednesday','Thursday','Friday'])

qual_rows = []

for _, row in df.iterrows():
    hours_raw = row['hours']
    hours_list = parse_hours_str(hours_raw)
    open_after_6 = False
    # hours_list expected as list of [day, timestr]
    for entry in hours_list:
        if not isinstance(entry, (list, tuple)) or len(entry) < 2:
            continue
        day = entry[0]
        timestr = entry[1]
        if day not in weekdays:
            continue
        if not isinstance(timestr, str):
            continue
        if timestr.strip().lower() == 'closed':
            continue
        # Normalize dash characters to standard '-'
        timestr_norm = timestr.replace('\u2013', '-').replace('\u2014','-').replace('\u2012','-').replace('\u2010','-')
        # Some entries use en dash directly; also there may be unicode in the raw string; ensure proper
        timestr_norm = timestr_norm.replace('\u2013', '-').replace('\u2014','-')
        # Replace any unicode en-dash literal
        timestr_norm = timestr_norm.replace('\u2013', '-')
        # Split on '-' or '–' or '\u2013'
        parts = re.split(r'[-–—]', timestr_norm)
        if len(parts) < 2:
            continue
        close_raw = parts[-1]
        # Ensure AM/PM present; if close_raw contains spaces like '9:30PM' fine
        close_min = time_to_minutes(close_raw)
        if close_min is None:
            # try to extract with regex for patterns like '9:30PM'
            m = re.search(r"(\d{1,2}(:\d{2})?\s*(AM|PM))", close_raw, re.IGNORECASE)
            if m:
                close_min = time_to_minutes(m.group(1))
        if close_min is None:
            continue
        if close_min > 18*60:
            open_after_6 = True
            break
    if open_after_6:
        qual_rows.append({
            'gmap_id': row['gmap_id'],
            'name': row['name'],
            'hours': hours_raw,
            'avg_rating': row['avg_rating'],
            'n_reviews': row.get('n_reviews', None)
        })

# Sort by avg_rating desc, then n_reviews desc
qual_df = pd.DataFrame(qual_rows)
if qual_df.empty:
    result = []
else:
    qual_df['avg_rating'] = qual_df['avg_rating'].astype(float)
    if 'n_reviews' in qual_df.columns:
        qual_df['n_reviews'] = qual_df['n_reviews'].astype('Int64')
    qual_df = qual_df.sort_values(by=['avg_rating','n_reviews'], ascending=[False, False])
    top5 = qual_df.head(5)
    result = []
    for _, r in top5.iterrows():
        result.append({
            'name': r['name'],
            'gmap_id': r['gmap_id'],
            'hours': r['hours'],
            'avg_rating': float(round(r['avg_rating'], 3)),
            'n_reviews': int(r['n_reviews']) if pd.notna(r['n_reviews']) else None
        })

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_1DD2ubBRQ2ynQcANCsxPtE0S': ['business_description'], 'var_call_C4BLxMC08IKryIBmJy9Z3GWV': 'file_storage/call_C4BLxMC08IKryIBmJy9Z3GWV.json', 'var_call_8QgOAtlXUWStwHo7ZiV3gh2O': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889', 'n_reviews': '18'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0', 'n_reviews': '3'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0', 'n_reviews': '1'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605', 'n_reviews': '378'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0', 'n_reviews': '2'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625', 'n_reviews': '8'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375', 'n_reviews': '8'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111', 'n_reviews': '45'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0', 'n_reviews': '6'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118', 'n_reviews': '34'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0', 'n_reviews': '4'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0', 'n_reviews': '8'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177', 'n_reviews': '17'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'n_reviews': '56'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333', 'n_reviews': '15'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333', 'n_reviews': '6'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0', 'n_reviews': '8'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875', 'n_reviews': '8'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0', 'n_reviews': '1'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889', 'n_reviews': '18'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0', 'n_reviews': '5'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875', 'n_reviews': '8'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925', 'n_reviews': '26'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667', 'n_reviews': '27'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857', 'n_reviews': '21'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0', 'n_reviews': '8'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667', 'n_reviews': '6'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125', 'n_reviews': '8'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5', 'n_reviews': '8'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143', 'n_reviews': '84'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0', 'n_reviews': '8'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0', 'n_reviews': '3'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'n_reviews': '7'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223', 'n_reviews': '18'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25', 'n_reviews': '4'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'n_reviews': '35'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'n_reviews': '18'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856', 'n_reviews': '7'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'n_reviews': '6'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'n_reviews': '6'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5', 'n_reviews': '6'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381', 'n_reviews': '168'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586', 'n_reviews': '58'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4', 'n_reviews': '5'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0', 'n_reviews': '8'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0', 'n_reviews': '5'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0', 'n_reviews': '3'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0', 'n_reviews': '18'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105', 'n_reviews': '58'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263', 'n_reviews': '38'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875', 'n_reviews': '8'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0', 'n_reviews': '3'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0', 'n_reviews': '28'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789', 'n_reviews': '38'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75', 'n_reviews': '8'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421', 'n_reviews': '38'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75', 'n_reviews': '4'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058', 'n_reviews': '17'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0', 'n_reviews': '3'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353', 'n_reviews': '68'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375', 'n_reviews': '16'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25', 'n_reviews': '8'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615', 'n_reviews': '52'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5', 'n_reviews': '2'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806', 'n_reviews': '31'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0', 'n_reviews': '4'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333', 'n_reviews': '48'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838', 'n_reviews': '37'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889', 'n_reviews': '18'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625', 'n_reviews': '16'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895', 'n_reviews': '38'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0', 'n_reviews': '1'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667', 'n_reviews': '18'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944', 'n_reviews': '143'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0', 'n_reviews': '3'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0', 'n_reviews': '3'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222', 'n_reviews': '18'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0', 'n_reviews': '2'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0', 'n_reviews': '3'}]}

exec(code, env_args)
