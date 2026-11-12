
from sklearn.model_selection import train_test_split

# Import Mage decorator.
# If Mage is not installed, use a normal Python function.
try:
    from mage_ai.data_preparation.decorators import transformer
except ImportError:
    def transformer(func):
        return func


@transformer
def transform(df, *args, **kwargs):
    """
    Divide Iris dataset into 80% training and 20% testing data.
    """

    train_indices, test_indices = train_test_split(
        df.index,
        test_size=0.3,
        random_state=42,
        stratify=df["target"]
    )

    output = df.copy()

    output["split"] = "train"
    output.loc[test_indices, "split"] = "test"

    return output
