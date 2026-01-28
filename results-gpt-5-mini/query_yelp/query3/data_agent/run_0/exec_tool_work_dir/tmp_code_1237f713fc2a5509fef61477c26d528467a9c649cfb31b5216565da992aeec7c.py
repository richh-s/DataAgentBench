code = """import json
import pandas as pd

# Load query results from storage
busi = json.load(open(var_call_qW2dgEEQmeG6SKIID9yY4utr))
busi_2018 = json.load(open(var_call_9qanhyygFtpbt4EdPjkLY73y))
rev_2018 = var_call_tknbe2qnYYNSqLxTSn8rfToS

# Create DataFrames
df_all = pd.DataFrame(busi)
# df_all may have attributes as various types; normalize missing as None

df_reviewed = pd.DataFrame(rev_2018)
# Convert review business_ref to business_id form by replacing prefix

def to_businessid(ref):
    if pd.isna(ref):
        return None
    return ref.replace('businessref_', 'businessid_')

reviewed_ids = df_reviewed['business_ref'].apply(to_businessid).unique().tolist()

# Filter businesses for those reviewed in 2018
df_busi_2018 = pd.DataFrame(busi_2018)

# Some businesses in business collection may not be present in this subset if they were missing earlier; ensure using df_busi_2018

# Function to detect parking attributes
import ast

def has_parking(attrs):
    if attrs is None:
        return False
    # attrs may be a dict or a string; handle both
    if isinstance(attrs, dict):
        # Check BikeParking key
        bike = attrs.get('BikeParking')
        bp = attrs.get('BusinessParking') or attrs.get('BusinessParking') or attrs.get('BusinessParking')
        # BikeParking sometimes as 'True'/'False'
        bike_flag = False
        if bike is not None:
            if isinstance(bike, bool):
                bike_flag = bike
            else:
                if isinstance(bike, str) and 'True' in bike:
                    bike_flag = True
        # BusinessParking may be 'None' or a string representation of dict
        lot_flag = False
        if bp is not None and bp != 'None':
            if isinstance(bp, dict):
                # check any True
                for v in bp.values():
                    if v in (True, 'True', "u'True'", "'True'"):
                        lot_flag = True
            elif isinstance(bp, str):
                try:
                    p = ast.literal_eval(bp)
                    if isinstance(p, dict):
                        for v in p.values():
                            if v in (True, 'True', "u'True'", "'True'"):
                                lot_flag = True
                except Exception:
                    # if string like "None" or other, ignore
                    pass
        return bike_flag or lot_flag
    else:
        # attrs is string
        try:
            parsed = ast.literal_eval(attrs)
        except Exception:
            return False
        if not isinstance(parsed, dict):
            return False
        # same logic
        bike = parsed.get('BikeParking')
        bp = parsed.get('BusinessParking')
        bike_flag = False
        if bike is not None:
            if isinstance(bike, bool):
                bike_flag = bike
            else:
                if isinstance(bike, str) and 'True' in bike:
                    bike_flag = True
        lot_flag = False
        if bp is not None:
            if isinstance(bp, dict):
                for v in bp.values():
                    if v in (True, 'True', "u'True'", "'True'"):
                        lot_flag = True
            elif isinstance(bp, str):
                if 'True' in bp:
                    lot_flag = True
        return bike_flag or lot_flag

# Now, filter df_busi_2018 for business_ids in reviewed_ids

reviewed_set = set(reviewed_ids)

# Ensure business ids are present in df_busi_2018
ids_present = set(df_busi_2018['business_id'].tolist())
intersect_ids = sorted(list(reviewed_set & ids_present))

# Filter rows
filtered = df_busi_2018[df_busi_2018['business_id'].isin(intersect_ids)]

# Apply has_parking
filtered['has_parking'] = filtered['attributes'].apply(has_parking)

count = int(filtered['has_parking'].sum())

# Prepare result
result = {"business_reviewed_count_with_parking_2018": count}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_euLWc2cjaKwfxdMqC1Bdh2IB': ['business', 'checkin'], 'var_call_FllgcV6rqj7gSKb9rG7bLslF': ['review', 'tip', 'user'], 'var_call_qW2dgEEQmeG6SKIID9yY4utr': 'file_storage/call_qW2dgEEQmeG6SKIID9yY4utr.json', 'var_call_tknbe2qnYYNSqLxTSn8rfToS': [{'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}], 'var_call_9qanhyygFtpbt4EdPjkLY73y': 'file_storage/call_9qanhyygFtpbt4EdPjkLY73y.json'}

exec(code, env_args)
