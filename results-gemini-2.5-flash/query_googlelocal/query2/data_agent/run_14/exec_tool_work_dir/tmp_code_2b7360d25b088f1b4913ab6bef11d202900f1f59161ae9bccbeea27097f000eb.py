code = """import pandas as pd
businesses_by_name_raw = locals()['var_function-call-1565265896210988980']
businesses_by_description_raw = locals()['var_function-call-3412823493371676147']

businesses_by_name = businesses_by_name_raw # Access the list directly
businesses_by_description = businesses_by_description_raw # Access the list directly

all_businesses = businesses_by_name + businesses_by_description
gmap_ids = set()
for biz_dict in all_businesses:
    for key, value in biz_dict.items():
        if key == 'results':
            for biz in value:
                gmap_ids.add(biz['gmap_id'])

# Create a list of gmap_ids to use in the SQL query
gmap_ids_list = list(gmap_ids)

# Format the gmap_ids_list for the SQL IN clause
gmap_ids_sql = ', '.join([f"'{gmap_id}'" for gmap_id in gmap_ids_list])

print('__RESULT__:')
print(gmap_ids_sql)"""

env_args = {'var_function-call-7744200679938300142': [], 'var_function-call-1349735286009423669': ['business_description'], 'var_function-call-13542849556448319270': ['review'], 'var_function-call-141071803890650734': [{'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.'}, {'description': ' This inviting eatery in La Mirada, CA 90638 serves a diverse menu of delicious dishes, perfect for casual dining and family gatherings.'}, {'description': ' Offering a wide selection of winter sports equipment for hire, this service in Mammoth Lakes, CA 93546 ensures you’re fully equipped for an unforgettable day on the slopes.'}, {'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'description': 'Chain selling interior & exterior paints, primers & finishes, plus supplies. This vibrant shop in Roseville, CA 95661 offers a wide variety of high-quality coatings and supplies for all your home improvement and artistic needs.'}, {'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}], 'var_function-call-3412823493371676147': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_32', 'name': 'J B Oriental Inc'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage'}, {'gmap_id': 'gmap_4', 'name': 'Lafayette Entrance 1'}, {'gmap_id': 'gmap_10', 'name': 'Jjironwork'}, {'gmap_id': 'gmap_70', 'name': 'CrossFit to the Core'}, {'gmap_id': 'gmap_5', 'name': 'Dr. Syverain Skincare Clinic'}, {'gmap_id': 'gmap_75', 'name': 'HAVEN™ Dispensary'}, {'gmap_id': 'gmap_54', 'name': 'Wildomar Campground'}], 'var_function-call-1565265896210988980': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage'}]}

exec(code, env_args)
