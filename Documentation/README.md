# Documentation

> **Purpose:** The map of `.github`'s documents and how the shared workflows are used. Project-wide documents live in `caldera-handbook`; link to them instead of copying them here.
> **Owner:** Development Lead · **Last Reviewed:** 2026-11-21

## This Repository

| Path | Owns |
| --- | --- |
| `.github/workflows/` | The shared workflows every repository calls, and this repository's own CI (`ci.yml`). |
| `.github/actionlint.yaml` | Workflow lint settings: the self-hosted runner label. |
| `Scripts/` | The check scripts the shared workflows run, and the workflow security scan settings (`zizmor.yml`). |
| `ISSUE_TEMPLATE/`, `PULL_REQUEST_TEMPLATE.md` | Default issue and pull request forms for every repository. |
| `SECURITY.md` | How to report a security problem privately. |
| `profile/README.md` | The organization's public profile page. |

## Shared Workflows

Each repository's `.github/workflows/ci.yml` calls these at `main`, so a change here reaches every repository at once. Test a change on a pull request in this repository first: its own CI runs the hygiene checks with the scripts from the pull request.

| Workflow | Runs | Where |
| --- | --- | --- |
| `hygiene.yml` | Secret scan of the whole history (gitleaks), workflow lint (actionlint) and security scan (zizmor), formatting, JSON and YAML parsing, Markdown links. | GitHub-hosted, every repository |
| `framework-checks.yml` | The framework text checks from `caldera-framework`'s `Scripts/Checks`. Workbench checks once the Windows runner exists. | GitHub-hosted; Windows runner later |
| `addon-build.yml` | File and folder names, Git LFS pointers and file sizes. Packing and Workshop publishing on pushes to `main` once the Windows runner exists. | GitHub-hosted; Windows runner later |
| `platform-ci.yml` | Fails as soon as platform code exists without its checks; the real checks are written with the first code, once the stack is chosen. | GitHub-hosted |
| `notify-discord.yml` | Posts a failed run on `main` to the team's Discord channel. | GitHub-hosted |

### Turning On the Windows Build Runner

`framework-checks.yml` and `addon-build.yml` have a `windows-runner` input that defaults to off. When the runner exists, with the labels `self-hosted`, `Windows` and `Workbench`:

1. Add `Scripts/Checks/Run-WorkbenchChecks.ps1` to `caldera-framework` and `Scripts/Build/Publish-Addon.ps1` to each addon repository.
2. Change the input's default to `true` in both workflows.

Until then, those jobs write a notice saying they are not running yet. A job turned on without its script fails, so nothing is skipped silently.

### Discord Notifications

Add the team channel's webhook address to each repository as the `DISCORD_WEBHOOK_URL` secret (repository settings, Secrets and variables, Actions). Only failures on `main` are posted. Without the secret, failed runs only show on GitHub. Which repository posts to which channel: `caldera-handbook`, `Documentation/Engineering/Delivery/Developer-Discord.md`.

### Tool Versions

`hygiene.yml` pins every tool's version, and checks the downloaded gitleaks and actionlint files against their published SHA-256 checksums. Third-party actions are pinned to a commit. To update a tool, change its version and checksum together.

## In the Handbook (`caldera-handbook`)

| Need | Document |
| --- | --- |
| Checks, builds and releases | `Documentation/Engineering/Delivery/CI-CD-And-Release-Management.md` |
| Folder layout of every repository | `Documentation/Engineering/Architecture/Repository-Layouts.md` |
| Components, data, repositories, access | `Documentation/Engineering/Architecture/System-Architecture.md` |
