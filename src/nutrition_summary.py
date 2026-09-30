

"""Nutrition analysis module used in Parts 2 and 3 of Lab 2."""


class NutritionAnalyzer:
    """Explore descriptive statistics for selected nutrition features."""

    def __init__(self, dataframe):
        """Store the food DataFrame used by the analysis methods."""
        self.dataframe = dataframe

    def describe_features(self, feature_names):
        """Return descriptive statistics for the selected feature columns."""
        return self.dataframe[feature_names].describe()

    def summarize_sugars(self):
        """Return mean and median sugar values."""
        sugar_values = self.dataframe["sugars_100g"]
        return {
            "mean_sugar": sugar_values.mean(),
            "median_sugar": sugar_values.median(),
        }

    def summarize_proteins(self):
        """Return mean and median protein values."""
        protein_values = self.dataframe["proteins_100g"]
        return {
            "mean_protein": protein_values.mean(),
            "median_protein": protein_values.median(),
        }

    def build_nutrition_summary(self):
        """Return both sugar and protein summaries."""
        return {
            "sugar_summary": self.summarize_sugars(),
            "protein_summary": self.summarize_proteins(),
        }
