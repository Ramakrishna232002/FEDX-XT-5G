#  NEXUS Sentinel | FedX-ZT-5G

## Federated Learning + Explainable AI + Zero Trust for 5G Network Intrusion Detection, Federated Learning and Explainable AI powered Zero Trust Security Framework for Fifth Generation Networks

[![Python 3.13](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3+-orange.svg)](https://scikit-learn.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Business Problem](#business-problem)
- [Solution Architecture](#solution-architecture)
- [Tech Stack](#tech-stack)
- [Dataset](#dataset)
- [Model Performance](#model-performance)
- [API Endpoints](#api-endpoints)
- [Installation & Setup](#installation--setup)
- [Running the Application](#running-the-application)
- [Docker Deployment](#docker-deployment)
- [Project Structure](#project-structure)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Project Overview

**NEXUS Sentinel** is an intelligent intrusion detection system designed for 5G networks. It combines **Federated Learning**, **Explainable AI (XAI)**, and **Zero Trust** security principles to detect network threats while preserving data privacy.

Unlike traditional IDS that centralize sensitive network data, AEGIS Sentinel trains models locally on edge nodes and only shares model updates, ensuring **privacy-by-design**.

### Key Features

- 🔒 **Privacy-Preserving** - Raw network traffic never leaves edge nodes
- 🧠 **Federated Learning** - Collaborative training across 3 edge nodes without data sharing
- 📊 **Explainable AI** - Feature importance for every prediction
- 🛡️ **Zero Trust Ready** - Continuous authentication simulation
- 📈 **Real-time Detection** - Instant threat classification with confidence scores
- 🎯 **Risk Level Indicator** - HIGH/MEDIUM/LOW risk assessment
- 🔌 **REST API** - FastAPI-based backend for easy integration
- 🎨 **Interactive Dashboard** - Streamlit UI for real-time analysis

---

## 🏥 Business Problem

**Problem:** Traditional intrusion detection systems (IDS) struggle with 5G networks due to:
- Distributed and virtualized architecture
- Privacy regulations preventing data centralization
- High volume of network traffic
- Sophisticated cyber threats

**Solution:** A decentralized IDS using Federated Learning that:
- Trains models locally on edge nodes
- Never shares raw network data
- Provides interpretable predictions
- Continuously validates network entities

**Impact:**
- 📉 **99.7% reduction** in data communication vs centralized
- ⏱️ **<5ms inference time** per packet
- 🎯 **88% F1-Score** on UNSW-NB15 dataset
- 🔍 **100% interpretable** with feature importance
---

## 💻 Tech Stack

| Category | Technology | Version |
|----------|------------|---------|
| **Language** | Python | 3.13 |
| **Data Processing** | Pandas, NumPy | 2.0+, 1.24+ |
| **Machine Learning** | Scikit-learn, Random Forest | 1.3+ |
| **Federated Learning** | Custom FedAvg | - |
| **Interpretability** | SHAP (planned) | 0.42+ |
| **API Framework** | FastAPI, Uvicorn | 0.100+, 0.23+ |
| **Frontend** | Streamlit, Plotly | 1.28+, 5.0+ |
| **Containerization** | Docker | Latest |
| **Cloud Platform** | AWS (ECR, EC2) | - |
| **Version Control** | Git, GitHub | - |

---

## 📊 Dataset

**UNSW-NB15 Network Traffic Dataset**

- **Source:** UNSW Canberra Cyber
- **Training Samples:** 175,341 (after dedup: 96,822)
- **Testing Samples:** 82,332
- **Features:** 34 numerical features
- **Attack Categories:** 9 types + Normal
**Features Engineered (21 features):**

### Features Engineered (34 features):

| Category | Features |
|----------|----------|
| **Basic Flow** | dur, proto, service, state |
| **Packet/Byte** | spkts, dpkts, sbytes, dbytes, rate |
| **Load/Loss** | sload, dload, sloss, dloss |
| **Inter-packet** | sinpkt, dinpkt, sjit, djit |
| **TCP Window** | swin, stcpb, dtcpb, dwin, tcprtt |
| **Timing** | synack, ackdat, smean, dmean, trans_depth |
| **Content** | response_body_len |
| **Time Window** | ct_src_dport_ltm, ct_dst_sport_ltm |
| **FTP/HTTP** | is_ftp_login, ct_ftp_cmd, ct_flw_http_mthd |
| **Other** | is_sm_ips_ports |


### Attack Categories:

| Attack Type | Description | Samples |
|-------------|-------------|---------|
| Normal | Legitimate traffic | 48,894 |
| Exploits | Vulnerability exploitation | 19,360 |
| Fuzzers | Random input attacks | 14,082 |
| Reconnaissance | Information gathering | 6,000 |
| DoS | Denial of Service | 3,369 |
| Generic | General attacks | 1,800 |
| Backdoor | Unauthorized access | 1,121 |
| Analysis | Port scanning | 1,119 |
| Shellcode | Code injection | 954 |
| Worms | Self-propagating | 123 |

---

## 📈 Model Performance

### Treatment Classification Model

## 📈 Model Performance

### Federated Learning Results (3 Edge Nodes)

| Metric | Score |
|--------|-------|
| **Accuracy** | 85.5% |
| **Precision** | 80.2% |
| **Recall** | 97.8% |
| **F1-Score** | 88.2% |


### Per-Node Training Accuracy

| Node | Training Accuracy | Samples |
|------|------------------|---------|
| Node 1 | 97.9% | 79,560 |
| Node 2 | 97.9% | 79,560 |
| Node 3 | 97.9% | 79,562 |

### Detection Rate by Attack Type

| Attack Type | Detection Rate |
|-------------|----------------|
| Exploits | 94% |
| DoS | 91% |
| Fuzzers | 89% |
| Reconnaissance | 87% |
| Generic | 85% |
| Backdoor | 83% |
| Normal Traffic | 92% |

### Top Features by Importance

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | Source Load (sload) | 32% |
| 2 | Transfer Rate (rate) | 24% |
| 3 | Source Packets (spkts) | 16% |
| 4 | TCP RTT (tcprtt) | 10% |
| 5 | SYN-ACK Time (synack) | 8% |

---

## 🔌 API Endpoints

### Base URL: `http://localhost:8000`

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Health check and API info |
| `GET` | `/health` | Detailed health status |
| `POST` | `/predict` | Predict attack vs normal |
| `POST` | `/predict/batch` | Batch predictions |
| `GET` | `/docs` | Swagger UI documentation |

### Request Example

```json
POST /predict
Content-Type: application/json

{
  "features": [
    0.5, 0, 0, 0, 2000, 1500, 50000, 40000, 100,
    8000, 6000, 20, 15, 0.01, 0.01, 0, 0, 0,
    0, 0, 0, 0.5, 0.4, 0.3, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0
  ]
}
{
  "prediction": 1,
  "prediction_label": "Attack",
  "confidence": 85.3,
  "attack_category": "DoS",
  "attack_description": "Denial of Service - Resource exhaustion",
  "network_health": "UNDER ATTACK",
  "network_health_icon": "🔴",
  "top_features": [
    "✓ High source load",
    "✓ Suspicious traffic rate",
    "✓ High packet count",
    "✓ Abnormal RTT",
    "✓ Slow handshake response"
  ]
}

```

### Installation & Setup 🚀

## Prerequisites

- Python 3.10 or higher
- pip package manager
- Git (optional)

## Clone Repository
- git clone https://github.com/Ramakrishna232002/FedX-ZT-5G.git
- cd FedX-ZT-5G

## Create Virtual Environment
- python3 -m venv venv
- source venv/bin/activate  # On Windows: venv\Scripts\activate

## Install Dependencies
- pip install -r requirements.txt

## Download Dataset
- Download UNSW-NB15 dataset from: https://www.unsw.adfa.edu.au/unsw-canberra-cyber/cybersecurity/ADFA-NB15-Datasets/

## Terminal 1 - Running the Application
- cd /Users/ma-66/Desktop/p1/FedX-ZT-5G
- source venv/bin/activate
- python backend/app.py

## Terminal 2 - Start Frontend UI
- cd /Users/ma-66/Desktop/p1/FedX-ZT-5G
- source venv/bin/activate
- streamlit run frontend/app.py

## 🏗️ Architecture
```text

FedX-ZT-5G/
├── backend/
│   ├── app.py                 # FastAPI server
│   └── model_handler.py       # Model loading & prediction
├── frontend/
│   └── app.py                 # Streamlit UI
├── data/
│   ├── raw/                   # UNSW-NB15 dataset
│   │   ├── UNSW_NB15_training-set.parquet
│   │   └── UNSW_NB15_testing-set.parquet
│   ├── processed/             # Normalized data
│   │   ├── X_train_normalized.npy
│   │   ├── y_train_balanced.npy
│   │   ├── X_test.npy
│   │   └── y_test.npy
│   └── edge_nodes/            # 3 node datasets
│       ├── node1_X.npy, node1_y.npy
│       ├── node2_X.npy, node2_y.npy
│       └── node3_X.npy, node3_y.npy
├── models/
│   └── saved/
│       └── federated_models.pkl  # Trained federated model
├── notebooks/
│   └── 01_eda.ipynb           # EDA notebook
├── L.png                      # Logo image
├── requirements.txt           # Dependencies
├── .gitignore                 # Git ignore rules
└── README.md                  # Documentation

```

## 🔄 Data Flow Architecture

```text

                    ┌──────────────────────────────────────┐
                    │           5G NETWORK LAYER           │
                    │  IoT Devices | User Equipment |      │
                    │  Network Slices | Edge Nodes         │
                    └──────────────┬───────────────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────────────────┐
                    │         DATA COLLECTION              │
                    │      (Traffic Monitoring)            │
                    │   Packets | Flow | Rate | Duration   │
                    └──────────────┬───────────────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────────────────┐
                    │          PREPROCESSING UNIT          │
                    │  Cleaning | Feature Extraction |     │
                    │  Normalization | Encoding            │
                    └──────────────┬───────────────────────┘
                                   │
                                   ▼
        ┌──────────────────────────┼──────────────────────────┐
        │                          │                          │
        ▼                          ▼                          ▼
┌───────────────┐          ┌───────────────┐          ┌───────────────┐
│  EDGE NODE 1  │          │  EDGE NODE 2  │          │  EDGE NODE 3  │
│   (79,560     │          │   (79,560     │          │   (79,562     │
│    samples)   │          │    samples)   │          │    samples)   │
│               │          │               │          │               │
│ ┌───────────┐ │          │ ┌───────────┐ │          │ ┌───────────┐ │
│ │  Random   │ │          │ │  Random   │ │          │ │  Random   │ │
│ │  Forest   │ │          │ │  Forest   │ │          │ │  Forest   │ │
│ │  Model    │ │          │ │  Model    │ │          │ │  Model    │ │
│ └─────┬─────┘ │          │ └─────┬─────┘ │          │ └─────┬─────┘ │
└───────┼───────┘          └───────┼───────┘          └───────┼───────┘
        │                          │                          │
        │ (Local Weights)          │ (Local Weights)          │ (Local Weights)
        │                          │                          │
        └──────────────────────────┼──────────────────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────────────────┐
                    │         FEDERATED SERVER             │
                    │     (Model Aggregation - FedAvg)     │
                    │  Weighted Average of Local Models    │
                    └──────────────┬───────────────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────────────────┐
                    │           GLOBAL IDS MODEL           │
                    │     Ensemble of 3 Edge Nodes         │
                    └──────────────┬───────────────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────────────────┐
                    │        INTRUSION DETECTION           │
                    │      Attack / Normal Classification  │
                    └──────────────┬───────────────────────┘
                                   │
        ┌──────────────────────────┼──────────────────────────┐
        │                          │                          │
        ▼                          ▼                          ▼
┌───────────────┐          ┌───────────────┐          ┌───────────────┐
│  EXPLAINABLE  │          │   ZERO TRUST  │          │  ALERT &      │
│  AI (XAI)     │          │   ENGINE      │          │  RESPONSE     │
│               │          │               │          │               │
│ • Feature     │          │ • Continuous  │          │ • Admin       │
│   Importance  │          │   Validation  │          │   Dashboard   │
│ • SHAP Values │          │ • Device Auth │          │ • Real-time   │
│ • Top 5       │          │ • Behavioral  │          │  Notifications│
│   Contributors│          │   Baseline    │          │ • Incident    │
└───────────────┘          └───────────────┘          │   Reports     │
                                                      └───────────────┘

                                   │
                                   ▼
                    ┌──────────────────────────────────────┐
                    │           USER INTERFACE             │
                    │        (Streamlit Dashboard)         │
                    │                                      │
                    │  ┌─────────┐ ┌─────────┐ ┌─────────┐ │
                    │  │ Threats │ │Confidence││  Risk   │ │
                    │  │Detected │ │  Score  │ │  Level  │ │
                    │  └─────────┘ └─────────┘ └─────────┘ │
                    │                                      │
                    │  ┌─────────────────────────────────┐ │
                    │  │     Attack Type + Description   │ │
                    │  └─────────────────────────────────┘ │
                    │                                      │
                    │  ┌─────────────────────────────────┐ │
                    │  │    Explainability (Top Features)│ │
                    │  │  sload  ████████ 32%            │ │
                    │  │  rate   ██████   24%            │ │
                    │  │  spkts  ████     16%            │ │
                    │  └─────────────────────────────────┘ │
                    └──────────────────────────────────────┘

```

## Complete Solution Architecture - All Phases

### Federated Learning + Explainable AI + Zero Trust for 5G Network Intrusion Detection

---

## 📐 PHASE 1: DATA ENGINEERING LAYER

```text

╔═══════════════════════════════════════════════════════════════════════════════════════╗
║                         PHASE 1: DATA ENGINEERING LAYER                               ║
╚═══════════════════════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────────────────────────────────────────────┐
│                           5G NETWORK ENVIRONMENT                                    │
│                                                                                     │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                 │
│  │    IoT      │  │   User      │  │  Network    │  │   Edge      │                 │
│  │  Devices    │  │  Equipment  │  │   Slices    │  │   Nodes     │                 │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘                 │
│         │                │                │                │                        │
│         └────────────────┴────────────────┴-───────────────┘                        │
│                                    │                                                │
│                                    ▼                                                │
│                    ┌─────────────────────────────────────┐                          │
│                    │        DATA COLLECTION              │                          │
│                    │     (Traffic Monitoring)            │                          │
│                    │  • Packet Capture (pcap)            │                          │
│                    │  • Flow Export (NetFlow/IPFIX)      │                          │
│                    │  • Real-time Streaming (Kafka)      │                          │
│                    └────────────────┬────────────────────┘                          │
│                                     │                                               │
│                                     ▼                                               │
│                    ┌─────────────────────────────────────┐                          │
│                    │        RAW DATA STORAGE             │                          │
│                    │     (UNSW-NB15 Dataset)             │                          │
│                    │                                     │                          │
│                    │  ┌─────────────────────────────┐    │                          │
│                    │  │ Training: 175,341 samples   │    │                          │
│                    │  │ Testing:  82,332 samples    │    │                          │
│                    │  │ Features: 36 columns        │    │                          │
│                    │  └─────────────────────────────┘    │                          │
│                    └────────────────┬────────────────────┘                          │
│                                     │                                               │
│                                     ▼                                               │
│                    ┌─────────────────────────────────────┐                          │
│                    │        DATA PREPROCESSIN            │                          │
│                    │                                     │                          │
│                    │  ┌───────────────────────────────┐  │                          │
│                    │  │ 1. Data Cleaning              │  │                          │
│                    │  │    • Remove duplicates (44.8%)│  │                          │
│                    │  │    • Handle missing values    │  │                          │
│                    │  │    • Remove irrelevant columns│  │                          │
│                    │  └───────────────────────────────┘  │                          │
│                    │                                     │                          │
│                    │  ┌───────────────────────────────┐  │                          │
│                    │  │ 2. Feature Engineering        │  │                          │
│                    │  │    • 34 numerical features    │  │                          │
│                    │  │    • Categorical encoding     │  │                          │
│                    │  │      (proto, service, state)  │  │                          │
│                    │  │    • Label encoding for labels│  │                          │
│                    │  └───────────────────────────────┘  │                          │
│                    │                                     │                          │
│                    │  ┌───────────────────────────────┐  │                          │
│                    │  │ 3. Data Normalization         │  │                          │
│                    │  │    • StandardScaler           │  │                          │
│                    │  │    • Mean = 0, Std = 1        │  │                          │
│                    │  │    • Min-Max scaling          │  │                          │
│                    │  └───────────────────────────────┘  │                          │
│                    │                                     │                          │
│                    │  ┌───────────────────────────────┐  │                          │
│                    │  │ 4. Class Balancing (SMOTE)    │  │                          │
│                    │  │    • Before: 56k Normal,      │  │                          │
│                    │  │              119k Attack      │  │                          │
│                    │  │    • After: 119k Normal,      │  │                          │
│                    │  │              119k Attack      │  │                          │
│                    │  └───────────────────────────────┘  │                          │
│                    └────────────────┬────────────────────┘                          │
│                                     │                                               │
│                                     ▼                                               │
│                    ┌─────────────────────────────────────┐                          │
│                    │      PROCESSED DATA STORAGE         │                          │
│                    │                                     │                          │
│                    │  ┌─────────────────────────────┐    │                          │
│                    │  │ X_train_balanced: 238,682   │    │                          │
│                    │  │ y_train_balanced: 238,682   │    │                          │
│                    │  │ X_test: 82,332              │    │                          │
│                    │  │ y_test: 82,332              │    │                          │
│                    │  └─────────────────────────────┘    │                          │
│                    └─────────────────────────────────────┘                          │
└─────────────────────────────────────────────────────────────────────────────────────┘

                                    │
                                    ▼
═══════════════════════════════════════════════════════════════════════════════════════

╔═══════════════════════════════════════════════════════════════════════════════════════╗
║                         PHASE 2: FEDERATED LEARNING LAYER                             ║
╚═══════════════════════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────────────────────────────────────────────┐
│                      FEDERATED LEARNING ARCHITECTURE                                │
│                                                                                     │
│                         ┌─────────────────────────┐                                 │
│                         │   FEDERATED SERVER      │                                 │
│                         │   (Aggregation Node)    │                                 │
│                         │                         │                                 │
│                         │   Algorithm: FedAvg     │                                 │
│                         │   Rounds: 5-10          │                                 │
│                         │   Strategy: Majority    │                                 │
│                         │            Voting       │                                 │
│                         └───────────┬─────────────┘                                 │
│                                     │                                               │
│              ┌──────────────────────┼──────────────────────┐                        │
│              │                      │                      │                        │
│              ▼                      ▼                      ▼                        │
│  ┌────────────────────┐  ┌────────────────────┐  ┌────────────────────┐             │
│  │    EDGE NODE 1     │  │    EDGE NODE 2     │  │    EDGE NODE 3     │             │
│  │                    │  │                    │  │                    │             │
│  │  Data Distribution │  │  Data Distribution │  │  Data Distribution │             │
│  │  ┌──────────────┐  │  │  ┌──────────────┐  │  │  ┌──────────────┐  │             │
│  │  │ 79,560       │  │  │  │ 79,560       │  │  │  │ 79,562       │  │             │
│  │  │ samples      │  │  │  │ samples      │  │  │  │ samples      │  │             │
│  │  └──────────────┘  │  │  └──────────────┘  │  │  └──────────────┘  │             │
│  │                    │  │                    │  │                    │             │
│  │  Local Model       │  │  Local Model       │  │  Local Model       │             │
│  │  ┌──────────────┐  │  │  ┌──────────────┐  │  │  ┌──────────────┐  │             │
│  │  │Random Forest │  │  │  │Random Forest │  │  │  │Random Forest │  │             │
│  │  │n_estimators= │  │  │  │n_estimators= │  │  │  │n_estimators= │  │             │
│  │  │   100        │  │  │  │   100        │  │  │  │   100        │  │             │
│  │  │max_depth=20  │  │  │  │max_depth=20  │  │  │  │max_depth=20  │  │             │
│  │  └──────┬───────┘  │  │  └──────┬───────┘  │  │  └──────┬───────┘  │             │
│  │         │          │  │         │          │  │         │          │             │
│  │  ┌──────▼───────┐  │  │  ┌──────▼───────┐  │  │  ┌──────▼───────┐  │             │
│  │  │Train Acc:    │  │  │  │Train Acc:    │  │  │  │Train Acc:    │  │             │
│  │  │  97.9%       │  │  │  │  97.9%       │  │  │  │  97.9%       │  │             │
│  │  └──────────────┘  │  │  └──────────────┘  │  │  └──────────────┘  │             │
│  │                    │  │                    │  │                    │             │
│  │  ┌──────────────┐  │  │  ┌──────────────┐  │  │  ┌──────────────┐  │             │
│  │  │Local Weights │──┼──┼──│Local Weights │──┼──┼──│Local Weights │  │             │
│  │  └──────────────┘  │  │  └──────────────┘  │  │  └──────────────┘  │             │
│  └────────────────────┘  └────────────────────┘  └────────────────────┘             │
│              │                      │                      │                        │
│              └──────────────────────┼──────────────────────┘                        │
│                                     │                                               │
│                                     ▼                                               │
│                    ┌─────────────────────────────────────┐                          │
│                    │      FEDERATED AGGREGATION          │                          │
│                    │         (FedAvg Algorithm)          │                          │
│                    │                                     │                          │
│                    │   w_global = (1/N) * Σ w_i          │                          │
│                    │                                     │                          │
│                    │   Where:                            │                          │
│                    │   • N = Number of nodes (3)         │                          │
│                    │   • w_i = Weights from node i       │                          │
│                    │                                     │                          │
│                    └────────────────┬────────────────────┘                          │
│                                     │                                               │
│                                     ▼                                               │
│                    ┌─────────────────────────────────────┐                          │
│                    │         GLOBAL IDS MODEL            │                          │
│                    │                                     │                          │
│                    │  ┌─────────────────────────────┐    │                          │
│                    │  │ Final Aggregated Model      │    │                          │
│                    │  │ • Accuracy: 85.5%           │    │                          │
│                    │  │ • Precision: 80.2%          │    │                          │
│                    │  │ • Recall: 97.8%             │    │                          │
│                    │  │ • F1-Score: 88.2%           │    │                          │
│                    │  └─────────────────────────────┘    │                          │
│                    └─────────────────────────────────────┘                          │
└─────────────────────────────────────────────────────────────────────────────────────┘

                                    │
                                    ▼
═══════════════════════════════════════════════════════════════════════════════════════

╔═══════════════════════════════════════════════════════════════════════════════════════╗
║                         PHASE 3: INFERENCE & API LAYER                                ║
╚═══════════════════════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────────────────────────────────────────────┐
│                         INFERENCE & API ARCHITECTURE                                │
│                                                                                     │
│                    ┌─────────────────────────────────────┐                          │
│                    │      FASTAPI BACKEND SERVER         │                          │
│                    │         (Port 8000)                 │                          │
│                    │                                     │                          │
│                    │  ┌─────────────────────────────┐    │                          │
│                    │  │      API Endpoints          │    │                          │
│                    │  │  GET  /                     │    │                          │
│                    │  │  GET  /health               │    │                          │
│                    │  │  POST /predict              │    │                          │
│                    │  │  POST /predict/batch        │    │                          │
│                    │  │  GET  /docs                 │    │                          │
│                    │  └─────────────────────────────┘    │                          │
│                    │                                     │                          │
│                    │  ┌─────────────────────────────┐    │                          │
│                    │  │    Model Handler            │    │                          │
│                    │  │  • Load federated models    │    │                          │
│                    │  │  • Predict attack/normal    │    │                          │
│                    │  │  • Calculate confidence     │    │                          │
│                    │  │  • Return explainability    │    │                          │
│                    │  └─────────────────────────────┘    │                          │
│                    └────────────────┬────────────────────┘                          │
│                                     │                                               │
│                                     ▼                                               │
│                    ┌─────────────────────────────────────┐                          │
│                    │      STREAMLIT FRONTEND UI          │                          │
│                    │         (Port 8501)                 │                          │
│                    │                                     │                          │
│                    │  ┌─────────────────────────────┐    │                          │
│                    │  │      Input Section          │    │                          │
│                    │  │  • 34 Network Parameters    │    │                          │
│                    │  │  • Real-time validation     │    │                          │
│                    │  │  • Batch upload option      │    │                          │
│                    │  └─────────────────────────────┘    │                          │
│                    │                                     │                          │
│                    │  ┌─────────────────────────────┐    │                          │
│                    │  │      Dashboard Section      │    │                          │
│                    │  │  • KPI Cards (Threats,      │    │                          │
│                    │  │    Confidence, Risk)        │    │                          │
│                    │  │  • Attack Classification    │    │                          │
│                    │  │  • Explainability Bars      │    │                          │
│                    │  └─────────────────────────────┘    │                          │
│                    └─────────────────────────────────────┘                          │
└─────────────────────────────────────────────────────────────────────────────────────┘

                                    │
                                    ▼
═══════════════════════════════════════════════════════════════════════════════════════

╔═══════════════════════════════════════════════════════════════════════════════════════╗
║                         PHASE 4: EXPLAINABILITY & ZERO TRUST LAYER                    ║
╚═══════════════════════════════════════════════════════════════════════════════════════╝

┌───────────────────────────────────────────────────────────────────────────────────-──┐
│                    EXPLAINABLE AI (XAI) & ZERO TRUST ARCHITECTURE                    │
│                                                                                      │
│  ┌─────────────────────────────────────────────────────────────────────────────────-┐│
│  │                         EXPLAINABLE AI COMPONENT                                 ││
│  │                                                                                  ││
│  │  ┌─────────────────────────┐    ┌────────────────────────────────────────────-─┐ ││
│  │  │   Feature Importance    │    │           SHAP Integration (Planned)         │ ││
│  │  │                         │    │                                              │ ││
│  │  │  sload    ████████ 32%  │    │  ┌─────────────────────────────────────┐     │ ││
│  │  │  rate     ██████   24%  │    │  │  SHAP Force Plot Visualization      │     │ ││
│  │  │  spkts    ████     16%  │    │  │  ┌─────────────────────────────────┐│     │ ││
│  │  │  tcprtt   ███      10%  │    │  │  │ Higher Confidence → Higher Risk ││     │ ││
│  │  │  synack   ██       8%   │    │  │  └───────────────────────────────── │     │ ││
│  │  └─────────────────────────┘    │  └─────────────────────────────────────┘     │ ││
│  │                                 │                                              │ ││
│  │  ┌─────────────────────────────┐│  ┌─────────────────────────────────────────┐ ││
│  │  │   Attack Category Mapping   ││  │        Confidence Scoring               │ ││
│  │  │                             ││  │                                         │ ││
│  │  │  Confidence > 65% → HIGH    ││  │  ┌─────────────────────────────────────┐│ ││
│  │  │  Confidence 30-65% → MEDIUM ││  │  │  Risk = Attack Probability          ││ ││
│  │  │  Confidence < 30% → LOW     ││  │  │  Health = f(Confidence)             ││ ││
│  │  └─────────────────────────────┘│  │  └─────────────────────────────────────┘│  ││
│  │                                 │  │                                         │  ││
│  └─────────────────────────────────┘  └─────────────────────────────────────────┘  ││
│                                                                                     │
│  ┌─────────────────────────────────────────────────────────────────────────────────┐│
│  │                         ZERO TRUST ENGINE                                       ││
│  │                                                                                 ││
│  │  ┌─────────────────────────┐  ┌─────────────────────────┐  ┌───────────────────┐││
│  │  │  Continuous Validation  │  │  Device Authentication  │  │  Behavioral       │││
│  │  │                         │  │                         │  │  Baseline         │││
│  │  │  • Every request        │  │  • Unique device ID     │  │  • Normal traffic │││
│  │  │    validated            │  │  • Token verification   │  │    patterns       │││
│  │  │  • No implicit trust    │  │  • Session management   │  │  • Anomaly        │││
│  │  │  • Least privilege      │  │                         │  │    detection      │││
│  │  └─────────────────────────┘  └─────────────────────────┘  └───────────────────┘││
│  │                                                                                 ││
│  └─────────────────────────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────────────────────────┘

                                    │
                                    ▼
═══════════════════════════════════════════════════════════════════════════════════════

╔═══════════════════════════════════════════════════════════════════════════════════════╗
║                         PHASE 5: DEPLOYMENT & MONITORING LAYER                        ║
╚═══════════════════════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────────────────────────────────────────────┐
│                       DEPLOYMENT & MONITORING ARCHITECTURE                          │
│                                                                                     │
│  ┌─────────────────────────────────────────────────────────────────────────────────┐│
│  │                         CI/CD PIPELINE (GitHub Actions)                         ││
│  │                                                                                 ││
│  │  ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐        ││
│  │  │ GitHub  │───▶│ GitHub  │───▶│ Docker  │───▶│  AWS    │───▶│  AWS    │        ││
│  │  │  Code   │    │ Actions │    │  Build  │    │   ECR   │    │   EC2   │        ││
│  │  └─────────┘    └─────────┘    └─────────┘    └─────────┘    └─────────┘        ││
│  │                                                                                 ││
│  └─────────────────────────────────────────────────────────────────────────────────┘│
│                                                                                     │
│  ┌─────────────────────────────────────────────────────────────────────────────────┐│
│  │                         CONTAINER ORCHESTRATION                                 ││
│  │                                                                                 ││
│  │  ┌─────────────────────────────────────────────────────────────────────────────┐││
│  │  │                              Docker Compose                                 │││
│  │  │                                                                             │││
│  │  │  ┌──────────────────┐         ┌──────────────────┐                          │││
│  │  │  │   backend        │         │   frontend       │                          │││
│  │  │  │   (FastAPI)      │◀───────▶│   (Streamlit)    │                          │││
│  │  │  │   Port: 8000     │         │   Port: 8501     │                          │││
│  │  │  └──────────────────┘         └──────────────────┘                          │││
│  │  │                                                                             │││
│  │  └─────────────────────────────────────────────────────────────────────────────┘││
│  │                                                                                 ││
│  └─────────────────────────────────────────────────────────────────────────────────┘│
│                                                                                     │
│  ┌─────────────────────────────────────────────────────────────────────────────────┐│
│  │                         MONITORING & OBSERVABILITY                              ││
│  │                                                                                 ││
│  │  ┌─────────────────────────┐  ┌─────────────────────────┐                       ││
│  │  │     CloudWatch          │  │     Performance         │                       ││
│  │  │                         │  │     Metrics             │                       ││
│  │  │  • API Logs             │  │  • Response Time        │                       ││
│  │  │  • Error Tracking       │  │  • Throughput           │                       ││
│  │  │  • Resource Usage       │  │  • Error Rate           │                       ││
│  │  │  • Drift Detection      │  │  • Model Accuracy       │                       ││
│  │  └─────────────────────────┘  └─────────────────────────┘                       ││
│  │                                                                                 ││
│  │  ┌─────────────────────────┐  ┌─────────────────────────┐                       ││
│  │  │     Alerts &            │  │     Retraining          │                       ││
│  │  │     Notifications       │  │     Trigger             │                       ││
│  │  │                         │  │                         │                       ││
│  │  │  • Slack Integration    │  │  • Weekly retraining    │                       ││
│  │  │  • Email Alerts         │  │  • On-data drift        │                       ││
│  │  │  • PagerDuty            │  │  • Manual trigger       │                       ││
│  │  └─────────────────────────┘  └─────────────────────────┘                       ││
│  │                                                                                 ││
│  └─────────────────────────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────────────────────────┘

                                    │
                                    ▼
═══════════════════════════════════════════════════════════════════════════════════════

╔═══════════════════════════════════════════════════════════════════════════════════════╗
║                              COMPLETE DATA FLOW SUMMARY                               ║
╚═══════════════════════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────────────────────────────────────────────┐
│                                                                                     │
│   5G Network ──▶ Data Collection ──▶ Preprocessing ──▶ Federated Learning           │
│       │                │                    │                   │                   │
│       │                │                    │                   │                   │
│       ▼                ▼                    ▼                   ▼                   │
│   [IoT]           [Packets]           [34 Features]      [3 Edge Nodes]             │
│   [UE]            [Flows]             [Normalized]       [Local Models]             │
│   [Slices]        [Rates]             [Balanced]         [FedAvg Agg]               │
│                                                                                     │
│                                    │                                                │
│                                    ▼                                                │
│                          ┌─────────────────────┐                                    │
│                          │   Global IDS Model  │                                    │
│                          └──────────┬──────────┘                                    │
│                                    │                                                │
│                    ┌───────────────┼───────────────┐                                │
│                    │               │               │                                │
│                    ▼               ▼               ▼                                │
│              ┌──────────┐   ┌──────────┐   ┌──────────┐                             │
│              │  Attack  │   │  Normal  │   │  Explain │                             │
│              │  Detected│   │  Traffic │   │  -ability│                             │
│              └────┬─────┘   └────┬─────┘   └────┬─────┘                             │
│                   │              │              │                                   │
│                   └──────────────┼──────────────┘                                   │
│                                  │                                                  │
│                                  ▼                                                  │
│                    ┌─────────────────────────────────────┐                          │
│                    │         User Dashboard              │                          │
│                    │  • Threats Detected: X              │                          │
│                    │  • Confidence: X%                   │                          │
│                    │  • Risk Level: HIGH/MEDIUM/LOW      │                          │
│                    │  • Attack Type: [Classification]    │                          │
│                    │  • Explainability: Top Features     │                          │
│                    └─────────────────────────────────────┘                          │
│                                                                                     │
└─────────────────────────────────────────────────────────────────────────────────────┘

═══════════════════════════════════════════════════════════════════════════════════════

```


