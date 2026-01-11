# How to contribute?

Thank you for investing your time in interacting with the repo and suggesting changes

| :exclamation:  **Read this file before you make any change to the repo**   |
|----------------------------------------------------------------------------|

## Quick info

#### Found a bug?
[report](https://github.com/wiktorKycia/space_shooter/issues/new?template=bug_report.md)

#### Wanna make a change?
**don't**

Unless it's a really small one

#### Wanna help?
- follow my profile
- look for issues labeled as:
  - [`detail`](https://github.com/wiktorKycia/space_shooter/issues?q=is%3Aissue%20state%3Aopen%20label%3Adetail)
  - [`help wanted`](https://github.com/wiktorKycia/space_shooter/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22help%20wanted%22)
  - [`good first issue`](https://github.com/wiktorKycia/space_shooter/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22)
- make a pull request referring these issues

## Contributing types and general guidelines

### What is accepted
- creating pull requests that are a response for issues marked as `help wanted`, `good first issue` or `detail`
- correcting a typo in texts displayed in the game
- reporting bugs
  - use the [bug report template](https://github.com/wiktorKycia/space_shooter/issues/new?template=bug_report.md)

### What is not accepted
- creating new or changing game features
   - this is my own project and I have a precise vision of how it should be, so these kind of changes won't be accepted no matter if it is an issue or a pr
- force pushes
   - the most important branches are protected and it's not a problem, but don't be rude and don't push any code to existing branches, just create your own
- editing game and repo assets
  - **meaning:** all the files inside `./images`, `./sounds` and `./.github` folders, including texts of licenses, `README.md` file
 
### Issues
- for bug reports use [bug report template](https://github.com/wiktorKycia/space_shooter/issues/new?template=bug_report.md) and follow the instructions in it
- If you want to suggest a _minor_ change, please specify where the problem is (exact file or screen in game) and label the issue as `detail`
- If you want to suggest a _major_ change: **don't**

### Pull requests
- Please create a PR to only existing active issues
- Every pull request should have an issue bind to it, description of changes and their overall impact/severity
- do not set `base` branch as `master`, instead set `develop` as `base` branch, only the repository owner is allowed to merge to `master` after the manual checks passes
- if you are still working on a pull request, please convert it to draft PR, and change it back to normal when you are finished - just to prevent me from accidental merging
- when your PR is ready, ask me for review

