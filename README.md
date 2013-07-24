Bacula config generator from JSON
=====================

**Usage:** bacula-gen.py -c config.json -t template.tmpl [-o filename] [-n server_name]

Options:
-------
-   --version             show program's version number and exit
-  -h, --help            show this help message and exit
-  -c CONF\_FILE, --config==CONF_FILE
                        JSON configuration file
-  -t TMPL\_FILE, --template==TMPL\_FILE Jinja2 template file
-  -o OUT\_FILE, --output==OUT\_FILE
                        print config to filename instead of stdout
-  -n SERVER]_NAME, --name=SERVER\_NAME
                        Generate config only for specified server (in development)
