# 🧭 BuffTeks Commit Ritual - How To Guide

Welcome to your first digital ritual, BuffTeks member! 🎉
This guide will walk you through every step to install, run, and complete the **BuffTeks Commit Ritual** — your initiation into our developer community.

---

## ⚙️ 1. Prerequisites

Before starting, make sure your system has:

| Requirement             | Version                        | Check Command      |
| ----------------------- | ------------------------------ | ------------------ |
| **Python**              | 3.8 or higher                  | `python --version` |
| **Git**                 | Latest                         | `git --version`    |
| **Internet Connection** | Required for GitHub validation | Open GitHub.com    |

### 🧰 Install Dependencies

After cloning the repository, install the required packages:

```bash
pip install -r requirements.txt
```

---

## 🚀 2. Run the Commit Ritual

To begin your journey:

```bash
python main.py
```

When you start the program, you’ll see the **BuffTeks Loading Ritual** — a dynamic, emoji-filled progress animation powered by the **Rich** library. 💫

### 🪄 The Ritual Process

1. **System Validation:** The app checks for Python, Git, and required dependencies.
2. **Workshop Loading:** A visual sequence simulates our digital initiation process.
3. **Member Input:** You’ll be prompted to enter your **GitHub username** (and optionally your name).
4. **Verification:** The app validates your GitHub profile live.
5. **Hall of Fame Update:** Your name is written into the `README.md` automatically! 🏆

---

## 💻 3. What Happens Behind the Scenes

Each time you run the ritual:

* **`validator.py`** ensures your environment is ready.
* **`ui.py`** runs the animated loading sequence using `Rich.Progress` and emoji indicators.
* **`logic.py`** verifies your GitHub username via API and safely appends it to the Hall of Fame table in the README.
* **`main.py`** orchestrates it all.

---

## 🧱 4. Verifying Your Success

After completing the ritual, open your `README.md` file.
Scroll down to the **Hall of Fame** section. You should see a new entry like this:

| Name      | GitHub                                       | Join Date  |
| --------- | -------------------------------------------- | ---------- |
| Your Name | [@YourGitHub](https://github.com/YourGitHub) | YYYY-MM-DD |

✅ Congratulations — you are now officially a **BuffTeks Contributor!**

---

## 🧠 5. Troubleshooting

| Issue                 | Cause                            | Solution                              |
| --------------------- | -------------------------------- | ------------------------------------- |
| `ModuleNotFoundError` | Missing dependency               | Run `pip install -r requirements.txt` |
| `Network Error`       | No internet connection           | Connect to WiFi and retry             |
| `Username Not Found`  | Incorrect GitHub handle          | Double-check spelling                 |
| `Permission Denied`   | README locked or unsaved changes | Commit or unlock file                 |

---

## 🧩 6. Learn More

To expand your skills:

* Explore **Git Basics**: [Git Documentation](https://git-scm.com/doc)
* Learn **GitHub Collaboration**: [GitHub Guides](https://guides.github.com/activities/hello-world/)
* Try **Rich Library**: [Rich Docs](https://rich.readthedocs.io/en/stable/)

---

## 🐃 7. Join the Legacy

Once you’ve completed the ritual, share your success on Discord or LinkedIn using the hashtag **#BuffTeksCommitRitual** 🔥
Encourage other members to join, contribute, and keep our developer legacy alive.

---

**Built with Pride by the BuffTeks Student Organization**
West Texas A&M University – Paul & Virginia Engler College of Business
