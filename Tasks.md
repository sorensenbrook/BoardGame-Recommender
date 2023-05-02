# Tasks

## DATASET 
- Combine different datasets to create dataset with all necessary information
- Determine which information is needed
- Summarize which different datasets combined contain all info
- Download different datasets
- Extract needed info from the different datasets
- Create new dataset containing all info

## QUESTIONNAIRE

Basis: Create questionnaire which extracts player preferences
- Determine which preferences we need for the recommender system
- Come up with user friendly question which extract this needed info
- Program a function which asks question to the user in a user-friendly way and saves the answers 
- Program a function for which the input is the answers of the questionnaire and puts out the preferences we need 

Advanced: Open questions and use model to interpret the players answers 
- Alter the function which takes in the answers and outputs the preferences. It should now contain a language modelling part where the answers of the user are interpret and linked to the most likely / best matching preference

More complex: Create user friendly interface to ask player about its preferences 
- Alter the function which asks questions and saves the answer. It should be asked in a more user friendly way using interface- which is easy to use

## RECOMMENDER 
- Depending on the given players preferences, recommend a few boardgames
- Find a way to search through dataset in a quick way (not looping through it)
- Match different aspects of preferences to the boardgames in the dataset
- Find a way to determine what to recommend if different games match different preferences  
- Determine top 3 recommendations


## SUMMARY 
A small story about the recommended games. Why is it recommended and what is the game about (description)?

- Present the 3 recommendations in a user friendly way
- Present the description of the game to the user
- Explain why the 3 games where chosen and which game best match which preferences

-------------------------------------------------------------------------------------------------------------------------------------------------------
## OPTIMIZING
- Check if code is complete
- Check if comments explain the code enough
- Check if anything can be made more efficient

## EVALUTATION
- A/B testing
- Small survey to ask if people like their recommendation
- Different method / dataset testing 
- Determine which evaluation method could work the best for our project
- Make a plan on how the chosen evaluation method should work
- Program the method 
  
-------------------------------------------------------------------------------------------------------------------------------------------------------
## WRITE REPORT
- Abstract
- Author contributions and division of tasks
- Background (goal of the project) / introduction
- Quality of specific research question
	
- Method and data
    -	Does the described approach address the research question?
    -	Are details provided about dataset(s), method(s) and libraries used?
    -	Is there enough info so that someone can reproduce the results?
    -	Is the valuation effective?
	      
- Result and result analyzing 
- Conclusions
- Original contribution (are there sources which do a similar thing? Do you address a research gap?)
- Clarity of expression
- Figures, graphs, tables 
- Supplementary materials (does your report refer to repository when appropriate?)
- Structure 

## UPDATES 1&2 (2nd of May & 15th of May)
- Report progress that has been made in previous week(s)
- Ask questions you would like to ask
- Use GitHub issue for every update 
- Add links to code or data where applicable 

## PRESENTATION (30th of May)
- Background of project
- Key findings
- Critical appraisal of your project and results
- Connection of your project to the course's topics
- Questions/discussion

## SUBMIT PROJECT (2nd of June)
- Hand in report
- Submit public URL to project’s repository 
- Slide deck (slides from presentation)
- The repository or folder containing the code, data and README file
- Proper documentation to navigate the repository (links to repository)
- Put bulk of code into a single notebook, with clear instructions and dependences 


## NOTE
- Always take notes on what you are doing
- Keep a logbook on when what is done
- Make notes in the code on why and how it is programmed

## Tasks

First, we divided task from the first phase among the three of us. 

Thereafter we worked on our own tasks individually. Occasionally we met to discuss how to connect our work in a smooth way or how our all parts should interplay. So far this is what we got: 

#### Joep (questionnaire):
Did some research on how to make and use graphical user interface using PySimpleGUI. This way can ask the question from the questionnaire and present the results in a user-friendly way. Furthermore, worked on how to extract key information which is necessary for the recommender system from user answers. (See code: extract_info_noun). Finally, worked a bit on which questions to ask in odor to get the user to give the right type of answers (see document: questionnaire).

#### Iason (data, GitHub):
Found and edited the appropriate data. From a Kaggle dataset with hundreds of categories, I made sub-selections and groupings which combine all the useful categories we have, such that there is a direct correspondence between our data and the features we want to extract. Also, I am in charge of updating GitHub with our project progress.

#### Brook (TM model):       
Started making the user_to_feature model, to be tested further with the processed data that we collect. Also, created the GitHub page, and work on it regularly.
