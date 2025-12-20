code = """import json
import collections
import re

# Load metadata
meta_var = locals()['var_function-call-11571275440922023109']
with open(meta_var, 'r') as f:
    meta_list = json.load(f)

# Load articles
articles_var = locals()['var_function-call-13545390733052603041']
with open(articles_var, 'r') as f:
    articles_list = json.load(f)

# Map article_id to region
id_to_region = {}
for m in meta_list:
    aid = str(m['article_id'])
    id_to_region[aid] = m['region']

# Keywords
# Remove very short ones or be careful.
# "un" is dangerous if not exact word.
keywords = {
    "Sports": ["sport", "sports", "game", "match", "cup", "league", "team", "player", "coach", "score", "win", "won", "loss", "lost", "olympic", "nfl", "nba", "mlb", "nhl", "soccer", "football", "baseball", "basketball", "tennis", "golf", "racing", "medal", "champion", "tournament", "stadium", "athens", "sox", "yankees", "red sox", "doping", "athlete"],
    "Business": ["business", "market", "markets", "stock", "stocks", "trade", "economy", "fiscal", "fed", "bank", "banks", "profit", "earnings", "dollar", "euro", "yen", "oil", "price", "prices", "corp", "inc", "ltd", "company", "companies", "merger", "deal", "ceo", "invest", "investment", "dow", "nasdaq", "wall st", "revenue", "financial", "share", "shares", "imf", "growth", "job", "jobs", "money", "fund", "funds"],
    "Sci/Tech": ["science", "technology", "tech", "computer", "computers", "software", "hardware", "internet", "web", "online", "google", "microsoft", "apple", "space", "nasa", "biotech", "study", "research", "cancer", "virus", "health", "mobile", "phone", "chip", "server", "data", "biology", "physics", "astronomy", "drug", "drugs", "fda", "browser"],
    "World": ["world", "international", "war", "peace", "military", "army", "troop", "troops", "president", "minister", "government", "parliament", "senate", "election", "vote", "un", "united nations", "eu", "european union", "treaty", "nuclear", "bomb", "attack", "terror", "isis", "al qaeda", "syria", "iraq", "iran", "china", "russia", "korea", "afghanistan", "israel", "palestine", "ukraine", "protest", "crisis", "refugee", "diplomat", "foreign", "blast", "killed", "kill", "police", "security", "gaza", "baghdad", "cairo", "premier", "official", "officials", "strike", "hostage", "darfur", "sudan", "greece", "putin", "obama", "bush", "leader", "leaders", "talks", "sanction", "sanctions", "border"]
}

region_world_counts = collections.defaultdict(int)
total_matches = 0

# Pre-compile regexes for performance
regex_map = {}
for cat, kws in keywords.items():
    # Sort by length descending to match longer phrases first?
    # Regex alternation: \b(kw1|kw2|...)\b
    # Escape kws just in case
    pattern = r'\b(' + '|'.join(re.escape(k) for k in kws) + r')\b'
    regex_map[cat] = re.compile(pattern)

for art in articles_list:
    aid = str(art.get('article_id'))
    if aid in id_to_region:
        total_matches += 1
        title = art.get('title', '')
        desc = art.get('description', '')
        if title is None: title = ""
        if desc is None: desc = ""
        
        text = (title + " " + desc).lower()
        
        scores = {}
        for cat, regex in regex_map.items():
            # Count number of matches
            matches = regex.findall(text)
            scores[cat] = len(matches)
        
        if max(scores.values()) > 0:
            m = max(scores.values())
            best_cats = [c for c, s in scores.items() if s == m]
            
            # Tie breaker: Prefer World if present, else pick one
            # The prompt implies articles BELONG to a category.
            # In standard datasets (AG News):
            # 1: World, 2: Sports, 3: Business, 4: Sci/Tech
            
            # If tie between World and Business (e.g. "Oil prices in Iraq"), it's tricky.
            # Usually specific entities drive it.
            # Let's stick to simple priority: World > others.
            
            if "World" in best_cats:
                best_cat = "World"
            elif "Sports" in best_cats:
                best_cat = "Sports"
            elif "Business" in best_cats:
                best_cat = "Business"
            else:
                best_cat = best_cats[0]
            
            if best_cat == "World":
                region_world_counts[id_to_region[aid]] += 1

print("__RESULT__:")
print(json.dumps({"region_world_counts": region_world_counts, "processed": total_matches}))"""

