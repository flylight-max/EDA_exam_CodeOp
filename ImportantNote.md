# **Can we confidently predict customer spend?**  

#### I have here 2 samples (plus a third one that doesn't contain the 'spend' column. This dataset is the one I will use to apply the prediction model).  
#### The first one is the first one I received and I am doing an extensive EDA on it (cleaning it up and looking how the spend behaves with the different variables in hand). From this dataset, I am making suggestions to the team of what the team could focus on and what strategy they could do to improve the benefit of the loyal card towards our advantage (good reward for the customer but also better spending expenses in our premises).  
#### The second dataset is a dataset I received along with the one used for prediction. I used both dataset individually (the first one and this one) to evaluate the best model to use. This dataset was already cleaned (no missing values, no typos).  
#### Which dataset should I use to predict the unknown 'spend' of my third dataset (the test dataset)?  
#### This *DataCamp* excersise presumed that I will use the second one, the one that was delivered at the same time as the first one. Because of that, I was biased into thinking that both datasets, coming from the same company *International Essential*, would behave the same. However, taht wasn't the case. As a consequence, when I combined both datasets to increase my sample size to train the model, I obtained a terrible score, whether I mixed all samples or even when I do a resampling (sampling with replacement).  
#### Because of this, I compared the two datasets and realised that they were not behaving the same regarding to the spend. Hence, I started to becmoe more doubtful.  
### **Which dataset should I use to train my model?**  
#### This excersise made me realise one thing. When I develop a supervised machine learning model to predict a value, using a dataset in hand, I should **NEVER** presume that the dataset to test behaves the same as the one I sued to train the model.  
#### Hence, to choose the best dataset to train the model in order to get the best prediction, I compared the distribution of the different features between the 3 datasets.  
#### Of course, because that wasn't the goal of this excersise (figuring which dataset to use to train the model), the second dataset was the one that behaved the same way as the test dataset.  
#### Nevertheless, in the future, **ALWAYS** keep in mind this:  
### **Before using .predict() ALWAYS cmpare the distribution of the features between the dataset used to train the model and the dataset you received to do the prediction.**  

In the case I receive two dataset with drastique different distributions of the datasets, I will train an ensemble model on the combined dataset and look for the best performance. Here, I found that Bagging was a good catch. At the end when comparing the predictions between linear regression (fit with the second dataset, the one I was supposed to use) and bagging (fit with the 2 datasets combined), I obtain a very nice correlation with a low variability. 
