code = """import json
import re

# Load metadata
# Key: var_function-call-15200062645534143946
# This contains the list of {article_id, year}
path_meta = locals()['var_function-call-15200062645534143946']
with open(path_meta, 'r') as f:
    meta_list = json.load(f)

# Create a lookup map
# Ensure article_id is string for matching
meta_map = {str(item['article_id']): item['year'] for item in meta_list}

# Load articles
# Key: var_function-call-16298070203329204653
path_articles = locals()['var_function-call-16298070203329204653']
with open(path_articles, 'r') as f:
    articles_list = json.load(f)

# Define Keywords
# Heuristic approach based on common words in the preview and domain knowledge
business_keywords = {
    'business', 'market', 'stock', 'economy', 'economic', 'finance', 'financial', 
    'investor', 'investment', 'invest', 'profit', 'revenue', 'loss', 'share', 'shares', 
    'bank', 'banking', 'trade', 'trading', 'dollar', 'euro', 'currency', 'rate', 
    'inflation', 'fed', 'federal reserve', 'treasury', 'bond', 'deficit', 'budget', 
    'recession', 'gdp', 'ceo', 'merger', 'acquisition', 'ipo', 'dow', 'nasdaq', 
    'oil price', 'crude', 'wall street', 'company', 'corp', 'corporate', 'job', 'jobs', 
    'tax', 'sales', 'retail', 'price', 'prices', 'money', 'cost', 'funds', 'growth'
}

tech_keywords = {
    'technology', 'tech', 'computer', 'software', 'hardware', 'internet', 'web', 'online', 
    'google', 'microsoft', 'apple', 'intel', 'linux', 'windows', 'chip', 'phone', 
    'mobile', 'wireless', 'network', 'broadband', 'server', 'virus', 'hacker', 
    'space', 'nasa', 'astronomy', 'science', 'scientist', 'research', 'lab', 'drug', 
    'medical', 'game', 'video game', 'robot', 'digital'
}
# Note: 'game' is in tech (video games) and sports. 

sports_keywords = {
    'sport', 'sports', 'game', 'team', 'player', 'coach', 'win', 'won', 'lose', 'lost', 
    'score', 'match', 'cup', 'olympic', 'medal', 'championship', 'champion', 'league', 
    'tournament', 'football', 'baseball', 'basketball', 'soccer', 'tennis', 'golf', 
    'hockey', 'cricket', 'rugby', 'racing', 'driver', 'athlete', 'stadium'
}

world_keywords = {
    'world', 'international', 'war', 'peace', 'military', 'army', 'troops', 'attack', 
    'bomb', 'blast', 'kill', 'killed', 'president', 'minister', 'prime minister', 
    'government', 'parliament', 'election', 'vote', 'politics', 'political', 'party', 
    'official', 'leader', 'foreign', 'un', 'united nations', 'treaty', 'border', 
    'security', 'police', 'court', 'judge', 'law', 'legal', 'iraq', 'iran', 'palestinian', 
    'israel', 'afghanistan', 'china', 'russia', 'eu', 'european union'
}

def classify(title, desc):
    text = (title + " " + desc).lower()
    # Tokenize simply
    words = set(re.findall(r'\w+', text))
    
    # Count matches
    # Simple set intersection might miss phrases like "wall street", so iterating is safer for phrases if needed.
    # But for single words set intersection is fast.
    # Let's handle phrases separately or just stick to single words?
    # "Wall St." -> "wall", "st"
    # "Wall Street" -> "wall", "street"
    # Added "wall" and "street" individually? "street" is common. "wall" is common.
    # Let's check for phrases in text string, and words in word set.
    
    score_biz = 0
    score_tech = 0
    score_sport = 0
    score_world = 0
    
    # Check phrases
    if 'wall street' in text or 'wall st' in text: score_biz += 5
    if 'federal reserve' in text: score_biz += 5
    if 'united nations' in text: score_world += 5
    
    # Check words
    score_biz += len(words.intersection(business_keywords))
    score_tech += len(words.intersection(tech_keywords))
    score_sport += len(words.intersection(sports_keywords))
    score_world += len(words.intersection(world_keywords))
    
    # Conflict resolution
    # "Oil prices" -> "oil" (biz?), "prices" (biz). 
    # "Google IPO" -> "google" (tech), "ipo" (biz).
    # "Google" is very tech. "IPO" is very biz.
    # Maybe weight some words?
    
    # If "game" and "team" -> Sports
    # If "game" and "software" -> Tech
    
    scores = {'Business': score_biz, 'Sci/Tech': score_tech, 'Sports': score_sport, 'World': score_world}
    
    # Find max
    max_cat = max(scores, key=scores.get)
    if scores[max_cat] == 0:
        return 'Unknown' # or default?
    
    # Tie breaking
    # If Business and World tie? (e.g. Oil price in Iraq)
    # The question is specifically about "Business articles". 
    # Usually datasets like AG News have distinct categories.
    # Let's prioritize Business if close?
    # Or just stick to max.
    
    return max_cat

# Process
counts_per_year = {str(y): 0 for y in range(2010, 2021)}

business_article_count = 0
processed_count = 0

for article in articles_list:
    aid = str(article.get('article_id'))
    if aid in meta_map:
        year = meta_map[aid]
        if year in counts_per_year: # check range 2010-2020 just in case
            cat = classify(article.get('title', ''), article.get('description', ''))
            if cat == 'Business':
                counts_per_year[year] += 1
                business_article_count += 1
        processed_count += 1

# Calculate average
years = range(2010, 2021)
total_years = len(years)
total_business = sum(counts_per_year[str(y)] for y in years)
average = total_business / total_years

print(f"Processed: {processed_count}")
print(f"Business Articles: {business_article_count}")
print(f"Counts per year: {counts_per_year}")
print("__RESULT__:")
print(json.dumps(average))"""

env_args = {'var_function-call-15200062645534143946': 'file_storage/function-call-15200062645534143946.json', 'var_function-call-11441645720328395150': 'file_storage/function-call-11441645720328395150.json', 'var_function-call-15752402694126459352': 14860, 'var_function-call-15388242534425523559': [{'_id': '6944e7128e7b436dadc1534d', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944e7128e7b436dadc1534e', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944e7128e7b436dadc1534f', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944e7128e7b436dadc15350', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944e7128e7b436dadc15351', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-4349881094402028571': 127583, 'var_function-call-16298070203329204653': 'file_storage/function-call-16298070203329204653.json'}

exec(code, env_args)
