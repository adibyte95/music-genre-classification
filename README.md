# Music Genre Classification
Topic- to classify the type of genre a music belongs. genres include blues, classical, country, disco, hiphop, jazz, metal, pop, reggae, rock.<br/>

# Dataset 
data set is GTZAN. Dataset is from <a href= 'http://marsyasweb.appspot.com/download/data_sets/'>Here</a> . It contains 100 music from each of the 10 class.<br/>


# Approach 
we will first convert the .au audio files given into .wav files first . then we will convert the .wav files into spectogram and then use an cnn to classify them into different groups.<br/>
typically a spectogram lookes like this <br/>
<img src='https://github.com/adibyte95/music-genre-classification/blob/master/images/blues/0.png'>

# confusion matrix
<img src = 'https://github.com/adibyte95/music-genre-classification/blob/master/media/confusion_matrix.png'>

# loss curve
<img src='https://github.com/adibyte95/music-genre-classification/blob/master/media/loss_curve_73_90_10_split.png'> <br/>
the model was was trained for 100 epochs and as we can see the slight overfitting is there. we took the model which gave the best validaiton accuracy. the model was validated on 100 samples, 10 from each of the 10 classes and trained on 900 images 90 from each of the 10 classes

# Accuracy
the model we used was fine tuned VGG16 model . validation accuracy was about 73% and training accuracy was about 88%. considering only 1000 samples this is good accuracy.

# Note
pull request for any further approach to improve this problem is accepted
