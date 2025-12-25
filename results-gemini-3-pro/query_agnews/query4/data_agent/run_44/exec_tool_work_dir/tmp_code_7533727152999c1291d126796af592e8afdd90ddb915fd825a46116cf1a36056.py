code = """# Re-run the classification and collect top words for verification
import json
import re
from collections import Counter

with open(locals()['var_function-call-1914971640396700157'], 'r') as f:
    meta_list = json.load(f)

with open(locals()['var_function-call-13503504558976548684'], 'r') as f:
    articles_list = json.load(f)

meta_map = {str(item['article_id']): item['region'] for item in meta_list}

# Keywords (Same as before)
world_keywords = {
    "iraq", "iraqi", "baghdad", "iran", "tehran", "nuclear", "palestinian", "gaza", "israel", "jerusalem",
    "peace", "troops", "forces", "military", "army", "war", "rebel", "insurgent", "attack", "kill", "dead", "blast", "bomb", "suicide",
    "president", "minister", "prime", "official", "leader", "government", "parliament", "senate", "election", "vote", "poll",
    "darfur", "sudan", "africa", "chavez", "venezuela", "russia", "putin", "china", "beijing", "korea", "afghanistan", "kabul",
    "un", "united nations", "nato", "eu", "european", "treaty", "sanction", "diplomat", "envoy", "talks", "meeting", "summit",
    "hostage", "kidnap", "terror", "qaeda", "bin laden", "militant", "clash", "violence", "security", "police", "court", "trial", "judge",
    "hurricane", "storm", "typhoon", "tsunami", "earthquake", "disaster", "relief", "aid", "crash", "plane", "zimbabwe", "pakistan", "musharraf", "arafat", "sharon", "bush", "kerry"
}
# ... (Other keywords are used but I only need World logic validation)
# I will copy the scoring logic exactly.

sports_keywords = {
    "sport", "sports", "game", "match", "cup", "league", "tournament", "championship", "champion", "title",
    "win", "won", "winner", "victory", "loss", "lost", "defeat", "beat", "score", "result", "standings",
    "team", "squad", "club", "coach", "manager", "player", "athlete", "medal", "olympic", "athens", "gold", "silver", "bronze",
    "football", "soccer", "basketball", "nba", "baseball", "mlb", "red sox", "yankees", "hockey", "nhl", "tennis", "golf", "tiger woods",
    "racing", "f1", "formula one", "schumacher", "ferrari", "cricket", "rugby", "boxing", "nfl", "super bowl", "quarterback"
}

business_keywords = {
    "business", "company", "companies", "firm", "corp", "corporation", "inc", "ltd", "industry", "sector",
    "market", "stock", "share", "wall st", "dow", "nasdaq", "s&p", "index", "price", "rate", "value",
    "economy", "economic", "growth", "inflation", "recession", "deficit", "budget", "finance", "financial", "bank", "banking",
    "profit", "loss", "earnings", "quarter", "revenue", "sales", "deal", "merger", "acquisition", "bid", "buy", "sell",
    "invest", "investor", "investment", "fund", "dollar", "euro", "yen", "currency", "oil", "crude", "barrel", "energy", "gas",
    "airline", "airways", "boeing", "airbus", "delta", "fed", "greenspan", "wto", "imf", "job", "unemployment", "labor", "strike"
}

tech_keywords = {
    "technology", "tech", "science", "scientific", "research", "study", "discovery", "new", "innovation",
    "computer", "software", "hardware", "internet", "web", "online", "net", "cyber", "digital",
    "google", "yahoo", "microsoft", "windows", "linux", "apple", "ipod", "mac", "ibm", "intel", "amd", "oracle", "cisco",
    "mobile", "phone", "wireless", "cell", "network", "broadband", "telecom", "nokia", "motorola",
    "space", "nasa", "shuttle", "mission", "launch", "orbit", "mars", "moon", "saturn", "cassini", "astronomy", "universe",
    "virus", "worm", "spam", "security", "hacker", "patch", "browser", "search", "engine", "blog",
    "game", "video game", "sony", "nintendo", "xbox", "playstation", "doom", "halo"
}

region_words = {"North America": [], "Africa": []}

for article in articles_list:
    aid = str(article.get('article_id', ''))
    if aid in meta_map:
        text = (article.get('title', '') + " " + article.get('description', '')).lower()
        words = list(re.findall(r'\w+', text)) # Keep duplicates for frequency
        words_set = set(words)
        
        scores = {
            'World': sum(1 for w in words_set if w in world_keywords),
            'Sports': sum(1 for w in words_set if w in sports_keywords),
            'Business': sum(1 for w in words_set if w in business_keywords),
            'Tech': sum(1 for w in words_set if w in tech_keywords)
        }
        
        if scores['World'] == 0 and scores['Sports'] == 0 and scores['Business'] == 0 and scores['Tech'] == 0:
            continue

        best_cat = max(scores, key=scores.get)
        
        if scores['World'] == scores['Business'] and scores['World'] > 0:
            if "iraq" in words_set or "war" in words_set or "president" in words_set:
                best_cat = 'World'
            elif "oil" in words_set or "price" in words_set or "market" in words_set:
                best_cat = 'Business'
        
        if best_cat == 'World':
            region = meta_map[aid]
            if region in region_words:
                region_words[region].extend(words)

# Analyze top words
top_words = {}
for reg in region_words:
    c = Counter(region_words[reg])
    # Filter stopwords roughly
    stopwords = {"the", "a", "an", "to", "in", "of", "and", "for", "on", "with", "at", "by", "from", "as", "is", "said", "has", "that", "it", "its", "are", "was", "will", "be", "have", "us", "reuters", "ap", "afp", "new", "york", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"}
    top_words[reg] = [w for w, count in c.most_common(50) if w not in stopwords]

print("__RESULT__:")
print(json.dumps(top_words))"""

env_args = {'var_function-call-1914971640396700157': 'file_storage/function-call-1914971640396700157.json', 'var_function-call-10479132233513005664': 6696, 'var_function-call-8989729352298864404': [{'_id': '6945236d71e5a520afd3711f', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6945236d71e5a520afd37120', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6945236d71e5a520afd37121', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6945236d71e5a520afd37122', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6945236d71e5a520afd37123', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-17645446409733323876': [{'_id': '6945236d71e5a520afd3711f', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6945236d71e5a520afd37120', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6945236d71e5a520afd37121', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6945236d71e5a520afd37122', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6945236d71e5a520afd37123', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-7763971529073008408': [], 'var_function-call-306862715966043572': [{'_id': '6945236d71e5a520afd3712c', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'_id': '6945236d71e5a520afd37131', 'article_id': '18', 'title': 'US trade deficit swells in June', 'description': 'The US trade deficit has exploded 19 to a record \\$55.8bn as oil costs drove imports higher, according to a latest figures.'}, {'_id': '6945236d71e5a520afd37139', 'article_id': '26', 'title': 'Google auction begins on Friday', 'description': 'An auction of shares in Google, the web search engine which could be floated for as much as \\$36bn, takes place on Friday.'}], 'var_function-call-9887750109441631916': 5, 'var_function-call-13503504558976548684': 'file_storage/function-call-13503504558976548684.json', 'var_function-call-17053250052862343729': {'region_counts': {'Europe': 374, 'Asia': 381, 'North America': 393, 'Africa': 393, 'South America': 388}, 'max_region': 'North America', 'matched_articles': 6696}}

exec(code, env_args)
