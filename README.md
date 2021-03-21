# Edge TPU Object Detction Model Building & Training

This is repo is derived from the [google coral repo](https://github.com/google-coral/tutorials). 
I've updated some of the scripts in the docker/object_detection/scripts folder to enable training with my own data.

## Usage

To use this repo to train and build a model for the Edge TPU with your own data, follow the instructions here:
https://coral.ai/docs/edgetpu/retrain-detection/


However, the following suggested changes should be made in these sections:

### Setting up Docker container

+ In Step 3, change:
   > "git clone https://github.com/google-coral/tutorials.git" 
   to
   > "git clone https://github.com/samuel-ogbonnaya/google_coral_detection.git"

+  Before executing Step 4, update the follwoing lines in constants.sh: 
   ```
   LEARN_DIR="${OBJ_DET_DIR}/sportseye"
   DATASET_DIR="${LEARN_DIR}/sportseye_data" 
   ```
   to
   ```
   LEARN_DIR="${OBJ_DET_DIR}/your-dir"
   DATASET_DIR="${LEARN_DIR}/your-dir-data"
   ```
+  In Step 6, update the following:
   ```
   "...--mount type=bind,src=${DETECT_DIR},dst=/tensorflow/models/research/learn_pet detect-tutorial-tf1"
   ```
   to 
   ```
   "...--mount type=bind,src=${DETECT_DIR},dst=/tensorflow/models/research/your-dir detect-tutorial-tf1"
   ```
### Download and configure the training data
Before running the bash script from within the docker container, complete the following for pre-processing your image data, or utilise you own pre-processing methods:
- Collate your collected images into a folder
- Take a clean subset of images (e.g not blurred etc)
- From the preprocessing folder, run the image_naming.py script, then the resizer.py script
- Use Labellimg, instructions [here](https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/training.html#annotate-the-dataset)
- Run the partition_dataset script on the processed (annotated) images 
- Run the xml_to_csv.py scriptto generat csv files for both the train and test images
- Create a label map using these [instructions] (https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/training.html#create-label-map)
- Copy the train and test image folders, label map, geenrate_tfrecord.py and the train and test csv files into the mounted docker directory on your host   filesystem.
+ Run my updated bash script:
```
> ./prepare_checkpoint_and_dataset_2.sh --network_type mobilenet_v2_ssd --train_whole_model false
```

+ NOTE: may also have to change file ownerships using chmod +x for some of the bash scripts
+ NOTE: my updates have only been made for the mobilenet_v2_ssd network type

### Next Steps
+ Complete all other steps as per the google coral tutorial
