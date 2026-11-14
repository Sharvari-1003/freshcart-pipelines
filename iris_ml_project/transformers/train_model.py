
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer

if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def train_model(data, *args, **kwargs):
    train_df = data['train']
    test_df = data['test']

    X_train = train_df.drop(columns=['target'])
    y_train = train_df['target']

    X_test = test_df.drop(columns=['target'])
    y_test = test_df['target']

    max_depth = kwargs.get('max_depth', 3)

    model = DecisionTreeClassifier(max_depth=max_depth, random_state=42)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    print(f"max_depth = {max_depth} | Test accuracy = {accuracy:.3f}")

    result = test_df.copy()
    result['predicted'] = predictions

    return result


@test
def test_output(output, *args):
    accuracy = accuracy_score(output['target'], output['predicted'])
    assert accuracy >= 0.80, f"Accuracy too low: {accuracy:.3f}"
    print("Model accuracy test passed!")
