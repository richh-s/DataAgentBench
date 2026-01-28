code = """import json, pandas as pd

# Load business hours (may be large)
biz_src = var_call_ucGG3W3TZgM7ibcKc9udOA8D
if isinstance(biz_src, str):
    with open(biz_src, 'r', encoding='utf-8') as f:
        biz = json.load(f)
else:
    biz = biz_src

ratings = var_call_ke6lf6Aes7gYWGHSaKN0b7ho

df_b = pd.DataFrame(biz)
df_r = pd.DataFrame(ratings)
if df_b.empty or df_r.empty:
    out = []
else:
    df_r['avg_rating'] = pd.to_numeric(df_r['avg_rating'], errors='coerce')

    # parse hours: stored as a JSON string representing list of [day, hours]
    def parse_hours(s):
        if s is None:
            return None
        if isinstance(s, (list, dict)):
            return s
        if isinstance(s, str):
            st = s.strip()
            try:
                return json.loads(st)
            except Exception:
                return None
        return None

    weekday_set = {'Monday','Tuesday','Wednesday','Thursday','Friday'}

    def closes_after_6pm(hours_list):
        # hours_list: list like [[day, '9AM–10PM'], ...]
        if not isinstance(hours_list, list):
            return False
        for item in hours_list:
            if not (isinstance(item, list) and len(item) >= 2):
                continue
            day = item[0]
            hrs = item[1]
            if day not in weekday_set:
                continue
            if not isinstance(hrs, str):
                continue
            h = hrs.strip()
            if h.lower() == 'closed':
                continue
            if 'Open 24 hours'.lower() in h.lower():
                return True
            # split on en dash or hyphen
            parts = None
            if '–' in h:
                parts = h.split('–')
            elif '-' in h:
                parts = h.split('-')
            else:
                continue
            if len(parts) < 2:
                continue
            close_str = parts[-1].strip()

            # parse close time (e.g., '6PM', '9:30PM')
            def to_minutes(t):
                tt = t.replace(' ', '')
                # handle cases like '12PM'
                import re
                m = re.match(r'^(\d{1,2})(?::(\d{2}))?(AM|PM)$', tt, re.I)
                if not m:
                    return None
                hour = int(m.group(1))
                minute = int(m.group(2) or 0)
                ampm = m.group(3).upper()
                if hour == 12:
                    hour = 0
                if ampm == 'PM':
                    hour += 12
                return hour*60 + minute

            cm = to_minutes(close_str)
            if cm is None:
                continue
            if cm > 18*60:
                return True
        return False

    df_b['hours_parsed'] = df_b['hours'].apply(parse_hours)
    df_b['open_after_6_weekday'] = df_b['hours_parsed'].apply(closes_after_6pm)

    df = df_b[df_b['open_after_6_weekday']].merge(df_r, on='gmap_id', how='inner')
    df = df.sort_values(['avg_rating','name'], ascending=[False, True]).head(5)

    def hours_to_str(h):
        if not isinstance(h, list):
            return None
        return '; '.join([f"{d}: {hrs}" for d, hrs in h if isinstance(d,str)])

    out_df = df[['name','hours_parsed','avg_rating']].copy()
    out_df['operating_hours'] = out_df['hours_parsed'].apply(hours_to_str)
    out_df = out_df.drop(columns=['hours_parsed'])
    out = out_df.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_ucGG3W3TZgM7ibcKc9udOA8D': 'file_storage/call_ucGG3W3TZgM7ibcKc9udOA8D.json', 'var_call_ke6lf6Aes7gYWGHSaKN0b7ho': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0'}], 'var_call_bH758tckR3QGv1JjIrypnbi2': [{'n_businesses': '79'}], 'var_call_onlzy8CsWmgRIU6z60PgGWce': [{'n_open_with_hours': '50'}]}

exec(code, env_args)
