# Dir Maker CLI

A simple directory maker CLI app.

## What does it do?

This app creates a series of directories inside the current directory or in the specified directory passed by user.

## How to use?

```bash
dir_maker_cli range_from range_to container_dir
```

- range_to: Integer. Last directory number (Required)
- range_from: Integer. First directory number (Optional, defaults to 1)
- container_dir: String. Name of container directory to create directories inside (Optional, defaults to current directory)

## Installation

```bash
poetry install
poetry run dir_maker_cli
```
