code = """import pandas as pd
import json

business_descriptions_path = locals()['var_function-call-12310435437091382967']
with open(business_descriptions_path, 'r') as f:
    business_descriptions = json.load(f)

df_business = pd.DataFrame(business_descriptions)

massage_businesses = df_business[
    df_business['name'].str.contains('massage', case=False, na=False) |
    df_business['description'].str.contains('massage', case=False, na=False)
]

massage_gmap_ids = massage_businesses['gmap_id'].tolist()

print("__RESULT__:")
print(json.dumps(massage_gmap_ids))"""

env_args = {'var_function-call-17279278589973870021': [], 'var_function-call-16321567348690240873': ['business_description'], 'var_function-call-15772595162693890058': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.'}, {'gmap_id': 'gmap_74', 'name': 'Vons Chicken', 'description': ' This inviting eatery in La Mirada, CA 90638 serves a diverse menu of delicious dishes, perfect for casual dining and family gatherings.'}, {'gmap_id': 'gmap_17', 'name': 'Black Tie Ski Rental Delivery of Mammoth', 'description': ' Offering a wide selection of winter sports equipment for hire, this service in Mammoth Lakes, CA 93546 ensures you’re fully equipped for an unforgettable day on the slopes.'}, {'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'gmap_id': 'gmap_29', 'name': 'Dunn-Edwards Paints', 'description': 'Chain selling interior & exterior paints, primers & finishes, plus supplies. This vibrant shop in Roseville, CA 95661 offers a wide variety of high-quality coatings and supplies for all your home improvement and artistic needs.'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}], 'var_function-call-11788074021926978003': [], 'var_function-call-2821586654856070928': [], 'var_function-call-15244681733715932801': 'file_storage/function-call-15244681733715932801.json', 'var_function-call-11831712446615644542': [], 'var_function-call-1147331165202037750': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage'}], 'var_function-call-17404829770804390456': [], 'var_function-call-12310435437091382967': 'file_storage/function-call-12310435437091382967.json'}

exec(code, env_args)
