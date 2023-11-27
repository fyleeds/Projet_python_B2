from get_info import get_infos

def verify(username):
    info = get_infos()
    for item in info:
        if username == item: 
            return False
    return True