# Git

| Task | Command |
|---|---|
| Inspect changes | `git status --short` |
| Inspect unstaged diff | `git diff` |
| Inspect staged diff | `git diff --cached` |
| Stage one file | `git add README.md` |
| Commit | `git commit -m "docs: update guide"` |
| New branch | `git switch -c feature/example` |
| Update safely | `git pull --ff-only` |
| Publish branch | `git push -u origin HEAD` |
| Undo published commit | `git revert COMMIT_SHA` |
| Inspect history | `git log --oneline -10` |

Review diffs before staging secrets. Prefer revert over rewriting shared history.

## Official reference

[Git documentation](https://git-scm.com/docs)
