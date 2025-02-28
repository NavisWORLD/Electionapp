# voting_mechanism.py

import json
from collections import defaultdict

# Data structures to hold proposals, votes, user votes, and against votes
proposals = []
votes = defaultdict(int)
against_votes = defaultdict(int)
user_votes = defaultdict(list)


def submit_proposal(proposal, user):
    """
    Submit a new proposal.

    Parameters:
    proposal (str): The proposal text.
    user (str): The username of the person submitting the proposal.

    Returns:
    int: The ID of the submitted proposal.

    Raises:
    ValueError: If proposal text or user is empty.
    """
    if not proposal:
        raise ValueError("Proposal text cannot be empty")
    if not user:
        raise ValueError("User cannot be empty")

    proposal_id = len(proposals)
    proposals.append({'id': proposal_id, 'proposal': proposal, 'user': user, 'votes': 0, 'against_votes': 0})
    return proposal_id


def cast_vote(proposal_id, user):
    """
    Cast a vote for a proposal.

    Parameters:
    proposal_id (int): The ID of the proposal to vote for.
    user (str): The username of the person casting the vote.

    Raises:
    ValueError: If proposal ID is invalid or user is empty.
    """
    if not user:
        raise ValueError("User cannot be empty")
    if not 0 <= proposal_id < len(proposals):
        raise ValueError("Invalid proposal ID")

    if proposal_id < len(proposals):
        proposals[proposal_id]['votes'] += 1
        user_votes[user].append(proposal_id)
        votes[proposal_id] += 1


def cast_vote_against(proposal_id, user):
    """
    Cast a vote against a proposal.

    Parameters:
    proposal_id (int): The ID of the proposal to vote against.
    user (str): The username of the person casting the vote.

    Raises:
    ValueError: If proposal ID is invalid or user is empty.
    """
    if not user:
        raise ValueError("User cannot be empty")
    if not 0 <= proposal_id < len(proposals):
        raise ValueError("Invalid proposal ID")

    if proposal_id < len(proposals):
        proposals[proposal_id]['against_votes'] += 1
        user_votes[user].append(proposal_id)
        against_votes[proposal_id] += 1


def tally_votes():
    """
    Tally the votes and return proposals sorted by their number of votes.

    Returns:
    list: List of proposals sorted by votes.
    """
    return sorted(proposals, key=lambda x: (x['votes'], -x['against_votes']), reverse=True)


def get_user_votes(user):
    """
    Get a list of proposals a specific user has voted for.

    Parameters:
    user (str): The username whose votes are to be fetched.

    Returns:
    list: List of proposal IDs the user has voted for.

    Raises:
    ValueError: If user is empty.
    """
    if not user:
        raise ValueError("User cannot be empty")
    return user_votes[user]


if __name__ == "__main__":
    import argparse


    def parse_arguments():
        parser = argparse.ArgumentParser(description="Voting Mechanism")
        subparsers = parser.add_subparsers(dest="command")

        submit_parser = subparsers.add_parser("submit")
        submit_parser.add_argument("proposal", type=str, help="Proposal text")
        submit_parser.add_argument("user", type=str, help="Username")

        vote_parser = subparsers.add_parser("vote")
        vote_parser.add_argument("proposal_id", type=int, help="Proposal ID")
        vote_parser.add_argument("user", type=str, help="Username")
        vote_parser.add_argument("vote_type", type=str, choices=["for", "against"], help="Vote type")

        tally_parser = subparsers.add_parser("tally", help="Tally votes")

        user_votes_parser = subparsers.add_parser("user_votes")
        user_votes_parser.add_argument("user", type=str, help="Username")

        return parser.parse_args()


    args = parse_arguments()

    if args.command == "submit":
        try:
            proposal_id = submit_proposal(args.proposal, args.user)
            print(f"Proposal submitted with ID: {proposal_id}")
        except ValueError as e:
            print(f"Error: {e}")

    elif args.command == "vote":
        try:
            if args.vote_type == "for":
                cast_vote(args.proposal_id, args.user)
                print(f"Vote cast for proposal ID: {args.proposal_id}")
            elif args.vote_type == "against":
                cast_vote_against(args.proposal_id, args.user)
                print(f"Vote cast against proposal ID: {args.proposal_id}")
        except ValueError as e:
            print(f"Error: {e}")

    elif args.command == "tally":
        results = tally_votes()
        print("Vote Tally:")
        for proposal in results:
            print(
                f"ID: {proposal['id']}, Text: {proposal['proposal']}, Votes For: {proposal['votes']}, Votes Against: {proposal['against_votes']}")

    elif args.command == "user_votes":
        try:
            user_votes_list = get_user_votes(args.user)
            print(f"User {args.user} has voted for proposals: {user_votes_list}")
        except ValueError as e:
            print(f"Error: {e}")
