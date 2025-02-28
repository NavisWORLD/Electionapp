# main.py
from calculations import calculate_D8D
from voting_mechanism import submit_proposal, cast_vote, cast_vote_against, tally_votes, get_user_votes
from visualization import plot_popularity, plot_voting_trends, plot_user_engagement
from authentication import register_user, login_user, logout_user
from password_recovery import generate_recovery_token, reset_password

# Initialize data storage
proposals = []
votes = {}
against_votes = {}
user_votes = {}


def display_proposals():
    """
    Display the current proposals.
    """
    print("\nCurrent Proposals:")
    for proposal in proposals:
        print(
            f"ID: {proposal['id']}, User: {proposal['user']}, Proposal: {proposal['proposal']}, Votes For: {proposal['votes']}, Votes Against: {proposal.get('against_votes', 0)}")


def main():
    print("Welcome to the Election Management App!")

    logged_in_user = None

    while True:
        print("\nOptions:")
        print("1: Register")
        print("2: Login")
        print("3: Submit a proposal")
        print("4: View proposals and vote")
        print("5: View tally")
        print("6: Show visualizations")
        print("7: Logout")
        print("8: Generate Password Recovery Token")
        print("9: Reset Password")
        print("10: Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            try:
                print(register_user(username, password))
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            try:
                login_status = login_user(username, password)
                print(login_status)
                if login_status == "Login successful.":
                    logged_in_user = username
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '3':
            if not logged_in_user:
                print("You need to log in first.")
                continue
            user = logged_in_user
            proposal = input("Enter your proposal: ")
            if not proposal:
                print("Proposal text is required.")
                continue
            try:
                proposal_id = submit_proposal(proposal, user)
                proposals.append(
                    {'id': proposal_id, 'proposal': proposal, 'user': user, 'votes': 0, 'against_votes': 0})
                votes[proposal_id] = 0
                against_votes[proposal_id] = 0
                print("Proposal submitted.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '4':
            if not logged_in_user:
                print("You need to log in first.")
                continue
            display_proposals()
            try:
                proposal_id = int(input("Enter proposal ID to vote on: "))
                if any(proposal['id'] == proposal_id for proposal in proposals):
                    user_choice = input("Enter 'for' to vote for or 'against' to vote against: ").strip().lower()
                    if user_choice == 'for':
                        cast_vote(proposal_id, logged_in_user)
                        for proposal in proposals:
                            if proposal['id'] == proposal_id:
                                proposal['votes'] += 1
                                break
                        votes[proposal_id] += 1
                    elif user_choice == 'against':
                        cast_vote_against(proposal_id, logged_in_user)
                        for proposal in proposals:
                            if proposal['id'] == proposal_id:
                                proposal['against_votes'] = proposal.get('against_votes', 0) + 1
                                break
                        against_votes[proposal_id] += 1
                    else:
                        print("Invalid choice. You can only vote 'for' or 'against'.")
                        continue
                    if logged_in_user not in user_votes:
                        user_votes[logged_in_user] = []
                    user_votes[logged_in_user].append(proposal_id)
                    print("Vote cast.")
                else:
                    print("Invalid proposal ID.")
            except ValueError:
                print("Invalid input. Please enter a number for proposal ID.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '5':
            results = tally_votes()
            print("\nTally Results:")
            for proposal in results:
                print(
                    f"Proposal {proposal['id']} by {proposal['user']}: {proposal['proposal']} - Votes For: {proposal['votes']}, Votes Against: {proposal.get('against_votes', 0)}")

        elif choice == '6':
            print("\nVisualizations:")
            print("1: Proposal Popularity")
            print("2: Voting Trends")
            print("3: User Engagement")
            vis_choice = input("Choose visualization: ")

            if vis_choice == '1':
                plot_popularity(proposals)
            elif vis_choice == '2':
                plot_voting_trends(votes)
            elif vis_choice == '3':
                plot_user_engagement(user_votes)
            else:
                print("Invalid choice.")

        elif choice == '7':
            if not logged_in_user:
                print("No user is logged in.")
            else:
                print(logout_user())
                logged_in_user = None

        elif choice == '8':
            username = input("Enter your username to generate recovery token: ")
            try:
                token = generate_recovery_token(username)
                print(f"Recovery token: {token}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '9':
            token = input("Enter your recovery token: ")
            new_password = input("Enter your new password: ")
            try:
                print(reset_password(token, new_password))
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '10':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
