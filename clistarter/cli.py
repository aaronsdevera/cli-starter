import json
import random

import click

from clistarter.utils import get_keyring_variable, set_environment_variable, get_environment_variable, from_base64
from clistarter.const import ART
from clistarter import CLIStarter

####################################################################################################
# CREATE A CLISTARTER INSTANCE
####################################################################################################
cs = CLIStarter()

####################################################################################################
# CLI ENTRY POINT
####################################################################################################

@click.group()
@click.option('--socks5', '-s', is_flag=False, help='Supply a SOCKS5 proxy.')
@click.option('--user_agent', '-ua', is_flag=False, help='Supply a User Agent.')
def cli(socks5, user_agent):
    """cli starter: starter repo for CLI tools"""

    cs.create_session(socks5=socks5, user_agent=user_agent)

    pass


####################################################################################################
# UTIL COMMANDS
####################################################################################################

@cli.group()
def utils():
    """Utilities, tools, and config commands."""
    pass

@utils.group()
def keyring():
    """Keyring management."""
    pass

@keyring.command()
@click.argument('key')
@click.argument('value')
def set(key: str, value: str):
    """Set a keyring variable."""
    click.echo(get_keyring_variable(key))
    click.echo("Setting an environment variable...")
    click.echo('Note: this will not persist across sessions, if at all.')
    click.echo('It\'s better to use keyring from the command line to set a secure variable: try python3 -m keyring set <SERVICE NAME> <key> <value>')

@keyring.command()
@click.argument('key')
def get(key: str):
    """Get a keyring variable."""
    click.echo(get_keyring_variable(key))

@utils.group()
def env():
    """Environment variable management."""
    pass

@env.command()
@click.argument('key')
@click.argument('value')
def set(key: str, value: str):
    """Set an environment variable."""
    click.echo("Setting an environment variable...")
    click.echo('Note: this will not persist across sessions, if at all.')
    click.echo(set_environment_variable(key, value))

@env.command()
@click.argument('key')
def get(key: str):
    """Get an environment variable."""
    click.echo(get_environment_variable(key))

@utils.command()
def ipcheck():
    """Check your IP address."""

    r = cs.session.get('https://wtfismyip.com/json')
    click.echo(json.dumps(r.json()))

@utils.command()
def uacheck():
    """Check your User Agent"""

    r = cs.session.get('https://www.whatsmyua.info/api/v1/ua')
    click.echo(json.dumps(r.json()))

####################################################################################################
# ART COMMANDS
####################################################################################################

@cli.group()
def art():
    """Text art generation and viewing."""
    pass

@art.command()
def ls():
    """List available art."""
    art_names = list(ART.keys())
    click.echo('\n'.join([x + ' - ' + ART[x]['description'] for x in art_names]))

@art.command()
@click.argument('name', default='default_ansi')
def get(name):
    """Get and print art by name."""
    click.echo(from_base64(ART[name]['base64']))

@art.command()
def lucky():
    """Feeling lucky? Get and print random art."""
    click.echo(from_base64(ART[random.choice(list(ART.keys()))]['base64']))