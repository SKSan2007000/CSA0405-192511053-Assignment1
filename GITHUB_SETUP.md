# Create and publish the required GitHub repository
1. Go to https://github.com/new and sign in.
2. Repository name: `CSA04-192511053-Assignment1`.
3. Choose Public, or Private and add your course faculty as collaborator.
4. Do not initialise with README, licence or .gitignore (these are already in this project).
5. Extract this ZIP and open PowerShell/Terminal in the extracted `CSA04-192511053-Assignment1` folder.
6. Configure your verified Git identity:
   `git config --global user.name "B. Santhosh Kumar"`
   `git config --global user.email "YOUR-VERIFIED-GITHUB-EMAIL"`
7. Initialise and commit each task progressively:
   `git init`
   `git branch -M main`
   `./commit_each_task.sh` (run in Git Bash/Ubuntu; if on PowerShell, use the individual commands in GITHUB_COMMIT_PLAN.md).
8. Add remote and push:
   `git remote add origin https://github.com/YOUR-USERNAME/CSA04-192511053-Assignment1.git`
   `git push -u origin main`
9. Add actual screenshots from your own Ubuntu machine to `Screenshots/`, then `git add Screenshots && git commit -m "Add personal execution screenshots" && git push`.
10. Copy the actual repository URL to the Word report and submit it to faculty.
