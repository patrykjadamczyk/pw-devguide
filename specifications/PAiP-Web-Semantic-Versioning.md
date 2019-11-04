# PAiP Web Semantic Versioning 1.0.0

## Format of Version

Here are some options which you can use:

```javascript
`${major}`
`${major}.${minor}`
`${major}.${minor}.${patch}`
`${major}.${minor}.${patch}.${build}`
`${major}.${minor}.${patch}+${metadata}
`${major}.${minor}.${patch}-${release_type}${release_level}`
`${major}.${minor}.${patch}-${release_type}${release_level}+${metadata}`
```

## Meaning behind number names inside version

- **major**
	- Increment this version if you made one of the following:
    	- Changed API so it is not backward compatible (API)
        - Changed UI in very strong manner (UI)
        - Changed meaning of any section which provide you with completely another meaning in the end (Text)
    - Special versions that have specific meaning under this version:
    	- `0.*` - This is version for initial development. This version means that anything may change at any time and anything under this version shouldn't be considered stable.
        - `1.0` - This is first release version. This version means that base of thing which you are building is considered stable enough that can be run or used on production environment.
- **minor**
    - This version have to reset to 0 on change of major
	- Increment this version if you made one of the following (M1):
    	- Changed API in backwards compatible manner (API)
        	- New backward compatible functionality
            - New deprecation of functionality
            - New functionality or improvements are introduced within the private code
        - Changed UI in any way that is not bug fix (UI)
        - Changed phrasing of any section which provide you with exactly same or similiar meaning in the end (Text)
- **patch**
	- Increment this version if you made one of the following (M1):
    	- Changed API due to bug fixing in backwards compatible manner (API)
        - Changed UI due to bug fixing (UI)
        - Fixed typos or small phrasing issues which doesn't change meaning (Text)
    - Definitions needed for this version:
    	- Bug fix - internal change that fixes incorrect behaviour
    - This version have to reset to 0 on change of any upper level of version
- **build**
	- This element of version is used only in very specific situations
    - It's not recommended to use this if you don't really need it
    - Increment this version if you make new build of current version
    - This version should to reset to 0 on change of any upper level of version
- **metadata**
	- Here is section where you can add your metadata if you need it
    - It's not recommended to use this if you don't really need it
- **release_type**
	- This section of version is for specifing in which element of version lifecycle is current version
    - Possible values of this section are:
    	- `dev`
        	- This specifies development version of application
            - Using this version should signalize to the user that this version is unstable and can have bugs because it's still in active development
        - `alpha` or `a`
        	- This specifies alpha version of application
            - Using this version should signalize to the user that this version is more stable than dev version but can have bugs because it's still in active development.
            - In this version new features can go in.
        - `beta` or `b`
        	- This specifies beta version of application
            - Using this version should signalize to the user that this version should be stable, still can have small bugs because of it's development but features of it shouldn't change.
        - `rc` or `candidate`
        	- This specifies release candidate version of application
            - Using this version should signalize to the user that this version should be completely stable, this version should be mainly for getting feedback on new features and for finding last bugs that might be left.
- **release_level**
	- This part of version is for next number of version inside current version lifecycle
    - Increment this version if you made any changes when inside a version lifecycle described above
    - This version have to reset to 0 on change of any upper level of version or change of release type
    
### Legend
- **`M1`** - These rules apply only for major > 0
    
## Types of elements that can be versioned
- **`API`** - If it is anything with public API interface
- **`UI`** - If it is anything frontend related ( meaning everything which user can interact with as part of application )
- **`Text`** - If it is anything text related ( meaning things like books, documentation etc. )

## Rules of versioning

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in [RFC 2119](http://tools.ietf.org/html/rfc2119).

1. `major`, `minor`, `patch`, `build` and `release_level` are non-negative integers, and MUST NOT contain leading zeroes.  Each element MUST increase numerically. For instance: 1.9.0 -> 1.10.0 -> 1.11.0.
2. Once versioned package has been released, the contents of that version MUST NOT be modified. Any modifications MUST be released as a new version.

## Precedence

```javascript
'1' < '2'
'1.1' < '1.2'
'1.1.1' < '1.1.2'
'1.1.1.1' < '1.1.1.2'
'1.1.1+20130313144700' == '1.1.1+exp.sha.5114f85' // Metadata is ignored
'1.1.1-dev1' < '1.1.1-dev2'
'1.1.1-dev2' < '1.1.1-alpha1'
'1.1.1-dev2' < '1.1.1-beta1'
'1.1.1-dev2' < '1.1.1-rc1'
'1.1.1-dev2' < '1.1.1-rtm1'
'1.1.1-dev2+20130313144700' == '1.1.1-dev2+exp.sha.5114f85' // Metadata is ignored
'1.2' < '1.2.1.2'
'1.2' > '1.2-dev2'
/*
 * Precedense is on side of `1.4-dev1` but through package managers
 * should be used `1.3` because `1.4-dev1` is pre release
 */
'1.3' < '1.4-dev1'
```
