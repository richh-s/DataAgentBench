code = """import json
import re
from datetime import datetime

review_file_path = locals()['var_functions.query_db:12']
with open(review_file_path, 'r') as f:
    high_rating_reviews = json.load(f)

business_data = locals()['var_functions.query_db:22']
business_names = {b['gmap_id']: b['name'] for b in business_data}

def parse_date(date_str):
    date_str = str(date_str).strip()
    
    formats = [
        '%Y-%m-%d %H:%M:%S',
        '%B %d, %Y at %I:%M %p',
        '%Y-%m-%d %H:%M:%S.%f',
        '%d %b %Y, %H:%M',
        '%d %b %Y, %H:%M:%S',
        '%B %d, %Y at %I:%M:%S %p',
        '%Y-%m-%d',
    ]
    
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    
    year_match = re.search(r'(\d{4})', date_str)
    if year_match:
        year = int(year_match.group(1))
        return datetime(year, 1, 1)
    
    return None

business_review_count = {}
for review in high_rating_reviews:
    date_obj = parse_date(review['time'])
    if date_obj and date_obj.year == 2019:
        gmap_id = review['gmap_id']
        business_review_count[gmap_id] = business_review_count.get(gmap_id, 0) + 1

top_3 = sorted(business_review_count.items(), key=lambda x: x[1], reverse=True)[:3]

result = []
for gmap_id, count in top_3:
    business_name = business_names.get(gmap_id, 'Unknown')
    result.append({
        'business_name': business_name,
        'gmap_id': gmap_id,
        'high_rating_review_count': count
    })

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:4': [{'name': 'Michael Rizal', 'time': 'September 03, 2020 at 04:15 PM', 'rating': '5', 'text': 'Located in the vibrant area of Los Angeles, CA 90023, this company truly stands out. "Great company. Amazing customer service and they always have what we need in stock. Sometimes, we’d ask to hold for future orders and they will! Miss Jane is very helpful and great communicator."', 'gmap_id': 'gmap_44'}, {'name': 'Faranak Rafizadeh', 'time': '2021-04-12 17:07:52', 'rating': '5', 'text': 'Los Angeles is known for its vibrant culture and friendly atmosphere. "Nice people helpful."', 'gmap_id': 'gmap_44'}, {'name': 'Javier Perez', 'time': '2018-04-23 16:24:26', 'rating': '5', 'text': 'I had a fantastic experience at this amazing spot in Los Angeles, CA 90023, where the friendly staff went above and beyond to make my visit truly enjoyable!', 'gmap_id': 'gmap_44'}, {'name': 'Luis P.', 'time': '2017-07-10 22:12:19', 'rating': '5', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the friendly staff and delicious pastries made my day truly special!', 'gmap_id': 'gmap_44'}, {'name': 'His Mama Cakez', 'time': 'May 19, 2021 at 03:55 AM', 'rating': '3', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the coffee was exceptional and the atmosphere was incredibly welcoming!', 'gmap_id': 'gmap_44'}], 'var_functions.query_db:8': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.', 'num_of_reviews': '7', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store pickup"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.', 'num_of_reviews': '6', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'MISC': '{"Accessibility": ["Wheelchair accessible entrance"]}', 'state': 'Open ⋅ Closes 5:30PM'}], 'var_functions.execute_python:10': {'review_count': 5, 'business_count': 5}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'total_high_rating_reviews': 1666}, 'var_functions.execute_python:20': {'total_high_rating_reviews': 1666, 'reviews_from_2019': 238}, 'var_functions.query_db:22': [{'gmap_id': 'gmap_44', 'name': 'City Textile'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles'}, {'gmap_id': 'gmap_74', 'name': 'Vons Chicken'}, {'gmap_id': 'gmap_17', 'name': 'Black Tie Ski Rental Delivery of Mammoth'}, {'gmap_id': 'gmap_22', 'name': 'Angel-A Massage'}, {'gmap_id': 'gmap_29', 'name': 'Dunn-Edwards Paints'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage'}, {'gmap_id': 'gmap_19', 'name': 'PODS Sacramento Hub'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_32', 'name': 'J B Oriental Inc'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage'}, {'gmap_id': 'gmap_48', 'name': 'State Street/7th Street'}, {'gmap_id': 'gmap_50', 'name': 'HDR'}, {'gmap_id': 'gmap_18', 'name': 'Porvene Doors'}, {'gmap_id': 'gmap_16', 'name': 'Hanford Auto Supply'}, {'gmap_id': 'gmap_26', 'name': "Jeff's Auto Repair"}, {'gmap_id': 'gmap_28', 'name': 'Good Massage'}, {'gmap_id': 'gmap_23', 'name': 'Tax Deferred Solutions (TDS Group, INC)'}, {'gmap_id': 'gmap_31', 'name': 'Origin Church'}, {'gmap_id': 'gmap_27', 'name': 'Colfax Elementary School'}, {'gmap_id': 'gmap_2', 'name': 'Life Pointe Church'}, {'gmap_id': 'gmap_30', 'name': 'The Beauty Bar'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_72', 'name': "Zuby's Brake Tires & Wheels"}, {'gmap_id': 'gmap_63', 'name': 'Regus - California, Irvine - Oracle Tower'}, {'gmap_id': 'gmap_52', 'name': 'Fitness Machine Technicians'}, {'gmap_id': 'gmap_56', 'name': 'J & T Plumbing Pros'}, {'gmap_id': 'gmap_65', 'name': 'Excel Hair & Nails'}, {'gmap_id': 'gmap_37', 'name': 'Birdi Systems, Inc.'}, {'gmap_id': 'gmap_51', 'name': 'Taba Rug Gallery'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More'}, {'gmap_id': 'gmap_36', 'name': 'Beauty Divine Artistry'}, {'gmap_id': 'gmap_59', 'name': 'IBEW 441'}, {'gmap_id': 'gmap_57', 'name': "Ely's Beauty Salon"}, {'gmap_id': 'gmap_13', 'name': 'United Methodist Church'}, {'gmap_id': 'gmap_15', 'name': 'Dirk Vermeulen - State Farm Insurance Agent'}, {'gmap_id': 'gmap_12', 'name': 'White Barn Candle Co'}, {'gmap_id': 'gmap_14', 'name': "Teter's Oakdale Jewelry"}, {'gmap_id': 'gmap_3', 'name': 'Timmons Auto & Truck Repair'}, {'gmap_id': 'gmap_35', 'name': 'Encino Dermatology & Laser: Alex Khadavi MD'}, {'gmap_id': 'gmap_4', 'name': 'Lafayette Entrance 1'}, {'gmap_id': 'gmap_6', 'name': 'ATSI'}, {'gmap_id': 'gmap_7', 'name': "Rossy's Beauty Salon"}, {'gmap_id': 'gmap_8', 'name': 'TACOS LA CABANA'}, {'gmap_id': 'gmap_10', 'name': 'Jjironwork'}, {'gmap_id': 'gmap_9', 'name': 'Mariscos el poblano'}, {'gmap_id': 'gmap_77', 'name': 'Climate Control'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan'}, {'gmap_id': 'gmap_78', 'name': 'Avani Staffing Solutions'}, {'gmap_id': 'gmap_70', 'name': 'CrossFit to the Core'}, {'gmap_id': 'gmap_5', 'name': 'Dr. Syverain Skincare Clinic'}, {'gmap_id': 'gmap_34', 'name': "Ruby's Boutique"}, {'gmap_id': 'gmap_11', 'name': 'Paradise tattoo'}, {'gmap_id': 'gmap_0', 'name': 'Full Circle Trading Post'}, {'gmap_id': 'gmap_1', 'name': 'Northern Builders Supply'}, {'gmap_id': 'gmap_62', 'name': 'Acuity Eye Group, Retina Institute & Acuity 360 Advanced Vision Center - Tustin'}, {'gmap_id': 'gmap_61', 'name': 'Off The Hoof'}, {'gmap_id': 'gmap_58', 'name': 'Weatherline Reroofing & Repairs'}, {'gmap_id': 'gmap_66', 'name': 'HIGHPOINTE'}, {'gmap_id': 'gmap_46', 'name': 'B2Sign, Inc.'}, {'gmap_id': 'gmap_47', 'name': 'Laptop Masters'}, {'gmap_id': 'gmap_75', 'name': 'HAVEN™ Dispensary'}, {'gmap_id': 'gmap_76', 'name': 'IronStep'}, {'gmap_id': 'gmap_73', 'name': 'CYD Works Electric'}, {'gmap_id': 'gmap_55', 'name': 'Mobile Moreno Valley Dispensary'}, {'gmap_id': 'gmap_54', 'name': 'Wildomar Campground'}, {'gmap_id': 'gmap_68', 'name': 'Advanced Auto Upholstery'}, {'gmap_id': 'gmap_71', 'name': 'AMMCOR Management Company, Inc.'}, {'gmap_id': 'gmap_67', 'name': 'LuXe Organic Nails Boutique'}, {'gmap_id': 'gmap_69', 'name': 'Taitz Orly DDS'}, {'gmap_id': 'gmap_64', 'name': 'St John Knits International Inc'}, {'gmap_id': 'gmap_49', 'name': 'NEX Barbershop'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}, {'gmap_id': 'gmap_60', 'name': 'The Dream Junction'}]}

exec(code, env_args)
