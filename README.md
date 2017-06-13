# wps

wps or wireless position system is an experiment to try and identify your
position based on the signal strengths of wireless access points.

## Quick start

### Requirements
* Linux
* numpy - pip install numpy
* pandas - pip install pandas
* sklearn - pip install sklearn
* nmcli - Most distributions ship with it

### Download wps
```sh
git clone https://github.com/sanketh95/wps
cd wps
```

### Data collection

Initially we collect data for signal strengths in various locations (This variance of these locations cannot be too high.
This would work well for places surrounded by various access points. For instance, your home) and label them. eg. kitchen, bedroom etc

```sh
./collect_data.sh hall.txt
```

This creates a number of files, one for each location. 

### Data preparation
You need combine them and split into train and test sets.
Currently the split ratio is hardcoded to 0.9. Change the file if needed or better raise a pull request.

```sh
python parse.py parse.py hall,kitchen,livingroom
```

This script searches for the files hall.txt,kitchen.txt and livingroom.txt. Make sure the files exist.

It considers an intersection of all access points available in the locations.
That is, if an AP signal is absent at a location, then that AP's signal strength is ignored from other locations.

This also creates some meta files *fields.txt*, *train.txt* and *test.txt*.
As long as your individual location data has not changed, you need not run this step everytime. You can directly skip
to training. 

### Training

Then we need to train the model to predict the location. The model used here is a LogisticalRegressionCV model from sklearn.
You can try with any other model you prefer (let me know how it goes). Once training is done, it prints the test accuracy
as well.

```sh
python train.py
```

### Prediction

Now you are all set to predict your location. This can be done using

```sh
python predict.py
```

## Results

I got an accuracy of 97% with 5 classes (livingroom,bedroom1,bedroom2,bedroom3,kitchen) and with 5 access points (dimensionality).
This differs based on the AP positions, obstructions etc. 

## Note

This was wrapped up under a few hours and wasn't written cleanly. I may not find time to work on improving
the aesthetics or the usability of the scripts. If you think something can be made better, please go ahead and
log a pull request.

## Usage policy

You are free to use this however you wish to.


