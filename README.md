# 🐍 Python DS & AI 複習筆記

> 用於存放 Python 資料科學（Data Science）與人工智慧（AI）相關的複習筆記、練習程式碼與專案實作。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)

---

## 📖 目錄

- [專案說明](#專案說明)
- [主題涵蓋範圍](#主題涵蓋範圍)
- [目錄結構（規劃）](#目錄結構規劃)
- [環境需求](#環境需求)
- [使用方式](#使用方式)
- [授權](#授權)

---

## 專案說明

本 Repo 作為個人學習歷程的記錄空間，包含：

- Python 語法與資料結構複習
- 資料科學工具（NumPy、Pandas、Matplotlib 等）練習
- 機器學習演算法原理與實作（scikit-learn）
- 深度學習框架入門（TensorFlow / PyTorch）
- 資料分析與視覺化實戰案例

---

## 主題涵蓋範圍

| 類別 | 主題 |
|------|------|
| **Python 基礎** | 資料型態、串列/字典/集合、函式、物件導向、例外處理、模組 |
| **資料處理** | NumPy 陣列運算、Pandas DataFrame 操作、資料清理 |
| **資料視覺化** | Matplotlib、Seaborn 圖表繪製 |
| **機器學習** | 監督式學習、非監督式學習、模型評估、特徵工程 |
| **深度學習** | 神經網路基礎、CNN、RNN、Transformer 概念 |
| **自然語言處理 (NLP)** | 文字前處理、詞向量、文本分類 |
| **電腦視覺 (CV)** | 影像前處理、卷積神經網路應用 |

---

## 目錄結構（規劃）

```
python-DS-review/
├── 01_python_basics/        # Python 基礎語法複習
├── 02_numpy/                # NumPy 陣列與數值運算
├── 03_pandas/               # Pandas 資料處理
├── 04_visualization/        # 資料視覺化
├── 05_machine_learning/     # 機器學習演算法
│   ├── supervised/          #   監督式學習
│   └── unsupervised/        #   非監督式學習
├── 06_deep_learning/        # 深度學習
│   ├── tensorflow/
│   └── pytorch/
├── 07_nlp/                  # 自然語言處理
├── 08_computer_vision/      # 電腦視覺
└── projects/                # 完整專案實作
```

---

## 環境需求

- Python 3.8+
- 建議使用虛擬環境（`venv` 或 `conda`）

### 常用套件

```bash
pip install numpy pandas matplotlib seaborn scikit-learn jupyter
# 深度學習（擇一）
pip install tensorflow
pip install torch torchvision
```

---

## 使用方式

1. **Clone 此 Repo**

   ```bash
   git clone https://github.com/YU-XIANG-0925/python-DS-review.git
   cd python-DS-review
   ```

2. **建立虛擬環境**

   ```bash
   python -m venv venv
   source venv/bin/activate        # macOS / Linux
   venv\Scripts\activate           # Windows
   ```

3. **安裝相依套件**

   ```bash
   pip install -r requirements.txt
   ```

4. **開啟 Jupyter Notebook**

   ```bash
   jupyter notebook
   ```

---

## 授權

本專案採用 [MIT License](LICENSE) 授權。
