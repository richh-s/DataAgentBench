code = """import json, pandas as pd

# Load business rows (may be a path)
biz_src = var_call_pzxbX9oVIPYi7bVDwXp6PbPO
if isinstance(biz_src, str):
    with open(biz_src, 'r', encoding='utf-8') as f:
        biz = json.load(f)
else:
    biz = biz_src

rev = var_call_7XeIwz1fMzTvUy3no0acBd2j

biz_df = pd.DataFrame(biz)
rev_df = pd.DataFrame(rev)
if not rev_df.empty:
    rev_df['avg_rating'] = pd.to_numeric(rev_df['avg_rating'], errors='coerce')
    rev_df['review_count'] = pd.to_numeric(rev_df['review_count'], errors='coerce')

weekday_set = {'Monday','Tuesday','Wednesday','Thursday','Friday'}

def closes_after_6(timestr: str) -> bool:
    if timestr is None:
        return False
    s = str(timestr)
    if s.lower().strip() in ['closed', 'none', 'nan', '']:
        return False
    if 'Open 24 hours' in s:
        return True
    # handle possible multiple intervals separated by ','
    parts = [p.strip() for p in s.split(',')]
    for p in parts:
        # get end time after dash/en-dash
        if '–' in p:
            segs = p.split('–')
        elif '-' in p:
            segs = p.split('-')
        else:
            continue
        end = segs[-1].strip()
        # normalize end like '9:30PM'
        # if end lacks AM/PM but start has, skip
        if not any(x in end.upper() for x in ['AM','PM']):
            continue
        end_norm = end.replace(' ', '')
        # parse to minutes
        import re
        m = re.match(r'^(\d{1,2})(?::(\d{2}))?(AM|PM)$', end_norm, re.I)
        if not m:
            continue
        hh = int(m.group(1))
        mm = int(m.group(2) or 0)
        ap = m.group(3).upper()
        if ap == 'AM':
            if hh == 12:
                hh = 0
        else:
            if hh != 12:
                hh += 12
        mins = hh*60 + mm
        if mins > 18*60:  # strictly after 6:00 PM
            return True
    return False


def open_after_6_on_weekday(hours_json: str) -> bool:
    if hours_json is None:
        return False
    try:
        h = json.loads(hours_json) if isinstance(hours_json, str) else hours_json
    except Exception:
        return False
    if not isinstance(h, list):
        return False
    for row in h:
        if not (isinstance(row, list) and len(row) >= 2):
            continue
        day, times = row[0], row[1]
        if day in weekday_set and closes_after_6(times):
            return True
    return False

biz_df = biz_df.dropna(subset=['hours'])
biz_df['open_after_6_weekday'] = biz_df['hours'].apply(open_after_6_on_weekday)
filtered = biz_df[biz_df['open_after_6_weekday']].copy()

merged = filtered.merge(rev_df[['gmap_id','avg_rating']], on='gmap_id', how='left')
merged = merged.dropna(subset=['avg_rating'])
merged = merged.sort_values(['avg_rating','name'], ascending=[False, True]).head(5)

out = merged[['name','hours','avg_rating']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_SmRldoqI0Cjl5YikfDygiAfh': [], 'var_call_7XeIwz1fMzTvUy3no0acBd2j': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0', 'review_count': '1'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605', 'review_count': '378'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0', 'review_count': '2'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625', 'review_count': '8'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375', 'review_count': '8'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111', 'review_count': '45'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0', 'review_count': '6'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118', 'review_count': '34'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0', 'review_count': '4'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0', 'review_count': '8'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177', 'review_count': '17'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'review_count': '56'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333', 'review_count': '15'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333', 'review_count': '6'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0', 'review_count': '8'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0', 'review_count': '1'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0', 'review_count': '5'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925', 'review_count': '26'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667', 'review_count': '27'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857', 'review_count': '21'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0', 'review_count': '8'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667', 'review_count': '6'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125', 'review_count': '8'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5', 'review_count': '8'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143', 'review_count': '84'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0', 'review_count': '8'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'review_count': '7'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223', 'review_count': '18'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25', 'review_count': '4'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'review_count': '35'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'review_count': '18'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856', 'review_count': '7'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'review_count': '6'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'review_count': '6'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5', 'review_count': '6'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381', 'review_count': '168'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586', 'review_count': '58'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4', 'review_count': '5'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0', 'review_count': '8'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0', 'review_count': '5'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0', 'review_count': '18'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105', 'review_count': '58'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263', 'review_count': '38'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0', 'review_count': '3'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0', 'review_count': '28'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789', 'review_count': '38'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75', 'review_count': '8'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421', 'review_count': '38'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75', 'review_count': '4'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058', 'review_count': '17'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0', 'review_count': '3'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353', 'review_count': '68'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375', 'review_count': '16'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25', 'review_count': '8'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615', 'review_count': '52'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5', 'review_count': '2'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806', 'review_count': '31'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0', 'review_count': '4'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333', 'review_count': '48'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838', 'review_count': '37'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625', 'review_count': '16'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895', 'review_count': '38'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0', 'review_count': '1'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667', 'review_count': '18'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944', 'review_count': '143'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222', 'review_count': '18'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0', 'review_count': '2'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0', 'review_count': '3'}], 'var_call_G2upDv1wKaSYbbYzJ3aIqiVd': ['business_description'], 'var_call_lZiSI1wcLSxdu862jaRwQiAb': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None', 'state': 'Open now'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'state': 'Open ⋅ Closes 6PM'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'state': 'Open ⋅ Closes 5:30PM'}], 'var_call_pzxbX9oVIPYi7bVDwXp6PbPO': 'file_storage/call_pzxbX9oVIPYi7bVDwXp6PbPO.json'}

exec(code, env_args)
