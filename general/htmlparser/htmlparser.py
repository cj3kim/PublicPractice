from collections import deque
import os
import re

class HtmlParser():
    def __init__():
        "None"

def parse(file_path):
    html_file = open(file_path, 'r')
    stack = deque()

    left_angle_index  = 0
    right_angle_index = 0
    end_tag = False

    for line in html_file:
        for i, char in enumerate(line):
            if char == "<":
                end_tag_check = line[i+1] == "/"
                left_angle_index = i+1 if end_tag_check else i
                end_tag = True if end_tag_check else False
            elif char == ">":
                right_angle_index = i

                tag_name = line[left_angle_index+1: right_angle_index]
                if end_tag:
                    if stack[-1] == tag_name: stack.pop()
                    end_tag = False
                else: stack.append(tag_name)

    return True if len(stack) == 0 else False



def test_parse():
    assert parse(os.path.join(os.getcwd(),'text.html')) == True





