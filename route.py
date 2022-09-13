first_floor = tuple()
second_floor = tuple()
third_floor = tuple()


def route(dest_room_number: int, src_room_number: int):
    # We will need it in string form
    dest_room_number = str(dest_room_number)
    # Check if they are on the same floor
    if dest_room_number[0] == src_room_number[0]:
        return (dest_room_number),
    else:
        if dest_room_number[2:] < 60:
            return "wws", dest_room_number
        else:
            return "ews", dest_room_number
