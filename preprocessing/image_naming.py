import os
import argparse
from shutil import move


parser = argparse.ArgumentParser()
parser.add_argument("-i", "--inputdir", help="full directory path which hold images/data", type=str)
args = parser.parse_args()

def num_sort(filename):
    num = filename.split('_')[1].split('.')[0]
    return int(num)

try:
    sorted_list =  sorted(os.listdir(args.inputdir), key=num_sort)
except ValueError:
    sorted_list  = os.listdir(args.inputdir)


count = 1
for filename in sorted_list:
    try:
        new_name = "football_" + str(count) + ".jpg"
        if os.path.join(args.inputdir, filename) == os.path.join(args.inputdir, new_name):
            count += 1
            continue
        else:
           os.rename(os.path.join(args.inputdir, filename) , os.path.join(args.inputdir, new_name))
           count += 1
    except:
        pass



