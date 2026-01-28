code = """import json
import re
from collections import defaultdict

# Load metadata to get year mapping
metadata_path = locals()['var_functions.query_db:2']
with open(metadata_path, 'r') as f:
    metadata = json.load(f)

# Create mapping of article_id to year
year_mapping = {}
for item in metadata:
    article_id = int(item['article_id'])
    year = int(item['publication_date'][:4])
    year_mapping[article_id] = year

# Business keyword classifier
business_keywords = [
    'business', 'economy', 'stock', 'market', 'finance', 'financial', 'company', 
    'companies', 'dollar', 'euro', 'IPO', 'wall st', 'investment', 'trade',
    'sales', 'revenue', 'profit', 'bank', 'banking', 'corporation', 'merger',
    'acquisition', 'earnings', 'quarterly', 'fiscal', 'GDP', 'inflation',
    'unemployment', 'jobs', 'hiring', 'retail', 'consumer', 'oil', 'energy',
    'commodity', 'commodities', 'exchange', 'shares', 'index', 'nasdaq',
    'dow jones', 'FTSE', 'bond', 'treasury', 'fed', 'federal reserve',
    'ECB', 'european central bank', 'currency', 'deficit', 'surplus',
    'export', 'import', 'tariff', 'tax', 'budget', 'stocks', 'trading',
    'share price', 'quarter', 'economic', 'economics', 'billion', 'million'
]

def is_business_article(title, description):
    if not title and not description:
        return False
    
    text = ((title or '') + ' ' + (description or '')).lower()
    
    for keyword in business_keywords:
        if keyword in text:
            return True
    
    # Check for money patterns
    if re.search(r'\$\s*\d+', text):
        return True
    if re.search(r'\d+\s*(billion|million|trillion)\s*\$', text):
        return True
    
    return False

# Prepare article IDs and batches
article_ids = list(year_mapping.keys())
batch_size = 1000
batches = [article_ids[i:i + batch_size] for i in range(0, len(article_ids), batch_size)]

result = {
    'total_articles': len(article_ids),
    'num_batches': len(batches),
    'batch_size': batch_size
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': 'file_storage/functions.execute_python:6.json', 'var_functions.execute_python:8': 14860, 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.execute_python:12': {'total_articles': 14860, 'articles_per_year': {'2010': 1306, '2011': 1316, '2012': 1355, '2013': 1354, '2014': 1372, '2015': 1357, '2016': 1364, '2017': 1391, '2018': 1351, '2019': 1328, '2020': 1366}}, 'var_functions.execute_python:14': '{"collection": "articles", "filter": {"article_id": {"$in": [3, 9, 13, 14, 21, 27, 43, 60, 62, 63, 64, 66, 78, 128, 140, 142, 143, 144, 151, 154, 164, 179, 181, 190, 201, 202, 203, 210, 214, 216, 223, 243, 257, 265, 268, 270, 271, 279, 298, 300, 309, 328, 336, 338, 339, 348, 371, 379, 383, 394, 398, 400, 429, 439, 446, 452, 456, 457, 460, 474, 482, 484, 485, 502, 509, 510, 514, 532, 534, 536, 539, 554, 557, 564, 567, 569, 572, 576, 584, 597, 624, 642, 647, 661, 663, 669, 678, 682, 697, 712, 717, 756, 763, 768, 774, 782, 793, 805, 810, 846, 865, 879, 919, 935, 940, 974, 982, 984, 987, 990, 993, 999, 1001, 1003, 1014, 1030, 1045, 1054, 1061, 1101, 1103, 1108, 1129, 1135, 1140, 1144, 1148, 1168, 1182, 1190, 1193, 1208, 1229, 1244, 1265, 1284, 1289, 1310, 1323, 1327, 1333, 1334, 1337, 1343, 1362, 1377, 1378, 1380, 1386, 1391, 1406, 1412, 1416, 1422, 1439, 1441, 1450, 1462, 1495, 1510, 1529, 1536, 1541, 1549, 1551, 1565, 1567, 1570, 1572, 1581, 1594, 1600, 1609, 1611, 1627, 1635, 1642, 1646, 1659, 1662, 1669, 1677, 1678, 1690, 1707, 1712, 1719, 1730, 1732, 1744, 1760, 1769, 1788, 1800, 1802, 1816, 1818, 1834, 1835, 1839, 1846, 1852, 1853, 1887, 1889, 1909, 1911, 1928, 1936, 1944, 1949, 1955, 1963, 1978, 1983, 1992, 2017, 2046, 2056, 2066, 2077, 2084, 2087, 2099, 2114, 2142, 2146, 2148, 2151, 2154, 2158, 2162, 2166, 2167, 2172, 2173, 2182, 2186, 2203, 2229, 2232, 2253, 2261, 2272, 2275, 2285, 2286, 2289, 2301, 2303, 2304, 2321, 2322, 2323, 2332, 2364, 2378, 2387, 2396, 2401, 2403, 2409, 2410, 2418, 2421, 2442, 2457, 2473, 2488, 2505, 2515, 2520, 2527, 2543, 2574, 2577, 2585, 2587, 2597, 2608, 2612, 2615, 2616, 2618, 2623, 2630, 2632, 2674, 2676, 2681, 2683, 2684, 2693, 2708, 2717, 2719, 2734, 2736, 2739, 2748, 2751, 2769, 2773, 2774, 2798, 2811, 2815, 2827, 2829, 2846, 2861, 2862, 2869, 2885, 2887, 2893, 2907, 2914, 2915, 2919, 2924, 2932, 2941, 2943, 2944, 2963, 2970, 2989, 3003, 3008, 3035, 3040, 3048, 3067, 3072, 3073, 3078, 3098, 3100, 3106, 3108, 3116, 3123, 3127, 3133, 3143, 3149, 3169, 3170, 3191, 3192, 3196, 3209, 3226, 3239, 3255, 3261, 3263, 3264, 3280, 3301, 3310, 3312, 3320, 3325, 3347, 3354, 3364, 3366, 3368, 3374, 3392, 3403, 3404, 3418, 3425, 3441, 3446, 3447, 3471, 3492, 3500, 3504, 3507, 3514, 3520, 3525, 3526, 3528, 3541, 3542, 3550, 3577, 3590, 3601, 3605, 3609, 3616, 3619, 3627, 3641, 3651, 3656, 3672, 3676, 3690, 3699, 3707, 3714, 3732, 3745, 3773, 3780, 3782, 3803, 3815, 3816, 3824, 3831, 3846, 3856, 3859, 3860, 3878, 3891, 3901, 3902, 3903, 3905, 3932, 3942, 3944, 3954, 3957, 3967, 3973, 3979, 3990, 4002, 4016, 4022, 4027, 4032, 4050, 4064, 4078, 4098, 4099, 4103, 4108, 4112, 4115, 4143, 4144, 4169, 4174, 4178, 4181, 4184, 4195, 4199, 4202, 4234, 4236, 4260, 4269, 4274, 4285, 4291, 4293, 4301, 4319, 4325, 4332, 4339, 4343, 4356, 4358, 4373, 4387, 4395, 4404, 4448, 4463, 4466, 4468, 4474, 4482, 4489, 4501, 4514, 4532, 4536, 4543, 4565, 4568, 4577, 4579, 4589, 4598, 4600, 4611, 4632, 4643, 4644, 4648, 4654, 4680, 4687, 4720, 4724, 4734, 4740, 4746, 4780, 4787, 4797, 4799, 4802, 4804, 4807, 4813, 4830, 4837, 4851, 4852, 4859, 4868, 4871, 4889, 4897, 4906, 4917, 4920, 4922, 4934, 4939, 4949, 4954, 4960, 4966, 4979, 4998, 4999, 5015, 5016, 5043, 5050, 5053, 5060, 5070, 5078, 5081, 5102, 5112, 5122, 5139, 5143, 5149, 5163, 5168, 5177, 5186, 5189, 5202, 5222, 5229, 5245, 5265, 5268, 5274, 5289, 5292, 5293, 5301, 5313, 5328, 5336, 5340, 5348, 5355, 5358, 5360, 5381, 5407, 5409, 5426, 5429, 5434, 5441, 5464, 5493, 5516, 5541, 5544, 5558, 5560, 5575, 5598, 5607, 5613, 5626, 5636, 5641, 5642, 5644, 5652, 5654, 5658, 5659, 5661, 5663, 5670, 5674, 5683, 5697, 5702, 5706, 5707, 5718, 5722, 5752, 5758, 5763, 5786, 5787, 5828, 5848, 5853, 5856, 5859, 5861, 5871, 5874, 5888, 5906, 5915, 5930, 5947, 5956, 5962, 5988, 5989, 5996, 5999, 6000, 6005, 6015, 6024, 6029, 6034, 6076, 6082, 6083, 6085, 6100, 6107, 6115, 6125, 6139, 6157, 6174, 6175, 6205, 6208, 6211, 6213, 6215, 6231, 6258, 6259, 6264, 6275, 6282, 6290, 6296, 6301, 6311, 6323, 6325, 6330, 6338, 6349, 6356, 6360, 6367, 6372, 6379, 6392, 6401, 6403, 6404, 6408, 6415, 6416, 6436, 6441, 6449, 6458, 6460, 6465, 6466, 6471, 6486, 6487, 6497, 6511, 6518, 6538, 6560, 6562, 6569, 6573, 6587, 6589, 6621, 6622, 6623, 6629, 6634, 6635, 6643, 6644, 6655, 6663, 6664, 6665, 6675, 6677, 6701, 6703, 6707, 6710, 6718, 6725, 6754, 6764, 6768, 6773, 6778, 6782, 6783, 6787, 6793, 6795, 6796, 6818, 6847, 6848, 6861, 6868, 6870, 6871, 6883, 6897, 6898, 6907, 6913, 6914, 6929, 6930, 6937, 6950, 6953, 6981, 6984, 7008, 7046, 7066, 7067, 7084, 7094, 7099, 7111, 7113, 7116, 7122, 7123, 7124, 7126, 7135, 7140, 7141, 7144, 7152, 7161, 7164, 7172, 7176, 7188, 7201, 7216, 7228, 7229, 7236, 7238, 7248, 7250, 7254, 7260, 7264, 7268, 7275, 7281, 7286, 7289, 7295, 7298, 7313, 7324, 7345, 7361, 7368, 7369, 7370, 7371, 7379, 7391, 7392, 7414, 7456, 7478, 7497, 7508, 7532, 7542, 7563, 7579, 7593, 7609, 7610, 7630, 7632, 7641, 7647, 7649, 7669, 7670, 7676, 7679, 7698, 7700, 7731, 7732, 7740, 7752, 7760, 7766, 7782, 7784, 7785, 7791, 7794, 7800, 7814, 7817, 7861, 7872, 7883, 7884, 7893, 7895, 7896, 7906, 7910, 7914, 7917, 7923, 7927, 7940, 7943, 7962, 7970, 7975, 7986, 7998, 8010, 8031, 8041, 8056, 8059, 8062, 8065, 8072, 8075, 8112, 8115, 8119, 8120, 8132, 8134, 8137, 8138, 8143, 8148, 8149, 8157, 8170, 8183, 8196, 8198, 8200, 8217, 8218, 8229, 8236, 8242, 8248, 8249, 8271, 8272, 8276, 8285, 8291, 8296, 8297, 8317, 8322, 8329, 8346, 8348, 8352, 8355, 8356, 8366, 8377, 8378, 8383, 8389, 8392, 8393, 8398, 8417, 8423, 8428, 8449, 8456, 8459, 8466, 8469, 8472, 8495, 8502, 8511, 8518, 8522, 8532, 8536, 8539, 8547, 8553, 8566, 8580, 8585, 8589, 8603, 8606, 8619, 8621, 8639, 8645, 8665, 8683, 8688, 8693, 8696, 8707, 8712, 8723, 8733, 8760, 8764, 8766, 8775, 8793, 8806, 8808, 8829, 8853, 8866, 8867, 8885, 8920, 8937, 8954, 8971, 8976, 8984, 8988, 8989, 8997, 8999, 9000, 9003, 9007, 9016, 9018, 9024, 9033, 9038]}}, "projection": {"_id": 0, "article_id": 1, "title": 1, "description": 1}}', 'var_functions.query_db:16': [{'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}, {'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'article_id': '14', 'title': 'Dollar Falls Broadly on Record Trade Gap', 'description': " NEW YORK (Reuters) - The dollar tumbled broadly on Friday  after data showing a record U.S. trade deficit in June cast  fresh doubts on the economy's recovery and its ability to draw  foreign capital to fund the growing gap."}, {'article_id': '21', 'title': 'Eurozone economy keeps growing', 'description': 'Official figures show the 12-nation eurozone economy continues to grow, but there are warnings it may slow down later in the year.'}], 'var_functions.execute_python:22': {'business_articles': 5, 'total_articles': 5, 'classification_rate': 100.0}}

exec(code, env_args)
