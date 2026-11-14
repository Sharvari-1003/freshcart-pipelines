
from sklearn.model_selection import train_test_split

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer

if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def prepare_data(df, *args, **kwargs):
    X = df.drop(columns=['target'])
    y = df['target']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    train_df = X_train.copy()
    train_df['target'] = y_train

    test_df = X_test.copy()
    test_df['target'] = y_test

    print("Train rows:", len(train_df), "| Test rows:", len(test_df))

    return {'train': train_df, 'test': test_df}


@test
def test_output(output, *args):
    assert len(output['train']) == 120
    assert len(output['test']) == 30
    print("Data split test passed!")
