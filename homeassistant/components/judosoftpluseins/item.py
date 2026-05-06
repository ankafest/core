"""Fill and get Items."""


class Item:
    """items definition."""

    def __init__(self, translation_key: str, icon: str, format: str) -> None:
        """Init the items definition."""
        self._translation_key = translation_key
        self._text = " "
        self._icon = icon
        self._unit_of_measurement = " "
        self._min = 0
        self._max = 0
        self._format = format

    @property
    def translation_key(self) -> str:
        """Return the translation key."""
        return self._translation_key

    @translation_key.setter
    def translation_key(self, value: str) -> None:
        """Set the translation key."""
        self._translation_key = value

    @property
    def format(self) -> str:
        """Return the format."""
        return self._format

    @format.setter
    def format(self, value: str) -> None:
        """Set the format."""
        self._format = value

    @property
    def text(self) -> str:
        """Return the text."""
        return self._text

    @text.setter
    def value(self, value: str) -> None:
        """Set the value."""
        self._text = value

    @property
    def icon(self) -> str:
        """Return the icon."""
        return self._icon

    @icon.setter
    def icon(self, value) -> None:
        """Set the icon."""
        self._icon = value

    @property
    def unit_of_measurement(self) -> str:
        """Return the unit of measurement."""
        return self.unit_of_measurement

    @unit_of_measurement.setter
    def unit_of_measurement(self, value: str) -> None:
        """Set the unit of measurement."""
        self._unit_of_measurement = value

    @property
    def min(self) -> float:
        """Return the Min."""
        return self._min

    @min.setter
    def min(self, value: float) -> None:
        """Set the Min."""
        self.min = value

    @property
    def max(self) -> float:
        """Return the Max."""
        return self._max

    @max.setter
    def max(self, value: float) -> None:
        """Set the Max."""
        self._max = value
