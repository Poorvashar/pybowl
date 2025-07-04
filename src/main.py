#def score(score_sheet):
    #score = 0
    #for char in score_sheet:
        #if char.isdigit():
            #score += int(char) 
    #return score


def score(score_sheet):
    frames = score_sheet.split()
    total_score = 0
    rolls = []

    # Flatten all rolls from frames into a single list
    for frame in frames:
        if frame == 'X':
            rolls.append('X')
        else:
            for ch in frame:
                rolls.append(ch)

    i = 0  # Index in the rolls list
    frame_count = 0

    while frame_count < 10:
        roll = rolls[i]

        # STRIKE
        if roll == 'X':
            total_score += 10

            # Bonus: next two rolls
            for j in range(1, 3):
                if i + j < len(rolls):
                    bonus = rolls[i + j]
                    if bonus == 'X':
                        total_score += 10
                    elif bonus == '/':
                        total_score += 10 - int(rolls[i + j - 1])
                    elif bonus.isdigit():
                        total_score += int(bonus)
            i += 1
            frame_count += 1

        # SPARE
        elif i + 1 < len(rolls):
            first = rolls[i]
            second = rolls[i + 1]

            if second == '/':
                total_score += 10
                # Bonus: next roll
                if i + 2 < len(rolls):
                    bonus = rolls[i + 2]
                    if bonus == 'X':
                        total_score += 10
                    elif bonus.isdigit():
                        total_score += int(bonus)
            else:
                # Open frame
                if first.isdigit():
                    total_score += int(first)
                if second.isdigit():
                    total_score += int(second)
            i += 2
            frame_count += 1

    return total_score
