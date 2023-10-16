import json

def lets_see_who_does_not_follow_me(following, followers):
    with open(following, 'r') as file1:
        data1 = json.load(file1)

    with open(followers, 'r') as file2:
        data2 = json.load(file2)

    values_following = [entry['string_list_data'][0]['value'] for entry in data1]
    values_followers = [entry['string_list_data'][0]['value'] for entry in data2]

    not_followers = [value for value in values_following if value not in values_followers]

    print("------------------------------------\n"
          "People who does not follow you back:\n")

    n = 0
    for user_name in not_followers:
        print("[", n, "] ", user_name, " - https://www.instagram.com/" + user_name)
        n += 1

    print("------------------------------------\n"
          "Following: ", len(values_following), "\n"
          "Followers: ", len(values_followers), "\n\n"
          "NOT Followers: ", len(not_followers), "\n"
          "------------------------------------")


# USAGE:
following_path = "data/following.json"
followers_path = "data/followers_1.json"
lets_see_who_does_not_follow_me(following_path, followers_path)

