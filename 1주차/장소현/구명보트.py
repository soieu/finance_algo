from collections import deque

def solution(people, limit):
    count = 0
    # 오름차순으로 정렬
    people = deque(sorted(people))

    # 모든 사람이 구출될 때까지 반복
    while people:
        # 몸무게가 가장 무거운 사람 구출
        person = people.pop()
        # 무게 제한을 넘지 않는다면, 몸무게가 가장 가벼운 사람과 함께 구출
        if len(people) > 0 and person + people[0] <= limit:
            people.popleft()

        count += 1

    return count