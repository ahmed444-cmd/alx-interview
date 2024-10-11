#!/usr/bin/python3
'''LockBoxes'''


def canUnlockAll(boxes):
    '''Checks whether all the boxes can be unlocked.
    Returns:
        True: If all boxes are unlocked.
        False: If some boxes remain locked.
    '''
    length = len(boxes)
    keys = set()
    opened_boxes = []
    i = 0

    while i < length:
        oldi = i
        opened_boxes.append(i)
        keys.update(boxes[i])
        for key in keys:
            if key != 0 and key < length and key not in opened_boxes:
                i = key
                break
        if oldi != i:
            continue
        else:
            break

    for i in range(length):
        if i not in opened_boxes and i != 0:
            return False
    return True
