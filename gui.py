from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QFileDialog


class GUI(QMainWindow):
    def __init__(self, current_state, state_callback, current_path, path_callback):
        super().__init__()

        self.setWindowTitle('Hearthstone Firewall Switcher')
        self.setFixedSize(QSize(280, 100))

        self.state = current_state
        self.state_callback = state_callback
        self.state_button = StateButton()

        self.path = current_path
        self.path_callback = path_callback
        self.path_button = QPushButton()

        self.init_ui()

        self.state_button.toggled.connect(self.set_state)
        self.path_button.clicked.connect(self.on_path_button_click)

        self.show()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.path_button)
        main_layout.addWidget(self.state_button)

        self.set_path(self.path, call_callback=False)
        if self.path:
            self.state_button.setChecked(self.state)
            self.set_state(self.state, call_callback=False)
        else:
            self.state_button.setChecked(False)
            self.state_button.setDisabled(True)
            self.set_state(False, call_callback=False)

        container = QWidget()
        container.setLayout(main_layout)

        self.setCentralWidget(container)

    def on_path_button_click(self):
        new_path = QFileDialog.getOpenFileName(
            self, 'Select Hearthstone executable',
            directory='/'.join(self.path.split('/')) if self.path else None,
            filter='Executables (*.exe)'
        )[0].replace('/', '\\').lower()

        if self.path is None:
            self.state_button.setDisabled(False)

        if new_path and new_path != self.path:
            self.set_path(new_path)
            self.set_state(False)

    def set_path(self, path, call_callback: bool = True):
        self.path = path
        if path:
            text = 'Change path to executable...'
        else:
            text = 'Select Hearthstone executable...'
        self.path_button.setText(text)

        if call_callback:
            self.path_callback(path)

    def set_state(self, state: bool, call_callback: bool = True):
        self.state = state
        if state:
            text = 'Hearthstone has no access to internet!'
        else:
            text = 'Hearthstone has access to internet...'
        self.state_button.setText(text)

        if call_callback:
            self.state_callback(state)


class StateButton(QPushButton):
    COLOR_TEXT_INACTIVE = (41, 176, 1)
    COLOR_TEXT_ACTIVE = (173, 26, 1)
    COLOR_TEXT_DISABLED = (54, 62, 74)
    COLOR_INACTIVE = (117, 217, 87)
    COLOR_ACTIVE = (219, 84, 59)
    COLOR_DISABLED = (0, 0, 0)

    def __init__(self):
        super().__init__()

        self.setCheckable(True)
        self.setFixedHeight(50)

        self.setStyleSheet(
            f"""
            QPushButton {{
                border: 2px solid;
                color: rgb{self.COLOR_TEXT_INACTIVE};
                background-color: rgba{self.get_inactive_color(0.25)};
                border-color: rgba{self.get_inactive_color(0.25)};
            }}

            QPushButton::hover {{
                background-color: rgba{self.get_inactive_color(0.5)};
            }}
            
            QPushButton::disabled {{
                background-color: rgba{self.get_disabled_color(0.5)};
                color: rgb{self.COLOR_TEXT_DISABLED};
                border-color: rgba{self.get_disabled_color(0.25)};
            }}
            
            QPushButton::disabled::hover {{
                background-color: rgba{self.get_inactive_color(0.5)};
            }}

            /* QPushButton::pressed {{
                background-color: rgba{self.get_inactive_color(0.7)};
            }} */

            QPushButton::checked {{
                color: rgb{self.COLOR_TEXT_ACTIVE};
                background-color: rgba{self.get_active_color(0.25)};
                border-color: rgba{self.get_active_color(0.25)};
            }}

            QPushButton::checked::hover {{
                background-color: rgba{self.get_active_color(0.5)};
            }}

            /* QPushButton::checked::pressed {{
                background-color: rgba{self.get_active_color(0.7)};
            }} */
            """
        )

    def get_active_color(self, alpha: float):
        return self.COLOR_ACTIVE + (alpha,)

    def get_inactive_color(self, alpha: float):
        return self.COLOR_INACTIVE + (alpha,)

    def get_disabled_color(self, alpha: float):
        return self.COLOR_DISABLED + (alpha,)