env_args = {'var_function-call-11571275440922023109': 'file_storage/function-call-11571275440922023109.json', 'var_function-call-3574930073058179550': {'count': 6696, 'ids': ['13', '18', '26', '51', '52', '67', '70', '74', '86', '97']}, 'var_function-call-11051996893389232622': [{'_id': '69451246c36b2bdffa0eca9e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69451246c36b2bdffa0eca9f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69451246c36b2bdffa0ecaa0', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69451246c36b2bdffa0ecaa1', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69451246c36b2bdffa0ecaa2', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-14877180744595698851': {'region_counts': {}, 'debug': {'total_articles_2015': 6696, 'processed': 0, 'classified_world': 0}}, 'var_function-call-1451022451502767515': {'article_count_fetched': 5}, 'var_function-call-6334326690121328290': 'file_storage/function-call-6334326690121328290.json', 'var_function-call-1075493348490906335': {'region_counts': {'South America': 44, 'Asia': 43, 'North America': 45, 'Europe': 46, 'Africa': 51}, 'processed': 494, 'debug': [{'title': 'Delightful Dell', 'region': 'South America', 'scores': {'Sports': 0, 'Business': 1, 'Sci/Tech': 1, 'World': 1}}, {'title': 'IT Myth 5: Most IT projects fail', 'region': 'Asia', 'scores': {'Sports': 0, 'Business': 1, 'Sci/Tech': 0, 'World': 1}}, {'title': 'Oracle Sales Data Seen Being Released (Reuters)', 'region': 'Asia', 'scores': {'Sports': 0, 'Business': 3, 'Sci/Tech': 2, 'World': 3}}, {'title': "What's in a Name? Well, Matt Is Sexier Than Paul (Reuters)", 'region': 'North America', 'scores': {'Sports': 0, 'Business': 0, 'Sci/Tech': 0, 'World': 1}}, {'title': 'Indictments Using DNA on Rise Nationally (AP)', 'region': 'Asia', 'scores': {'Sports': 0, 'Business': 1, 'Sci/Tech': 0, 'World': 1}}, {'title': 'Reverse Psychology', 'region': 'Europe', 'scores': {'Sports': 0, 'Business': 0, 'Sci/Tech': 1, 'World': 1}}, {'title': "News: Climate Change Could Doom Alaska's Tundra", 'region': 'South America', 'scores': {'Sports': 1, 'Business': 0, 'Sci/Tech': 0, 'World': 2}}, {'title': 'News: Warmer Weather, Human Disturbances Interact to Change Forests', 'region': 'Europe', 'scores': {'Sports': 0, 'Business': 0, 'Sci/Tech': 0, 'World': 2}}, {'title': "Saturn's Moon Titan: Prebiotic Laboratory", 'region': 'Europe', 'scores': {'Sports': 0, 'Business': 0, 'Sci/Tech': 1, 'World': 1}}, {'title': 'Tools wrap: Sun, Javalobby, Infravio make moves', 'region': 'North America', 'scores': {'Sports': 0, 'Business': 0, 'Sci/Tech': 1, 'World': 2}}]}, 'var_function-call-4997264960781706308': {'min': 13, 'max': 127570, 'count': 6696}, 'var_function-call-11573342436693632203': [{'_id': '69451246c36b2bdffa0ecaab', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}], 'var_function-call-5429234915162844433': [{'_id': '69451246c36b2bdffa0ecaab', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'_id': '69451246c36b2bdffa0ecaac', 'article_id': '14', 'title': 'Dollar Falls Broadly on Record Trade Gap', 'description': " NEW YORK (Reuters) - The dollar tumbled broadly on Friday  after data showing a record U.S. trade deficit in June cast  fresh doubts on the economy's recovery and its ability to draw  foreign capital to fund the growing gap."}, {'_id': '69451246c36b2bdffa0ecaad', 'article_id': '15', 'title': 'Rescuing an Old Saver', 'description': "If you think you may need to help your elderly relatives with their finances, don't be shy about having the money talk -- soon."}, {'_id': '69451246c36b2bdffa0ecaae', 'article_id': '16', 'title': 'Kids Rule for Back-to-School', 'description': 'The purchasing power of kids is a big part of why the back-to-school season has become such a huge marketing phenomenon.'}, {'_id': '69451246c36b2bdffa0ecaaf', 'article_id': '17', 'title': 'In a Down Market, Head Toward Value Funds', 'description': "There is little cause for celebration in the stock market these days, but investors in value-focused mutual funds have reason to feel a bit smug -- if only because they've lost less than the folks who stuck with growth."}], 'var_function-call-13545390733052603041': 'file_storage/function-call-13545390733052603041.json', 'var_function-call-2758515178061073584': {'region_world_counts': {'South America': 714, 'Asia': 673, 'North America': 685, 'Europe': 705, 'Africa': 687}, 'processed': 6696}, 'var_function-call-7738927760703925047': {'samples': [{'title': 'Delightful Dell', 'scores': {'Sports': 0, 'Business': 1, 'Sci/Tech': 1, 'World': 1}}, {'title': "News: Climate Change Could Doom Alaska's Tundra", 'scores': {'Sports': 1, 'Business': 0, 'Sci/Tech': 0, 'World': 2}}, {'title': 'Ex-colleague backs Scrafton on PM #39;s call', 'scores': {'Sports': 1, 'Business': 0, 'Sci/Tech': 1, 'World': 1}}, {'title': 'Karzai likely to visit Pakistan next week', 'scores': {'Sports': 0, 'Business': 0, 'Sci/Tech': 0, 'World': 1}}, {'title': 'Rockies Pitcher Frets Health, Not Baseball (AP)', 'scores': {'Sports': 1, 'Business': 0, 'Sci/Tech': 1, 'World': 1}}]}}

exec(code, env_args)
