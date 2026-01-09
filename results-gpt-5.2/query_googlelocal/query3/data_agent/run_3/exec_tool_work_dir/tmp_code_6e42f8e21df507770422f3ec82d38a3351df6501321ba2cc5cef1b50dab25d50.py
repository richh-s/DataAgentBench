code = """import json, re
import pandas as pd

biz = pd.DataFrame(var_call_OOCEemLXe31cKdMpoZ8qSTou if var_call_OOCEemLXe31cKdMpoZ8qSTou else var_call_ZVqa8UAZiw396bzfOoVcSMoL)
rev = pd.DataFrame(var_call_igv8zR0cByzYqwXboMias6EO)
if biz.empty:
    out = []
else:
    def parse_close_time(s):
        if not s or s.strip().lower()=='closed':
            return None
        s = s.replace('\u2013','-').replace('–','-')
        if '-' not in s:
            return None
        end = s.split('-',1)[1].strip()
        m = re.match(r'^(\d{1,2})(?::(\d{2}))?\s*(AM|PM)$', end, re.I)
        if not m:
            return None
        h = int(m.group(1)) % 12
        mi = int(m.group(2) or 0)
        ap = m.group(3).upper()
        if ap=='PM':
            h += 12
        return h*60+mi

    weekdays = {'Monday','Tuesday','Wednesday','Thursday','Friday'}

    def open_after_6(hours_json):
        try:
            hrs = json.loads(hours_json) if isinstance(hours_json,str) else hours_json
        except Exception:
            return False
        for day, times in hrs:
            if day in weekdays:
                ct = parse_close_time(times)
                if ct is not None and ct > 18*60:
                    return True
        return False

    biz['open_after_6_weekday'] = biz['hours'].apply(open_after_6)
    biz2 = biz[biz['open_after_6_weekday']].copy()

    df = biz2.merge(rev, on='gmap_id', how='inner')
    df['avg_rating'] = df['avg_rating'].astype(float)
    top = df.sort_values(['avg_rating','review_count'], ascending=[False, False]).head(5)

    def hours_pretty(hours_json):
        try:
            hrs = json.loads(hours_json) if isinstance(hours_json,str) else hours_json
        except Exception:
            return None
        return '; '.join([f"{d}: {t}" for d,t in hrs])

    out = []
    for _, r in top.iterrows():
        out.append({
            'name': r['name'],
            'gmap_id': r['gmap_id'],
            'operating_hours': hours_pretty(r['hours']),
            'avg_rating': round(float(r['avg_rating']), 3)
        })

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_yY0EjCuPNhb0JspFxnxNmdLx': [], 'var_call_igv8zR0cByzYqwXboMias6EO': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0', 'review_count': '1'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605', 'review_count': '378'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0', 'review_count': '2'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625', 'review_count': '8'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375', 'review_count': '8'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111', 'review_count': '45'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0', 'review_count': '6'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118', 'review_count': '34'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0', 'review_count': '4'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0', 'review_count': '8'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177', 'review_count': '17'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'review_count': '56'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333', 'review_count': '15'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333', 'review_count': '6'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0', 'review_count': '8'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0', 'review_count': '1'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0', 'review_count': '5'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925', 'review_count': '26'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667', 'review_count': '27'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857', 'review_count': '21'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0', 'review_count': '8'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667', 'review_count': '6'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125', 'review_count': '8'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5', 'review_count': '8'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143', 'review_count': '84'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0', 'review_count': '8'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'review_count': '7'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223', 'review_count': '18'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25', 'review_count': '4'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'review_count': '35'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'review_count': '18'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856', 'review_count': '7'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'review_count': '6'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'review_count': '6'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5', 'review_count': '6'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381', 'review_count': '168'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586', 'review_count': '58'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4', 'review_count': '5'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0', 'review_count': '8'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0', 'review_count': '5'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0', 'review_count': '18'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105', 'review_count': '58'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263', 'review_count': '38'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0', 'review_count': '3'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0', 'review_count': '28'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789', 'review_count': '38'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75', 'review_count': '8'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421', 'review_count': '38'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75', 'review_count': '4'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058', 'review_count': '17'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0', 'review_count': '3'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353', 'review_count': '68'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375', 'review_count': '16'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25', 'review_count': '8'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615', 'review_count': '52'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5', 'review_count': '2'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806', 'review_count': '31'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0', 'review_count': '4'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333', 'review_count': '48'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838', 'review_count': '37'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625', 'review_count': '16'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895', 'review_count': '38'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0', 'review_count': '1'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667', 'review_count': '18'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944', 'review_count': '143'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222', 'review_count': '18'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0', 'review_count': '2'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0', 'review_count': '3'}], 'var_call_ZVqa8UAZiw396bzfOoVcSMoL': [{'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}, {'gmap_id': 'gmap_74', 'name': 'Vons Chicken', 'hours': '[["Thursday", "11AM–9:30PM"], ["Friday", "11AM–9:30PM"], ["Saturday", "11AM–9:30PM"], ["Sunday", "11AM–9:30PM"], ["Monday", "Closed"], ["Tuesday", "11AM–9:30PM"], ["Wednesday", "11AM–9:30PM"]]'}], 'var_call_OOCEemLXe31cKdMpoZ8qSTou': []}

exec(code, env_args)
