# 🔐 Selenium Login Automation - BrowserStack Demo

This project automates the login process for [BrowserStack's Demo Site](https://www.bstackdemo.com/) using **Selenium WebDriver**, **Python**, and **Pytest**, following the **Page Object Model (POM)** design pattern.

---

## 🚀 Project Overview

- **Objective**: Automate login functionality for a demo e-commerce web app.
- **Tech Stack**:
  - Selenium WebDriver
  - Python 3.11
  - Pytest for test execution
  - WebDriver Manager for handling browser drivers
  - POM (Page Object Model) for clean test architecture

---

## 📁 Project Structure

login_automation/
│
├── src/
│   ├── __init__.py
│   ├── pages/                     # Page Object classes
│   │   ├── __init__.py
│   │   ├── homepage.py
│   │   └── sign_in_page.py
│   └── utils/                     # Utility/helper modules
│       └── helpers.py
│
├── tests/                         # Test files
│   ├── __init__.py
│   └── test_login.py
│
├── conftest.py                    # Pytest fixtures (setup/teardown)
├── requirements.txt              # Dependencies
├── README.md                     # Project documentation

# Cache and metadata (auto-generated)
├── .pytest_cache/                # Pytest cache
├── __pycache__/                  # Python bytecode cache

---

## 🧪 How to Run This Project

### 1. 🔧 Install Dependencies

Make sure you have Python 3.11+ and `pip` installed.

```bash
pip install -r requirements.txt
```

### 2. ▶️ Run the Test

```bash
pytest tests/test_login.py -s
```

---

## ✅ Key Features

- Complete login flow automation
- Clean separation via Page Object Model
- Explicit waits for stability
- Pytest fixtures to manage setup and teardown
- Assertion to verify successful login
- Utility functions via src/utils/helpers.py for future scaling

---

## 📸 Example Output

```bash
Login Successful
.
1 passed in 5.21s
```

---

## 📌 Future Enhancements

- Add negative test scenarios (e.g., invalid credentials)
- Add logout and product/cart interactions
- Screenshot capture on test failure
- CI integration (GitHub Actions, Jenkins, etc.)
- Test reporting with pytest-html or Allure

---

## 👨‍💻 Author

Zach Coleman
QA Automation Engineer in Training

---

## 🏁 License

This project is intended for educational and portfolio use. You are free to clone, modify, and use it for personal learning or demo purposes.