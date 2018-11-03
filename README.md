# Overview

What makes a fragrance sold at Sephora a bestseller? Most people buy products without understanding all the factors that influence them to purchase. We can use data to better understand what factors are most influential to purchasing behavior. 

Our objective is to determine if there are underlying characteristics of fragrances that influence their status as bestseller the most and if so, to identify what those characteristics are. 

# Methodology
1. Create a script to scrape fragrances, extracting the product's name, size, price, description, and artist.
2. Clean the data and engineer features.
3. Download fragrance images and cluster fragrances by most dominant color
4. Get dummies for fragrance and run a classifier to see predictive capabilities of 
5. Create a Gradient Boosted Classifier and train it on the perfume properties and color clusters in order to see if the predictive ability for bestsellers is improved by adding image color clusters.

# Deliverables
- Jupyter notebooks documenting scraping and cleaning
- Jupyter notebook documenting data exploration
- Jupyter notebook documenting modeling


# Dataset
The final processed dataset "fragrance_details.csv"  can be found under data/processed. The data folder also includes the raw dataset.

# Hypothesis
There are certain characteristics of a fragrance available on their website Color has the ability to influence purchasing behavior and will improve 

# Results
The final Gradient Boosted Classifier model incorporating color cluster improved previous model without color clusters. The final model was able to predict 9 of the 27 bestsellers, the model achieved an accuracy of 0.865, precision of .47, and recall of .33. The model was build using 450 trees at a max depth of 5 for each tree. 

The precision and recall when cross validating was much higher on the validation set, but low on the test set. The model is overfitting, meaning we should collect more data to get more accurate results from cross-validation and grid search parameter tuning.

# Next Steps
- Continue to refine the dataset and scrape more data
	- After gathering more data use gridsearch cross-validation 

