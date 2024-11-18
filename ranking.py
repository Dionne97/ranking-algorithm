import sys
from collections import defaultdict


def parse_match_results(matches):
    """Parses match results and computes scores for all teams."""
    scores = defaultdict(int)

    for match in matches:
        team1, team2 = match.split(", ")
        name1, score1 = team1.rsplit(" ", 1)
        name2, score2 = team2.rsplit(" ", 1)

        score1, score2 = int(score1), int(score2)

        # Ensure all teams are added to the scores dictionary
        if name1 not in scores:
            scores[name1] = 0
        if name2 not in scores:
            scores[name2] = 0

        if score1 > score2:
            scores[name1] += 3
        elif score1 < score2:
            scores[name2] += 3
        else:
            scores[name1] += 1
            scores[name2] += 1

    return scores




def rank_teams(scores):
    """Ranks teams by scores and breaks ties alphabetically."""
    return sorted(
        scores.items(),
        key=lambda item: (-item[1], item[0])
    )


def format_output(ranked_teams):
    """Formats ranked teams for output."""
    result = []
    rank = 0
    previous_score = None

    for idx, (team, points) in enumerate(ranked_teams, start=1):
        if points != previous_score:
            rank = idx
        point_label = "pt" if points == 1 else "pts"
        result.append(f"{rank}. {team}, {points} {point_label}")
        previous_score = points

    return "\n".join(result)


def main(input_lines):
    scores = parse_match_results(input_lines)
    ranked_teams = rank_teams(scores)
    return format_output(ranked_teams)


if __name__ == "__main__":
    input_lines = []

    # Support input via file or stdin
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as file:
            input_lines = file.read().strip().split("\n")
    else:
        input_lines = sys.stdin.read().strip().split("\n")

    print(main(input_lines))
