code = """import json, re
import pandas as pd

# load business hours from file
path = var_call_NwzMD3G1dc8TSkx6hfEUawKp
with open(path, 'r', encoding='utf-8') as f:
    biz_records = json.load(f)

biz = pd.DataFrame(biz_records)
rev = pd.DataFrame(var_call_jA0NJfgg2GDvtKONbgtYXBL1)

biz['hours_parsed'] = biz['hours'].apply(lambda s: json.loads(s) if isinstance(s,str) else s)
weekdays = {'Monday','Tuesday','Wednesday','Thursday','Friday'}

def end_minutes(end):
    end = end.strip()
    m = re.match(r'^(\d{1,2})(?::(\d{2}))?(AM|PM)$', end.replace(' ',''))
    if not m:
        return None
    h = int(m.group(1)); minute = int(m.group(2) or 0); ampm = m.group(3)
    if ampm=='AM':
        h24 = 0 if h==12 else h
    else:
        h24 = 12 if h==12 else h+12
    return h24*60+minute

def closes_after_6pm(hours_list):
    for item in hours_list or []:
        if not (isinstance(item, (list, tuple)) and len(item)==2):
            continue
        day, hrs = item
        if day not in weekdays or not isinstance(hrs,str):
            continue
        if '24 hours' in hrs:
            return True
        if 'Closed' in hrs:
            continue
        sep = '–' if '–' in hrs else ('-' if '-' in hrs else None)
        if not sep:
            continue
        end = hrs.split(sep)[-1].strip()
        mins = end_minutes(end)
        if mins is None:
            continue
        if mins > 18*60:
            return True
    return False

biz = biz[biz['hours_parsed'].apply(closes_after_6pm)]

out = biz.merge(rev, on='gmap_id', how='inner')
out['avg_rating'] = out['avg_rating'].astype(float)
out['review_count'] = out['review_count'].astype(int)

out = out.sort_values(['avg_rating','review_count','name'], ascending=[False, False, True]).head(5)

# format hours as readable lines
hours_strs = []
for hl in out['hours_parsed']:
    parts = [f"{d}: {h}" for d,h in hl]
    hours_strs.append('; '.join(parts))

result = []
for (_, row), hs in zip(out.iterrows(), hours_strs):
    result.append({
        'name': row['name'],
        'hours': hs,
        'average_rating': round(float(row['avg_rating']), 3)
    })

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_vhUn0cZ7Y5rq74EeG6B2UFgq': [], 'var_call_jA0NJfgg2GDvtKONbgtYXBL1': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0', 'review_count': '1'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605', 'review_count': '378'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0', 'review_count': '2'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625', 'review_count': '8'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375', 'review_count': '8'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111', 'review_count': '45'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0', 'review_count': '6'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118', 'review_count': '34'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0', 'review_count': '4'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0', 'review_count': '8'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177', 'review_count': '17'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'review_count': '56'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333', 'review_count': '15'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333', 'review_count': '6'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0', 'review_count': '8'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0', 'review_count': '1'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0', 'review_count': '5'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925', 'review_count': '26'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667', 'review_count': '27'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857', 'review_count': '21'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0', 'review_count': '8'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667', 'review_count': '6'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125', 'review_count': '8'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5', 'review_count': '8'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143', 'review_count': '84'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0', 'review_count': '8'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'review_count': '7'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223', 'review_count': '18'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25', 'review_count': '4'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'review_count': '35'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'review_count': '18'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856', 'review_count': '7'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'review_count': '6'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'review_count': '6'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5', 'review_count': '6'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381', 'review_count': '168'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586', 'review_count': '58'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4', 'review_count': '5'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0', 'review_count': '8'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0', 'review_count': '5'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0', 'review_count': '18'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105', 'review_count': '58'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263', 'review_count': '38'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0', 'review_count': '3'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0', 'review_count': '28'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789', 'review_count': '38'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75', 'review_count': '8'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421', 'review_count': '38'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75', 'review_count': '4'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058', 'review_count': '17'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0', 'review_count': '3'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353', 'review_count': '68'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375', 'review_count': '16'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25', 'review_count': '8'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615', 'review_count': '52'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5', 'review_count': '2'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806', 'review_count': '31'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0', 'review_count': '4'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333', 'review_count': '48'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838', 'review_count': '37'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625', 'review_count': '16'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895', 'review_count': '38'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0', 'review_count': '1'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667', 'review_count': '18'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944', 'review_count': '143'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222', 'review_count': '18'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0', 'review_count': '2'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0', 'review_count': '3'}], 'var_call_8cE2DGc07W53HSjK70lEasV8': [{'n_reviews': '2000', 'n_businesses': '79'}], 'var_call_DXjaXs6se9Gpyt9PIJP1X95y': [{'n_open_with_hours': '0'}], 'var_call_aSUXGgxI21xPPxV2zWb4VK1f': [{'state': 'Open ⋅ Closes 5PM', 'n': '18'}, {'state': 'None', 'n': '9'}, {'state': 'Closed ⋅ Opens 10AM', 'n': '5'}, {'state': 'Open ⋅ Closes 9:30PM', 'n': '4'}, {'state': 'Open now', 'n': '4'}, {'state': 'Open ⋅ Closes 8PM', 'n': '3'}, {'state': 'Permanently closed', 'n': '3'}, {'state': 'Open ⋅ Closes 7PM', 'n': '3'}, {'state': 'Open ⋅ Closes 4PM', 'n': '3'}, {'state': 'Open ⋅ Closes 10PM', 'n': '3'}, {'state': 'Open ⋅ Closes 6PM', 'n': '3'}, {'state': 'Closed ⋅ Opens 9AM', 'n': '3'}, {'state': 'Open ⋅ Closes 5:30PM', 'n': '2'}, {'state': 'Open 24 hours', 'n': '2'}, {'state': 'Closed ⋅ Opens 12PM', 'n': '1'}, {'state': 'Closed ⋅ Opens 5PM Fri', 'n': '1'}, {'state': 'Temporarily closed', 'n': '1'}, {'state': 'Opens soon ⋅ 10AM', 'n': '1'}, {'state': 'Closed ⋅ Opens 3PM', 'n': '1'}, {'state': 'Open ⋅ Closes 12PM ⋅ Reopens 1PM', 'n': '1'}, {'state': 'Open ⋅ Closes 12AM', 'n': '1'}, {'state': 'Closed ⋅ Opens 11AM', 'n': '1'}, {'state': 'Open ⋅ Closes 11:30AM ⋅ Reopens 1PM', 'n': '1'}, {'state': 'Open ⋅ Closes 12PM ⋅ Reopens 12:30PM', 'n': '1'}, {'state': 'Open ⋅ Closes 11AM ⋅ Reopens 4PM', 'n': '1'}, {'state': 'Open ⋅ Closes 9PM', 'n': '1'}, {'state': 'Open ⋅ Closes 4:30PM', 'n': '1'}, {'state': 'Open ⋅ Closes 3:30PM', 'n': '1'}], 'var_call_XopDAaXkaco6Ep15PNhnDFRB': [{'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'state': 'Open ⋅ Closes 6PM', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'state': 'Open ⋅ Closes 5PM', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'state': 'Open ⋅ Closes 5PM', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'state': 'Open ⋅ Closes 5:30PM', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}, {'gmap_id': 'gmap_74', 'name': 'Vons Chicken', 'state': 'Open ⋅ Closes 9:30PM', 'hours': '[["Thursday", "11AM–9:30PM"], ["Friday", "11AM–9:30PM"], ["Saturday", "11AM–9:30PM"], ["Sunday", "11AM–9:30PM"], ["Monday", "Closed"], ["Tuesday", "11AM–9:30PM"], ["Wednesday", "11AM–9:30PM"]]'}], 'var_call_eJwGiRKOMatzhmM1U3LJlSuN': [{'name': 'Vons Chicken', 'hours_parsed': [['Thursday', '11AM–9:30PM'], ['Friday', '11AM–9:30PM'], ['Saturday', '11AM–9:30PM'], ['Sunday', '11AM–9:30PM'], ['Monday', 'Closed'], ['Tuesday', '11AM–9:30PM'], ['Wednesday', '11AM–9:30PM']], 'avg_rating': 4.666666666666667}], 'var_call_NwzMD3G1dc8TSkx6hfEUawKp': 'file_storage/call_NwzMD3G1dc8TSkx6hfEUawKp.json'}

exec(code, env_args)
