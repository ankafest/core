"""Fill and get Items."""


class Item:
    """items definition."""

    def __init__(self, translation_key: str, icon: str, format: str) -> None:
        """Init the items definition."""
        self.tranlation_key = translation_key
        self.value = " "
        self.icon = icon
        self.unit_of_measurement = " "
        self.min = 0
        self.max = 0
        self.format = format

    @property
    def translation_key(self) -> str:
        """Return the translation key."""
        return self.translation_key

    @translation_key.setter
    def translation_key(self, value: str) -> None:
        """Set the translation key."""
        self.translation_key = value

    @property
    def format(self) -> str:
        """Return the format."""
        return self.format

    @format.setter
    def format(self, value: str) -> None:
        """Set the format."""
        self.format = value

    @property
    def value(self) -> str:
        """Return the value."""
        return self.value

    @value.setter
    def value(self, value: str) -> None:
        """Set the value."""
        self.value = value

    @property
    def icon(self) -> str:
        """Return the icon."""
        return self.icon

    @icon.setter
    def icon(self, value) -> None:
        """Set the icon."""
        self.icon = value

    @property
    def text(self) -> str:
        """Return the text."""
        return self.text

    @property
    def unit_of_measurement(self) -> str:
        """Return the unit of measurement."""
        return self.unit_of_measurement

    @unit_of_measurement.setter
    def unit_of_measurement(self, value: str) -> None:
        """Set the unit of measurement."""
        self.unit_of_measurement = value

    @property
    def min(self) -> float:
        """Return the Min."""
        return self.min

    @min.setter
    def min(self, value: float) -> None:
        """Set the Min."""
        self.min = value

    @property
    def max(self) -> float:
        """Return the Max."""
        return self.max

    @max.setter
    def max(self, value: float) -> None:
        """Set the Max."""
        self.max = value
