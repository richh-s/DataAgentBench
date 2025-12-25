code = """import pandas as pd
import json

business_names = locals()['var_function-call-6429786230136242767']
df_business_names = pd.DataFrame(business_names)
massage_gmap_ids = df_business_names['gmap_id'].tolist()

print('__RESULT__:')
print(json.dumps(massage_gmap_ids))"""

env_args = {'var_function-call-5806132711522617287': [], 'var_function-call-2920753959660314623': [], 'var_function-call-3123390929511229942': ['business_description'], 'var_function-call-17070349829733189226': [{'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.'}], 'var_function-call-2352639253836709257': ['review'], 'var_function-call-12402395841031509992': [], 'var_function-call-11621653440149310878': [], 'var_function-call-932136603055988270': 'file_storage/function-call-932136603055988270.json', 'var_function-call-2052708101499572230': 'file_storage/function-call-2052708101499572230.json', 'var_function-call-15817599168867148858': [], 'var_function-call-6429786230136242767': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage'}]}

exec(code, env_args)
