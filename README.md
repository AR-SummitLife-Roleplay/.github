# .github

Organization-wide settings for Caldera: the shared CI workflows every repository calls, default issue and pull request templates, the security policy and the organization's public profile page.

| | |
| --- | --- |
| Owner | Development Lead |
| License | All rights reserved: [LICENSE.md](LICENSE.md). Not open source. |
| Visibility | [Assumed] Public: GitHub requires it for organization-wide templates and the profile page. It never holds secrets or private plans. |
| Status | Shared checks running since 2026-11-21; Windows build runner jobs not yet |

## Setup

1. Clone this repository.
2. Change shared workflows carefully: every repository calls them.

## Shared Workflows

| Workflow | Does |
| --- | --- |
| `hygiene.yml` | Secret scan, workflow lint and security scan, formatting, JSON and YAML parsing, links |
| `framework-checks.yml` | Framework text checks; Workbench checks once the Windows build runner exists |
| `addon-build.yml` | File names, Git LFS pointers, file sizes; pack and Workshop publish once the Windows build runner exists |
| `platform-ci.yml` | Fails if platform code exists without checks; real checks come with the first code |
| `notify-discord.yml` | Failed runs to Discord |

How to call them, turn on the Windows runner and set up Discord: [Documentation/README.md](Documentation/README.md).
Details: `caldera-handbook`, `Documentation/Engineering/Delivery/CI-CD-And-Release-Management.md`

## Documents

- This repository: [Documentation/README.md](Documentation/README.md).
- Project-wide (features, rules, architecture, delivery): `caldera-handbook`, starting at `Documentation/README.md`.
