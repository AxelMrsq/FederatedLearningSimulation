# Federated Learning Simulation: Master's Project

This repository contains the framework for a **Federated Learning (FL)** simulation using TensorFlow. This project is structured to first validate the local environment before launching distributed training simulations.

---

## 🛠️ Phase 1: Environment Setup

### 1. Virtual Environment
This project requires **Python 3.11** to ensure compatibility with specific TensorFlow versions.
```command prompt
# Create the environment
py -3.11 -m venv tf_env

# Activate the environment (Windows)
.\tf_env\Scripts\activate
```

###2. Dependencies
Install all necessary packages, including TensorFlow and data processing libraries:
```command prompt
pip install -r requirements.txt
```

###3. Dataset Preparation
The **Imagenette2-160** dataset is provided as a compressed ```.tgz``` file due to GitHub storage limits. Use the utility script to extract and organize the data:
```command prompt
py util.py
```

---

##🧪 Phase 2: Set up Validation
Before running a full federated simulation, verify that TensorFlow can access your hardware and that the dataset is correctly loaded by running a baseline training test:
```command prompt
py test.py
```

---

##🌐 Phase 3: Federated Learning Simulation
Once the setup is validated, the project moves into the Federated Learning phase. This mimics a network of decentralized clients training a global model without sharing raw data.

**work in progress**

