# Report - Week of Feb 6th, 2022 #


## Agenda ##
(notes from meeting w Prof Clark)
1. Make a new notebook from scratch for our model, now that we have actual training data
2. Construct a dataloader, taking inspiration from the current one in sine_model notebook
    + It needs to read from the csv of outputs that we already have
3. Create a new model, again taking most of the inspiration from the current notebook. We want to add batch normalization and dropout at some point
    + the model should have 12 outputs (just the angles for the legs)
    + we can start with a Resent model or some equivalent model already available via pytorch
    + the layers of the model should look roughly like:
        - linear
        - relu
        - batch normalization
        - activation
    + inputs should probably be 12 as well. it will make sense to grab them from the shape of the csv.

## Activities/Accomplishments and Concepts/Lessons Learned ##
I first scanned through the old notebook and added some sections that I thought wouldn't need to change much: the dataset class, test/train functions, train/train_batch. 

Then, I was reading through the csv's to prepare for making a dataloader and realized pd.read_csv() was parsing them weirdly. I think it thought the first row of data was the labels, so it was hard to read. I changed gaitpt to add those headers in to the csv's. 

I read [these docs](https://pytorch.org/tutorials/beginner/data_loading_tutorial.html#) to help figure out how to make a dataloader and realized I did need to re-write the dataset class after all. I think once I do this, I can easily create a dataloader from it. I have a concern about which is supposed to be the x and y data in the dataset. From the old notebook, I can see that the x values were basically a timestamp - since they represented an x along the graph of a sin curve. I wonder how well that will work here, so I'm also including the option for x to be the previous set of angles. I think that meshes well with the conversation we had about using "feedback" by introducing the past angles into the dataset. 

For now, I'm proceeding with having the last set of angles be the input and the next set be the expected output. I've had to modify the dataset class to also have a function that breaks up the dataset into 



### Accomplished






## Issues/Problems
- Data seemed to be reading incorrectly with `df.iloc`. I figured out that it was because my csv's had no headers. I put in column headers and that should stop it from reading the first row of results as the header. 

## Questions
- why is the batch size of the test dataset the length of the whole set, whereas the train dataloader has a batch size of 16?


## Plans for next session
