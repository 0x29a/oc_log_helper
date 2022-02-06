# oc_log_helper

> My template for small libraries and command-line tools.

[![PyPI Version][pypi-image]][pypi-url]
[![Build Status][build-image]][build-url]
[![Code Coverage][coverage-image]][coverage-url]
[![Code Quality][quality-image]][quality-url]

## Installation

1. Install `python3-gi`:
    ```
    sudo apt install python3-gi
    ```
1. Install `oc_log_helper`:
    ```sh
    pipx install oc_log_helper --system-site-packages
    ```
    or
    ```sh
    pip install oc_log_helper --system-site-packages
    ```
1. Configure toggl:
    ```sh
    toggl config
    ```
    It'll ask for token. You can generate it at the bottom of [this page](https://track.toggl.com/profile).
1. Add hotkey to quickly execute `oc_log_helper log-work`.

<!-- Badges -->

[pypi-image]: https://img.shields.io/pypi/v/oc_log_helper
[pypi-url]: https://pypi.org/project/oc_log_helper/
[build-image]: https://github.com/0x29a/oc_log_helper/actions/workflows/build.yml/badge.svg
[build-url]: https://github.com/0x29a/oc_log_helper/actions/workflows/build.yml
[coverage-image]: https://codecov.io/gh/0x29a/oc_log_helper/branch/master/graph/badge.svg
[coverage-url]: https://codecov.io/gh/0x29a/oc_log_helper
[quality-image]: https://api.codeclimate.com/v1/badges/3af8e49ce0ce13dca358/maintainability
[quality-url]: https://codeclimate.com/github/0x29a/oc_log_helper
