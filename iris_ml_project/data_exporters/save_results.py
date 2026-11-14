
if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_exporter
def save_results(df, *args, **kwargs):
    df.to_csv('/content/iris_predictions.csv', index=False)
    print(f"Saved {len(df)} predictions to iris_predictions.csv")


@test
def test_output(*args):
    import os
    assert os.path.exists('/content/iris_predictions.csv'), "CSV file was not created"
    print("CSV export test passed!")
