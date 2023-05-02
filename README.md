# BoardGame Recommender test

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


We have separated these tasks into 3 phases, in accordance with the Project Updates:

### 1st phase:
- Questionnaire	
We want to make software that asks questions about the players' preferences and saves these answers for later use in the recommender system
 
- Detailed Database
Creating detailed database which focus on: name, description, mechanisms of the game, category, rating, playtime, number of players and theme.

- Recommender System
	- Depending on the player’s given preferences, our software should recommend the top 3 board games to play.

### 2nd phase:
- Optimizing
Check if all code is efficient and if there are enough comments 

- Summarizing
In its recommendation, the software should summarize what the game is about and why it recommended it.

### 3rd phase:
- Write the report 
- Create presentation slides & content


## Research Questions

Q1: Is it possible to find the best classification of board games based on these several parameters for each player?

Q2: If we use supervised learning, how can we find labeled data for the best choice of board game based on player preferences?

Q3: Using a detailed database, can we make a program that uses the answers from a questionnaire to determine which boardgame is best for a user? 

## Dataset

-  [https://www.kaggle.com/datasets/caesuric/bgggamesdata](https://www.kaggle.com/datasets/caesuric/bgggamesdata)


### Potential Guilds from BBG to Scrap user data

- 1206 users [https://boardgamegeek.com/guild/2246]

- 1233 users [https://boardgamegeek.com/guild/2198]

- 996 users [https://boardgamegeek.com/guild/1338]

## A Tentative List of Milestones for the Project

The roles we have not divided yet, as we are still all working together in looking for appropriate data and outlining our project. Our roles will be more fleshed out in the process. For the roles that we have divided so far, as seen through the tasks carried out by each of us in this first phase, see the 'Tasks' document.

- Extract information from [https://boardgamegeek.com](https://boardgamegeek.com/)
#### DONE

- Create database with focus on: name, description, mechanisms of the game, category, rating, playtime, number of players, theme, price
#### NEED: playtime, num. of players --> DONE

- Create questionnaire that users can fill in with their preferences on set parameters
#### NEED: make the software(?) that asks the questions and saves answers --> ALMOST DONE

- Create recommender system
#### NEED: hardcore TM classification problem --> SEE 'user_to_feature.py'

- Present results in a user-friendly way
#### NEED: again, make software(?) for user-friendly way

- Evaluation of recommender system
#### NEED: maybe by users? maybe automated based on user data on BGG?
