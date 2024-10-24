def badge_maker(name):
    return f"Hello, my name is {name}."


def batch_badge_creator(names):
    badges = []
    for name in names:
        badges.append(badge_maker(name))
    return badges


def assign_rooms(speakers):
    room_assignments = []
    for index, speaker in enumerate(speakers):
        room_assignments.append(f"Hello, {speaker}! You'll be assigned to room {index + 1}!")
    return room_assignments


def printer(speakers):
    for badge in batch_badge_creator(speakers):
        print(badge)
    
    for assignment in assign_rooms(speakers):
        print(assignment)

