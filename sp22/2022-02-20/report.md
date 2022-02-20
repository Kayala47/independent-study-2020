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

For now, I'm proceeding with having the last set of angles be the input and the next set be the expected output. I've had to modify the dataset class to also have a function that breaks up the dataset into numpy arrays to pass into the dataset class. 

As for the dataset itself, I realized the output I had before wasn't optimal. A huge part of the problem is that the angles get recorded as strings because the csv is trying to account for the brackets and commas inside of each array. I had to take a medium-sized detour here to figure out the issue. I experimented with the "quoting", "delimiter" and "escapechar" fields of csv writer, but none really worked out. Even `quoting=QUOTE_NONE` proved unfruitful, since the csv writer really had no way to deal with the data otherwise.

I had an idea though! I flattened the array of frames that we got so that it was all one long string, and then I had the csv writer write in 12 numbers to a single row at a time. Since that's the shape of the tensor we want anyway, it ends up being more efficient. It also allows me to strip the brackets out and still keep the legibility. I kept the quote_none rule, but allowed it to take the defaults for the rest. I ended up with a file of pure numbers, that pandas could read as separate numbers thanks to the lack of brackets and extraneous commas. 


Now I'm working on getting the model itself to work. I've sidelined the batch-normalization step since I'm only working with 1D tensors for now (just the angles for a particular frame), but am still not able to get it to work quite correctly. The issue seems to stem from the batch size when it trains. The batch size is 12, which doesn't divide evenly throughout the test set. For some reason, it leaves the last training with an input size of 2, which causes a mismatch of shapes. However, when I adjust the batch size to 14 to make it divide evenly, I get a warning from pytorch about errors due to broadcasting, since the input size is 12 and broadcasting errors may occur when the batch size and input don't match. Here's the warning text:
```
UserWarning: Using a target size (torch.Size([14])) that is different to the input size (torch.Size([12])). This will likely lead to incorrect results due to broadcasting. Please ensure they have the same size.

```

Correction to the above:
I wrote the last paragraph after making some "fixes" to the model to try to get it to work. The real issue ended up being that, when I switched to using np.array instead of just `[]`, numpy flattened my arrays. Instead of having a tensor of 79x12, I just had one giant array. That meant that the code I wrote to separate the testing and training sets cut the angles unevenly, resulting in that obnoxious 2-length layer. By fixing that issue, I was able to re-introduce batch-normalization and get the sizes to work properly.


### Accomplished
I managed to train the model on the walk data. With it, we achieved a final loss of 0.41 (0.35 was the best I saw). It's not great, but definitely something to start with. As I'm able to load in more of the data and tune the hyperparameters, I think it can get much better.



## Issues/Problems
- Data seemed to be reading incorrectly with `df.iloc`. I figured out that it was because my csv's had no headers. I put in column headers and that should stop it from reading the first row of results as the header. 
    + Solution: see Activity for description of "remodel" of save_data function, which allowed us to save data one frame at a time with type integer for each of the angles.


## Questions
- why is the batch size of the test dataset the length of the whole set, whereas the train dataloader has a batch size of 16?
- I'm still unsure how to load all the different gait angle files into one dataset. I think this stems from not knowing whether my x and y values are correct.
- Should I be converting those angles (to radians or degrees) for the testing? might be worth trying?

## Plans for next session
