code = """import json
from collections import Counter

# Load 2015 metadata
metadata_2015 = locals()['var_functions.query_db:60']
if isinstance(metadata_2015, str) and metadata_2015.endswith('.json'):
    with open(metadata_2015, 'r') as f:
        metadata_2015 = json.load(f)

# Create region lookup
region_lookup = {int(item['article_id']): item['region'] for item in metadata_2015}
print(f"Total 2015 articles: {len(region_lookup)}")

# World category keywords
world_keywords = [
    'trade', 'deficit', 'international', 'global', 'war', 'peace', 'diplomat',
    'embassy', 'conflict', 'treaty', 'sanction', 'oil', 'energy', 'crisis',
    'refugee', 'aid', 'world', 'abroad', 'overseas', 'foreign', 'nation',
    'europe', 'asia', 'africa', 'america', 'china', 'japan', 'india', 'russia',
    'germany', 'france', 'uk', 'britain', 'afghanistan', 'iraq', 'iran',
    'israel', 'palestine', 'syria', 'climate', 'environment', 'warming',
    'pollution', 'security', 'terror', 'military', 'nuclear', 'korea', 'pakistan',
    'diplomacy', 'negotiation', 'alliance', 'summit', 'conference', 'refugees',
    'mideast', 'weapons', 'defense', 'aids', 'disease', 'epidemic', 'mexico',
    'canada', 'brazil', 'venezuela', 'colombia', 'indonesia', 'thailand'
]

def is_world_article(title, description):
    """Check if article belongs to World category based on keywords"""
    text = ((title or '') + ' ' + (description or '')).lower()
    return any(keyword in text for keyword in world_keywords)

# Load the 2015 articles batch
articles_batch = locals()['var_functions.query_db:50']
if isinstance(articles_batch, str) and articles_batch.endswith('.json'):
    with open(articles_batch, 'r') as f:
        articles_batch = json.load(f)

# Count World articles by region
world_articles_by_region = Counter()
processed_count = 0
world_count = 0

for article in articles_batch:
    article_id = int(article['article_id'])
    if article_id in region_lookup:
        processed_count += 1
        title = article.get('title', '')
        description = article.get('description', '')
        
        if is_world_article(title, description):
            region = region_lookup[article_id]
            world_articles_by_region[region] += 1
            world_count += 1

# Calculate results
if world_articles_by_region:
    most_common = world_articles_by_region.most_common(1)[0]
    message = f"Based on processed articles, {most_common[0]} published the most World articles with {most_common[1]} articles."
    message += f" Total World articles found: {world_count} out of {processed_count} processed."
    message += f" Region breakdown: {dict(world_articles_by_region)}"
else:
    message = f"No World articles found in the {processed_count} articles processed."

print('__RESULT__:')
print(message)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:8': {'total_articles_2015': 6696, 'unique_article_ids': 6696, 'sample_article_ids': [13, 18, 26]}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'total_articles': 6696, 'min_id': 13, 'max_id': 127570}, 'var_functions.execute_python:14': {'total_articles': 6696, 'number_of_batches': 14, 'batch_size': 500, 'first_batch_sample': [13, 18, 26, 51, 52]}, 'var_functions.execute_python:16': {'total_articles': 6696, 'number_of_batches': 7, 'first_batch_size': 1000, 'last_article_id': 127570}, 'var_functions.query_db:18': [{'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'article_id': '18', 'title': 'US trade deficit swells in June', 'description': 'The US trade deficit has exploded 19 to a record \\$55.8bn as oil costs drove imports higher, according to a latest figures.'}, {'article_id': '26', 'title': 'Google auction begins on Friday', 'description': 'An auction of shares in Google, the web search engine which could be floated for as much as \\$36bn, takes place on Friday.'}, {'article_id': '51', 'title': 'Delightful Dell', 'description': "The company's results show that it's not grim all over tech world. Just all of it that isn't Dell."}, {'article_id': '52', 'title': "Chrysler's Bling King", 'description': "After a tough year, Detroit's troubled carmaker is back -- thanks to a maverick designer and a car that is dazzling the hip-hop crowd"}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'article_id': '18', 'title': 'US trade deficit swells in June', 'description': 'The US trade deficit has exploded 19 to a record \\$55.8bn as oil costs drove imports higher, according to a latest figures.'}, {'article_id': '26', 'title': 'Google auction begins on Friday', 'description': 'An auction of shares in Google, the web search engine which could be floated for as much as \\$36bn, takes place on Friday.'}, {'article_id': '51', 'title': 'Delightful Dell', 'description': "The company's results show that it's not grim all over tech world. Just all of it that isn't Dell."}, {'article_id': '52', 'title': "Chrysler's Bling King", 'description': "After a tough year, Detroit's troubled carmaker is back -- thanks to a maverick designer and a car that is dazzling the hip-hop crowd"}], 'var_functions.execute_python:26': {'articles_fetched': 5, 'sample_articles': [{'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'article_id': '18', 'title': 'US trade deficit swells in June', 'description': 'The US trade deficit has exploded 19 to a record \\$55.8bn as oil costs drove imports higher, according to a latest figures.'}]}, 'var_functions.execute_python:30': {'world_articles_found': 2, 'total_articles_checked': 5, 'region_counts': {'South America': 2}, 'most_common_region': ['South America', 2]}, 'var_functions.execute_python:32': {'total_article_ids': 6696, 'number_of_batches': 7, 'first_batch_size': 1000, 'last_batch_size': 696, 'sample_batch_ids': [13, 18, 26, 51, 52]}, 'var_functions.execute_python:36': {'total_articles': 6696, 'batches': 7, 'batch_size': 1000}, 'var_functions.query_db:42': [{'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}, {'article_id': '5', 'title': 'Stocks End Up, But Near Year Lows (Reuters)', 'description': 'Reuters - Stocks ended slightly higher on Friday\\but stayed near lows for the year as oil prices surged past  #36;46\\a barrel, offsetting a positive outlook from computer maker\\Dell Inc. (DELL.O)'}], 'var_functions.execute_python:46': {'error': 'No World articles found'}, 'var_functions.execute_python:48': {'total_2015_articles': 6696, 'number_of_batches': 14, 'batch_size': 500, 'first_batch': [13, 18, 26, 51, 52, 67, 70, 74, 86, 97, 116, 117, 141, 165, 179, 203, 240, 243, 266, 271, 309, 314, 364, 365, 369, 379, 408, 429, 488, 498, 501, 509, 519, 534, 606, 652, 698, 743, 745, 879, 885, 902, 907, 924, 932, 935, 941, 970, 987, 993, 1001, 1045, 1053, 1061, 1065, 1077, 1084, 1108, 1137, 1171, 1190, 1242, 1244, 1277, 1332, 1363, 1366, 1386, 1435, 1470, 1477, 1494, 1531, 1548, 1570, 1589, 1611, 1631, 1662, 1678, 1689, 1720, 1727, 1736, 1769, 1791, 1792, 1848, 1853, 1866, 1880, 1905, 1910, 1969, 1978, 1996, 2009, 2010, 2017, 2023, 2041, 2168, 2180, 2214, 2218, 2270, 2285, 2302, 2322, 2351, 2358, 2368, 2389, 2395, 2414, 2430, 2457, 2470, 2491, 2501, 2505, 2512, 2514, 2517, 2519, 2602, 2613, 2616, 2617, 2668, 2675, 2676, 2693, 2707, 2725, 2740, 2741, 2762, 2767, 2783, 2798, 2859, 2887, 2901, 2903, 3006, 3016, 3019, 3028, 3059, 3061, 3079, 3096, 3127, 3137, 3139, 3153, 3215, 3222, 3231, 3232, 3234, 3239, 3244, 3257, 3265, 3289, 3305, 3368, 3389, 3417, 3445, 3457, 3482, 3492, 3510, 3523, 3545, 3559, 3564, 3570, 3574, 3601, 3631, 3643, 3665, 3678, 3688, 3733, 3750, 3755, 3789, 3846, 3852, 3861, 3909, 3914, 3917, 3945, 4016, 4041, 4050, 4056, 4089, 4090, 4129, 4144, 4181, 4224, 4270, 4272, 4327, 4339, 4369, 4370, 4411, 4437, 4438, 4440, 4568, 4575, 4583, 4600, 4623, 4665, 4679, 4719, 4731, 4763, 4801, 4890, 4906, 4909, 4922, 4953, 4959, 4996, 5003, 5009, 5023, 5031, 5037, 5041, 5062, 5078, 5100, 5102, 5109, 5111, 5143, 5149, 5151, 5158, 5171, 5172, 5176, 5293, 5300, 5303, 5313, 5351, 5357, 5365, 5370, 5393, 5395, 5396, 5410, 5430, 5471, 5532, 5581, 5584, 5600, 5605, 5614, 5655, 5671, 5683, 5687, 5694, 5713, 5722, 5723, 5768, 5784, 5831, 5834, 5841, 5870, 5904, 5915, 5935, 5945, 5951, 5959, 5983, 6009, 6030, 6034, 6054, 6111, 6115, 6140, 6166, 6183, 6231, 6249, 6295, 6301, 6306, 6346, 6400, 6411, 6417, 6435, 6436, 6486, 6507, 6527, 6528, 6538, 6557, 6569, 6584, 6615, 6654, 6691, 6692, 6742, 6745, 6756, 6761, 6768, 6814, 6830, 6834, 6838, 6840, 6870, 6881, 6893, 6905, 6913, 6918, 6949, 6997, 7068, 7114, 7122, 7140, 7218, 7243, 7257, 7275, 7289, 7301, 7336, 7338, 7356, 7371, 7376, 7388, 7393, 7415, 7418, 7426, 7458, 7488, 7499, 7500, 7516, 7567, 7600, 7610, 7629, 7630, 7643, 7656, 7665, 7685, 7700, 7714, 7731, 7737, 7783, 7790, 7875, 7876, 7887, 7896, 7897, 7901, 7906, 7923, 7946, 7949, 7952, 7957, 8023, 8027, 8042, 8079, 8142, 8154, 8185, 8217, 8218, 8248, 8260, 8302, 8304, 8309, 8327, 8348, 8360, 8373, 8416, 8443, 8473, 8475, 8486, 8495, 8516, 8521, 8522, 8546, 8572, 8576, 8607, 8616, 8631, 8632, 8645, 8681, 8692, 8695, 8739, 8762, 8778, 8803, 8831, 8849, 8853, 8899, 9000, 9055, 9083, 9101, 9120, 9127, 9163, 9164, 9165, 9216, 9220, 9249, 9261, 9268, 9292, 9295, 9348, 9409, 9429, 9439, 9466, 9490, 9506, 9521, 9530, 9534, 9576, 9590, 9650, 9657, 9660, 9681, 9684, 9693, 9705, 9751, 9764, 9772, 9793, 9801, 9848, 9860, 9898, 9913, 9933, 9937, 9948, 9975, 9978, 10045, 10050, 10051, 10062, 10079, 10084], 'world_keywords': ['trade', 'deficit', 'international', 'global', 'war']}, 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.execute_python:62': {'status': 'processing_setup', 'total_2015_articles': 6696, 'first_id': 13, 'last_id': 127570}, 'var_functions.execute_python:68': {'total_2015_articles': 6696, 'articles_processed': 100, 'world_articles_found': 59, 'world_articles_by_region': {'South America': 13, 'Asia': 14, 'North America': 10, 'Europe': 14, 'Africa': 8}, 'most_world_articles_region': 'Asia', 'most_world_articles_count': 14}, 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.execute_python:72': {'total_2015_articles': 6696, 'articles_by_region': {'Europe': 1357, 'South America': 1332, 'Africa': 1345, 'Asia': 1333, 'North America': 1329}, 'regions': ['Europe', 'South America', 'Africa', 'Asia', 'North America']}}

exec(code, env_args)
