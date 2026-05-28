Spotify Hit Predictor

A Deep Learning based project that predicts whether a Spotify track will become a hit song using audio features and track metadata.

Project Overview

This project analyzes Spotify song data and builds a Neural Network model capable of classifying songs into hit and non-hit categories based on musical characteristics such as danceability, energy, loudness, tempo, valence, acousticness, and more.

The project pipeline includes:

* Data preprocessing
* Exploratory Data Analysis
* Feature engineering
* Feature scaling
* Genre encoding
* Neural Network model building
* Model training and evaluation
* Prediction on custom song samples
* Saving trained model files

Dataset

The dataset contains Spotify track information including:

* Popularity
* Danceability
* Energy
* Loudness
* Speechiness
* Acousticness
* Instrumentalness
* Liveness
* Valence
* Tempo
* Genre
* Explicit content
* Duration

Target Variable

A binary feature called is_hit is created:

* 1 → Popularity greater than or equal to 70
* 0 → Popularity less than 70

Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn
* TensorFlow
* Keras
* Joblib

Exploratory Data Analysis

The project includes:

* Missing value handling
* Correlation heatmap
* Distribution analysis
* Genre encoding
* Feature visualization

Deep Learning Architecture

The Neural Network consists of:

* Dense Layer with 256 neurons
* Dropout Layer
* Dense Layer with 128 neurons
* Dropout Layer
* Dense Layer with 64 neurons
* Output Layer with Sigmoid activation

Training Configuration

* Optimizer: Adam
* Loss Function: Binary Crossentropy
* Metric: Accuracy
* Epochs: 30
* Batch Size: 64

Model Evaluation

The model is evaluated using:

* Accuracy Score
* Classification Report
* Confusion Matrix
* Accuracy Curves
* Loss Curves

Saved Files

* spotify_model.keras
* scaler.pkl
* feature_columns.pkl

Project Structure

Spotify-Hit-Predictor/
│
├── spotify_hit_predictor.ipynb
├── spotify_model.keras
├── scaler.pkl
├── feature_columns.pkl
├── dataset.csv
└── README.md

How to Run

1. Clone the repository

git clone https://github.com/your-username/Spotify-Hit-Predictor.git

2. Install dependencies

pip install -r requirements.txt

3. Run Jupyter Notebook

jupyter notebook

4. Open and run

spotify_hit_predictor.ipynb

Future Improvements

* Add Streamlit web application
* Integrate Spotify API
* Improve model accuracy
* Deploy using Flask or FastAPI
* Add real-time prediction support

Contributing

Contributions and improvements are welcome. Feel free to fork the repository and create a pull request.

License

This project is open-source and available under the MIT License.

Author

Priyanshu Panigrahi

Interests:

* Deep Learning
* Artificial Intelligence
* Data Science
* Software Development
