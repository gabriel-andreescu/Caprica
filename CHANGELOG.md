# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

## [2026.9.16] - 2026-09-16

### Added

- Provide built-in Skyrim and Fallout 4 user flags when no flags file is supplied.

### Fixed

- Evaluate compound-assignment targets once, including member receivers and array indices.
- Accept `Parent` and `Self` struct member names in Fallout 4.
- Fix compilation hanging after writing PEX files during temporary namespace cleanup.

## [2026.9.15] - 2026-09-15

### Fixed

- Allow native functions in Skyrim scripts.
- Report custom Skyrim events as warnings instead of errors.
- Fix single-script Fallout 4 compilation returning success without writing a PEX.

[Unreleased]: https://github.com/gabriel-andreescu/Caprica/compare/v2026.9.16...HEAD
[2026.9.16]: https://github.com/gabriel-andreescu/Caprica/compare/v2026.9.15...v2026.9.16
[2026.9.15]: https://github.com/gabriel-andreescu/Caprica/releases/tag/v2026.9.15
