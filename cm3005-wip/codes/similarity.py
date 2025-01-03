import difflib
from dataclasses import dataclass

import pandas as pd



@dataclass()
class FuzzyMerge:
    """
        Works like pandas merge except also merges on approximate matches.
    """
    left: pd.DataFrame
    right: pd.DataFrame
    left_on: str
    right_on: str
    how: str = "inner"
    cutoff: float = 0.3

    def main(self) -> pd.DataFrame:
        temp = self.right.copy()
        temp[self.left_on] = [
            self.get_closest_match(x, self.left[self.left_on]) for x in temp[self.right_on]
        ]

        return self.left.merge(temp, on=self.left_on, how=self.how)

    def get_closest_match(self, left: pd.Series, right: pd.Series) -> str | None:
        matches = difflib.get_close_matches(left, right, cutoff=self.cutoff)
        return matches[0] if matches else None
