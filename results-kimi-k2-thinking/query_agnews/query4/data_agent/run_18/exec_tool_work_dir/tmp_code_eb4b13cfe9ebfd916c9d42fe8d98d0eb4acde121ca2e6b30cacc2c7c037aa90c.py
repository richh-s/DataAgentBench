code = """import json
import re
from collections import defaultdict

# Load data
metadata_file_path = locals()['var_functions.query_db:4']
with open(metadata_file_path, 'r') as f:
    metadata_2015 = json.load(f)

articles_file_path = locals()['var_functions.query_db:12']
with open(articles_file_path, 'r') as f:
    all_articles = json.load(f)

# Create lookup
metadata_dict = {item['article_id']: item for item in metadata_2015}
articles_dict = {item['article_id']: item for item in all_articles}

# More precise World category detection
def is_world_news(title, description):
    text = (title + ' ' + description).lower()
    
    # Strong indicators of World news
    world_indicators = [
        'iraq', 'iran', 'afghanistan', 'israel', 'palestine', 'syria', 'lebanon',
        'pakistan', 'india conflict', 'korea', 'china', 'russia', 'ukraine', 'taliban',
        'al qaeda', 'terrorist', 'terrorism', 'militant', 'insurgent', 'war in', 'attack on',
        'bombing in', 'explosion in', 'killed in', 'dead in', 'violence in', 'crisis in',
        'united nations', 'un secretary', 'un security council', 'un resolution', 'peace treaty',
        'diplomatic', 'embassy', 'ambassador', 'foreign minister', 'state visit', 'summit',
        'international', 'global summit', 'world bank', 'imf', 'world leaders', 'nato',
        'european union', 'eu', ' refugee', 'african union', 'oas', 'world court', 'icc'
    ]
    
    # Business keywords that should NOT be world news
    business_indicators = [
        'stocks', 'stock market', 'wall st', 'wall street', 'earnings', 'profit', 'ipo',
        'merger', 'acquisition', 'revenue', 'sales', 'quarterly', 'shares', 'investment',
        'company', 'corporation', 'business', 'economy', 'economic', 'trade deficit', 'oil prices'
    ]
    
    # Sports and Tech indicators
    sports_indicators = ['football', 'baseball', 'basketball', 'soccer', 'tennis', 'game', 'score', 'season']
    tech_indicators = ['google', 'microsoft', 'software', 'hardware', 'computer', 'technology', 'tech']
    
    # Check if it's world news
    world_score = sum(1 for indicator in world_indicators if indicator in text)
    business_score = sum(1 for indicator in business_indicators if indicator in text)
    sports_score = sum(1 for indicator in sports_indicators if indicator in text)
    tech_score = sum(1 for indicator in tech_indicators if indicator in text)
    
    # It's World if it has world indicators and doesn't have stronger business/sports/tech signals
    if world_score > 0:
        if business_score > world_score or sports_score > 0 or tech_score > world_score:
            return False
        return True
    
    return False

# Collect World articles from 2015
world_articles_by_region = defaultdict(list)

for article_id, article in articles_dict.items():
    if article_id in metadata_dict:
        metadata = metadata_dict[article_id]
        if is_world_news(article.get('title', ''), article.get('description', '')):
            region = metadata['region']
            world_articles_by_region[region].append({
                'article_id': article_id,
                'title': article.get('title', ''),
                'description': article.get('description', '')
            })

# Count by region
region_counts = {region: len(articles) for region, articles in world_articles_by_region.items()}
sorted_counts = sorted(region_counts.items(), key=lambda x: x[1], reverse=True)

# Get samples from top region
top_region = sorted_counts[0][0] if sorted_counts else None
samples = world_articles_by_region[top_region][:5] if top_region else []

print('__RESULT__:')
print(json.dumps({
    'top_region': top_region,
    'region_counts': region_counts,
    'sorted_regions': sorted_counts,
    'samples_from_top': samples
}, default=str))"""

