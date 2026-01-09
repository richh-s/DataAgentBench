code = """import json, pandas as pd

# business list containing massage in name
biz = pd.DataFrame(var_call_km8IVHG1uRj7m9Wxva2oAvTJ)

# load reviews
path = var_call_GTWg9txQs0G8GPom3jhUZYZX
with open(path, 'r', encoding='utf-8') as f:
    reviews = json.load(f)
rev = pd.DataFrame(reviews)
rev['rating'] = pd.to_numeric(rev['rating'], errors='coerce')

merged = rev.merge(biz, on='gmap_id', how='inner')
avg = merged.groupby(['gmap_id','name'], as_index=False)['rating'].mean()
avg = avg.rename(columns={'rating':'avg_rating'})
res = avg[avg['avg_rating'] >= 4.0].sort_values(['avg_rating','name'], ascending=[False, True])
res['avg_rating'] = res['avg_rating'].round(3)

print('__RESULT__:')
print(res.to_json(orient='records'))"""

env_args = {'var_call_4Oc67zlSYCKvawPxLnzwUV1a': [], 'var_call_GTWg9txQs0G8GPom3jhUZYZX': 'file_storage/call_GTWg9txQs0G8GPom3jhUZYZX.json', 'var_call_5BWx6Luc6IqIIntiwmtOtied': [], 'var_call_YRdi2fozwjlA5PwNXlUKsQjZ': [], 'var_call_ZpYnrVZiyx1kMvTSoac1lwRD': ['business_description'], 'var_call_YYRE8BXoUaUQiLdMTauPdlHp': [{'name': 'Taba Rug Gallery', 'cnt': '1'}, {'name': 'Nova Fabrics', 'cnt': '1'}, {'name': 'Dunn-Edwards Paints', 'cnt': '1'}, {'name': 'Elite Massage', 'cnt': '1'}, {'name': 'Good Massage', 'cnt': '1'}, {'name': 'Hanford Auto Supply', 'cnt': '1'}, {'name': 'Orient Massage', 'cnt': '1'}, {'name': 'Aurora Massage', 'cnt': '1'}, {'name': 'Timmons Auto & Truck Repair', 'cnt': '1'}, {'name': 'PODS Sacramento Hub', 'cnt': '1'}, {'name': 'Acuity Eye Group, Retina Institute & Acuity 360 Advanced Vision Center - Tustin', 'cnt': '1'}, {'name': "Ruby's Boutique", 'cnt': '1'}, {'name': "Zuby's Brake Tires & Wheels", 'cnt': '1'}, {'name': 'City Textile', 'cnt': '1'}, {'name': 'AMMCOR Management Company, Inc.', 'cnt': '1'}, {'name': 'IBEW 441', 'cnt': '1'}, {'name': 'Widows Peak Salon', 'cnt': '1'}, {'name': 'St John Knits International Inc', 'cnt': '1'}, {'name': 'HIGHPOINTE', 'cnt': '1'}, {'name': 'CYD Works Electric', 'cnt': '1'}], 'var_call_eOMQfEgqI0RilZPKxbTEyTTq': {'error': 'Insufficient business metadata filter: no businesses matched massage therapy via description/name, and we lack gmap_id-name mapping for massage therapy identification.'}, 'var_call_km8IVHG1uRj7m9Wxva2oAvTJ': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage'}]}

exec(code, env_args)
