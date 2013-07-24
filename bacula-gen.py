#!/usr/bin/env python

import os, jinja2, json, sys
from optparse import OptionParser

usage = 'Usage: %prog -c config.json -t template.tmpl [-o filename] [-n server_name]'
parser = OptionParser(usage = usage, conflict_handler='resolve', version='0.2',\
                      description='Bacula config generator from JSON file')

parser.add_option('-c', '--config=', action='store', type='string', dest='CONF_FILE', help='JSON configuration file')
parser.add_option('-t', '--template=', action='store', type='string', dest='TMPL_FILE', help='Jinja2 template file')
parser.add_option('-o', '--output=', action='store', type='string', dest='OUT_FILE',\
                  help='print config to filename instead of stdout')
parser.add_option('-n', '--name', action='store', dest='server_name',\
                  help='Generate config only for specified server (in development)')

options,arguments = parser.parse_args()

if options.CONF_FILE is None or options.TMPL_FILE is None:
    parser.print_help()
    sys.exit(-1)

if options.server_name:
    parser.error('Too early for option "-n". Sorry.')

config = json.load(open(options.CONF_FILE, 'r'))
templateLoader = jinja2.FileSystemLoader(searchpath=os.getcwd())
templateEnv = jinja2.Environment(loader=templateLoader)

template = templateEnv.get_template(options.TMPL_FILE)
templateVars = { "servers" : config["servers"],  "common_excludes" : config["common_excludes"],\
                 "common_exclude_patterns" : config["common_exclude_patterns"] }

outputText = template.render(templateVars)
if options.OUT_FILE:
    f = open(options.OUT_FILE, 'w')
    f.write(outputText)
    f.write('\n')
    f.close()
else:
    print "#" * 80, '\n', outputText,'\n', "#" * 80, '\n', "Check it with \'bacula-\<daemon\> -t \/path\/to\/config\'"

# TODO: YAML support