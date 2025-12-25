code = """import pandas as pd
import json

# Load article_metadata for 2015 from the file
with open(locals()['var_function-call-8800878086019593703'], 'r') as f:
    article_metadata_2015 = json.load(f)

# articles_data is already a list of dictionaries, not a file path
articles_data = locals()['var_function-call-17844915051056866953']

# Create DataFrames
df_metadata_2015 = pd.DataFrame(article_metadata_2015)
df_articles = pd.DataFrame(articles_data)

# Convert 'article_id' columns to string type for consistent merging
df_metadata_2015['article_id'] = df_metadata_2015['article_id'].astype(str)
df_articles['article_id'] = df_articles['article_id'].astype(str)

# Perform an inner merge to combine metadata with article content for 2015 articles
df_categorize = pd.merge(df_metadata_2015, df_articles, on='article_id', how='inner')

# If no articles remain after merging, return an appropriate message
if df_categorize.empty:
    result = "No articles found for 2015 after merging metadata and article content."
    print("__RESULT__:")
    print(json.dumps(result))
else:
    # Define comprehensive keywords for categories (case-insensitive)
    sports_keywords = ['sport', 'team', 'game', 'match', 'league', 'cup', 'championship', 'athlete', 'coach', 'player', 'score', 'win', 'lose', 'olympic', 'football', 'basketball', 'baseball', 'soccer', 'tennis', 'golf', 'season', 'final', 'medal', 'record', 'arena', 'stadium', 'fan', 'rival', 'champion', 'tournament', 'race', 'sportsman', 'sportswoman', 'pitch', 'court', 'field', 'goal', 'point', 'referee', 'umpire', 'trophy', 'playoffs']
    business_keywords = ['business', 'market', 'economy', 'company', 'firm', 'stock', 'invest', 'finance', 'profit', 'earn', 'trade', 'deal', 'merger', 'acquisition', 'ceo', 'bank', 'industry', 'economic', 'financial', 'corporate', 'share', 'bond', 'dividend', 'revenue', 'cost', 'growth', 'startup', 'entrepreneur', 'venture', 'capital', 'recession', 'inflation', 'jobs', 'employment', 'globalization', 'stock exchange', 'commodities', 'currency', 'interest rate', 'debt', 'fund', 'management', 'strategy', 'tax', 'regulation', 'profitability', 'forecast', 'outlook', 'report']
    science_tech_keywords = ['science', 'technology', 'tech', 'research', 'study', 'discover', 'invent', 'develop', 'digital', 'internet', 'software', 'hardware', 'computer', 'phone', 'space', 'medical', 'health', 'robot', 'ai', 'data', 'network', 'cyber', 'bio', 'genetic', 'universe', 'planet', 'experiment', 'innovation', 'engineering', 'scientist', 'engineer', 'biotech', 'nanotech', 'quantum', 'astronomy', 'physics', 'chemistry', 'biology', 'medicine', 'algorithm', 'app', 'platform', 'device', 'gadget', 'virtual', 'augmented', 'crypto', 'blockchain']

    def categorize_article_final(title, description):
        title_str = str(title) if title is not None else ""
        description_str = str(description) if description is not None else ""
        text = (title_str + ' ' + description_str).lower()

        if any(keyword in text for keyword in sports_keywords):
            return 'Sports'
        elif any(keyword in text for keyword in business_keywords):
            return 'Business'
        elif any(keyword in text for keyword in science_tech_keywords):
            return 'Science/Technology'
        else:
            return 'World' # Default to World if no other category matches

    # Apply the categorization function to create a new 'category' column
    df_categorize['category'] = df_categorize.apply(lambda row: categorize_article_final(row['title'], row['description']), axis=1)

    # Filter for 'World' category articles
    world_articles = df_categorize[df_categorize['category'] == 'World']

    # Check if there are any 'World' articles
    if world_articles.empty:
        result = "No 'World' category articles found for 2015 based on the categorization logic."
    else:
        # Count articles per region for 'World' category
        region_counts = world_articles['region'].value_counts().reset_index()
        region_counts.columns = ['region', 'article_count']

        # Find the region with the largest number of articles
        if not region_counts.empty:
            largest_region = region_counts.loc[region_counts['article_count'].idxmax()]
            result = largest_region['region']
        else:
            result = "No 'World' category articles found for 2015 based on the categorization logic."

    print("__RESULT__:")
    print(json.dumps(result))"""

env_args = {'var_function-call-4142005257738235693': 'file_storage/function-call-4142005257738235693.json', 'var_function-call-10407798788679954601': 'file_storage/function-call-10407798788679954601.json', 'var_function-call-10122244090567098285': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-14299870682571490829': "No 'World' category articles found for 2015.", 'var_function-call-8077269091591802355': "No 'World' category articles found for 2015.", 'var_function-call-14084660972261546348': "No 'World' category articles found for 2015.", 'var_function-call-414973047835796734': {'category_distribution': {}, 'largest_world_region': "No 'World' category articles found for 2015 based on the current categorization logic."}, 'var_function-call-14497284248624298721': {'category_distribution': {}, 'largest_world_region': "No 'World' category articles found for 2015 based on the current categorization logic."}, 'var_function-call-12422755852677945469': {'category_distribution': {}, 'largest_world_region': 'No articles found for 2015 after merging metadata and article content.'}, 'var_function-call-17094805444415060670': {'category_distribution': {}, 'largest_world_region': 'No articles found for 2015 after merging metadata and article content.'}, 'var_function-call-6530078997115481032': 'No articles found for 2015 after merging metadata and article content.', 'var_function-call-8800878086019593703': 'file_storage/function-call-8800878086019593703.json', 'var_function-call-17844915051056866953': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-10068210157425533868': 'No articles found for 2015 after merging metadata and article content.', 'var_function-call-14619298643565278279': 'No articles found for 2015 after merging metadata and article content. This could indicate an issue with article_id types or data availability.', 'var_function-call-6698322969342098020': [{'article_id': '0'}, {'article_id': '1'}, {'article_id': '2'}, {'article_id': '3'}, {'article_id': '4'}]}

exec(code, env_args)
