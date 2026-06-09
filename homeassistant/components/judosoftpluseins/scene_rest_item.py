"""for definition scene rest item."""  #


class SceneRestItem:
    """scene rest item definition."""

    def __init__(self, rest_command: str, value: str) -> None:
        """Init the scene rest item definition."""
        self._rest_command = rest_command
        self._value = value

    @property
    def rest_command(self) -> str:
        """Return the REST command."""
        return self._rest_command

    @rest_command.setter
    def rest_command(self, value: str) -> None:
        """Set the REST command."""
        self._rest_command = value

    @property
    def value(self) -> str:
        """Return the value."""
        return self._value

    @value.setter
    def value(self, value: str) -> None:
        """Set the value."""
        self._value = value
