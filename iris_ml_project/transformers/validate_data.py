
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer

if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def validate_data(df, *args, **kwargs):
    print("Checking missing values...")
    print("Missing values:", df.isnull().sum().sum())

    print("Checking Iris classes...")
    print("Unique classes:", sorted(df['target'].unique()))

    return df


@test
def test_output(output, *args):
    assert output.isnull().sum().sum() == 0, "Dataset contains missing values"
    assert output['target'].nunique() == 3, "Dataset must have exactly 3 classes"
    print("Data validation tests passed!")