env_args = {'var_functions.list_db:0': ['authors', 'article_metadata'], 'var_functions.list_db:1': ['articles'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': [{'_id': '6969df3b0f682e5f6f226df5', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969df3b0f682e5f6f226df6', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969df3b0f682e5f6f226df7', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969df3b0f682e5f6f226df8', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969df3b0f682e5f6f226df9', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:10': {'metadata_2015_count': 6696, 'articles_data_count': 5, 'sample_metadata': [{'article_id': '13', 'region': 'Europe', 'publication_date': '2015-10-17'}, {'article_id': '18', 'region': 'South America', 'publication_date': '2015-08-15'}, {'article_id': '26', 'region': 'Africa', 'publication_date': '2015-08-03'}], 'sample_articles': [{'_id': '6969df3b0f682e5f6f226df5', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969df3b0f682e5f6f226df6', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969df3b0f682e5f6f226df7', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}]}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'metadata_2015_count': 6696, 'all_articles_count': 50000, 'sample_metadata': [{'article_id': '13', 'region': 'Europe', 'publication_date': '2015-10-17'}, {'article_id': '18', 'region': 'South America', 'publication_date': '2015-08-15'}, {'article_id': '26', 'region': 'Africa', 'publication_date': '2015-08-03'}], 'sample_articles': [{'_id': '6969df3b0f682e5f6f226df5', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969df3b0f682e5f6f226df6', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969df3b0f682e5f6f226df7', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}]}, 'var_functions.execute_python:16': {'world_articles_count': 1092, 'region_counts': {'South America': 236, 'Asia': 209, 'North America': 194, 'Europe': 219, 'Africa': 234}, 'top_region': ['South America', 236], 'top_5_regions': [['South America', 236], ['Africa', 234], ['Europe', 219], ['Asia', 209], ['North America', 194]]}, 'var_functions.execute_python:18': {'samples_by_region': {'Europe': [{'article_id': '13', 'region': 'Europe', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'article_id': '179', 'region': 'Europe', 'title': 'Reverse Psychology', 'description': "\\\\I really hope SUN doesn't Open Source Java at JavaOne this year.  It would be a\\terrible decision and seriously hurt the tech industry.  Also, it would hurt SUN\\and I'm sure their responsible enough to realize this.\\\\(Lets hope that works!)\\\\"}, {'article_id': '203', 'region': 'Europe', 'title': "'Madden,' 'ESPN' Football Score in Different Ways", 'description': ' PROVIDENCE, R.I. (Reuters) - Was absenteeism a little high  on Tuesday among the guys at the office? EA Sports would like  to think it was because "Madden NFL 2005" came out that day,  and some fans of the football simulation are rabid enough to  take a sick day to play it.'}], 'South America': [{'article_id': '18', 'region': 'South America', 'title': 'US trade deficit swells in June', 'description': 'The US trade deficit has exploded 19 to a record \\$55.8bn as oil costs drove imports higher, according to a latest figures.'}, {'article_id': '51', 'region': 'South America', 'title': 'Delightful Dell', 'description': "The company's results show that it's not grim all over tech world. Just all of it that isn't Dell."}, {'article_id': '74', 'region': 'South America', 'title': 'HP to Buy Synstar', 'description': 'Hewlett-Packard will pay \\$297 million for the British company. Also: TiVo goes all out to attract customers   hellip;. Sprint offers service guarantees for business wireless subscribers   hellip;. and more.'}], 'Africa': [{'article_id': '26', 'region': 'Africa', 'title': 'Google auction begins on Friday', 'description': 'An auction of shares in Google, the web search engine which could be floated for as much as \\$36bn, takes place on Friday.'}, {'article_id': '52', 'region': 'Africa', 'title': "Chrysler's Bling King", 'description': "After a tough year, Detroit's troubled carmaker is back -- thanks to a maverick designer and a car that is dazzling the hip-hop crowd"}, {'article_id': '117', 'region': 'Africa', 'title': 'Earth is Rare, New Study Suggests (SPACE.com)', 'description': "SPACE.com - Flip a coin. Heads, Earth is a common sort of planet. Tails, and ours is as unusual as a coin landing on edge. That's about the state of knowledge for scientists who ponder the question of our planet's rarity."}], 'Asia': [{'article_id': '67', 'region': 'Asia', 'title': 'IT Myth 5: Most IT projects fail', 'description': 'Do most IT projects fail? Some point to the number of giant consultancies such as IBM Global Services, Capgemini, and Sapient, who feed off bad experiences encountered by enterprises. Sapient is a company founded on the realization that IT projects are not successful, says Sapient CTO Ben Gaucherin.'}, {'article_id': '70', 'region': 'Asia', 'title': "U.K.'s NHS taps Gartner to help plan \\$9B IT overhaul", 'description': "LONDON -- The U.K.'s National Health Service (NHS) has tapped IT researcher Gartner Inc. to provide market intelligence services as the health organization forges ahead with a mammoth, 5 billion (\\$9.2 billion) project to upgrade its information technology infrastructure."}, {'article_id': '86', 'region': 'Asia', 'title': 'Oracle Sales Data Seen Being Released (Reuters)', 'description': "Reuters - Oracle Corp. sales documents\\detailing highly confidential information, such as which\\companies receive discounts on Oracle's business software\\products and the size of the discounts, are likely to be made\\public, a federal judge said on Friday."}], 'North America': [{'article_id': '97', 'region': 'North America', 'title': "What's in a Name? Well, Matt Is Sexier Than Paul (Reuters)", 'description': 'Reuters - As Shakespeare said, a rose by any other\\name would smell as sweet. Right?'}, {'article_id': '165', 'region': 'North America', 'title': "Insecurity: (Or Why Americans Aren't Feeling The Recovery)", 'description': "The New Republic's website is currently carrying an interesting piece which tries to explain the anomaly that although the US economy is growing, a lot of its citizens are still feeling worse off. The article explains the results of a 40 year panel study which has shown that although mean incomes have increased, income variability has increased massively, causing many Americans to feel less well off, despite the growing economy.      "}, {'article_id': '364', 'region': 'North America', 'title': 'Tools wrap: Sun, Javalobby, Infravio make moves', 'description': 'Officials at Sun Microsystems, Javalobby, and Infravio this week revealed initiatives positioned as advances in either Java development or Web services consumption.'}]}}, 'var_functions.execute_python:20': {'total_world_articles': 311, 'world_by_region': {'Europe': 59, 'South America': 68, 'Africa': 69, 'Asia': 57, 'North America': 58}, 'sorted_world_regions': [['Africa', 69], ['South America', 68], ['Europe', 59], ['North America', 58], ['Asia', 57]], 'top_world_region': ['Africa', 69]}}

exec(code, env_args)
