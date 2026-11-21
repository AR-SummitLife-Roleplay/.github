# .github

Organization-wide settings for Caldera: the shared CI workflows every repository calls, default issue and pull request templates, the security policy and the organization's public profile page.

| | |
| --- | --- |
| Owner | Development Lead |
| Visibility | [Assumed] Public: GitHub requires it for organization-wide templates and the profile page. It never holds secrets or private plans. |
| Status | Scaffolded 2026-11-21; nothing built yet |

## Setup

1. Clone this repository.
2. Change shared workflows carefully: every repository calls them.

## Shared Workflows (to be written)

| Workflow | Does |
| --- | --- |
| `hygiene.yml` | Secret scan, workflow lint, formatting, links |
| `framework-checks.yml` | Framework text checks and Workbench checks |
| `addon-build.yml` | Pack, size budget, Workshop publish |
| `platform-ci.yml` | Tests, image builds, scans |
| `notify-discord.yml` | Results to Discord |

Details: `caldera-handbook`, `Documentation/Engineering/Delivery/CI-CD-And-Release-Management.md`

## Documents

- This repository: [Documentation/README.md](Documentation/README.md).
- Project-wide (features, rules, architecture, delivery): `caldera-handbook`, starting at `Documentation/README.md`.
