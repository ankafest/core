"""Fill and get Items."""

from .entity_item import EntityItem


class Item:
    """items definition."""

    def __init__(
        self, rest_item_name: str, list_of_entites: list[EntityItem], format: str
    ) -> None:
        """Init the items definition."""
        self._rest_item_name = rest_item_name
        self._list_of_entites = list_of_entites
        self._format = format

    @property
    def rest_item_name(self) -> str:
        """Return the rest item name."""
        return self._rest_item_name

    @rest_item_name.setter
    def rest_item_name(self, value: str) -> None:
        """Set the rest item name."""
        self._rest_item_name = value

    @property
    def format(self) -> str:
        """Return the format."""
        return self._format

    @format.setter
    def format(self, value: str) -> None:
        """Set the format."""
        self._format = value

    @property
    def list_of_entites(self) -> list[EntityItem]:
        """Return the list of entities."""
        return self._list_of_entites

    @list_of_entites.setter
    def list_of_entites(self, entity_list: list[EntityItem]) -> None:
        """Set the list of entities."""
        self._list_of_entites = entity_list
