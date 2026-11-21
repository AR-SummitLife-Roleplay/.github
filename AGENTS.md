# Agent Instructions: .github

> **Purpose:** How AI coding agents and new developers work in `.github`. Project-wide documents live in `caldera-handbook`; this file covers this repository only.

## This Repository

Organization-wide settings for Caldera: the shared CI workflows every repository calls, default issue and pull request templates, the security policy and the organization's public profile page.

- **Owner:** Development Lead
- **Access:** [Assumed] Public. Development Lead writes; everyone can read.

## Before You Start

1. Read `caldera-handbook`, `Documentation/Engineering/Standards/Engineering-Principles.md` (what good work looks like) and `Documentation/Engineering/Development/Working-With-AI-Agents.md` (the loop every task follows: understand, ask once, look before building, build small, prove it, update documents, hand over). If `caldera-handbook` is cloned beside this repository, it is at `../caldera-handbook/`.
2. Read this repository's `Documentation/README.md`.
3. Read the `caldera-handbook` documents for your task: `Documentation/Product/Product-Requirements.md` for features and business rules (the only home for tuning values), and `Documentation/Engineering/Architecture/System-Architecture.md` for how the parts fit together.
4. Check whether what you need already exists, here or in another team's published addon, before building it.

## Always

- Stay inside this repository's scope. If a change needs another repository, say so and link it; never copy another team's code or files here.
- Follow the folder and naming rules in `caldera-handbook`, `Documentation/Engineering/Architecture/Repository-Layouts.md`.
- This repository is public: never add secrets, internal plans, server addresses or anything not meant for players to see.
- Every repository calls these workflows; test a change on one repository before merging it here.
- GitHub fixes this repository's name and the names `profile/`, `ISSUE_TEMPLATE/`, `.github/workflows/`, `PULL_REQUEST_TEMPLATE.md` and `SECURITY.md`; keep them exactly.
- Update the documentation that owns what you changed, in the same change. Do not create summary, notes or status files.
- Add a line to `CHANGELOG.md` under Unreleased for anything players, staff or other teams will notice.
- Everything here is under [LICENSE.md](LICENSE.md): all rights reserved. Never copy any of it outside Caldera's repositories, and never add anything Caldera does not own or have the right to use.
- Never commit secrets, passwords, tokens or live server settings.
- Never weaken a check, test or security control to get a passing result.
- Do not push, merge, tag, publish to the Workshop, deploy or delete data without explicit approval from this repository's owner.
- Before calling a task done, run this repository's checks (listed in Working With AI Agents) and end with the hand-over report: done, checked, not checked, decisions, next.
