# FreeBuff Practice Project

This tiny Python project is for practicing FreeBuff's local review and Git workflow.

## Guided workflow

1. In FreeBuff, choose this original folder: `/Users/anurag/Documents/FreeBuff-Demo`.
2. Scan the project. FreeBuff should find the unprotected division in `app.py`.
3. Open the finding, inspect the proposed change, and approve it.
4. Scan again. The project should be ready to commit.
5. Prepare the Git review and create a local commit. FreeBuff adds that commit summary to `CHANGELOG.md`.
6. Push and open a pull request only after connecting a repository you own or have permission to update.

The initial bug is intentional and safe: running `python3 app.py` before the fix exits with `ZeroDivisionError`; after the reviewed fix it prints a zero fallback.
