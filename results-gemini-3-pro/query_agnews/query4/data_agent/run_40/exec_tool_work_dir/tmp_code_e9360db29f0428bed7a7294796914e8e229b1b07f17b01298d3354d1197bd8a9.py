code = """import json
import collections
import re

# File paths
metadata_path = locals()['var_function-call-842491368832431950']
articles_path = locals()['var_function-call-166910293649011894']

# 1. Load Metadata
with open(metadata_path, 'r') as f:
    metadata_list = json.load(f)

id_to_region = {str(m['article_id']): m['region'] for m in metadata_list}

# 2. Load Articles
with open(articles_path, 'r') as f:
    articles_list = json.load(f)

keywords_world = set(["politics", "minister", "parliament", "congress", "senate", "president", "premier", "governor", "election", "vote", "campaign", "party", "war", "military", "army", "navy", "troop", "soldier", "rebel", "terror", "bomb", "attack", "kill", "dead", "peace", "treaty", "talks", "diplomat", "foreign", "international", "un", "police", "court", "judge", "prison", "arrest", "crime", "murder", "protest", "strike", "refugee", "migrant", "border", "disaster", "earthquake", "tsunami", "hurricane", "flood", "crash", "virus", "flu", "health", "hospital", "school", "religion", "pope", "church", "islam", "muslim", "israel", "palestine", "iraq", "syria", "iran", "afghanistan", "china", "russia", "ukraine", "africa", "asia", "europe", "government", "official", "security", "crisis"])

keywords_business = set(["business", "company", "firm", "market", "stock", "share", "bond", "fund", "exchange", "economy", "finance", "bank", "fed", "rate", "inflation", "tax", "budget", "debt", "profit", "loss", "revenue", "sales", "trade", "deal", "merger", "acquisition", "price", "cost", "industry", "production", "oil", "gas", "energy", "gold", "dollar", "euro", "currency", "manager", "ceo", "job", "employment", "investor", "corp", "inc"])

keywords_sports = set(["sport", "game", "match", "team", "club", "player", "coach", "league", "cup", "tournament", "championship", "season", "final", "olympic", "score", "win", "loss", "victory", "goal", "run", "point", "stadium", "football", "soccer", "baseball", "basketball", "tennis", "golf", "cricket", "rugby", "hockey", "racing", "driver", "athlete"])

keywords_scitech = set(["technology", "tech", "science", "research", "computer", "software", "hardware", "app", "internet", "web", "online", "digital", "data", "mobile", "phone", "device", "robot", "ai", "space", "nasa", "satellite", "planet", "mars", "biology", "medical", "cancer", "google", "apple", "microsoft", "amazon", "facebook"])

def classify(title, desc):
    text = (title + " " + desc).lower()
    tokens = set(re.findall(r'\b\w+\b', text))
    
    score_world = len(tokens.intersection(keywords_world))
    score_business = len(tokens.intersection(keywords_business))
    score_sports = len(tokens.intersection(keywords_sports))
    score_scitech = len(tokens.intersection(keywords_scitech))
    
    scores = {
        "World": score_world,
        "Business": score_business,
        "Sports": score_sports,
        "Sci/Tech": score_scitech
    }
    
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0:
        return "Unknown", scores
    
    return best_cat, scores

# Test on sample
sample_title = "Google IPO Auction Off to Rocky Start"
sample_desc = "WASHINGTON/NEW YORK (Reuters) - The auction for Google Inc.'s highly anticipated initial public offering got off to a rocky start on Friday after the Web search company sidestepped a bullet from U.S. securities regulators."
cat, sc = classify(sample_title, sample_desc)
print(f"Sample Classification: {cat}, Scores: {sc}")

# Process
world_counts = collections.defaultdict(int)
cat_counts = collections.defaultdict(int)

for article in articles_list:
    aid = str(article['article_id'])
    if aid in id_to_region:
        cat, _ = classify(article.get('title', ''), article.get('description', ''))
        cat_counts[cat] += 1
        if cat == "World":
            region = id_to_region[aid]
            world_counts[region] += 1

print("Categories distribution:", dict(cat_counts))
print("World counts per region:", dict(world_counts))

if world_counts:
    max_region = max(world_counts, key=world_counts.get)
    print("__RESULT__:")
    print(json.dumps(max_region))
else:
    print("__RESULT__:")
    print(json.dumps("None"))"""

env_args = {'var_function-call-4885082808569749260': ['articles'], 'var_function-call-4885082808569747599': ['authors', 'article_metadata'], 'var_function-call-842491368832431950': 'file_storage/function-call-842491368832431950.json', 'var_function-call-842491368832431283': [{'_id': '69451cdaa3c653854d72a5f8', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69451cdaa3c653854d72a5f9', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69451cdaa3c653854d72a5fa', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69451cdaa3c653854d72a5fb', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69451cdaa3c653854d72a5fc', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-12270661439186357136': [{'_id': '69451cdaa3c653854d72a5f8', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69451cdaa3c653854d72a5f9', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69451cdaa3c653854d72a5fa', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69451cdaa3c653854d72a5fb', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69451cdaa3c653854d72a5fc', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-11107782028933462935': 6696, 'var_function-call-10443133168677105019': [{'_id': '69451cdaa3c653854d72a5f8', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69451cdaa3c653854d72a5f9', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69451cdaa3c653854d72a5fa', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69451cdaa3c653854d72a5fb', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69451cdaa3c653854d72a5fc', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-17213121137072458530': 'file_storage/function-call-17213121137072458530.json', 'var_function-call-1101150218082979582': {'max_region': None, 'count': 0, 'all_counts': {}}, 'var_function-call-14123822608347364619': {'meta_min': 13, 'meta_max': 127570, 'meta_count': 6696, 'art_min': 0, 'art_max': 99999, 'art_count': 100000, 'overlap': 5226}, 'var_function-call-166910293649011894': 'file_storage/function-call-166910293649011894.json', 'var_function-call-2953742791111605046': {'max_region': None, 'count': 0, 'all_counts': {}, 'cat_distribution': {'Unknown': 6696}}, 'var_function-call-12237246522851841748': {'_id': '69451cdaa3c653854d72a605', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}}

exec(code, env_args)
