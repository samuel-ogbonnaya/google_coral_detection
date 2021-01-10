import os
import argparse
from shutil import move
import cv2
import shutil



parser = argparse.ArgumentParser()
parser.add_argument("-i", "--inputdir", help="full directory path which hold images/data", type=str)
args = parser.parse_args()

new_dir = os.path.join (os.path.dirname(args.inputdir), "resized_selected_images")

if not os.path.isdir(new_dir):
    os.mkdir(new_dir)

for filename in os.listdir(args.inputdir):
    file_path = os.path.join(args.inputdir, filename)
    new_file_path = os.path.join(new_dir, filename)
    image = cv2.imread(file_path)
    if image.shape[0] <=400 or image.shape[1] <= 400:
        resized = image
    else:
        r = 400.0 / image.shape[1]
        dim = (400, int(image.shape[0] * r))
        resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA) 
        
    cv2.imwrite(new_file_path, resized)
    '''
    cv2.imshow("resized", resized)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break
    '''