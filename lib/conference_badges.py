def badge_maker(name):
    return "Hello, my name is {}.".format(name)

def batch_badge_creator(names):
    badges = [badge_maker(name) for name in names]
    return badges

def assign_rooms(names):
    room_assignments = ["Hello, {}! You'll be assigned to room {}!".format(name, index + 1) for index, name in enumerate(names)]
    return room_assignments

def printer(names):
    badges = batch_badge_creator(names)
    room_assignments = assign_rooms(names)
    
    for badge in badges:
        print(badge)
    
    for assignment in room_assignments:
        print(assignment)
speaker_names = ["Arel", "Carol"]
printer(speaker_names)
