code = """import json
import re

# Get the massage-related businesses from storage
# Since the variable name contains dots, we need to use locals()
massage_businesses_key = 'var_functions.query_db:8'
massage_businesses = locals()[massage_businesses_key]

# Debug: print what we got
print(f"Type of data: {type(massage_businesses)}")
print(f"Length: {len(massage_businesses) if hasattr(massage_businesses, '__len__') else 'N/A'}")

# Clean and extract gmap_ids for massage businesses that are actually therapy/massage
massage_ids = []
massage_names_desc = []

for business in massage_businesses:
    name_lower = business.get('name', '').lower()
    description_lower = business.get('description', '').lower()
    
    # Check if it's actually a massage therapy business
    if 'massage' in name_lower or 'massage therapy' in description_lower or 'bodywork' in description_lower or 'spa' in name_lower:
        # Filter out obvious non-massage businesses
        if not any(word in name_lower for word in ['oracle', 'gallery', 'ibew', 'entrance', 'highpoint']):
            massage_ids.append(business['gmap_id'])
            massage_names_desc.append((business['name'], business['description']))

print(f"Found {len(massage_ids)} likely massage therapy businesses")
for name, gid in massage_names_desc:
    print(f"  - {name}: {gid}")

result = {
    "massage_ids": massage_ids,
    "massage_names_desc": massage_names_desc,
    "count": len(massage_ids)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:4': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.', 'num_of_reviews': '7', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store pickup"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.', 'num_of_reviews': '6', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'MISC': '{"Accessibility": ["Wheelchair accessible entrance"]}', 'state': 'Open ⋅ Closes 5:30PM'}], 'var_functions.query_db:6': [], 'var_functions.query_db:8': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.'}, {'gmap_id': 'gmap_63', 'name': 'Regus - California, Irvine - Oracle Tower', 'description': ' This company in Irvine, CA 92614 specializes in providing flexible workspace solutions tailored to meet the needs of professionals and businesses.'}, {'gmap_id': 'gmap_51', 'name': 'Taba Rug Gallery', 'description': 'Longtime boutique featuring high-quality Persian & Oriental rugs, plus repair & cleaning services. Discover a curated selection of exquisite floor coverings and textiles that enhance any space, conveniently located in La Jolla, CA 92037.'}, {'gmap_id': 'gmap_59', 'name': 'IBEW 441', 'description': ' Located in Orange, CA 92868, this professional hub offers a variety of workspace solutions and essential services for entrepreneurs and companies seeking a productive environment.'}, {'gmap_id': 'gmap_4', 'name': 'Lafayette Entrance 1', 'description': ' This serene green space in Orinda, CA 94563 offers picturesque walking trails, lush picnic areas, and a tranquil environment for outdoor recreation and relaxation.'}, {'gmap_id': 'gmap_66', 'name': 'HIGHPOINTE', 'description': ' This professional workspace in Mission Viejo, CA 92691 offers flexible office solutions and meeting facilities designed to support your business needs.'}]}

exec(code, env_args)
