# ML-CVDs 🫀 Cardiovascular Disease Prediction Project

This project builds an **agent-based machine learning system** to predict the **presence of cardiovascular disease (CVD)** in individuals, using demographic, anthropometric, clinical, and lifestyle features. The dataset consists of ~70,000 individuals aged **29–64 years**.

---

## 📊 Dataset Description

The dataset contains the following features:

| Feature                  | Type              | Description |
|---------------------------|------------------|-------------|
| `age`                    | Objective (int)   | Age in days (to be converted to years) |
| `height`                 | Objective (cm)    | Height in centimeters |
| `weight`                 | Objective (kg)    | Weight in kilograms |
| `gender`                 | Objective (binary)| 1 = female, 2 = male |
| `ap_hi`                  | Examination (int) | Systolic blood pressure |
| `ap_lo`                  | Examination (int) | Diastolic blood pressure |
| `cholesterol`            | Examination (cat) | 1 = normal, 2 = above normal, 3 = well above normal |
| `gluc`                   | Examination (cat) | 1 = normal, 2 = above normal, 3 = well above normal |
| `smoke`                  | Subjective (bin)  | Smoking status (1 = yes, 0 = no) |
| `alco`                   | Subjective (bin)  | Alcohol intake (1 = yes, 0 = no) |
| `active`                 | Subjective (bin)  | Physical activity (1 = yes, 0 = no) |
| `cardio` (target)        | Binary            | Presence of cardiovascular disease (1 = yes, 0 = no) |

---

## ⚙️ Data Preprocessing

1. **Outlier Removal**   

2. **Feature Engineering**  

3. **Encoding**  

## 🔬 Exploratory Data Analysis (EDA)

- **Univariate Analysis**
- **Bivariate Analysis** 
- **Multivariate Analysis**

---

## 🔗 Medically Plausible Interactions

The following 2-way interactions were considered:

- **Blood Pressure × Age** (`age:ap_hi`, `age:ap_lo`)  
- **Age × Cholesterol** (`age:cholesterol`)  
- **Age × Smoking** (`age:smoke`)  
- **BMI × Glucose** (`BMI:gluc`)  


---

## 🤖 Modeling


---

## 📈 Libraries used
- **pandas**

- **numpy**

- **matplotlib / seaborn**

- **statsmodels**

- **scikit-learn**


---