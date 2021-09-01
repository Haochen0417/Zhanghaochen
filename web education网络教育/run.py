'''
    This is a file that configures how your server runs
    You may eventually wish to have your own explicit config file
    that this reads from.

    For now this should be sufficient.

    Keep it clean and keep it simple, you're going to have
    Up to 5 people running around breaking this constantly
    If it's all in one file, then things are going to be hard to fix

    If in doubt, `import this`
'''

#-----------------------------------------------------------------------------

import sys
from bottle import run, default_app


#-----------------------------------------------------------------------------
# You may eventually wish to put these in their own directories and then load 
# Each file separately

# For the template, we will keep them together

import model
import view
import controller
import bottle

#-----------------------------------------------------------------------------

# It might be a good idea to move the following settings to a config file and then load them
# Change this to your IP address or 0.0.0.0 when actually hosting
host = ''

# Test port, change to the appropriate port to host
port = 8080

# Turn this off for production
debug = True

# Turn this off for production
reloader = True

def run_server():    
    '''
        run_server
        Runs a bottle server
    '''
    run(host=host, port=port, debug=debug, reloader=reloader, app=default_app())

#-----------------------------------------------------------------------------
# Optional SQL support
# Comment out the current manage_db function, and 
# uncomment the following one to load an SQLite3 database

import sql

def initial_db():

    sql_db = sql.SQLDatabase("w4school.db")
    sql_db.database_setup()
    return

def check_db():
    sql_db = sql.SQLDatabase("w4school.db")
    
    sql_db.check_db()
#-----------------------------------------------------------------------------

# What commands can be run with this python file
# Add your own here as you see fit

command_list = {
    'server'    : run_server,
    'initdb'    : initial_db,
    'check_db'  : check_db
}

# The default command if none other is given
default_command = ['server']

def run_commands(args):
    '''
        run_commands
        Parses arguments as commands and runs them if they match the command list

        :: args :: Command line arguments passed to this function
    '''
    commands = args[1:]
    
    # Default command
    if len(commands) == 0:
        commands = default_command

    for command in commands:
        if command in command_list:
            command_list[command]()
        else:
            print("Command '{command}' not found".format(command=command))

#-----------------------------------------------------------------------------

# run_commands(sys.argv)

if __name__ == '__main__':
    run_commands(sys.argv)
else :
    application = default_app()
#run_commands(sys.argv)
