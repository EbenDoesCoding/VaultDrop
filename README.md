# DevOps-FinalProject

Link service: create, resolve, list and view stats for links. Built with Python, FastAPI, Postgres, Docker Compose and GitLab CI.

## Project Contributors

| Role       |Name              |Student Numbers|
|------------|------------------|---------------|
| Repo Owner | Eben John Valson |A00065522      |
| Maintainer | Abhinav Giridhar |A00022864      |
| Developer  | Subham Bhuyan    |A00050174      |
| Developer  | Christa Gigi     |A00060458      |
| Developer  | Khalid Ogidan    |A00056115      |

## Quick start
```
git clone <https://gitlab.computing.dcu.ie/eben.johnvalson2/devops-finalproject.git>
cd <devops-finalproject/>
make test
make run        # http://localhost:3000 (override: make run PORT=4000)
```

## Features
- Create a link
- Resolve a link (counts a hit)
- List links
- Per-link hit stats
- Data stored in Postgres

## API
| Method | Route | Result |
|---|---|---|
| POST | /links | Create a link |
| GET | /links/{id} | Resolve a link and count a hit |
| GET | /links | List links |
| GET | /links/{id}/stats | Hit stats |

Bad input returns 400. Unknown id returns 404.

## Requirements
- Git
- Make
- Docker and Docker Compose
- Python 3.12+ (only for running without Docker)

## Make targets
| Command | Action |
|---|---|
| `make build` | Build the Docker image |
| `make test` | Run the test suite |
| `make run` | Start API + database with Compose |
| `make clean` | Remove Vim undo/swap files and caches |

## Project structure
app/ service code
tests/ test suite
Dockerfile API image
compose.yaml API + Postgres
Makefile build / test / run / clean
.gitlab-ci.yml CI pipeline

## Contact

Any questions about the project or the repository should be directed to the repo owner, Eben: eben.johnvalson2@mail.dcu.ie

### Last Updated

Saturday, 07 November 2026

### License & Project Status

MIT License - code is free to use and adapt by all.
Status: In Development

<!-- Future sections, Project Overview, Setup, Usage, etc -->
