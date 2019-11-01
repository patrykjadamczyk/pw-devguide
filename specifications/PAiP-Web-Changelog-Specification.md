# PAiP Web Changelog Specification 1.0.0

## What is a changelog ?

A changelog is a file which contains a curated, chronologically ordered list of notable changes for each version of a project.

## Why make a changelog ?

To make it easier for users, contributors and everyone to see precisely what notable changes have been made betwwen each release (or version) of the project.

## Who needs a changelog ?

People do. Whether consumers or developers, the end users of software are human beings who care about what's in the software or anything else that need changelogs and versions. When it changes, people want to know why and how.

## Release Block Sections

### Special Sections

- `Informations` - for specifing informations about specific release

### Changes
- `Added` - for new features
- `Changed` - for changes in existing functionality
- `Deprecated` - for soon-to-be removed features
- `Removed` - for now removed features
- `Fixed` - for any bug fixes
- `Security` - for any fixes related to security vulnerabilities
- `Regression` - for changes that are regressions

## Rules of changelog

1. Changelogs are for humans, not machines
2. There should be an entry for every single version
3. The same types of changes should be grouped
4. Versions and sections should be linkable
5. The latest comes first
6. The release date of each version is displayed
7. Changes made in development of next release version should be under `Unreleased` Release Block
8. All dates in changelog should be ISO standard date (`YYYY-MM-DD`)

## Filename of changelog
It should be one of the following:
* `CHANGELOG.md` - Prefered
- `CHANGELOG.rst`
- `HISTORY.md` / `HISTORY.rst`

## Yanked Release

Yanked releases are versions that had to be pulled because of a serious bug or security issue.
They should be noted in changelog as `[YANKED]` after version and date.

## Example

```md
# Changelog
## [1.0.0] - 2017-06-20
### Added
- New feature A
### Changed
- Feature B to have additional power
```
