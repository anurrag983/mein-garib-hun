# FreeBuf practice project 2

This is a disposable Python project for practicing FreeBuf's scan, finding review, approved-fix, and local Git commit workflow.

The API-looking value in `app.py` is fabricated scanner-training data, not a working credential. Never copy it into a real service. The unguarded division is intentional; running `app.py` directly will raise `ZeroDivisionError`. FreeBuf scans source without executing the project.

## Try it in FreeBuf

1. Choose **Add folder** and select this folder.
2. Select **Scan project**. The findings should point to the credential and division lines in `app.py`.
3. Open each finding to review the code context and proposed fix. Save only fixes you approve.
4. Scan again and check the updated findings.
5. Prepare a Git review and make a local commit. This folder has a local Git repository but no GitHub remote, so pushing requires a repository URL and GitHub authentication.
