def analyze_user_activity(log_file_path: str) -> dict:
    
    infile = open(log_file_path, 'r')
    file_content = infile.read()
    infile.close()

    action_count = {}
    user_session = {}
    users = []

    for line in file_content.strip().split('\n'):
        parts = line.split()
        if len(parts) >= 4: 
            user = parts[1]
            action = parts[2]
            val_str = parts[3]
            if not val_str.replace('.','',1).isdigit():
                continue
            value = float(val_str)
            if user not in users:
                users.append(user)

            if action in action_count:
                action_count[action] += 1
            else:
                action_count[action] = 1

            if action == 'login':
                user_session[user] = value

    sorted_action_counts = {}
    for key in sorted(action_count.keys()):
        sorted_action_counts[key] = action_count[key]

    total_session_time = 0.0
    for val in user_session.values():
        total_session_time += val

    average_session_time = total_session_time / len(user_session) if user_session else 0.0

    most_active_user = None
    max_val = -1.0
    for user, val in user_session.items():
        if val > max_val:
            max_val = val
            most_active_user = user

    return {
        'action_counts': sorted_action_counts,
        'average_session_time': average_session_time,
        'most_active_user': most_active_user,
        'total_users': len(users)
    }

if __name__ == "__main__":
    result = analyze_user_activity("activity.log")
    from pprint import pprint
    pprint(result)

# {'action_counts': {'login': 2, 'logout': 2, 'submit': 1, 'view': 2},
#  'average_session_time': 160.0,
#  'most_active_user': 'u002',
#  'total_users': 2}
