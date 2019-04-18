from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from split_dataset import split_train_test
import numpy as np
import matplotlib.pyplot as plt


def run_random_forest(df_knn):
    print("\n\n----------------------Random Forest----------------------\n\n")

    y = np.array(df_knn["class"])
    x = np.array(df_knn.drop(columns="class"))

    x_train, x_test, y_train, y_test = split_train_test(x, y)

    rf = RandomForestClassifier(
        random_state=1, n_estimators=250, min_samples_split=8, min_samples_leaf=4
    )
    rf.fit(x_train, y_train)
    pred = rf.predict(x_test)
    test_pred = rf.predict(x_train)

    test_frame = x_train[1]
    pred_frame = rf.predict(np.reshape(test_frame, (1, -1)))
    print(
        "\n\n----------------------Pred Frame----------------------\n\n",
        pred_frame
    )
    
    # print the Training Accuracy
    print(
        "\n\n----------------------Training Set Accuracy----------------------\n\n",
        accuracy_score(y_train, test_pred),
    )
    print(
        "\n\n----------------------Training Set Accuracy----------------------\n\n",
        accuracy_score(y_test, pred),
    )

    return rf
