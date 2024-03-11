import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, cohen_kappa_score, roc_curve, auc
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# Load your CSV data
data = pd.read_csv('Rice_Cammeo_Osmancik_no_outliers.csv')

# Encode the 'Class' column to numerical values
label_encoder = LabelEncoder()
data['Class'] = label_encoder.fit_transform(data['Class'])

# Assuming your target variable is in a column named 'Class'
X = data.drop('Class', axis=1)
y = data['Class']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize a RandomForestClassifier (you can replace this with your preferred classifier)
classifier = RandomForestClassifier(n_estimators=100, random_state=42)
classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = classifier.predict(X_test)

# Calculate accuracy and kappa
accuracy = accuracy_score(y_test, y_pred)
kappa = cohen_kappa_score(y_test, y_pred)

# Get ROC curve and AUC for each class
n_classes = len(label_encoder.classes_)
fpr = dict()
tpr = dict()
roc_auc = dict()

for i in range(n_classes):
    y_test_class_i = (y_test == i).astype(int)
    y_pred_class_i = classifier.predict_proba(X_test)[:, i]
    fpr[i], tpr[i], _ = roc_curve(y_test_class_i, y_pred_class_i)
    roc_auc[i] = auc(fpr[i], tpr[i])

# Print the results
print(f'Accuracy: {accuracy:.4f}')
print(f'Kappa: {kappa:.4f}')

# Plot ROC curve for each class
plt.figure(figsize=(8, 6))
for i in range(n_classes):
    plt.plot(fpr[i], tpr[i], lw=2, label=f'ROC curve for Class {i} (area = {roc_auc[i]:.2f})')

plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve for Each Class')
plt.legend(loc='lower right')
plt.show()
