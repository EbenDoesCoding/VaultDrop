## Summary
<!-- What does this MR do, and why? 1-3 sentences. -->

## Related
- Stage: <!-- timeline stage number -->
- Closes: <!-- #issue -->

## Type of change
- [ ] Feature
- [ ] Bug fix
- [ ] Refactor (no behaviour change)
- [ ] Tests
- [ ] Docker / Compose / DB
- [ ] CI / Makefile
- [ ] Docs (README)
- [ ] Demo prep
- [ ] Chore (deps, config)

## Endpoints affected
- [ ] create
- [ ] resolve
- [ ] list
- [ ] stats
- [ ] none

## Changes
-

## How to test
```bash
make test
make up
# curl examples here
```

---

## Checklist

### Code quality
- [ ] Service code lives in `src/`
- [ ] No dead code, debug prints, or commented-out blocks
- [ ] Linter/formatter passes (`make lint` if defined)
- [ ] Functions/variables named clearly; no unexplained magic values
- [ ] Errors return correct HTTP status codes and messages

### API
- [ ] Request/response models validated (Pydantic)
- [ ] Edge cases handled: not found, duplicate, expired, invalid input
- [ ] OpenAPI docs (`/docs`) still accurate
- [ ] No breaking change to existing endpoints (or documented below)

### Database
- [ ] Schema changes included (migration/init script)
- [ ] Works on a fresh DB volume (`docker compose down -v && up`)
- [ ] Queries parameterised (no string-built SQL)
- [ ] Stats/list queries tested with realistic data

### Tests
- [ ] New/changed behaviour has tests (happy path + failure path)
- [ ] `make test` passes locally
- [ ] Tests don't depend on order or leftover data
- [ ] No tests skipped/disabled without reason

### Docker / Compose
- [ ] `docker compose up` starts API + DB cleanly from scratch
- [ ] DB healthcheck / `depends_on` still correct
- [ ] No hardcoded host ports or credentials in images
- [ ] `.dockerignore` up to date

### Makefile / CI
- [ ] Make targets used here still work (`up`, `down`, `test`, ...)
- [ ] GitLab CI pipeline is green
- [ ] New CI steps are fast and cached where sensible

### Dependencies (`uv`)
- [ ] `pyproject.toml` and lockfile both updated
- [ ] No unused or unpinned packages added

### Security
- [ ] No secrets, tokens, or `.env` committed
- [ ] Config via environment variables
- [ ] User input never trusted (validated/escaped)
- [ ] Error responses don't leak internals

### Docs
- [ ] README updated (setup, usage, endpoints) if anything changed
- [ ] New env vars documented
- [ ] Contributors list unchanged/correct

### Git hygiene
- [ ] Branch up to date with `main`, no conflicts
- [ ] Commits have clear messages
- [ ] MR is small and focused on one thing
- [ ] Source branch will be deleted after merge

### Demo readiness
- [ ] Change works in the demo flow (create → resolve → list → stats)
- [ ] Nothing here breaks a clean-clone setup

---

## Risks / trade-offs
<!-- What could go wrong? Alternatives considered? -->

## Breaking changes
<!-- None / describe -->

## Notes for reviewer
<!-- Where to look closely -->

/assign_reviewer @B
