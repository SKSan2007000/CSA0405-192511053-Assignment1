#!/bin/sh
set -eu
git init
git branch -M main
git config user.name "B. Santhosh Kumar"
echo "Git identity configured with your name. Set your own verified email using:"
echo 'git config user.email "YOUR-VERIFIED-GITHUB-EMAIL"'
echo "After setting your email, run this script again only if no commits exist."
