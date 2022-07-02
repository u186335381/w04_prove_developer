from ..shared.point import Point
from ..shared.color import Color
from ..casting.gem import Gem
from ..casting.rock import Rock
import random


class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.

        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service

    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.

        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.

        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")

        # Add a Gem or a Rock randomly
        artifact = None
        if random.choice([True, False]):
            artifact = Gem()
        else:
            artifact = Rock()

        # We randomly select a color
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        artifact.set_color(Color(r, g, b))

        # We randomly position our new element on the screen
        movement = -5
        x = random.randint(1, self._video_service.get_width() + movement)
        artifact.set_position(Point(x, y=movement).scale(
            self._video_service.get_cell_size()))
        artifact.set_font_size(robot.get_font_size())
        cast.add_actor("artifacts", artifact)

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)

        # Make the artifacts descend
        for artifact in cast.get_actors("artifacts"):
            x = artifact.get_position().get_x()
            y = artifact.get_position().get_y()
            artifact.set_position(Point(x, y + 5))

        for artifact in cast.get_actors("artifacts"):
            if robot.get_position().equals(artifact.get_position()):
                cast.set_score(cast.get_score() + artifact.get_points())
                banner.set_text(f"Score: {cast.get_score()}")
                cast.remove_actor("artifacts", artifact)

    def _do_outputs(self, cast):
        """Draws the actors on the screen.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()
