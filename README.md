# Steam Success Analysis: What Makes a Game Successful?
This project explores thousands of Steam games to identify the factors associated with commercial and player success. Through exploratory data analysis and an interactive dashboard, we investigate how pricing, genres, reviews, achievements, languages, and release dates relate to game performance.

Success is multidimensional. A game can sell well, retain players, or receive outstanding reviews. This project explores the factors associated with each dimension of success on Steam.

---
## Live Dashboard
https://steam-success-analysis.streamlit.app
---
## Project Goal

The objective of this project is to explore which game characteristics are associated with commercial success, player engagement, and player satisfaction on Steam.

The analysis focuses on three questions:

- What factors are associated with commercial success?
- What factors are associated with player engagement?
- What factors are associated with positive user reviews?

---
## Limitations

- Success is measured using estimated owners and not actual revenue.
- Observed relationships are correlational and should not be interpreted as causal.
- Steam metadata contains missing values and category inconsistencies that required preprocessing.
- User review scores were adjusted using a Bayesian weighted score to reduce the impact of games with very few reviews.

---
## Key findings
### Commercial Success
- RPG games show the highest success rates among major game genres, while Indie and Casual games are less likely to become commercial hits. This may reflect the larger budgets, longer development cycles, and stronger player retention commonly associated with RPG titles.

- Games priced between $20 and $40 exhibit the highest probability of becoming commercially successful on Steam. Very low-priced games are less likely to achieve top-selling status, likely due to the large volume of small indie releases in that segment. Conversely, games priced above $60 show lower success rates. Successful titles appear to balance accessibility and perceived production value.

- Supporting multiple languages is strongly associated with commercial success. Games available in 6–20 languages achieve substantially higher success rates than games supporting only one language. The relationship weakens for titles supporting more than 20 languages, suggesting that other factors may influence performance within this group.

### Player Engagement
- Genres such as RPG, Strategy, and Simulation tend to generate higher player engagement, measured through median playtime.
- Games with larger numbers of achievements are associated with longer playtimes. While this relationship is clear, it should not be interpreted as causal: larger and more content-rich games are also more likely to include extensive achievement systems.

### Player satisfaction
- Tags related to narrative and artistic experiences—such as Romance, Visual Novel, and Great Soundtrack—receive the highest user ratings on average.
- Competitive and multiplayer-focused tags—including Multiplayer, PvP, and Massively Multiplayer—receive lower ratings on average, possibly reflecting higher player expectations and greater exposure to balancing or technical issues.
- No meaningful relationship was found between playtime and review scores. Players do not necessarily rate a game more positively simply because they spend more time playing it.