import os
import json
import base64
import uuid
import time
import datetime
import keyring

from clistarter.const import DEFAULT_KEYRING_SERVICE

def generate_timestamp():
    '''
    Generate a timestamp in seconds since the epoch.
    '''
    return time.time()

def generate_datetime_timestamp(timestamp: float):
    '''
    Generate a datetime string from a float timestamp.
    '''
    return datetime.datetime.utcfromtimestamp(timestamp).isoformat()

def generate_uuid():
    '''
    Generate a UUID.
    '''
    return str(uuid.uuid4())

def to_base64(string: str):
    '''
    Convert a string to base64.
    '''
    return base64.b64encode(string.encode('utf-8')).decode('utf-8')

def from_base64(string: str):
    '''
    Convert a base64 string to a string.
    '''
    return base64.b64decode(string.encode('utf-8')).decode('utf-8')

def get_environment_variable(variable_name: str):
    '''
    Attempts to get a variable from the environment.
    '''
    try:
        return os.environ[variable_name]
    except KeyError:
        return None
    
def set_environment_variable(variable_name: str, variable_value: str):
    '''
    Sets a variable onto the environment.
    '''
    os.environ[variable_name] = variable_value
    
def get_keyring_variable(variable_name: str):
    '''
    Attempts to get a variable from the keyring.
    '''
    try:
        return keyring.get_password(DEFAULT_KEYRING_SERVICE, variable_name)
    except:
        return None
    
def set_keyring_variable(variable_name: str, variable_value: str):
    '''
    Sets a variable onto the keyring.
    '''
    return keyring.set_password(DEFAULT_KEYRING_SERVICE, variable_name, variable_value)

def check_for_var(variable_name: str):
    '''
    Checks to see if the user is authorized to use the application.
    '''
    if not get_keyring_variable(variable_name) or not get_environment_variable(variable_name):
        return False
    return True

def get_var(variable_name: str):
    '''
    Gets a variable from the environment or keyring.
    '''
    if get_environment_variable(variable_name):
        return get_environment_variable(variable_name)
    elif get_keyring_variable(variable_name):
        return get_keyring_variable(variable_name)
    else:
        return None
