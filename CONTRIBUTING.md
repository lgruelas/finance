# Contributing to finance
This is a learning space for django/react stack, and get used to be working with docker tools and a complete professional workflow with CI revisions, so everyone feel free to:

-   Report a bug
-   Discussing the current state of the code
-   Submitting a fix
-   Proposing new features
-   Comment a better approach to any part of the code.

## We Develop with Github
We use github to host code, to track issues and feature requests, as well as accept pull requests.

## Workflow
Pull requests are the best way to propose changes to the codebase.

1.  Fork the repo if you're not a contributor.
2.  Create your branch from `master`.
3.  If you've added code that should be tested, add tests.
4.  If you've changed APIs, update the documentation.
5.  Ensure the test suite passes.
6.  Make sure your code lints.
7.  Issue that pull request!

### PR format
There is a PR template in the repo, and for the title please use:
```
[<issue number that the PR solves>] - Description
```
Make sure to use the keywords in the Issue field, like closes and related, also, please remember to use the correct labels.

The PR will do a couple of checks, including CI bulid on TravisCI, Flake8 for python code, automated CR with codacy and coverage test with Codecov.

## Any contributions you make will be under the GPL-3.0 License.
In short, when you submit code changes, your submissions are understood to be under the same [GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/) that covers the project.

## Report bugs using Github's [issues](https://github.com/lgruelas/finance/issues)
We use GitHub issues to track public bugs. Report a bug by [opening a new issue](); it's that easy!

## Write bug reports with detail, background, and sample code

**Great Bug Reports** tend to have:

-   A quick summary and/or background
-   Steps to reproduce
  - Be specific!
  - Give sample code if you can (a minimum example).
-   What you expected would happen
-   What actually happens
-   Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)

## Use a Consistent Coding Style

### Python
*   4 spaces tabs for indentation.
*   flake8 linter.
*   120 character line length in special casses, preffered 79.
*   variable names in snakecase (start with nouns).
*   constant names in uppercase.
*   class names in camelcase.
*   function and methods in snakecase (start with verbs).

## License
By contributing, you agree that your contributions will be licensed under its GPL-3.0 License.

## References
This document was adapted from the open-source contribution guidelines for [Facebook's Draft](https://github.com/facebook/draft-js/blob/a9316a723f9e918afde44dea68b5f9f39b7d9b00/CONTRIBUTING.md)
