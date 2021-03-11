def studying_hours(hours: list) -> int:
    counter = 1
    study_streaks = []

    for index in range(len(hours) - 1):
        if hours[index] <= hours[index + 1]:
            counter += 1
        else:
            study_streaks.append(counter)
            counter = 1

    if counter and not len(study_streaks):
        return counter

    if len(study_streaks):
        return max(study_streaks)
    else:
        return 1