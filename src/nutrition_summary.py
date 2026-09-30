

"""Nutrition analysis module used in Parts 2 and 3 of Lab 2."""


class NutritionAnalyzer:
    """Explore descriptive statistics for selected nutrition features."""

    def __init__(self, dataframe):
        """Store the food DataFrame used by the analysis methods."""
        self.dataframe = dataframe

    def describe_features(self, feature_names):
        """Return descriptive statistics for the selected feature columns."""
        return self.dataframe[feature_names].describe()

    def build_nutrition_summary(self):
        """Return the nutrition summaries currently available in the project."""
        return {}
