new readme:
say course name and your name
project files split
where to find everything: EDA and Report
that's it....
move questions to EDA and add your report when you are done.






## Project Title
**An Empirical Study of Housing Price Drivers and Model Selection for Price Prediction**

## Project Overview
This project investigates the key factors that influence residential housing prices and evaluates how feature engineering and model selection impact predictive performance. Using the Ames Housing dataset, the analysis combines exploratory data analysis, feature engineering, and regression modeling to both understand price drivers and build reliable predictive models.

Rather than treating prediction as the sole objective, predictive modeling is used as an analytical tool to quantify the relationships between housing characteristics and sale prices and to assess how well these relationships generalize to unseen data.

## Dataset
**House Prices – Advanced Regression Techniques**  
Source: Kaggle  
Link: https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/overview

The dataset contains detailed information on residential properties in Ames, Iowa, including structural attributes, neighborhood characteristics, and temporal features, along with the target variable `SalePrice` measured in U.S. dollars.

## Research Questions
1. **Which original housing features have the strongest influence on residential sale prices?**

2. **Can engineered features derived from existing variables improve the predictive performance of house price models, and how does feature engineering affect model accuracy and stability compared to using raw features only?**

3. **Which predictive model performs best for house price estimation when evaluated on unseen data?**

Understanding the drivers of housing prices is important for buyers, sellers, and policymakers, and feature engineering may reveal latent factors not captured by raw variables.

## Methodology Overview
- Exploratory data analysis to understand distributions, relationships, and data quality
- Data cleaning and preprocessing, including handling missing values and categorical encoding
- Feature engineering to create informative derived variables
- Predictive modeling using multiple regression-based approaches
- Model evaluation on held-out test data to assess generalization performance

## Objectives
- Identify the most influential factors driving housing prices
- Evaluate the impact of feature engineering on model performance
- Compare predictive models to determine the most effective approach for house price estimation



----------------------------

## DELETE LATER:
IMPORTANT NOTE: you don't need to mention the project for the prof rn, just keep working on it and after they post some stuff you can share your result with them and ask for initial feedback to complete everything in the reading week.

UPDATE the readme and make it similar to your github ones, you already wasted a lot of time on sturing them, so just use your effort.

SOME TODOs:
- think about a research question
- try to use statistical hypothesis and some interesting techniques similar to what you did before.
- design proper report like the ones you did for your projects

UPDATE YOUR EDA INITIAL PART BASED ON THIS:
Some possible research question;
- which features are the most impactfull on our sale price 
- are ther some additional features that we can invent which might also have a big effect?


NOTE: your work does not have to be perfect, just put good effort, structure things well and represent them well... if he sees that he will probably give you some good marks, it does not have  to be extremely interesting ... it is a project that assumed to be first of its kind.

- MAKE IT PUBLIC LATER AND MAYBE EVEN USE IT ON RESUME!  -- update the repo name to remove 2010 from it .

Since using AI for everycoding thing shoould not take much time. (UNLIKE YOUR POROJECTS YOU DIDN"T RELY ON IT FULLY)

MAKE A BASELINE MODEL AND START IMPROVING IT WITH DIFFERENT TECHINQIUES (DO IT ON THE DATE AFTER CLEANING BUT BEFORE ADDING THE ENGINEERED FEATURES)

you don't have to try different configurations like credit card project ... just work on some stuff with trying various models should be enough in terms of the scope...
REMEMBER IT IS JUST 15% not much!

DO PROPER FEATURE SELECTION, 
- TRY TO USE THE LASSO TECHNIQUE OF FEATURE SELECTION TOO IF YOU WANT....



MAKE A WAY TO INTERACT WITH THE FINAL MODEL -- maybe a class or something 


ENDING WITH SUBMITTING TO KAGGLE TOO IF YOU WANT.

OKAY TO USE EDA STEPS FROM PREV NOTE BOOK :D  you did it at the end ....




- **DO IN PHASE 1 - CLEANING -- to reduce amount of features you have.**

Feature Reduction — Phase 1 (TODO)

The following steps will be completed by the end of the first analysis phase to reduce the feature space in a principled and reproducible way:

TODO: Remove Non-Informative Features

 Drop pure identifier columns (e.g., Id) that carry no predictive information.

 Identify and remove features with near-zero variance.

 Remove features with extreme sparsity (high proportion of missing values) where the information content is minimal.

TODO: Missing Value–Based Screening

 Quantify missingness for each feature.

 Drop features exceeding a predefined missing-value threshold unless domain knowledge suggests otherwise.

 Explicitly encode “not present” cases for structural features (e.g., basement, garage) instead of treating them as NaN.

TODO: Correlation-Based Feature Filtering

 Compute correlations between numerical features and the target variable.

 Rank features by absolute correlation strength.

 Retain strongly and moderately correlated features for further analysis.

 Flag weakly correlated numerical features as candidates for removal.

TODO: Feature Engineering and Consolidation

 Combine redundant or highly related features into engineered variables (e.g., total area, total bathrooms).

 Replace multiple low-impact features with fewer, higher-signal engineered features.

 Re-evaluate correlations after feature engineering.

TODO: Categorical Feature Screening

 Identify categorical features with rare or low-frequency levels.

 Merge infrequent categories into an “Other” group where appropriate.

 Remove categorical features that show minimal separation in sale prices.

TODO: Model-Guided Feature Selection

 Apply simple baseline models with regularization to identify low-importance features.

 Use model-based importance scores to support final feature selection decisions.




 ------------------------

TODO: 
- only submit the IPYNB (so, move anything related to the questions you are trying to answer to it...)
- don't submit the data but you may submit any scripts
- you don't need to split into directories as this will take you so much time - just do it in ipynb
- at the end try some models and stick with the largest result you get
- answer all the questions that were set: which columns were the most helpful, were they sufficient to get a large result -- maybe also compare to just training base model with the normal columns and see how much it increases. (CONCLUDE WITH HOW WHAT YOU DID IS USEABLE OR USEFUL IN GENERAL... BE CLEAR)
- RENAME COLS? - final ones at least for easier naming convetions.
- you don't need to report all prompts :)

ASK A QUESTION TO THE PROF TO CLARIFY IF WHAT YOU ARE DOING NOW IS ON THE RIGHT TRACK...