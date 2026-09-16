# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Fixed

- Fix CK-compatible compilation rejecting bare `Scriptname` declarations with Windows line endings.
- Fix a crash when optimization removes redundant instructions.
- Fix Skyrim compilation rejecting a block-local variable when the same name is declared later in an outer scope.
- Fix compilation of DebugOnly and BetaOnly return values, including when their calls are removed in release or final mode.
- Fix crashes when compilation or import preparation reports an error.

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
