code = """import json
import pandas as pd
import re

# Load metadata
with open(locals()['var_function-call-3160904242471063353'], 'r') as f:
    metadata_list = json.load(f)

# Load articles
with open(locals()['var_function-call-2834752330008738481'], 'r') as f:
    articles_list = json.load(f)

# Convert to DF
df_meta = pd.DataFrame(metadata_list)
df_arts = pd.DataFrame(articles_list)

# Ensure article_id is same type (int or str). Metadata had int in preview (check json load), articles had str "0".
# In previous tool output: metadata IDs in JSON were "3", "9" (strings) or numbers?
# Let's check the preview of metadata again.
# Preview: [{"article_id": "3", "publication_date": "2020-03-04"} ...]
# So metadata article_id is string.
# Articles article_id is string "0", "1"...
# So join should work on string.

df_merged = pd.merge(df_meta, df_arts, on='article_id', how='inner')

# Extract year
df_merged['year'] = pd.to_datetime(df_merged['publication_date']).dt.year

# Define keywords
# Business: economy, market, stock, trade, financial, business, bank, investor, profit, oil, dollar, euro, inflation, rate, price, ceo, deal, sales, growth
# Sports: sport, game, team, cup, player, win, loss, match, season, league, coach, olympic
# Sci/Tech: technology, science, computer, web, internet, software, space, study, research, new, device
# World: war, government, president, minister, country, police, attack, world, peace, election

# Note: "oil" is business usually. "win" is sports.
# I will use a simple scoring.

def classify(row):
    text = (str(row['title']) + " " + str(row['description'])).lower()
    
    keywords = {
        'Business': ['business', 'economy', 'economic', 'market', 'stock', 'share', 'trade', 'financial', 'finance', 'bank', 'invest', 'profit', 'money', 'dollar', 'euro', 'oil', 'price', 'rate', 'inflation', 'growth', 'deal', 'sale', 'ceo', 'company', 'corp', 'tax', 'fund'],
        'Sports': ['sport', 'game', 'team', 'match', 'cup', 'player', 'score', 'win', 'lose', 'league', 'championship', 'olympic', 'football', 'soccer', 'basketball', 'baseball', 'coach', 'season', 'medal'],
        'Sci/Tech': ['science', 'technology', 'tech', 'computer', 'software', 'internet', 'web', 'online', 'space', 'nasa', 'research', 'study', 'device', 'app', 'mobile', 'digital', 'network', 'virus', 'biology', 'physics'],
        'World': ['world', 'war', 'peace', 'politic', 'government', 'president', 'minister', 'election', 'vote', 'country', 'nation', 'attack', 'bomb', 'military', 'army', 'police', 'protest', 'un', 'treaty', 'law', 'court']
    }
    
    scores = {cat: 0 for cat in keywords}
    
    for cat, words in keywords.items():
        for w in words:
            if w in text:
                scores[cat] += 1
    
    # Get max score
    max_cat = max(scores, key=scores.get)
    if scores[max_cat] == 0:
        return 'World' # Default or Unknown
    return max_cat

df_merged['category'] = df_merged.apply(classify, axis=1)

# Filter for Business
business_arts = df_merged[df_merged['category'] == 'Business']

# Group by year
counts = business_arts.groupby('year').size()

# Years 2010 to 2020
years = range(2010, 2021)
# Ensure all years are present (fill 0 if missing)
counts = counts.reindex(years, fill_value=0)

average = counts.mean()

print("__RESULT__:")
print(json.dumps({
    "counts_by_year": counts.to_dict(),
    "average": average,
    "total_filtered_articles": len(df_merged),
    "business_articles_count": len(business_arts)
}))"""

env_args = {'var_function-call-3160904242471063353': 'file_storage/function-call-3160904242471063353.json', 'var_function-call-12368714050560337210': 'file_storage/function-call-12368714050560337210.json', 'var_function-call-12354598108839559361': 14860, 'var_function-call-13777281243144311029': [{'_id': '6944d5f310c69487e5042374', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944d5f310c69487e5042375', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944d5f310c69487e5042376', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944d5f310c69487e5042377', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944d5f310c69487e5042378', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-14363583995400240936': {'length': 5}, 'var_function-call-2834752330008738481': 'file_storage/function-call-2834752330008738481.json'}

exec(code, env_args)
