code = """import pandas as pd
business_data = locals()['var_function-call-8804047932765975182']
review_data = locals()['var_function-call-11008701934143889970']

business_df = pd.DataFrame(business_data)
review_df = pd.DataFrame(review_data)

merged_df = pd.merge(business_df, review_df, on='gmap_id')

result = merged_df[merged_df['description'].str.contains('massage', case=False)][['name', 'average_rating']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-9724614723280079991': ['business_description'], 'var_function-call-17162109538883717651': [], 'var_function-call-6225028923738472413': [], 'var_function-call-12914484081397281308': [{'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.'}, {'description': ' This inviting eatery in La Mirada, CA 90638 serves a diverse menu of delicious dishes, perfect for casual dining and family gatherings.'}, {'description': ' Offering a wide selection of winter sports equipment for hire, this service in Mammoth Lakes, CA 93546 ensures you’re fully equipped for an unforgettable day on the slopes.'}, {'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'description': 'Chain selling interior & exterior paints, primers & finishes, plus supplies. This vibrant shop in Roseville, CA 95661 offers a wide variety of high-quality coatings and supplies for all your home improvement and artistic needs.'}, {'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}], 'var_function-call-8804047932765975182': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}], 'var_function-call-11008701934143889970': [{'gmap_id': 'gmap_22', 'average_rating': '4.333333333333333'}]}

exec(code, env_args)
