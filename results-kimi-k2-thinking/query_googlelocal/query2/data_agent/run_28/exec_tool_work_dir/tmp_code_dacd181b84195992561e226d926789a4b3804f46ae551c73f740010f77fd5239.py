code = """import json

# Get the businesses from the previous query
businesses = var_functions.query_db:4

# Filter for massage therapy businesses only
massage_businesses = []
for b in businesses:
    name_lower = b['name'].lower()
    desc_lower = b['description'].lower()
    if 'massage' in name_lower or ('spa' in name_lower and 'massage' in desc_lower):
        massage_businesses.append(b)

print('__RESULT__:')
print(json.dumps(massage_businesses))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:4': [{'name': 'Angel-A Massage', 'gmap_id': 'gmap_22', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.', 'num_of_reviews': '6'}, {'name': 'Elite Massage', 'gmap_id': 'gmap_25', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.', 'num_of_reviews': '1'}, {'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'gmap_id': 'gmap_33', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.', 'num_of_reviews': '8'}, {'name': 'SUSY massage', 'gmap_id': 'gmap_24', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.', 'num_of_reviews': '8'}, {'name': 'Aurora Massage', 'gmap_id': 'gmap_20', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.', 'num_of_reviews': '56'}, {'name': 'Orient Massage', 'gmap_id': 'gmap_21', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.', 'num_of_reviews': '15'}, {'name': 'Good Massage', 'gmap_id': 'gmap_28', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.', 'num_of_reviews': '8'}, {'name': 'Regus - California, Irvine - Oracle Tower', 'gmap_id': 'gmap_63', 'description': ' This company in Irvine, CA 92614 specializes in providing flexible workspace solutions tailored to meet the needs of professionals and businesses.', 'num_of_reviews': '16'}, {'name': 'Taba Rug Gallery', 'gmap_id': 'gmap_51', 'description': 'Longtime boutique featuring high-quality Persian & Oriental rugs, plus repair & cleaning services. Discover a curated selection of exquisite floor coverings and textiles that enhance any space, conveniently located in La Jolla, CA 92037.', 'num_of_reviews': '18'}, {'name': 'IBEW 441', 'gmap_id': 'gmap_59', 'description': ' Located in Orange, CA 92868, this professional hub offers a variety of workspace solutions and essential services for entrepreneurs and companies seeking a productive environment.', 'num_of_reviews': '38'}, {'name': 'Lafayette Entrance 1', 'gmap_id': 'gmap_4', 'description': ' This serene green space in Orinda, CA 94563 offers picturesque walking trails, lush picnic areas, and a tranquil environment for outdoor recreation and relaxation.', 'num_of_reviews': '4'}, {'name': 'HIGHPOINTE', 'gmap_id': 'gmap_66', 'description': ' This professional workspace in Mission Viejo, CA 92691 offers flexible office solutions and meeting facilities designed to support your business needs.', 'num_of_reviews': '2'}]}

exec(code, env_args)
