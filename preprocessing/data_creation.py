import os
import argparse
import shutil


parser = argparse.ArgumentParser()
parser.add_argument("-i", "--imgdir", help="full directory path which hold images/data", type=str)
parser.add_argument("-x", "--xmldir", help="full directory path which hold xml data", type=str)
args = parser.parse_args()


def check (imgdir,xmldir):
    img_dir = os.listdir(imgdir)
    xml_dir = os.listdir(xmldir)
    xml_files = [xmlfile.split('.')[0] for xmlfile in xml_dir]
    missing  = []
    for img_filename in img_dir:
        img_name = img_filename.split('.')[0]
        if img_name in xml_files:
            continue
        else:
            missing.append(img_name)
    print(missing)
    return len(missing)

def image_folder(imgdir,xmldir):
    img_dir = os.listdir(imgdir)
    xml_dir = os.listdir(xmldir)

    new_dir = os.path.join(os.path.dirname(imgdir), "processed_images")
    if not os.path.isdir(new_dir):
        os.mkdir(new_dir)

    assert len(img_dir) == len(xml_dir)

    for img, xml in zip(img_dir, xml_dir,):
        img_file = os.path.join(imgdir, img)
        xml_file = os.path.join(xmldir, xml)
        if os.path.isfile(img_file) and os.path.isfile(xml_file):
            try:
                shutil.copy(img_file , new_dir)
                shutil.copy(xml_file , new_dir)
            except:
                print('error occured')
                continue

missing_files = check(args.imgdir, args.xmldir)

if missing_files == 0:
    image_folder(args.imgdir, args.xmldir)
