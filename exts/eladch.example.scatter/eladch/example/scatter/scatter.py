__all__ = ["scatter"]

from typing import List, Optional
import random
from pxr import Gf


def scatter(
    count: List[int],
    distance: List[float],
    randomization: List[float],
    id_count: int = 1,
    seed: Optional[int] = None
):
    """
    Returns generator with pairs containing transform matrices and ids to
    arrange multiple objects.
    ### Arguments:
        `count: List[int]`
            Number of matrices to generate per axis
        `distance: List[float]`
            The distance between objects per axis
        `randomization: List[float]`
            Random distance per axis
        `id_count: int`
            Count of different id
        `seed: int`
            If seed is omitted or None, the current system time is used. If seed
            is an int, it is used directly.
    """
    # Initialize the random number generator.
    random.seed(seed)

    for i in range(count[0]):
        x = (i - 0.5 * (count[0] - 1)) * distance[0]

        for j in range(count[1]):
            y = (j - 0.5 * (count[1] - 1)) * distance[1]

            for k in range(count[2]):
                z = (k - 0.5 * (count[2] - 1)) * distance[2]

                # Create a matrix with position randomization
                result = Gf.Matrix4d(1)
                result.SetTranslate(
                    Gf.Vec3d(
                        x,
                        y,
                        z,
                    )
                )

                id = int(random.random() * id_count)

                yield (result, id)