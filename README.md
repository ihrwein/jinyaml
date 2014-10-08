# JinYAML
A library to format Jinja2 templates based on a YAML configuration file.

## Description

There are some cases, when you want to create files based on templates.
Jinja2 is often used by developers as a template language and YAML is prevalent as a configuration file format.

This tool can be used to read variables from a YAML file (or command line) and substitute them into a template file.

## Installation

These command will install `jinyaml` and its dependencies.
```
$ git clone https://github.com/ihrwein/jinyaml.git
$ cd jinyaml
$ python setup.py install 
```

## Usage

Cd to the cloned directory:
```
$ jinyaml tests/template.j2 tests/result -y tests/vars.yaml
```

## Using as an API

```
import jinyaml
jinyaml.format_file('/this/is/a/jinja_template.j2',
                    '/the/result/should/be/written/here.out',
                    yaml_file='/path/to/the/config.yml',
                    additional_vars={})
```
