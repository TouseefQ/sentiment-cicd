# 🚀 CI/CD Sentiment Analysis Pipeline

### Automated Testing & Deployment for AI

**The Goal:** Build a robust "DevOps" pipeline that automatically tests and deploys a Machine Learning application whenever code is pushed to GitHub.

**The App:** A Flask-based API that uses Natural Language Processing (TextBlob) to detect sentiment (Positive/Negative/Neutral).

---

## ⚙️ Architecture

The pipeline consists of three main stages:

1.  **Push:** Developer pushes code to GitHub.
2.  **CI (Continuous Integration):**
    * **GitHub Actions** triggers a workflow.
    * Installs Python 3.9 & dependencies.
    * Runs the test suite (`pytest`) to verify the AI logic.
    * *Guardrail:* If tests fail, the deployment is blocked.
3.  **CD (Continuous Deployment):**
    * **Render** detects the successful commit.
    * Automatically deploys the new version to the production server.

---

## 🛠️ Tech Stack

* **Language:** Python 3.9
* **Framework:** Flask
* **AI Engine:** TextBlob
* **Testing:** Pytest
* **CI/CD:** GitHub Actions (CI) + Render (CD)
* **Server:** Gunicorn

---

## 🔗 Live Demo

**Base URL:** `https://sentiment-cicd-touseefq.onrender.com/`

**Test Endpoint:** `/predict` (POST)

---

## 🧪 How to Run Locally

If you want to run this project on your own machine:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/TouseefQ/sentiment-cicd
    cd sentiment-cicd
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run Tests:**
    ```bash
    python -m pytest
    ```

4.  **Start the Server:**
    ```bash
    python app.py
    ```

---

## 🧠 Project Learnings

* **Automated Verification:** The importance of running tests on a clean "runner" (Ubuntu) to ensure code works outside my local machine.
* **Pipeline Configuration:** Writing YAML workflows for GitHub Actions.
* **Production Deployment:** Configuring `gunicorn` for stable cloud hosting.