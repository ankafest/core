"""Item for each entity."""


class EntityItem:
    """Entity item definition."""

    def __init__(self, translation_key: str, icon: str, unit: str = " ") -> None:
        """Init the entity item definition."""
        self._translation_key = translation_key
        self._text = " "
        self._icon = icon
        self._unit_of_measurement = unit

    @property
    def translation_key(self) -> str:
        """Return the translation key."""
        return self._translation_key

    @translation_key.setter
    def translation_key(self, value: str) -> None:
        """Set the translation key."""
        self._translation_key = value

    @property
    def result(self) -> str:
        """Return the text."""
        return self._text

    @result.setter
    def result(self, value: str) -> None:
        """Set the result."""
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
        return self._unit_of_measurement

    @unit_of_measurement.setter
    def unit_of_measurement(self, value) -> None:
        """Set the unit of measurement."""
        self._unit_of_measurement = value
