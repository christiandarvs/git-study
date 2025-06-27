## Tasks:
1. Create 3 branches {b1, b2, b3} :white_check_mark:
2. Merge branches {b3} to {b1} :white_check_mark:
3. Merge branches {b3} to {b2}, then delete {b3} :white_check_mark:

## Branches:
- Main
- B1: {b1.py, b3.py}
- B2: {b2.py}
- B3: {b3.py}


## After task 3:
- Main
- B1: {b1.py, b3.py}
- B2: {b2.py, b3.py}

## Git commands used:
```
git checkout -b <branch-name>
git reset --hard <id>
git merge <branch-name>
git log
git log --oneline --decorate (compact info)
```