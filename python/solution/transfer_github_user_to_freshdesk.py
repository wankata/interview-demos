#!/usr/bin/env python3
import textwrap
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from collections.abc import Mapping
from github_api_client import users
from github_api_client.exceptions import GitHubClientError
from freshdesk_api_client import contacts
from freshdesk_api_client.exceptions import FreshdeskClientError


def transfer_user(args: Mapping[str, str]):
    """Fetch github user and create freshdesk client from it"""
    try:
        user = users.get_user(args['user'])
    except GitHubClientError:
        print("\nError occured while fetching the user'sinformation from GitHub\n\n")
        raise

    post_params = {
        'name': user.name or user.login,
        'email': user.email,
        'twitter_id': user.twitter_username,
        'address': user.location,
        'description': user.bio,
    }

    try:
        contact = contacts.create_contact(args['subdomain'], post_params)
    except FreshdeskClientError:
        print('\nError occured while creating the contact in Freshdesk\n\n')
        raise

    print(f'Successfully transfered GitHub user {user.login} to Freshdesk with id: {contact.id}')


def main() -> None:
    """Define available arguments and run transfer_user"""

    parser = ArgumentParser(
        formatter_class=RawDescriptionHelpFormatter,
        description=textwrap.dedent("""
        Transfer Github user and create Freshdesk client from the fetched info.
        """),
    )

    parser.add_argument('--user', help='GitHub login (username)', required=True)
    parser.add_argument('--subdomain', help='Freshdesk subdomain', required=True)
    args = parser.parse_args()
    transfer_user(vars(args))


if __name__ == '__main__':
    main()
