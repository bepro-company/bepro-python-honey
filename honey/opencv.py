import yaml


def yml2json(yml_text):
    text_lines = yml_text.split('\n')

    for start in ('%YAML:', '---'):
        if text_lines[0].startswith(start):
            del text_lines[0]

    yml_text = '\n'.join(text_lines)
    yml_text = yml_text.replace('!!opencv-matrix', '')
    return yaml.load(yml_text, yaml.Loader)
