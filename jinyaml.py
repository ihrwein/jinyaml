import jinja2
import argparse
import os
import sys
import yaml

def parse_cli_args():
    parser = argparse.ArgumentParser(description='Creates files using Jinja2 templates based on a YAML configuration')
    parser.add_argument('YAML_file', type=str, nargs=1,
        help='A YAML file wich contains variables')
    parser.add_argument('template_file', type=str, nargs=1,
        help='The Jinja2 template file')
    parser.add_argument('output_file', type=str, nargs=1,
        help='The path where the evaluated template should be written')

    args = parser.parse_args()
    return (args.YAML_file[0], args.template_file[0], args.output_file[0])

def fail_when_file_doesnot_exist(path, error_message):
    if not os.path.isfile(path):
        print(error_message)
        sys.exit(1)

def format_file(yaml_file_path, template_file_path, output_file_path):
    fail_when_file_doesnot_exist(yaml_file_path, "The YAML file does not exist")
    fail_when_file_doesnot_exist(template_file_path, "The template file does not exist")

    templateLoader = jinja2.FileSystemLoader( searchpath="." )
    templateEnv = jinja2.Environment( loader=templateLoader )
    template = templateEnv.get_template( template_file_path )

    with open(yaml_file_path, 'r') as stream:
        templateVars = yaml.load(stream)
    
    outputText = template.render( templateVars )
    with open(output_file_path, 'w') as output:
        output.write(outputText)

def main():
    (yaml_file, template_file, output_file) = parse_cli_args()
    format_file(yaml_file, template_file, output_file)

if __name__ == '__main__':
    main()
