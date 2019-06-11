def intersect(s1_x, s2_x, s1_y, s2_y, width_obj1, length_obj1):
    if ((s1_x > s2_x - length_obj1) and (s1_x < s2_x + length_obj1)
            and (s1_y > s2_y - width_obj1) and (s1_y < s2_y + width_obj1)):
        return True
    else:
        return False
