# Bash and Linux

| Task | Command |
|---|---|
| Current directory | `pwd` |
| List files | `ls -lah` |
| Disk space | `df -h` |
| Directory size | `du -sh .` |
| Find files | `find . -name '*.json'` |
| Search text | `grep -R -n -- 'needle' .` |
| Processes | `ps aux` |
| Check script syntax | `bash -n script.sh` |

```bash
set -euo pipefail
for file in ./*.txt; do
  [[ -f "$file" ]] || continue
  printf '%s\n' "$file"
done
```
Quote paths and inspect targets before deleting or changing permissions.

## Official reference

[Bash and Linux documentation](https://www.gnu.org/software/bash/manual/)
