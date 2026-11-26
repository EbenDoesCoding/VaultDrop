# Security Policy

## Reporting a Vulnerability

Please report security issues privately. Do not open a public issue.

- Contact: `ejohnvalson@gmail.com`
- Include: description, steps to reproduce, and potential impact.

We aim to acknowledge reports within 3 business days and provide a fix or mitigation plan within 14 days.

## Scope

In scope:

- Secret exposure, or viewing a drop after it expired or reached its view limit
- Bypassing view limits (e.g. race conditions)
- Token guessing or enumeration
- Weaknesses in encryption or key handling
- Injection, XSS, or other flaws in the API or frontend

Out of scope:

- Attacks requiring access to the server environment or `DROP_KEY`
- Denial of service through high traffic
- Issues in third-party dependencies with no demonstrated impact on VaultDrop
- Social engineering

## How VaultDrop Protects Secrets

- Secrets are encrypted at rest.
- Links use long, random tokens, and only a hash of each token is stored.
- Each view is consumed atomically, and the secret is deleted once its views run out or it expires.
- Expired drops are purged automatically.
- API responses are not cached.

## Operator Guidance

- Set a strong `DROP_KEY`, keep it secret, and never commit it.
- Serve VaultDrop over HTTPS only.
- Change the default database credentials and avoid exposing the database port.
- Keep dependencies up to date.
- Back up `DROP_KEY` securely: losing it makes stored secrets unrecoverable.

## Supported Versions

Only the latest version on the main branch receives security fixes.

## Disclosure

We ask for a reasonable period to fix issues before public disclosure. Reporters acting in good faith will be credited if they wish.
