# 🧪 Selenium Login Automation

This is a simple and clean Selenium automation project using Python, Pytest, and the Page Object Model (POM). It automates logging into the [BrowserStack Demo site](https://www.bstackdemo.com/), validates success, and demonstrates good structure for QA automation portfolios.

---

## 📁 Project Structure

```
login_automation/
├── .github/
│   └── workflows/
│       └── ci.yml   
├── src/
│   └── pages/
│       ├── homepage.py
│       └── sign_in_page.py
│
├── tests/
│   └── test_login.py
│
├── reports/                # Auto-generated HTML test reports
│   └── latest_report.html
│
├── screenshots/            # Screenshots taken on test failure
│   └── test_login.png
│
├── conftest.py             # Pytest fixtures + screenshot-on-failure logic
├── requirements.txt        # Dependencies
├── pytest.ini              # Pytest config for output + report
├── .gitignore
├── README.md
```

---

## 🔧 Setup Instructions

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 2. Run the test

This runs the login test, captures terminal output, saves a test report, and takes screenshots on failure:

```bash
pytest
```

Thanks to `pytest.ini`, this automatically:
- Shows `print()` statements in terminal (`-s`)
- Saves an HTML report to `reports/latest_report.html`
- Saves screenshots to `screenshots/` if a test fails

---

## ✅ Features

- ✅ Selenium WebDriver with Chrome
- ✅ Page Object Model (POM) structure
- ✅ Pytest test runner
- ✅ Fixtures for setup/teardown
- ✅ Explicit waits using `WebDriverWait`
- ✅ Assertion for verifying login
- ✅ Screenshot capture on failure
- ✅ HTML test reporting via `pytest-html`
- ✅ Organized, professional project layout
- ✅ CI pipeline with GitHub Actions

---

🚀 GitHub Actions CI
This project runs automated tests on every push and pull request to the main branch using GitHub Actions.

Workflow: .github/workflows/ci.yml
- Installs dependencies
- Runs tests via pytest
- Saves reports/report.html as a downloadable artifact

---

## 🖼 Screenshot on Failure

When a test fails, a screenshot is saved to:

```
screenshots/<test_name>.png
```

Example: `screenshots/test_login.png`

---

## 📊 HTML Test Report

After test runs, open the generated report here:

```
reports/latest_report.html
```

Use `--self-contained-html` for standalone reports (no CSS assets):

```bash
pytest --self-contained-html --html=reports/<your_report>.html
```

---

## 🔮 Future Enhancements

- ❌ Negative test scenarios (invalid credentials)
- 🛒 Cart and product interaction tests
- 📷 Embed screenshots directly in HTML report
- 🌐 Parallel test execution (e.g. with pytest-xdist)
- ☁️ Deploy reports to GitHub Pages or S3

---

## 👨‍💻 Author

**Zach Coleman**  
*QA Automation Engineer in Training*  
<!-- LinkedIn and GitHub coming soon -->

---

## 🏁 License

This project is intended for educational and portfolio use. You’re free to clone, modify, and share for personal or demo purposes.
