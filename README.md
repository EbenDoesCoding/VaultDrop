# VaultDrop

VaultDrop lets you share a text secret through a link that expires after a set time or number of views. FastAPI serves the browser interface and API. PostgreSQL stores the encrypted secret, expiry, and remaining views.

## Project Contributors

| Role       |Name              |Student Numbers|
|------------|------------------|---------------|
| Repo Owner | Eben John Valson |A00065522      |
| Maintainer | Abhinav Giridhar |A00022864      |
| Developer  | Subham Bhuyan    |A00050174      |
| Developer  | Christa Gigi     |A00060458      |
| Developer  | Khalid Ogidan    |A00056115      |

## Quick start

You need Git, Make, Docker with Compose v2, and `uv`. Docker must be running.

```bash
git clone <https://gitlab.computing.dcu.ie/eben.johnvalson2/vault-drop.git>
cd <vault-drop/>
uv sync --locked
```

For a fresh checkout, generate a local encryption key:

```bash
(umask 077; uv run --locked python -c 'from cryptography.fernet import Fernet; print("DROP_KEY=" + Fernet.generate_key().decode())' > .env)
```

Reuse the same `DROP_KEY` when restarting an instance with existing drops. And as always keey `.env.` out of Git.

```bash
make build
make test
make run
```

Open [VaultDrop](http://localhost:3000/). Run `make down` to stop the stack.

## Demo the service

1. Enter a secret and set the **Maximum views** to `1`.
2. Create the drop and copy the share link.
3. Open the link in a private window and refresh before clicking the **Reveal Secret**.
4. Click **Reveal secret** and confirm the message appears.
5. Reopen the same link and try revealing again. The drop should be unavailable.

## API

| Method | Route             | Result                                               |
|--------|-------------------|------------------------------------------------------|
| `POST` | `/drops`          | Creates a drop and returns its token with `201`.     |
| `GET`  | `/drops/{token}`  | Returns the secret with `200` and consumes one view. |
| `GET`  | `/health`         | Reports that the app is responding.                  |

Create requests accept `secret`, `max_views`, and `ttl_seconds`. Invalid input returns `400`. An unknown token returns `404`. An exhausted or expired drop returns `410` while its record exists. After expiry cleanup removes the record, the token returns `404`.

## Tests and CI

`make test` starts a dedicated PostgreSQL test service and runs pytest against `vaultdrop_test`. The tests cover creation, view limits, expiry, storage, and frontend routing. GitLab CI runs pytest with its own PostgreSQL service and publishes a JUnit report.

## Requirements

- Git
- Make
- Docker and Docker Compose
- Python 3.12+ (only for running without Docker)
- uv

## Make targets

| Command      | Action                                |
|--------------|---------------------------------------|
| `make build` | Build the Docker image                |
| `make test`  | Run the test suite                    |
| `make run`   | Start API + database with Compose     |
| `make clean` | Remove Vim undo/swap files and caches |
| `make down`  | Stop the service gracefully           |

## Project layout

- `src/` — FastAPI app, drop lifecycle, encryption, and database access.
- `frontend/` — Sender and recipient pages.
- `tests/` — Automated tests.
- `Dockerfile`, `compose.yaml`, `Makefile` — Build, run, and test workflow.
- `.gitlab-ci.yml` — GitLab pipeline.

## Contact

Any questions about the project or the repository should be directed to the repo owner, [Eben John Valson](eben.johnvalson2@mail.dcu.ie).

### Last Updated

Wednesday, 25 November 2026

### License & Project Status

MIT. See [LICENSE](LICENSE) - code is free to use and adapt by all.
