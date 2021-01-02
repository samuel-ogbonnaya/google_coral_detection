# Colab tutorials for Coral

This is repo is derived from the google coral repo: (https://github.com/google-coral/tutorials)
I've updated some of the scripts in the object_detection folder to enable training with my own data.

To use this repo to train and build a model for the Edge TPU with your own data, follow the instructions here:
https://coral.ai/docs/edgetpu/retrain-detection/

However, the following updates should be made:

In Step 3: change "git clone https://github.com/google-coral/tutorials.git" to "git clone https://github.com/samuel-ogbonnaya/google_coral_detection.git"

Before executing Step 4, 
Update the lines in constants.sh:
  LEARN_DIR="${OBJ_DET_DIR}/sportseye"
  DATASET_DIR="${LEARN_DIR}/sportseye_data" 
to
  LEARN_DIR="${OBJ_DET_DIR}/your-dir"
  DATASET_DIR="${LEARN_DIR}/your-dir-data"
  
In Step 6:
Update
"...--mount type=bind,src=${DETECT_DIR},dst=/tensorflow/models/research/learn_pet detect-tutorial-tf1"

to 

"...--mount type=bind,src=${DETECT_DIR},dst=/tensorflow/models/research/your-dir detect-tutorial-tf1"

Train and build a model for the Edge TPU:

+ [Retrain a classification model using post-training quantization (with TF2)](https://colab.research.google.com/github/google-coral/tutorials/blob/master/retrain_classification_ptq_tf2.ipynb)

  This shows how to build an image classification model with Keras, train it
  with a custom dataset, quantize it with post-training quantization, and then
  compile it for the Edge TPU.

  We have another [version of this tutorial using TF1](
  https://colab.research.google.com/github/google-coral/tutorials/blob/master/retrain_classification_ptq_tf1.ipynb).

+ [Retrain a classification model using quant-aware training (with TF1)](https://colab.research.google.com/github/google-coral/tutorials/blob/master/retrain_classification_qat_tf1.ipynb)

  This shows how to retrain a quant-aware classification model using TF1. This
  process is complex, so the notebook calls upon several Python scripts
  to do the work (links to these scripts are provided in the notebook).

+ [Retrain an object model using quant-aware training (with TF1)](https://colab.research.google.com/github/google-coral/tutorials/blob/master/retrain_detection_qat_tf1.ipynb)

  This shows how to retrain a quant-aware object detection model using TF1. This
  process is complex, so the notebook calls upon several Python scripts
  to do the work (links to these scripts are provided in the notebook).

Other tutorials:

+ [Run Colab on a Coral Dev Board](https://colab.research.google.com/github/google-coral/tutorials/blob/master/run_colab_on_devboard.ipynb)

  This shows how to run a Jupyter notebook on your Dev Board *from* a Google
  Colab interface on your host computer.

+ [Build all the C++ "edgetpu" examples](https://colab.research.google.com/github/google-coral/tutorials/blob/master/build_cpp_examples.ipynb)

  This is a convenient way to build all the C++ inferencing examples
  from `edgetpu/src/cpp/examples/`, and download them to your computer.

+ [Build the C++ "lstpu" example](https://colab.research.google.com/github/google-coral/tutorials/blob/master/build_cpp_example_lstpu.ipynb)

  This is a convenient way to build the "lstpu" C++ example
  (it lists all Edge TPUs in your system), and download it to your computer.
