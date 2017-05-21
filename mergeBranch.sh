#!/bin/bash
echo "Merging one branch to another"
echo "First switch to branch"
echo "branch to checkout :$1"
git checkout $2
echo "On branch: $2"
git branch
echo "Now merging branch: $1 to $2"
git merge --no-commit --no-ff origin/$1
git status
echo "-------------------------"
echo "Now commiting changes"
echo "-------------------------"
git commit -m "merge $1 to $2"
git status
echo "----------------------"
echo "Pushing to remote branch $2"
echo "----------------------"
git push origin master
echo "Done pushing branch: $2"
