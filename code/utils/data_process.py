

def mean_normalize(data):
    """Mean normalize columns of DataFrame"""

    # Calculate Z_score
    normalized = (data - data.mean()) / data.std()
    return normalized