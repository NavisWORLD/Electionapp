# visualization.py

import matplotlib.pyplot as plt
from typing import List, Dict


def plot_popularity(proposals: List[Dict[str, object]]):
    """
    Plot a bar chart of proposal popularity based on the number of votes.

    Parameters:
    proposals (list): List of dictionaries containing proposal information.
                      Each dictionary has keys 'id' and 'votes'.
    """
    if not proposals:
        raise ValueError("Proposals list cannot be empty")

    ids = [p['id'] for p in proposals]
    votes = [p['votes'] for p in proposals]

    plt.bar(ids, votes)
    plt.xlabel('Proposals')
    plt.ylabel('Votes')
    plt.title('Proposal Popularity')
    plt.xticks(ids)
    plt.grid(axis='y')
    plt.show()


def plot_voting_trends(votes: Dict[int, int]):
    """
    Plot a line chart showing voting trends for each proposal.

    Parameters:
    votes (dict): Dictionary with proposal IDs as keys and vote counts as values.
    """
    if not votes:
        raise ValueError("Votes dictionary cannot be empty")

    proposal_ids = sorted(votes.keys())
    vote_counts = [votes[pid] for pid in proposal_ids]

    plt.plot(proposal_ids, vote_counts, marker='o')
    plt.xlabel('Proposals')
    plt.ylabel('Votes')
    plt.title('Voting Trends')
    plt.xticks(proposal_ids)
    plt.grid()
    plt.show()


def plot_user_engagement(user_votes: Dict[str, List[int]]):
    """
    Plot a scatter plot of user engagement based on the number of votes cast by each user.

    Parameters:
    user_votes (dict): Dictionary with usernames as keys and lists of voted proposal IDs as values.
    """
    if not user_votes:
        raise ValueError("User votes dictionary cannot be empty")

    users = list(user_votes.keys())
    votes = [len(user_votes[user]) for user in users]

    plt.scatter(users, votes)
    plt.xlabel('Users')
    plt.ylabel('Number of Votes')
    plt.title('User Engagement')
    plt.grid()
    plt.show()
