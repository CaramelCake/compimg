import typing
import numbers
import numpy as np

_TYPES_AND_RANGES = {
    "uint8": (0, 255),
    "uint16": (0, 65535),
    "float": (0.0, 1.0),
    "float16": (0.0, 1.0),
    "float32": (0.0, 1.0),
    "float64": (0.0, 1.0),
}


def get_dtype_range(dtype: np.dtype) -> typing.Tuple[numbers.Integral, numbers.Integral]:
    """This also assumes that image are considered where by convention
        for floats values are stored within range 0.0 to 1.0."""
    dtype_range = _TYPES_AND_RANGES.get(dtype.name, None)
    if dtype_range is None:
        raise TypeError(f"{dtype} is a type that cannot be handled by compimg.")
    return dtype_range
