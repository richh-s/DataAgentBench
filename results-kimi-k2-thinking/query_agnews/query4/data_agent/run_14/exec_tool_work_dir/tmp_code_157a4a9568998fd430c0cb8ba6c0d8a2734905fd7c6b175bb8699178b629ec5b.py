code = """import json
import pandas as pd

# Load articles data
articles_data = locals()['var_functions.query_db:2']

# Load metadata from file
metadata_file = locals()['var_functions.query_db:3']
with open(metadata_file, 'r') as f:
    metadata_data = json.load(f)

# Convert to DataFrames
articles_df = pd.DataFrame(articles_data)
metadata_df = pd.DataFrame(metadata_data)

# Convert article_id to string for consistent merging
articles_df['article_id'] = articles_df['article_id'].astype(str)
metadata_df['article_id'] = metadata_df['article_id'].astype(str)

# Filter for 2015 articles
metadata_df['publication_date'] = pd.to_datetime(metadata_df['publication_date'])
metadata_2015 = metadata_df[metadata_df['publication_date'].dt.year == 2015]

# Merge with articles
merged_2015 = pd.merge(metadata_2015, articles_df, on='article_id', how='inner')

# Define a function to categorize articles
def categorize_article(title, description):
    """Categorize articles into World, Sports, Business, or Science/Technology"""
    text = f"{title} {description}".lower()
    
    # World category keywords
    world_keywords = ['iraq', 'iraqi', 'war', 'conflict', 'united nations', 'un', 'world', 'global', 
                     'international', 'foreign', 'diplomatic', 'treaty', 'peace', 'border', 
                     'embassy', 'consulate', 'refugee', 'asylum', 'migrant', 'migration',
                     'european union', 'eu', 'nato', 'oecd', 'g7', 'g8', 'g20', 'apec',
                     'africa', 'african', 'asia', 'asian', 'europe', 'european', 
                     'america', 'american', 'south america', 'north america', 'latin america',
                     'china', 'chinese', 'japan', 'japanese', 'korea', 'korean',
                     'russia', 'russian', 'putin', 'soviet', 'ukraine', 'ukrainian',
                     'syria', 'syrian', 'iran', 'iranian', 'israel', 'israeli', 'palestine', 'palestinian',
                     'afghanistan', 'afghan', 'pakistan', 'pakistani', 'india', 'indian',
                     'australia', 'australian', 'canada', 'canadian', 'mexico', 'mexican',
                     'germany', 'german', 'france', 'french', 'uk', 'britain', 'british', 'england', 'english',
                     'spain', 'spanish', 'italy', 'italian', 'turkey', 'turkish',
                     'saudi', 'arabia', 'arab', 'emirates', 'qatar', 'kuwait', 'oman', 'yemen',
                     'lebanon', 'lebanese', 'jordan', 'jordanian', 'egypt', 'egyptian', 'libya', 'libyan',
                     'sudan', 'somalia', 'somali', 'ethiopia', 'ethiopian', 'kenya', 'kenyan',
                     'nigeria', 'nigerian', 'south africa', 'congo', 'zimbabwe', 'zimbabwean']
    
    # Sports category keywords
    sports_keywords = ['sport', 'game', 'match', 'tournament', 'championship', 'league', 
                      'team', 'player', 'coach', 'olympic', 'world cup', 'nba', 'nfl', 
                      'mlb', 'nhl', 'soccer', 'football', 'basketball', 'baseball', 'hockey',
                      'tennis', 'golf', 'swimming', 'athletics', 'marathon', 'cycling']
    
    # Business category keywords
    business_keywords = ['business', 'economy', 'economic', 'stock', 'market', 'finance', 
                        'financial', 'company', 'corporation', 'investment', 'investor',
                        'profit', 'revenue', 'sales', 'merger', 'acquisition', 'ipo',
                        'wall street', 'bank', 'banking', 'federal reserve', 'fed', 'dollar',
                        'euro', 'currency', 'trade', 'trading', 'commission', 'earnings']
    
    # Science/Technology category keywords
    sci_tech_keywords = ['science', 'scientific', 'technology', 'tech', 'research', 'study',
                        'researchers', 'scientists', 'computer', 'software', 'hardware',
                        'internet', 'web', 'digital', 'mobile', 'smartphone', 'artificial intelligence',
                        'ai', 'machine learning', 'robot', 'robotics', 'space', 'nasa', 
                        'astronomy', 'physics', 'chemistry', 'biology', 'medical', 'medicine',
                        'health', 'disease', 'vaccine', 'clinical trial', 'breakthrough',
                        'innovation', 'innovative', 'discovery', 'discovered', 'developed']
    
    # Check world category first (it's often the most specific for geopolitical events)
    if any(keyword in text for keyword in world_keywords):
        return 'World'
    elif any(keyword in text for keyword in sports_keywords):
        return 'Sports'
    elif any(keyword in text for keyword in business_keywords):
        return 'Business'
    elif any(keyword in text for keyword in sci_tech_keywords):
        return 'Science/Technology'
    else:
        # Default to World if it contains location names not captured above
        # or if it's about international affairs
        if any(loc in text for loc in ['reuters', 'afp', 'ap', 'associated press', 'bbc', 'cnn']):
            # Check if it's about multiple countries or global issues
            country_count = sum(1 for keyword in world_keywords if keyword in text)
            if country_count >= 2:
                return 'World'
        
        return 'World'  # Default to World for uncategorized

# Categorize articles
merged_2015['category'] = merged_2015.apply(
    lambda row: categorize_article(row['title'], row['description']), 
    axis=1
)

# Filter for World category
world_2015 = merged_2015[merged_2015['category'] == 'World']

# Count articles by region
region_counts = world_2015['region'].value_counts()

# Find region with most articles
if not region_counts.empty:
    top_region = region_counts.idxmax()
    top_count = region_counts.max()
    result = f"{top_region} ({top_count} articles)"
else:
    result = "No World category articles found in 2015"

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json'}

exec(code, env_args)
