from sklearn.metrics import confusion_matrix


def f1_macro(y_true, y_pred):
    """Calculate the F1 macro score

    Harmonic mean of precision and recall

    :param numpy.ndarray y_true:
    :param numpy.ndarray y_pred:
    :return: F1 score
    :rtype: float
    """
    tn, fp, fn, tp = confusion_matrix(y_pred, y_true).ravel()
    p = tp / (tp + fp) # Precision
    r = tp / (tp + fn) # Recall
    # Harmonic Mean of Precision and Recall
    f1 = 2 / (p**-1 + r**-1)
    return f1
