"""Items for Scene."""

from .scene_rest_item import SceneRestItem


class SceneItem:
    """scene items definition."""

    def __init__(
        self, scene_name: str, icon: str, list_of_rest_commands: list[SceneRestItem]
    ) -> None:
        """Init the items definition."""
        self._scene_name = scene_name
        self._icon = icon
        self._list_of_rest_commands = list_of_rest_commands

    @property
    def icon(self) -> str:
        """Return the icon."""
        return self._icon

    @icon.setter
    def icon(self, value) -> None:
        """Set the icon."""
        self._icon = value

    @property
    def scene_name(self) -> str:
        """Return the scene name."""
        return self._scene_name

    @scene_name.setter
    def scene_name(self, value: str) -> None:
        """Set the scene name."""
        self._scene_name = value

    @property
    def list_of_rest_commands(self) -> list[SceneRestItem]:
        """Return the list of REST commands."""
        return self._list_of_rest_commands

    @list_of_rest_commands.setter
    def list_of_rest_commands(self, rest_command_list: list[SceneRestItem]) -> None:
        """Set the list of REST commands."""
        self._list_of_rest_commands = rest_command_list
