code = """import json, pandas as pd
from datetime import datetime

# Load full business data from file
with open(var_call_ccMj76SXJP44Gz9Cia5EqrY6, 'r') as f:
    business_records = json.load(f)

reviews = var_call_vMfMJz8xohOsgduq9LfNrrIe

b_df = pd.DataFrame(business_records)
r_df = pd.DataFrame(reviews)

# Merge on gmap_id to get avg_rating with business info
merged = pd.merge(b_df, r_df, on='gmap_id', how='inner')

# Function to parse closing time from an hours string like '9:30AM–9:30PM'

def parse_close_time(range_str):
    if not isinstance(range_str, str):
        return None
    if 'Closed' in range_str:
        return None
    try:
        # split on en dash or hyphen
        if '' in range_str:
            parts = range_str.split('')
        else:
            parts = range_str.split('')
    except Exception:
        parts = range_str.split('')
    # fallback: use common dash
    if len(parts) == 1:
        parts = range_str.split('-')
    if len(parts) != 2:
        return None
    close_str = parts[1].strip()
    close_str = close_str.replace('.', '')
    try:
        t = datetime.strptime(close_str, '%I%p')
    except ValueError:
        try:
            t = datetime.strptime(close_str, '%I:%M%p')
        except ValueError:
            return None
    return t.hour + t.minute/60.0

# Identify businesses open after 6PM (18.0) on at least one weekday

qualifying = []
for _, row in merged.iterrows():
    hours = row['hours']
    if hours in (None, 'None'):
        continue
    try:
        hrs = json.loads(hours)
    except Exception:
        continue
    open_after_6 = False
    for day, span in hrs:
        if day in ['Monday','Tuesday','Wednesday','Thursday','Friday']:
            if isinstance(span, str) and 'Open 24 hours' in span:
                open_after_6 = True
                break
            close_t = parse_close_time(span)
            if close_t is not None and close_t > 18.0:
                open_after_6 = True
                break
    if open_after_6:
        qualifying.append(row)

q_df = pd.DataFrame(qualifying)

# Convert avg_rating to float and sort
q_df['avg_rating'] = q_df['avg_rating'].astype(float)
q_df = q_df.sort_values(by='avg_rating', ascending=False).head(5)

# Prepare result: name, hours, avg_rating
result = []
for _, row in q_df.iterrows():
    result.append({
        'name': row['name'],
        'hours': row['hours'],
        'avg_rating': round(row['avg_rating'], 3)
    })

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_SuB1i6S59iq0vr5n66FR6OoK': [], 'var_call_vMfMJz8xohOsgduq9LfNrrIe': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0'}], 'var_call_YPfN48IvcOil8nhHa4YZMszU': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'hours': 'None'}], 'var_call_ccMj76SXJP44Gz9Cia5EqrY6': 'file_storage/call_ccMj76SXJP44Gz9Cia5EqrY6.json'}

exec(code, env_args)
