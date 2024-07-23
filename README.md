[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=15453478&assignment_repo_type=AssignmentRepo)
# Setup
This will download Lab 7 locally, allowing you to work on your scripts and upload (push) them back up to GitHub.

1. Clone your lab repository into your ~/ops445/lab7 directory using SSH:
```bash
git clone <ssh link> ~/ops445/lab7/
```
2. Copy your backed-up work into your new GitHub-linked directory:
```bash
cp ~/old_ops445/lab7/* ~/ops445/lab7/
```

# Submission
1. There is no checking script for this lab.

2. Paste the output of **running your scripts for this lab** into *laboutput.txt*:
```bash
vi ~/ops445/lab7/laboutput.txt
```

3. Commit and push (upload) your lab work:
```bash
git add lab*
git commit -m "Individual message or note."
git push
```

You can make changes to your scripts and reupload as many times as you like. Make sure you commit+push to do so.

**Note:** Your lab is automatically submitted at the due date and time using the last published code. Any changes you publish after the due date won't be marked or seen by your professor.
