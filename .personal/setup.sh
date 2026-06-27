#!/usr/bin/env bash
# .personal/setup.sh — make your OWN private Bible-study space.
#
# In plain words, this script:
#   1. Makes a folder named by your email inside .personal/ (e.g. you@example.com/)
#   2. Fills it from the starter kit (_template/)
#   3. Turns THAT folder into its own private git repo
#   4. (optional) points it at your own private git so you can push
#
# Your folder is invisible to this public repo — the repo is told to look away
# from it (see .personal/.gitignore). Your email and your notes never get
# pushed to GitHub from here. Where your private repo lives is YOUR choice.
#
# Run it from the repo root:   bash .personal/setup.sh
# Works in Git Bash (Windows), WSL, Linux, and macOS.

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

printf 'Your email (used only as your folder name — stays on YOUR machine): '
read -r EMAIL
[ -z "$EMAIL" ] && { echo "No email given — nothing to do."; exit 1; }

DEST="$SCRIPT_DIR/$EMAIL"
if [ -e "$DEST" ]; then
  echo "You already have a space: .personal/$EMAIL/  — just open it and study."
  exit 0
fi

# Copy the starter kit (no git history) into your new folder.
cp -r "$SCRIPT_DIR/_template" "$DEST"
rm -rf "$DEST/.git" 2>/dev/null || true

# Turn your folder into its own private repo.
cd "$DEST"
git init -b main >/dev/null
git add -A
git commit -m "Start my personal Bible-study space" >/dev/null
echo "Created your private space: .personal/$EMAIL/  (its own git repo)"

printf 'Optional — your private git URL to push to (Enter to skip): '
read -r REMOTE
if [ -n "$REMOTE" ]; then
  git remote add origin "$REMOTE"
  echo "Linked to $REMOTE  —  push anytime with:  git push -u origin main"
fi

cat <<EOF

Done. Your folder is ignored by the public repo, so your notes stay private.
Daily rhythm:
  read a chapter  ->  write in .personal/$EMAIL/  ->  git commit  ->  push to YOUR git
EOF
