Slack Reviewers - Command
=========================

This is a slack command used to retrieve random reviewers for a pull request.

How it works
============

This command reads the members of the channel where its called and return
a random number of people to review the pull request.

Example:
    >> /review http://github.com/lucasmagnum/slack-reviewers/pull/01

    Hey @user2, @user3, @user4 could you review this Pull Request?
    Pull request https://github.com/fyndiq/fyndiq-2.0/pull/74



How to install
==============

1. Deploy it to Heroku
2. Install a new app in your Slack account
3. Create an `review` command
4. Create a channel with your reviewers
5. Start using it
