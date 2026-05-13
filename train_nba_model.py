import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

def train_nba_engine(data_path='hcp_engagement_data.csv'):
    # 1. Load the HCP data
    df = pd.read_csv(data_path)
    
    # 2. Preprocessing: Convert 'specialty' and 'last_interaction' into numbers
    # This is "One-Hot Encoding" - essential for categorical pharma data
    X = pd.get_dummies(df.drop(['hcp_id', 'next_best_action'], axis=1))
    y = df['next_best_action']
    
    # 3. Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
    
    # 4. Train the Multi-Class Random Forest
    print("Training Omnichannel NBA Engine...")
    model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
    model.fit(X_train, y_train)
    
    # 5. Evaluate results
    y_pred = model.predict(X_test)
    print("\n--- NBA Channel Prediction Report ---")
    print(classification_report(y_test, y_pred))
    
    # 6. Generate the Confusion Matrix (The "Executive Verification")
    plt.figure(figsize=(8, 6))
    cm = confusion_matrix(y_test, y_pred, labels=model.classes_)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=model.classes_, yticklabels=model.classes_)
    plt.title('NBA Prediction Accuracy by Channel')
    plt.ylabel('Actual Best Action')
    plt.xlabel('Predicted Best Action')
    plt.savefig('nba_confusion_matrix.png')
    print("\nSuccess! 'nba_confusion_matrix.png' created.")

if __name__ == "__main__":
    train_nba_engine()
