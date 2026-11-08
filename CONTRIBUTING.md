# Contributing to VaultDrop

## Workflow
- No commits to `main`. Work on a branch: `feature/<name>`, `fix/<name>`, `docs/<name>`.
- Open a merge request (MR) into `main`. The other member reviews and merges.
- Never merge your own MR.
- Each member commits under their own Git identity.

## Commits
- Short, imperative messages: `Add create-link endpoint`.
- One logical change per commit.

## Merge requests
- Small and focused; describe what changed and how to test it.
- CI (`make test`) must pass before merging.
- Reviewer responds within 24h.

## Code
- Every new behaviour gets a test, including bad input (400/404).
- Run `make test` before pushing.

## AI use
- Tutor use only: explanations, small suggestions we read, edit and understand.
- Never commit code we can't explain.
- Tools and purposes are disclosed in the README.
