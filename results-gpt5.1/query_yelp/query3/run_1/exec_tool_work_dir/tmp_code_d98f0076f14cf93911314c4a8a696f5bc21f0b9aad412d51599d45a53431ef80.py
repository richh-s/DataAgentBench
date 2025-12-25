code = """import json, pandas as pd
from pathlib import Path

biz_attr_path = Path(var_call_yp00JtDfbHhlgIJ7wZNlrnXl)

biz_attr = json.loads(biz_attr_path.read_text())
attr_df = pd.DataFrame(biz_attr)

# Load 2018 business_ids list
biz_2018_ids = json.loads("""" + var_call_Br9YTh2UiAtX9qiNXc0TTJig + """")

attr_df = attr_df[attr_df['business_id'].isin(biz_2018_ids)]

mask = (
    attr_df['attributes'].apply(lambda a: (
        ('BikeParking' in a and str(a.get('BikeParking')) != 'False' and str(a.get('BikeParking')) != 'None') or
        ('BusinessParking' in a and str(a.get('BusinessParking')) != 'None')
    ))
)

selected = attr_df[mask]

count = int(selected['business_id'].nunique())

result = json.dumps(count)

print("__RESULT__:")
print(result)"""

env_args = {'var_call_yp00JtDfbHhlgIJ7wZNlrnXl': 'file_storage/call_yp00JtDfbHhlgIJ7wZNlrnXl.json', 'var_call_TfidTwfVZ3uQm8BvHrja5GoA': 'file_storage/call_TfidTwfVZ3uQm8BvHrja5GoA.json', 'var_call_4OuQj4VmeNlMUFt6yPlsJaOC': 'file_storage/call_4OuQj4VmeNlMUFt6yPlsJaOC.json', 'var_call_Br9YTh2UiAtX9qiNXc0TTJig': ['businessid_20', 'businessid_45', 'businessid_66', 'businessid_26', 'businessid_35', 'businessid_99', 'businessid_25', 'businessid_46', 'businessid_83', 'businessid_91', 'businessid_14', 'businessid_4', 'businessid_82', 'businessid_57', 'businessid_77', 'businessid_24', 'businessid_47', 'businessid_86', 'businessid_13', 'businessid_37', 'businessid_15', 'businessid_22', 'businessid_80', 'businessid_28', 'businessid_17', 'businessid_27', 'businessid_43', 'businessid_8', 'businessid_36', 'businessid_40', 'businessid_62', 'businessid_79', 'businessid_73', 'businessid_59', 'businessid_67', 'businessid_68']}

exec(code, env_args)
