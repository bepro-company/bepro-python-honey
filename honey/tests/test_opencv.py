from honey.opencv import yml2json


def test():
    yml_text = """%YAML:1.0
---
Camera 0:
    focal: 1
    R: !!opencv-matrix
        rows: 3
        cols: 3"""

    assert yml2json(yml_text) == {
        'Camera 0': {
            'focal': 1,
            'R': {
                'rows': 3,
                'cols': 3
            }
        }
    }
