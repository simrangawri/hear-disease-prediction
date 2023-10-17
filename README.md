
# Heart Disease Prediction

**Running the Code:**
1. Clone or download this repository to your local machine.
2. Open the Jupyter Notebook file heart_disease_prediction .ipynb using Jupyter Notebook or any compatible IDE.
3. Ensure that you have the dataset "heart_deseases.csv" in the same directory as the notebook.
4. Execute the code cell by cell to perform data preprocessing, model training, and evaluation.
5. Utilize the `predict_hdisease()` function to predict heart disease based on specific features.
6. The trained Logistic Regression model is saved as 'heartdisease.pickle'.

**Dataset:**
The code utilizes the "heart_deseases.csv" dataset for heart disease prediction. This dataset contains various features, including age, sex, cholesterol levels, and other health-related parameters.

**Algorithms Used:**
- Logistic Regression
- K-Nearest Neighbors
- Decision Tree
- Random Forest

**Evaluation Metrics:**
The code provides evaluation metrics such as accuracy, recall, and F1 score to assess the machine learning models' performance.

**Saving the Model:**
The trained Logistic Regression model is saved as 'heartdisease.pickle' for future usage.

**Author:**
This code was developed by Simran Gawri for educational and learning purposes.

**Acknowledgments:**
The dataset used in this project was obtained from Kaggle.
"""

# Write the README content to a file
with open('README.md', 'w') as readme_file:
    readme_file.write(readme_content)
