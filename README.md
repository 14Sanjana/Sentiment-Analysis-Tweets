This project is about analyzing the sentiment of tweets using machine learning and deep learning techniques. It involves cleaning the text data, extracting features using TF-IDF, and training models like Logistic Regression and LSTM to classify tweets as Positive, Negative, or Neutral. The project uses Python along with libraries such as Pandas, NumPy, NLTK, Scikit-learn, TensorFlow, and Keras. Visualizations are done using Matplotlib and Seaborn. All the code is organized in different folders like src/ for Python scripts, notebooks/ for the main notebook, and models/ for saved models. This project helps understand how NLP and classification models work for sentiment analysis tasks.

🧾 Output Format
After processing a tweet, the model predicts its sentiment as one of the following:
Positive 😄
Negative 😞


The output is typically displayed like this:
Input Tweet: "I love the new features in this update!"
Predicted Sentiment: Positive 😄 along with confidence level.
Here as we are dealing with a dataset we would give the index value of which row we need:
Enter Tweet index(from datset): 0
Predicted output : My whole body feels itchy and like its on fire
Prediction : negative 😞
confidence : 51.24%
