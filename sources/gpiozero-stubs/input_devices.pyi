from gpiozero import GPIODevice, EventsMixin, HoldMixin

try:
    from statistics import median
except ImportError:
    from .compat import median


class InputDevice(GPIODevice):
    def __init__(self, pin: int = None, pull_up=False, pin_factory=None) -> any: pass

    @property
    def pull_up(self) -> bool: pass

    def __repr__(self) -> str: pass


class DigitalInputDevice(EventsMixin, InputDevice):
    def __init__(
            self, pin=None, pull_up=False, bounce_time: float = None, pin_factory=None) -> any: pass


class SmoothedInputDevice(EventsMixin, InputDevice):
    def __init__(
            self, pin=None, pull_up=False, threshold=0.5, queue_len=5,
            sample_wait=0.0, partial=False, average=median, pin_factory=None) -> any: pass

    def close(self) -> any: pass

    def __repr__(self) -> str: pass

    @property
    def queue_len(self) -> int: pass

    @property
    def partial(self) -> bool: pass

    @property
    def value(self) -> float: pass

    @property
    def threshold(self) -> float: pass

    @threshold.setter
    def threshold(self, value) -> any: pass

    @property
    def is_active(self) -> bool: pass


class Button(HoldMixin, DigitalInputDevice):
    def __init__(
            self, pin: int = None, pull_up=True, bounce_time: float = None,
            hold_time: float = 1, hold_repeat=False, pin_factory=None) -> None: pass

    @property
    def is_pressed(self) -> bool: pass

    @property
    def pressed_time(self) -> float: pass

    @property
    def when_pressed(self) -> any: pass

    @property
    def when_released(self) -> any: pass

    def wait_for_press(self, timeout: float = None) -> bool: pass

    def wait_for_release(self, timeout: float = None) -> bool: pass


class LineSensor(SmoothedInputDevice):
    def __init__(
            self, pin: int = None, queue_len=5, sample_rate: float = 100, threshold=0.5,
            partial=False, pin_factory=None) -> None: pass

    @property
    def line_detected(self) -> bool: pass

    @property
    def when_line(self) -> any: pass

    @property
    def when_no_line(self) -> any: pass

    def wait_for_line(self, timeout: float = None) -> bool: pass

    def wait_for_no_line(self, timeout: float = None) -> bool: pass


class MotionSensor(SmoothedInputDevice):
    def __init__(
            self, pin: int = None, queue_len=1, sample_rate: float = 10, threshold=0.5,
            partial=False, pull_up=False, pin_factory=None) -> any: pass

    @property
    def motion_detected(self) -> bool: pass

    @property
    def when_motion(self) -> any: pass

    @property
    def when_no_motion(self) -> any: pass

    def wait_for_motion(self, timeout: float = None) -> bool: pass

    def wait_for_no_motion(self, timeout: float = None) -> bool: pass


class LightSensor(SmoothedInputDevice):
    def __init__(
            self, pin: int = None, queue_len=5, charge_time_limit=0.01,
            threshold=0.1, partial=False, pin_factory=None) -> any: pass

    @property
    def charge_time_limit(self) -> float: pass

    def _read(self) -> float: pass

    @property
    def light_detected(self) -> bool: pass

    @property
    def when_light(self) -> any: pass

    @property
    def when_dark(self) -> any: pass

    def wait_for_light(self, timeout: float = None) -> bool: pass

    def wait_for_dark(self, timeout: float = None) -> bool: pass


class DistanceSensor(SmoothedInputDevice):
    def __init__(
            self, echo: int = None, trigger: int = None, queue_len=10, max_distance: float = 1,
            threshold_distance=0.3, partial=False, pin_factory=None) -> any: pass

    def close(self) -> any: pass

    @property
    def max_distance(self) -> float: pass

    @max_distance.setter
    def max_distance(self, value) -> any: pass

    @property
    def threshold_distance(self) -> float: pass

    @threshold_distance.setter
    def threshold_distance(self, value) -> None: pass

    @property
    def distance(self) -> float: pass

    @property
    def trigger(self) -> any: pass

    @property
    def echo(self) -> any: pass

    def _echo_changed(self) -> None: pass

    def _read(self) -> float: pass

    @property
    def in_range(self) -> bool: pass

    @property
    def when_out_of_range(self) -> any: pass

    @property
    def when_in_range(self) -> any: pass

    def wait_for_out_of_range(self, timeout: float = None) -> bool: pass

    def wait_for_in_range(self, timeout: float = None) -> bool: pass
