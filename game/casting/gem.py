from game.casting.actor import Actor


class Gem(Actor):

    """
    A visible movable thing that participates in the game fulfilling the role of a Gem
    It adds points when the player captures it.

    Attributes:
        _points (int): The score the player currently has
        _text (string): The text displaying the current player score
        _text (string): The text to display
        _font_size (int): The font size to use.
        _color (Color): The color of the text.
        _position (Point): The screen coordinates.
        _velocity (Point): The speed and direction.
    """

    def __init__(self):
        self._points = 1
        self._text = "*"

    def set_points(self, _points):
        """
        Sets the points for the Gem element

        Args:
            points (int): The points this Gem will be able to grant to a player
        """
        self._points = _points

    def get_points(self):
        """
        Gets the points of the Gem

        Returns:
            int: The points that will be granted to the player if he/she catches it

        """
        return self._points

    def set_text(self, _text):
        """
        Sets the text for the Gem element in the screen

        Args:
            text (string): The new text the Gem is going to have
        """
        self._text = _text

    def get_text(self):
        """
        Gets the current text of the Gem

        Returns:
            string: The current text the Gem has

        """
        return self._text
