import logging
import os


RULE_NAME = 'hearthstone-firewall-switcher'


def execute_command(cmd: str) -> str:
    cmd = f'netsh advfirewall firewall {cmd}'
    logging.info(f'(CMD) Executing command \'{cmd}\'')
    stream = os.popen(cmd)
    output = stream.read()
    return output


def create_rule(path):
    create_cmd = f'add rule name="{RULE_NAME}" dir=out ' \
                 f'program="{path}" profile=any action=block'
    execute_command(create_cmd)


def delete_rule():
    delete_cmd = f'delete rule name="{RULE_NAME}"'
    execute_command(delete_cmd)


def get_rule_data() -> tuple[str, str] | tuple[None, None]:
    """Return rule state and path to executable"""
    state = None
    path = None

    cmd = f'show rule name="{RULE_NAME}" verbose'
    output = execute_command(cmd).lower()

    if 'no rules match the specified criteria' in output:
        return state, path

    for line in output.lower().split('\n'):
        if line.startswith('program:'):
            path = line.split(maxsplit=1)[1].lower()
        elif line.startswith('enabled'):
            state = True if line.endswith('yes') else False

    return state, path


def set_rule_path(path: str):
    delete_rule()
    create_rule(path)


def set_rule_state(block: bool):
    enable = 'yes' if block else 'no'
    cmd = f'set rule name="{RULE_NAME}" new enable={enable}'
    execute_command(cmd)
