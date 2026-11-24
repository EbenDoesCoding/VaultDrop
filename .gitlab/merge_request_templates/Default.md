## Summary
<!-- What does this MR do, and why? 1-3 sentences. -->

Closes: <!-- #issue -->

## Type of change
- [ ] Feature
- [ ] Bug fix
- [ ] Tests
- [ ] Security hardening
- [ ] Docker / CI / Makefile
- [ ] Docs

## Changes
-

## How to test
```bash
make lint
make test
make run   # http://localhost:3000
# curl examples here
```

## Checklist

### Code
- [ ] Service code in `src/`, frontend in `frontend/`
- [ ] `make lint` passes
- [ ] Correct status codes: 400 invalid, 404 not found, 410 expired/used

### Tests
- [ ] New behaviour has tests, including bad input
- [ ] `make test` passes locally and CI is green

### Docker / DB
- [ ] Works on a clean setup (`docker compose down -v && make run`)
- [ ] Queries are parameterised

### Security
- [ ] No secrets committed (`.env` / `DROP_KEY` stay local)
- [ ] Secrets never logged or returned except on a successful open

### Docs & Git
- [ ] README updated if setup, endpoints or Make targets changed
- [ ] `pyproject.toml` and `uv.lock` both updated if deps changed
- [ ] Small, focused MR; branch up to date with `main`
- [ ] Demo flow still works: create → open → open again (410)

## Risks / trade-offs
<!-- What could go wrong? Alternatives considered? None is fine. -->

## Notes for reviewer
<!-- Where to look closely. -->

