# cook your dish here
def find_winner_and_lead(N, scores):
    cumulative_score_1 = 0
    cumulative_score_2 = 0
    max_lead = 0
    winner = 0

    for score in scores:
        S, T = score
        cumulative_score_1 += S
        cumulative_score_2 += T

        if cumulative_score_1 > cumulative_score_2:
            lead = cumulative_score_1 - cumulative_score_2
            if lead > max_lead:
                max_lead = lead
                winner = 1
        else:
            lead = cumulative_score_2 - cumulative_score_1
            if lead > max_lead:
                max_lead = lead
                winner = 2

    return winner, max_lead

# Example usage
if __name__ == "__main__":
    N = int(input().strip())
    scores = [tuple(map(int, input().strip().split())) for _ in range(N)]
    winner, max_lead = find_winner_and_lead(N, scores)
    print(winner, max_lead)
    