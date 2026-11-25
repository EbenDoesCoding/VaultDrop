# Contributing to VaultDrop

## Workflow

1. Branch from current `main`. Use `feature/<name>`, `fix/<name>`, or `docs/<name>`.
2. Keep commits focused and use your own Git identity. Write short, imperative messages such as `Document VaultDrop demo setup`.
3. Open a merge request into `main`. Explain the change and how you verified it.
4. Have another team member review and merge the MR after GitLab CI passes.

## Verification

- Run `make test` before pushing code changes. It uses a dedicated test database.
- For API changes, cover successful requests and applicable failure cases, including invalid input, unknown tokens, expiry, and exhausted views.
- For UI changes, verify the create, copy, open, and reveal flow in a browser.
- For setup changes, follow the README from a fresh checkout and record the result.

## Secrets

Keep `.env`, encryption keys, real drop tokens, and sensitive demo data out of commits and merge requests. Use dummy secrets when testing or taking screenshots.

## AI use

AI was used strictly as a tutor and code checking. Code committed and merged was all done by the group.
