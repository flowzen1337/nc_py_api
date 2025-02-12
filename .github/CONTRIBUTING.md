# Contributing to nc_py_api

Bug fixes, feature additions, tests, documentation and more can be contributed via [issues](https://github.com/cloud-py-api/nc_py_api/issues) and/or [pull requests](https://github.com/cloud_py_api/nc_py_api/pulls).
All contributions are welcome.

## Bug fixes, feature additions, etc.

Please send a pull request to the `main` branch.  Feel free to ask questions [via issues](https://github.com/cloud-py-api/nc_py_api/issues) or [discussions](https://github.com/cloud_py_api/nc_py_api/discussions)

- Fork the nc_py_api repository.
- Create a new branch from `main`.
- Install dev requirements with `pip install ".[dev]"`
- Develop bug fixes, features, tests, etc.
- Most of the tests are designed to run from under the GitHub actions. If you want to run them locally, see this [guide](to-do)
- Install `pylint` locally, it will run during `pre-commit`.
- Install `pre-commit` hooks by `pre-commit install` command.
- Create a pull request to pull the changes from your branch to the nc_py_api `main`.

### Guidelines

- Separate code commits from reformatting commits.
- Where possible, provide tests for any newly added code.
- Follow PEP 8.
- Update CHANGELOG.md as needed or appropriate with your bug fixes, feature additions and tests.

## Security vulnerabilities

Please see our [security policy](https://github.com/cloud-py-api/nc_py_api/blob/main/.github/SECURITY.md).
