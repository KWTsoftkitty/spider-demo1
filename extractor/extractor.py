"""extractor"""

import jq


def extractor(inputs, jq_path):
    """
    Return the value given the dictionary and jq_path
    If the path does not exist, return NONE
    return str
    """
    return jq.compile(jq_path).input(inputs).first()
