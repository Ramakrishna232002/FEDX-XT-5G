import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import LabelEncoder
import joblib

print("="*60)
print("FEDERATED LEARNING FOR 5G INTRUSION DETECTION")
print("="*60)

# Load data
print("\n1. Loading data...")
train_df = pd.read_parquet('data/raw/UNSW_NB15_training-set.parquet')
test_df = pd.read_parquet('data/raw/UNSW_NB15_testing-set.parquet')

# Remove duplicates
train_df = train_df.drop_duplicates()
print(f"   Training samples: {len(train_df)}")
print(f"   Testing samples: {len(test_df)}")

# Encode categorical columns
print("\n2. Encoding categorical features...")
cat_cols = ['proto', 'service', 'state']
for col in cat_cols:
    combined = pd.concat([train_df[col], test_df[col]]).astype(str).unique()
    le = LabelEncoder()
    le.fit(combined)
    train_df[col] = le.transform(train_df[col].astype(str))
    test_df[col] = le.transform(test_df[col].astype(str))
    print(f"   {col}: {len(le.classes_)} classes")

# Prepare features and labels
X_train = train_df.drop(columns=['attack_cat', 'label']).values
y_train = train_df['label'].values
X_test = test_df.drop(columns=['attack_cat', 'label']).values
y_test = test_df['label'].values

print(f"\n   Features: {X_train.shape[1]}")
print(f"   Train attack ratio: {y_train.mean():.3f}")
print(f"   Test attack ratio: {y_test.mean():.3f}")

# Split into 3 edge nodes (non-IID distribution)
print("\n3. Splitting data across 3 edge nodes...")
indices = np.arange(len(X_train))
np.random.seed(42)
np.random.shuffle(indices)

node_sizes = [len(X_train) // 3] * 3
node_sizes[-1] = len(X_train) - sum(node_sizes[:-1])

node_data = []
start = 0
for i, size in enumerate(node_sizes):
    end = start + size
    node_idx = indices[start:end]
    node_X = X_train[node_idx]
    node_y = y_train[node_idx]
    node_data.append((node_X, node_y))
    print(f"   Node {i+1}: {len(node_X)} samples (Attack: {node_y.sum()}, Normal: {len(node_X)-node_y.sum()})")
    start = end

# Federated learning - train local models
print("\n4. Training local models on each edge node...")
local_models = []
for i, (node_X, node_y) in enumerate(node_data):
    print(f"   Training Node {i+1}...")
    model = RandomForestClassifier(n_estimators=100, max_depth=20, random_state=42, n_jobs=-1)
    model.fit(node_X, node_y)
    local_models.append(model)
    local_acc = model.score(node_X, node_y)
    print(f"   Node {i+1} training accuracy: {local_acc:.4f}")

# Federated aggregation - majority voting
print("\n5. Federated aggregation (majority voting)...")
predictions = []
for model in local_models:
    pred = model.predict(X_test)
    predictions.append(pred)

predictions = np.array(predictions)
final_pred = []
for i in range(len(X_test)):
    vote = np.bincount(predictions[:, i]).argmax()
    final_pred.append(vote)
final_pred = np.array(final_pred)

# Evaluation
print("\n6. Final evaluation on test data...")
print("="*60)
print("FINAL RESULTS")
print("="*60)
print(f"Accuracy:  {accuracy_score(y_test, final_pred):.4f}")
print(f"Precision: {precision_score(y_test, final_pred):.4f}")
print(f"Recall:    {recall_score(y_test, final_pred):.4f}")
print(f"F1-Score:  {f1_score(y_test, final_pred):.4f}")
print("="*60)

# Save models
print("\n7. Saving federated models...")
joblib.dump(local_models, 'models/saved/federated_models.pkl')
print("   Models saved to: models/saved/federated_models.pkl")

print("\n Federated Learning completed successfully!")
