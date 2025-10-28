# 🧭 BuffTeks Commit Ritual - How To Guide

Welcome to the **BuffTeks Commit Ritual** How-To Guide! 🎉  
This guide will walk you through **every step** to complete the **BuffTeks Commit Ritual** and make your first contribution to our project and student organization!

---

## ⚙️ 1. What You Need First

Before starting, make sure you have:

| Tool                    | Why You Need It                | How to Check           |
| ----------------------- | ------------------------------ | ---------------------- |
| **Python 3.8+**        | To run the ritual program      | `python --version`     |
| **Git**                 | To save and share your changes | `git --version`        |
| **GitHub Account**      | To contribute to the project   | Sign up at GitHub.com  |
| **Internet Connection** | To validate your GitHub profile| Open GitHub.com        |

---

## 📥 2. Get the Project Code

Choose **ONE** method below:

### Method A: Using Git Bash Terminal

```bash
# 1. Clone the project to your computer
git clone https://github.com/TorresjDev/BuffTeks-Commit-Ritual.git

# 2. Go into the project folder
cd BuffTeks-Commit-Ritual

# 3. Install required packages
pip install -r requirements.txt
```

### Method B: Using VS Code (Easier!)

1. Open **VS Code**
2. Press `Ctrl+Shift+P` (Windows) or `Cmd+Shift+P` (Mac)
3. Type: **"Git: Clone"**
4. Paste: `https://github.com/TorresjDev/BuffTeks-Commit-Ritual.git`
5. Choose a folder to save it
6. Open the terminal in VS Code: `Ctrl+`` 
7. Run: `pip install -r requirements.txt`

---

## 🌿 3. Create Your Feature Branch

Before making any changes, create your own branch to work on:

### Method A: Using Git Bash Terminal

```bash
# Create and switch to a new branch
git checkout -b <branch-name>

# Verify you're on the new branch
git branch
```

### Method B: Using VS Code

1. **Click** the branch name in the bottom-left status bar (should show "main")
2. **Select** **"Create new branch..."**
3. **Type** your branch name:  `<branch-name>`
4. **Press Enter**

**Why create a branch?** 
- Keeps your changes separate from the main code
- Allows you to experiment safely
- Required for creating Pull Requests

---

## 🚀 4. Run the BuffTeks Ritual

Now Run the program & begin your initiation!

```bash
python main.py
```

### What Happens:
1. **Loading Animation** - Cool progress bars and emojis! 💫
2. **System Check** - Validates your setup
3. **GitHub Username** - Enter your GitHub username
4. **Name Verification** - Confirm or enter your full name
5. **Magic!** - Your name gets added to the Hall of Fame automatically! 🏆

✅ **Ritual Complete!** You'll see your name in the `README.md` file.

---

## 📤 5. Save and Share Your Changes

Your changes are currently only on your computer. Let's save them properly and share them!

### Method A: Using Git Bash Terminal

```bash
# 1. Check what files changed
git status

# 2. STAGE your changes (prepare them for saving)
git add . # Stages all changes
# or
git add README.md # Stages just the README file

# 3. COMMIT your changes (save them with a message)
git commit -m "Init: first commit to BuffTeks!"

# 4. PUSH your branch to GitHub (share them with the world)
git push -u origin <branch-name> # branch-name --> buff-dev-<your-github-username>
```

### Method B: Using VS Code (Visual Way!)

#### Step 1: Stage Your Changes
1. **Click** the **Source Control** icon (left sidebar - looks like a branch)
2. You'll see `README.md` under "Changes"
3. **Click** the **"+"** next to `README.md` 
   - This **stages** the file (prepares it for saving)
   - The file moves to "Staged Changes" section

#### Step 2: Commit Your Changes  
1. **Type** a message in the text box: `Init: first commit to BuffTeks!`
2. **Click** the **"Commit"** button
   - This **saves** your changes with the message

#### Step 3: Push Your Branch to GitHub
1. **Click** **"Publish Branch"** (if first time pushing this branch)
   - OR **Click** **"Sync Changes"** or the sync icon
   - This **pushes** your branch to GitHub

---

## 🔄 6. Create a Pull Request

A **Pull Request** is how you ask the project maintainers to review and accept your changes.

### Step-by-Step:
1. Go to the main project: `https://github.com/TorresjDev/BuffTeks-Commit-Ritual`
2. GitHub will show a yellow banner: **"Compare & pull request"** - **click it!**
3. Fill out the form:
   - **Title**: `Init: first commit to BuffTeks!`
   - **Description**: `Completed BuffTeks Commit Ritual initiation`
4. **Click** **"Create pull request"**

🎉 **Done!** Your contribution is now waiting for review.

---

## 🎓 7. Understanding Git Workflow

You just learned the **core Git workflow** that every developer uses:

1. **📥 Clone** - Get the project code
2. **🌿 Branch** - Create your own workspace (`git checkout -b`)
3. **✏️ Edit** - Make your changes (run the ritual!)
4. **📋 Stage** - Select which changes to save (`git add`)
5. **💾 Commit** - Save changes with a message (`git commit`)  
6. **📤 Push** - Send changes to GitHub (`git push`)
7. **🔄 Pull Request** - Ask to merge your changes

**Think of it like this:**
- **Branch** = Get your own workspace/room
- **Stage** = Put items in your shopping cart
- **Commit** = Buy the items (final decision)
- **Push** = Ship the items to the store
- **Pull Request** = Ask the store to put items on shelves

---

## ✅ 8. What Happens Next?

1. **Review** - A project maintainer will review your changes
2. **Approval** - If everything looks good, they'll approve it
3. **Merge** - Your changes get added to the main project
4. **Celebration** - Your name is now permanently in the BuffTeks Hall of Fame! 🏆

---

## 🆘 9. Troubleshooting

| Problem                    | Solution                                    |
| -------------------------- | ------------------------------------------- |
| `python: command not found` | Install Python from python.org           |
| `git: command not found`    | Install Git from git-scm.com             |
| `ModuleNotFoundError`      | Run `pip install -r requirements.txt`    |
| `Network Error`            | Check your internet connection            |
| `Username Not Found`       | Double-check your GitHub username spelling |
| `Permission denied`        | You might need to authenticate with GitHub |
| `Branch already exists`    | Use a different branch name or switch to existing branch |

---

## 🌟 10. What You Just Learned

Congratulations! You just learned:

- ✅ How to **clone** a repository
- ✅ How to **create a branch** (`git checkout -b`)
- ✅ How to **stage** changes (`git add`)
- ✅ How to **commit** changes (`git commit`)
- ✅ How to **push** to GitHub (`git push`)
- ✅ How to create a **Pull Request**

These are the **core skills** every developer uses daily!

---

## 🚀 11. Next Steps

To expand your skills:

* CLI Commands **Git Github Cheatsheet**: [Git Cheatsheet](https://education.github.com/git-cheat-sheet-education.pdf)
* Git Commands **Git Cheatsheet**: [Git Cheatsheet](https://git-scm.com/cheat-sheet.html)
* Try **Rich Library**: [Rich Docs](https://rich.readthedocs.io/en/stable/) 🔥

---

## 🆘 Need Help?

- **Stuck?** Ask on our Discord server
- **Bug?** Create an issue on GitHub
- **Questions?** Reach out to a BuffTeks mentor

---

**Built with ❤️ by the BuffTeks Student Organization**  
West Texas A&M University – Paul & Virginia Engler College of Business
visit us at [buffteks.org](https://buffteks.org)

---

### 🐃 "Clone it. Branch it. Stage it. Commit it. Push it. Own it."