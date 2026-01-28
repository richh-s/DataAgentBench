code = """import json
from collections import defaultdict

# Get the reviews and businesses from previous queries
reviews = locals()['var_functions.query_db:10']
businesses = locals()['var_functions.query_db:5']

# Group ratings by gmap_id
ratings_by_business = defaultdict(list)
for review in reviews:
    ratings_by_business[review['gmap_id']].append(int(review['rating']))

# Calculate average ratings
business_avg_ratings = {}
for gmap_id, ratings in ratings_by_business.items():
    avg_rating = sum(ratings) / len(ratings)
    business_avg_ratings[gmap_id] = {
        'avg_rating': round(avg_rating, 2),
        'review_count': len(ratings)
    }

# Create a gmap_id to business name mapping
business_names = {b['gmap_id']: b['name'] for b in businesses if b['gmap_id'] in business_avg_ratings}

# Filter businesses with avg rating >= 4.0 and prepare results
results = []
for gmap_id, data in business_avg_ratings.items():
    if data['avg_rating'] >= 4.0:
        results.append({
            'business_name': business_names.get(gmap_id, 'Unknown'),
            'gmap_id': gmap_id,
            'avg_rating': data['avg_rating'],
            'review_count': data['review_count']
        })

# Sort by average rating descending
results.sort(key=lambda x: x['avg_rating'], reverse=True)

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:5': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.'}, {'gmap_id': 'gmap_63', 'name': 'Regus - California, Irvine - Oracle Tower', 'description': ' This company in Irvine, CA 92614 specializes in providing flexible workspace solutions tailored to meet the needs of professionals and businesses.'}, {'gmap_id': 'gmap_51', 'name': 'Taba Rug Gallery', 'description': 'Longtime boutique featuring high-quality Persian & Oriental rugs, plus repair & cleaning services. Discover a curated selection of exquisite floor coverings and textiles that enhance any space, conveniently located in La Jolla, CA 92037.'}, {'gmap_id': 'gmap_59', 'name': 'IBEW 441', 'description': ' Located in Orange, CA 92868, this professional hub offers a variety of workspace solutions and essential services for entrepreneurs and companies seeking a productive environment.'}, {'gmap_id': 'gmap_4', 'name': 'Lafayette Entrance 1', 'description': ' This serene green space in Orinda, CA 94563 offers picturesque walking trails, lush picnic areas, and a tranquil environment for outdoor recreation and relaxation.'}, {'gmap_id': 'gmap_66', 'name': 'HIGHPOINTE', 'description': ' This professional workspace in Mission Viejo, CA 92691 offers flexible office solutions and meeting facilities designed to support your business needs.'}], 'var_functions.execute_python:8': ['gmap_22', 'gmap_25', 'gmap_33', 'gmap_24', 'gmap_20', 'gmap_21', 'gmap_28', 'gmap_63', 'gmap_51', 'gmap_59', 'gmap_4', 'gmap_66'], 'var_functions.query_db:10': [{'gmap_id': 'gmap_22', 'rating': '5'}, {'gmap_id': 'gmap_22', 'rating': '5'}, {'gmap_id': 'gmap_22', 'rating': '4'}, {'gmap_id': 'gmap_22', 'rating': '4'}, {'gmap_id': 'gmap_22', 'rating': '5'}, {'gmap_id': 'gmap_22', 'rating': '3'}, {'gmap_id': 'gmap_25', 'rating': '5'}, {'gmap_id': 'gmap_33', 'rating': '1'}, {'gmap_id': 'gmap_33', 'rating': '2'}, {'gmap_id': 'gmap_33', 'rating': '1'}, {'gmap_id': 'gmap_33', 'rating': '1'}, {'gmap_id': 'gmap_33', 'rating': '1'}, {'gmap_id': 'gmap_33', 'rating': '1'}, {'gmap_id': 'gmap_33', 'rating': '5'}, {'gmap_id': 'gmap_33', 'rating': '5'}, {'gmap_id': 'gmap_24', 'rating': '5'}, {'gmap_id': 'gmap_24', 'rating': '1'}, {'gmap_id': 'gmap_24', 'rating': '5'}, {'gmap_id': 'gmap_24', 'rating': '5'}, {'gmap_id': 'gmap_24', 'rating': '4'}, {'gmap_id': 'gmap_24', 'rating': '5'}, {'gmap_id': 'gmap_24', 'rating': '5'}, {'gmap_id': 'gmap_24', 'rating': '1'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '1'}, {'gmap_id': 'gmap_20', 'rating': '2'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '4'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '1'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '1'}, {'gmap_id': 'gmap_20', 'rating': '1'}, {'gmap_id': 'gmap_20', 'rating': '2'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '1'}, {'gmap_id': 'gmap_20', 'rating': '3'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '4'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '1'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '1'}, {'gmap_id': 'gmap_20', 'rating': '1'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '3'}, {'gmap_id': 'gmap_20', 'rating': '3'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_21', 'rating': '4'}, {'gmap_id': 'gmap_21', 'rating': '5'}, {'gmap_id': 'gmap_21', 'rating': '5'}, {'gmap_id': 'gmap_21', 'rating': '1'}, {'gmap_id': 'gmap_21', 'rating': '5'}, {'gmap_id': 'gmap_21', 'rating': '1'}, {'gmap_id': 'gmap_21', 'rating': '4'}, {'gmap_id': 'gmap_21', 'rating': '5'}, {'gmap_id': 'gmap_21', 'rating': '1'}, {'gmap_id': 'gmap_21', 'rating': '4'}, {'gmap_id': 'gmap_21', 'rating': '5'}, {'gmap_id': 'gmap_21', 'rating': '5'}, {'gmap_id': 'gmap_21', 'rating': '5'}, {'gmap_id': 'gmap_21', 'rating': '4'}, {'gmap_id': 'gmap_21', 'rating': '5'}, {'gmap_id': 'gmap_28', 'rating': '5'}, {'gmap_id': 'gmap_28', 'rating': '5'}, {'gmap_id': 'gmap_28', 'rating': '5'}, {'gmap_id': 'gmap_28', 'rating': '4'}, {'gmap_id': 'gmap_28', 'rating': '1'}, {'gmap_id': 'gmap_28', 'rating': '5'}, {'gmap_id': 'gmap_28', 'rating': '1'}, {'gmap_id': 'gmap_28', 'rating': '5'}]}

exec(code, env_args)
