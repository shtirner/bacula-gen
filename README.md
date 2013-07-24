Bacula config generator from JSON file

Usage: bacula-gen.py -c config.json -t template.tmpl [-o filename] [-n server_name]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -c CONF_FILE, --config==CONF_FILE
                        JSON configuration file
  -t TMPL_FILE, --template==TMPL_FILE
                        Jinja2 template file
  -o OUT_FILE, --output==OUT_FILE
                        print config to filename instead of stdout
  -n SERVER_NAME, --name=SERVER_NAME
                        Generate config only for specified server (in development)
