# BoardGame Recommender

## Abstract
Our project consists of 4 parts:

- Survey Software 	
	- We want to make software that asks questions about the players' preferences and saves these answers for later use in the recommender system
 
- Creating a Detailed Database

	 - Creating detailed database which focus on: name, description, mechanisms of the game, category, rating, playtime, number of players, theme, price.

- Recommender System

	- Depending on the player’s given preferences, our software should recommend the top 3 board games to play.
- Summarizing

	- In its recommendation, the software should summarize what the game is about and why it recommended it.


## Research Questions

Q1: Is it possible to find the best classification of board games based on these several parameters for each player?

Q2: If we use supervised learning, how can we find labeled data for the best choice of board game based on player preferences?

## Dataset
Possible Datasets:

- [https://www.kaggle.com/datasets/jvanelteren/boardgamegeek-reviews](https://www.kaggle.com/datasets/jvanelteren/boardgamegeek-reviews)

-  [https://www.kaggle.com/datasets/bananalee67/board-games-dataset](https://www.kaggle.com/datasets/bananalee67/board-games-dataset)

-   [https://www.kaggle.com/datasets/kevinparks/board-game-geek-top-2000](https://www.kaggle.com/datasets/kevinparks/board-game-geek-top-2000)

-  [https://www.kaggle.com/datasets/dannykho/boardgames-clean](https://www.kaggle.com/datasets/dannykho/boardgames-clean)

- [https://www.kaggle.com/datasets/jingking/boardgaming-online-processed-game-records](https://www.kaggle.com/datasets/jingking/boardgaming-online-processed-game-records)

-  [https://www.kaggle.com/datasets/caesuric/bgggamesdata](https://www.kaggle.com/datasets/caesuric/bgggamesdata)

- [https://www.kaggle.com/datasets/medaxone/boardgamegeek-top100](https://www.kaggle.com/datasets/medaxone/boardgamegeek-top100)

-  [https://www.kaggle.com/datasets/extralime/20000-boardgames-dataset](https://www.kaggle.com/datasets/extralime/20000-boardgames-dataset)

- [https://www.kaggle.com/datasets/threnjen/board-games-database-from-boardgamegeek](https://www.kaggle.com/datasets/threnjen/board-games-database-from-boardgamegeek)

### Potential Guilds from BBG to Scrap user data

- 1206 users [https://boardgamegeek.com/guild/2246]

- 1233 users [https://boardgamegeek.com/guild/2198]

- 996 users [https://boardgamegeek.com/guild/1338]

## A Tentative List of Milestones for the Project

The roles we have not divided yet, as we are still all working together in looking for appropriate data and outlining our project. Our roles will be more fleshed out in the process.

- Extract information from [https://boardgamegeek.com](https://boardgamegeek.com/)
#### DONE

- Create database with focus on: name, description, mechanisms of the game, category, rating, playtime, number of players, theme, price
#### NEED: playtime, num. of players

- Create questionnaire that users can fill in with their preferences on set parameters
#### NEED: make the software(?) that asks the questions and saves answers

- Create recommender system
#### NEED: hardcore TM classification problem

- Present results in a user-friendly way
#### NEED: again, make software(?) for user-friendly way

- Evaluation of recommender system
#### NEED: maybe by users? maybe automated based on user data on BGG?
