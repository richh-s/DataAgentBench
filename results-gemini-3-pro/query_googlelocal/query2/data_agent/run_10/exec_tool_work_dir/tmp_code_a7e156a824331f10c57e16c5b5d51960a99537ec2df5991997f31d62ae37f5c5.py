code = """import pandas as pd
import json

businesses = locals()['var_function-call-15586748012385930034']
ratings = locals()['var_function-call-7034912143059623550']

df_bus = pd.DataFrame(businesses)
df_rate = pd.DataFrame(ratings)

# Ensure types are correct for merge
df_bus['gmap_id'] = df_bus['gmap_id'].astype(str)
df_rate['gmap_id'] = df_rate['gmap_id'].astype(str)

# df_rate avg_rating is string in the JSON output, convert to float
df_rate['avg_rating'] = df_rate['avg_rating'].astype(float)

merged = pd.merge(df_bus, df_rate, on='gmap_id')

# Select name and avg_rating
result = merged[['name', 'avg_rating']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-2454645333339318658': ['business_description'], 'var_function-call-2454645333339316423': ['review'], 'var_function-call-6236253224244342571': [{'name': 'City Textile', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'name': 'San Soo Dang', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'name': 'Nova Fabrics', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'name': 'Nobel Textile Co', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'name': 'Matrix International Textiles', 'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.'}], 'var_function-call-10068132626110439515': [], 'var_function-call-10486740529765878119': [{'name': 'Angel-A Massage', 'gmap_id': 'gmap_22', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'name': 'Elite Massage', 'gmap_id': 'gmap_25', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'gmap_id': 'gmap_33', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'name': 'SUSY massage', 'gmap_id': 'gmap_24', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'name': 'Aurora Massage', 'gmap_id': 'gmap_20', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}], 'var_function-call-10230717033347226040': [{'count': '7'}], 'var_function-call-8030870218653348263': [{'MISC': 'None'}], 'var_function-call-2479238423717589831': [{'MISC': 'None'}], 'var_function-call-15586748012385930034': [{'name': 'Angel-A Massage', 'gmap_id': 'gmap_22'}, {'name': 'Elite Massage', 'gmap_id': 'gmap_25'}, {'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'gmap_id': 'gmap_33'}, {'name': 'SUSY massage', 'gmap_id': 'gmap_24'}, {'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'Orient Massage', 'gmap_id': 'gmap_21'}, {'name': 'Good Massage', 'gmap_id': 'gmap_28'}], 'var_function-call-7034912143059623550': [{'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}]}

exec(code, env_args)
