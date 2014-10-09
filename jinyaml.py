import jinja2
import argparse
import os
import sys
import yaml
import json

def __parse_cli_args():
    parser = argparse.ArgumentParser(
         description='Creates files using Jinja2 templates based on a YAML configuration')
    parser.add_argument('-d', '--dict', type=json.loads,
        help='Some user defined variables in a JSON dictionary')
    parser.add_argument('-y', '--yaml', type=str, nargs='*',
        help='A YAML file wich contains variables')
    parser.add_argument('template_file', type=str, nargs=1,
        help='The Jinja2 template file')
    parser.add_argument('output_file', type=str, nargs=1,
        help='The path where the evaluated template should be written')

    args = parser.parse_args()
    return {'additional_vars': args.dict,
            'yaml_file': args.yaml,
            'template_file': args.template_file[0],
            'output_file': args.output_file[0]
            }

def __fail_when_file_doesnot_exist(path, error_message):
    if not os.path.isfile(path):
        print(error_message)
        sys.exit(1)

def __load_template(template_file):
    __fail_when_file_doesnot_exist(template_file, "The template file does not exist")

    templateLoader = jinja2.FileSystemLoader( searchpath=[".", "/"] )
    templateEnv = jinja2.Environment( loader=templateLoader )
    template = templateEnv.get_template( template_file )
    return template

def __load_variables(yaml_file, additional_vars):
    vars = {}
    
    if yaml_file and len(yaml_file) > 0:

        for f in yaml_file:
            if not os.path.isfile(f):
                print("YAML file {0} does not exist, skipping.", f)
            else:
                with open(f, 'r') as stream:
                    vars.update(yaml.load(stream))
    
    if additional_vars:
       vars.update(additional_vars)
    return vars
    

def format_file(template_file,
                output_file,
                yaml_file=None,
                additional_vars=None):
    template = __load_template(template_file)
    vars = __load_variables(yaml_file, additional_vars)
    
    outputText = template.render(vars)

    with open(output_file, 'w') as output:
        output.write(outputText)

def main():
    args = __parse_cli_args()
    format_file(**args)

if __name__ == '__main__':
    main()
