code = """import pandas as pd

business_data = locals()['var_function-call-13878724614924024884']
review_data = locals()['var_function-call-14936840933273729329']

df_business = pd.DataFrame(business_data)
df_review = pd.DataFrame(review_data)

merged_df = pd.merge(df_business, df_review, on='gmap_id', how='inner')

result = merged_df[['name', 'average_rating']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-5087031591675627126': [], 'var_function-call-692509943370713531': ['business_description'], 'var_function-call-573225344919451064': [{'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.'}], 'var_function-call-12161123589519027669': ['review'], 'var_function-call-4917025631794089577': [], 'var_function-call-13878724614924024884': [{'name': 'Angel-A Massage', 'gmap_id': 'gmap_22', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'name': 'Elite Massage', 'gmap_id': 'gmap_25', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'gmap_id': 'gmap_33', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'name': 'SUSY massage', 'gmap_id': 'gmap_24', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'name': 'Aurora Massage', 'gmap_id': 'gmap_20', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'name': 'Orient Massage', 'gmap_id': 'gmap_21', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.'}, {'name': 'Good Massage', 'gmap_id': 'gmap_28', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.'}], 'var_function-call-14936840933273729329': [{'gmap_id': 'gmap_20', 'average_rating': '4.178571428571429'}, {'gmap_id': 'gmap_22', 'average_rating': '4.333333333333333'}, {'gmap_id': 'gmap_25', 'average_rating': '5.0'}]}

exec(code, env_args)
