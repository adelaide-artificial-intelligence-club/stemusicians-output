# STEMusicians Output

## Install

### Ubuntu

Install some libraries, as described in the [hello magenta notebook](https://colab.research.google.com/notebooks/magenta/hello_magenta/hello_magenta.ipynb):

`sudo apt install build-essential libfluidsynth1 fluid-soundfont-gm build-essential libasound2-dev libjack-dev`

Create a new [Anaconda](https://www.anaconda.com/distribution/) environment and install Python 3:

`conda create --name stem`

`conda activate stem`

`conda install python`

Install some PIP dependencies, then magenta:

`pip install pyfluidsynth pretty_midi`

`pip install magenta`

At the time of writing, the latest TFP is incompatible with TF 1.14, so roll it back:

`pip install tensorflow-probability==0.7`

Get gsutil and download pretrained weights:

`sudo snap install google-cloud-sdk --classic`

`gsutil -m cp -R gs://download.magenta.tensorflow.org/models/music_vae/colab2/checkpoints/mel_2bar_big.ckpt.* checkpoints`

## Run

`python main.py`
