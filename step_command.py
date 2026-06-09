
1. NEXUS Sentinel 

Meaning:

Nexus = Connected federated nodes
Sentinel = Security guardian

Tagline:

Intelligent Threat Detection for Next-Generation Networks

🚀 Step-by-Step Setup Guide--

Step 1: Clone the Repository
git clone https://github.com/Ramakrishna232002/FedX-ZT-5G.git
cd FedX-ZT-5G

Step 2: Create Virtual Environment
python -m venv venv
venv\Scripts\activate

Step 3: Install Dependencies
pip install --upgrade pip
pip install -r requirements.txt

Step 4: Download Dataset
https://www.unsw.adfa.edu.au/unsw-canberra-cyber/cybersecurity/ADFA-NB15-Datasets/

Step 5: Train the Federated Model (First Time Only)
python src/federated_final.py

This will:

Preprocess the data

Split into 3 edge nodes

Train federated models

Save to models/saved/federated_models.pkl

Step 6: Run the Application
Terminal 1 - Backend API:
    python backend/app.py
Terminal 2 - Frontend UI:
    streamlit run frontend/app.py
    
