
from iris_project.transformers.prepare_data import transform


def test_transform():
    X_train, X_test, y_train, y_test = transform()

    assert len(X_train) == 120
    assert len(X_test) == 30
    assert len(y_train) == 120
    assert len(y_test) == 30
