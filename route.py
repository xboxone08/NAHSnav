first_floor = tuple()
second_floor = tuple()
third_floor = tuple()


def route(dest_room_number: int, src_room_number: int):
    # Check if they are on the same floor
    if str(dest_room_number)[0] == str(src_room_number)[0]:
        
