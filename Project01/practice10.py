users = [
    {"id": 0, "name": "호랑이0"},
    {"id": 1, "name": "호랑이1"},
    {"id": 2, "name": "호랑이2"},
    {"id": 3, "name": "호랑이3"},
    {"id": 4, "name": "호랑이4"},
    {"id": 5, "name": "호랑이5"},
    {"id": 6, "name": "호랑이6"},
    {"id": 7, "name": "호랑이7"},
    {"id": 8, "name": "호랑이8"},
    {"id": 9, "name": "호랑이9"}
]


friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

friendships = {user["id"]: [] for user in users}
# print(friendships)
# print('')

for i, j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)

# for k, v in friendships.items():
#     print(k, ':', v)

def number_of_friends(user):
    user_id = user["id"]
    friends_ids = friendships[user_id]
    return len(friends_ids)

total_connections = sum(number_of_friends(user) for user in users)

num_users = len(users)
avg_connections = total_connections / num_users

num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]

num_friends_by_id.sort(key=lambda id_and_friends: id_and_friends[1], reverse=True)

from collections import Counter

def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]
        for foaf_id in friendships[friend_id]
        if foaf_id != user_id
        and foaf_id not in friendships[user_id]
    )

# print(friends_of_friends(users[3]))

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

def data_scientist_who_like(target_interesrt):
    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interesrt]

# print(data_scientist_who_like("Big Data"))


from collections import defaultdict

# Key: user_id, Value: interest
interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

# print(interests_by_user_id[9])

# Key: interest, Value: user_id
user_ids_by_interests = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interests[interest].append(user_id)

# print(user_ids_by_interests["MapReduce"])

def most_common_interests_with(user):
    return Counter(
        interest_user_id
        for interest in interests_by_user_id[user["id"]]
        for interest_user_id in user_ids_by_interests[interest]
        if interest_user_id != user["id"]
    )

# print(most_common_interests_with(users[2]))

# words_and_counts = Counter(word
#                            for user, interest in interests
#                            for word in interest.lower().split())
#
# for word, count in words_and_counts.most_common():
#     if count > 1:
#         print(word, ':', count)


salaries_and_tenures = [(8300, 8.7), (8800, 7.1),
                        (4800, 0.7), (7600, 6),
                        (6900, 6.5), (7600, 7.5),
                        (6000, 2.5), (8300, 10),
                        (4800, 1.9), (6300, 4.2)]

salaries_by_tenures = defaultdict(list)

def tenure_bucket(tenure):
    if tenure < 2:
        return 'less than 2'
    elif tenure < 5:
        return 'between 2 and 5'
    else:
        return 'more than 5'

for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salaries_by_tenures[bucket].append(salary)

average_salary_by_bucket = {
    tenure : sum(salary) / len(salary)
    for tenure, salary in salaries_by_tenures.items()
}

# print(average_salary_by_bucket)




