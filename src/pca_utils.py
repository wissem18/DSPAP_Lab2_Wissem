"""Reusable PCA utilities for Lab 2.

During Task 2.4, move the functions developed in the notebook into this file.
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def run_pca(dataframe, feature_names, n_components):
    """Run PCA on selected features and return the fitted model outputs.

    Args:
        dataframe (pd.DataFrame): Input dataset containing the selected features.
        feature_names (list[str]): Names of the columns used for PCA.
        n_components (int): Number of principal components to retain.

    Returns:
        tuple: A tuple containing:
            - pca_model (PCA): The fitted PCA model.
            - transformed_data (np.ndarray): PCA-transformed data.
            - loadings (pd.DataFrame): PCA loadings with original features as rows.
    """
    cleaned_data = dataframe[feature_names].dropna()
    feature_matrix = cleaned_data[feature_names].values

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(feature_matrix)

    pca_model = PCA(n_components=n_components)
    transformed_data = pca_model.fit_transform(scaled_features)

    loadings = pd.DataFrame(
        pca_model.components_.T,
        index=feature_names,
        columns=[f"PC{i + 1}" for i in range(n_components)],
    )

    return pca_model, transformed_data, loadings

def plot_explained_variance(pca_model):
    """Plot the explained variance ratio for each principal component.

    Args:
        pca_model (PCA): A fitted PCA model.

    Returns:
        None: Displays the variance plot using matplotlib.
    """
    explained_variance = pca_model.explained_variance_ratio_

    plt.bar(range(1, len(explained_variance) + 1), explained_variance)
    plt.xlabel("Principal component")
    plt.ylabel("Explained variance ratio")
    plt.title("PCA explained variance")
    plt.xticks(range(1, len(explained_variance) + 1))
    plt.show()
