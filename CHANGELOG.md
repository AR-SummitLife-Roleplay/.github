# Changelog

All notable changes to `.github` are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added

- Platform CI builds every service's container image.
- Platform CI runs integration tests against a real PostgreSQL 18.
- Platform CI runs lint, type check, unit tests and a dependency audit.
- Shared workflows: hygiene (secret scan, workflow lint and security scan, formatting, links), framework checks, addon file checks, platform guard and Discord notifications, with their check scripts.
- Repository scaffold: folder layout, top-level files and documentation map.
