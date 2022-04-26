import logging

from PyQt6.QtWidgets import QApplication

from gui import GUI
from firewall import set_rule_state, set_rule_path, get_rule_data


logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s | %(asctime)s] - %(message)s',
    datefmt='%H:%M:%S'
)


if __name__ == '__main__':
    app = QApplication([])

    state, path = get_rule_data()
    gui = GUI(
        current_state=state,
        state_callback=set_rule_state,
        current_path=path,
        path_callback=set_rule_path
    )
    app.exec()
