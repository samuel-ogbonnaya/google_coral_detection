# Edge TPU Object Detction Model Building & Training

This is repo is derived from the [google coral repo](https://github.com/google-coral/tutorials)
I've updated some of the scripts in the docker/object_detection/scripts folder to enable training with my own data.

To use this repo to train and build a model for the Edge TPU with your own data, follow the instructions here:
https://coral.ai/docs/edgetpu/retrain-detection/

However, the following updates should be made:

+ In Step 3: change "git clone https://github.com/google-coral/tutorials.git" to "git clone https://github.com/samuel-ogbonnaya/google_coral_detection.git"

+  Before executing Step 4, 
   Update the lines in constants.sh:
     LEARN_DIR="${OBJ_DET_DIR}/sportseye"
     DATASET_DIR="${LEARN_DIR}/sportseye_data" 
   to
    LEARN_DIR="${OBJ_DET_DIR}/your-dir"
    DATASET_DIR="${LEARN_DIR}/your-dir-data"
  
+  In Step 6:
    Update
      "...--mount type=bind,src=${DETECT_DIR},dst=/tensorflow/models/research/learn_pet detect-tutorial-tf1"
    to 
      "...--mount type=bind,src=${DETECT_DIR},dst=/tensorflow/models/research/your-dir detect-tutorial-tf1"
