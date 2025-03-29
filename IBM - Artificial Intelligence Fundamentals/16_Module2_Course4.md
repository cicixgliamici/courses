# Preparing a Machine Learning Project in IBM Watson Studio

## Module Objectives
By the end of this module, you will be able to:
1. **Set up an ML project** in IBM Watson Studio
2. **Create a Cloud Object Storage resource**
3. **Import datasets** into Watson Studio

---

## 1. Setting Up a Project in Watson Studio

### Steps
| Step | Action                                 | Details                                                                      |
|------|----------------------------------------|------------------------------------------------------------------------------|
| 1    | Log in to **IBM Cloud**                | [IBM Cloud Console](https://cloud.ibm.com)                                   |
| 2    | Navigate to **Watson Studio**          | From the services catalog → "AI/Machine Learning" category                   |
| 3    | Create a new project                   | *Project Name*: Assign an identifier (e.g., "ML_Project_Test")                |
| 4    | Associate **Cloud Object Storage**     | Select an existing instance or create a new one                              |

### Requirements
- Active IBM Cloud account
- Permissions to create resources (role **Editor** or higher)

---

## 2. Creating a Cloud Object Storage Resource

### Procedure
1. From the IBM Cloud catalog:

       Catalog → Storage → Cloud Object Storage

2. Configure the service:
   | Option               | Recommended Value                      |
   |----------------------|----------------------------------------|
   | **Pricing Plan**     | Lite (free)                            |
   | **Instance Name**    | e.g., "cos-ml-dataset"                 |
   
3. Click **Create** → Link the instance to your Watson Studio project

**Key Features:**
- Secure storage for datasets and models
- Direct integration with Watson Studio

---

## 3. Importing a Dataset into Watson Studio

### Supported Methods
| Method                   | Description                                                                     |
|--------------------------|---------------------------------------------------------------------------------|
| **Direct Upload**        | Drag and drop files (CSV, Excel, JSON, etc.) into the editor                    |
| **Public URL**           | Enter a link to externally hosted datasets (e.g., GitHub, Kaggle)                 |
| **Cloud Object Storage** | Select a file from the COS instance linked to the project                       |

### Supported Formats
- CSV, XLSX, JSON, Parquet
- Images (JPG/PNG in ZIP archives)
- Text files (TXT, PDF)

### Data Preparation
1. Verify the file encoding (UTF-8 recommended)
2. Remove duplicate or irrelevant data
3. Define column types (numeric, categorical, date)

---

## Operational Checklist
- [ ] Watson Studio project created
- [ ] Cloud Object Storage instance configured
- [ ] Dataset imported and validated

---

> **Tip**: Use the integrated **Jupyter Notebooks** in Watson Studio to perform exploratory data analysis (EDA) and data cleaning before model training.

## Next Steps
1. Connect data to a notebook for analysis
2. Configure runtime (CPU/GPU) for training
3. Experiment with **AutoAI** for pre-optimized models
