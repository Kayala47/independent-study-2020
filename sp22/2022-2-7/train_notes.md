# Notes on Sine Mode Multiple Outputs Notebook
* I went ahead and changed the print statements to ic() for readability

## get train and test data (fx)
- this shouldn't be super relevant anymore? I think i would be replacing it with the actual pre-train data we can now create, but would we keep the sin function? what function does that serve?
- random inputs appends 4 random data sets and then another distribution a number of times equal to num_inputs - 5
    + I'm guessing the first are the leg positions and the second is the sine wave?
    + same happens for test later
    + as written it crashed when running the function. changing min to np.min worked (you can't pass in multi element arrays to min normally?)

## plot_xy_data
I know this plots data, but it's not used anywhere else. I tried to run it with the arguments x_train and y_train that I get from the previous function but the sizes of x and y don't match
+ oop! got it to work by changing the pytplot.scatter function so that it plotted y_data instead of yd (which is the iterating variable used in the loop a little higher). Now it prints out a sine functoin

## Model Architecture
- no activation function, should add one
- here's where the number 33 comes up. I'm getting an error when trying to run that m1 = 16x1 and m2 = 33 * 16. this is probably where the mismatch occurs; i'm betting one of the activation layers is doing that

# Moving Forward
I think my job is simply to create a new neural network to take in the data. We can try out different parameters, so perhaps also should be trying to optimize those later. 