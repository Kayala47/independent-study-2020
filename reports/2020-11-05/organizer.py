from PIL import Image
import csv
import os

list_images = os.listdir(
    "F:\\Unreal Engine\\Projects\\vechicle_test\\Saved\\Screenshots\\Windows")

txtfile_path = "F:\\Unreal Engine\\Projects\\vechicle_test\\Content\\textfiles\\2.txt"
txtfile = open(txtfile_path, 'r')  # no need to write to it

num_imgs = len(list_images)

img_starter = "HighresScreenshot"

num_zeroes = 5 - len(str(num_imgs))

# it'll then have a number of zeroes, up to 5, plus the number itself


with open('test.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    for i in range(0, num_imgs):
        # match up image with csv

        # decide num of zeroes
        num_zeroes = 5 - len(str(i))
        name = img_starter + ('0' * num_zeroes) + str(i)

        # now grab the line from the file
        desc = txtfile.readline().strip('\n')
        print(desc)

        writer.writerow((name, desc))
