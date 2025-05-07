from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import QValidator

""" ### Custom QValidator Classes for QT Modules
    #   -   PySide6 Custom Functions that are expected to be reused
"""

""" Custom validators are coupled 1:1 with QLineEdit instances; this isn't ideal, but it allows for
    users to change selection and make changes without overwriting their input while they're typing
"""
class PasswordValidator(QValidator):
    def __init__(self, le = QLineEdit):
        super().__init__()
        self._line_edit = le

    def validate(self, input_str: str, pos: int):
        """ Enforces length constraints and prevents blank spaces """
        # Allow for editing before finishing
        if self._line_edit.hasFocus(): return QValidator.State.Acceptable

        length = len(input_str)
        # No spaces
        if " " in input_str: return QValidator.Invalid, input_str, pos
        # Reject long-passwords
        if length > 50: return QValidator.Invalid, input_str, pos
        # Reject short-password
        if length < 14: return QValidator.Intermediate, input_str, pos

        return QValidator.Acceptable, input_str, pos

    def fixup(self, input_str: str) -> str:
        """
            Called when the editor loses focus with an Intermediate or Invalid value,
            Automatically removes spaces and fixes the length to 50 characters.
        """
        fix_inp = input_str.replace(" ", "")[:50]
        return fix_inp

class UsernameValidator(QValidator):
    def __init__(self, le = QLineEdit):
        super().__init__()
        self._line_edit = le

    def validate(self, input_str: str, pos: int):
        """ Enforces length constraints and prevents blank spaces """
        # Allow for editing before finishing
        if self._line_edit.hasFocus(): return QValidator.State.Acceptable

        length = len(input_str)
        # No spaces
        if " " in input_str: return QValidator.Invalid, input_str, pos
        # Reject long-username
        if length > 64: return QValidator.Invalid, input_str, pos
        # Reject short-username
        if length < 10: return QValidator.Intermediate, input_str, pos

        return QValidator.Acceptable, input_str, pos

    def fixup(self, input_str: str) -> str:
        """
            Called when the editor loses focus with an Intermediate or Invalid value,
            Automatically removes spaces and fixes the length to 64 characters.
        """
        fix_inp = input_str.replace(" ", "")[:64]
        return fix_inp