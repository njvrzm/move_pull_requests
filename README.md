# Intro

When you delete a branch from Github (for example, after switching your default branch from `master` to `main`) any open pull requests based on that branch are closed. This is a simple tool to update all open PRs with a given base branch to a different target.

Note that [Github's documentation on changing a PR's base branch](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/changing-the-base-branch-of-a-pull-request) includes this warning:

> Warning: When you change the base branch of your pull request, some commits may be removed from the timeline. Review comments may also become outdated, as the line of code that the comment referenced may no longer be part of the changes in the pull request.

See that doc for more information.

# Setup

```shell
$ git clone git@github.com:njvrzm/move_pull_requests
$ cd move_pull_requests
$ pip install -r requirements.txt
```

# Usage

1. Generate a [personal access token](https://github.com/settings/tokens) with the `repo` permission (`public_repo` will also work, if the repo you're working with is public). In the examples below the access token is abcdef01234567890; real tokens are 40 digit hexadecimal strings.
1. Run the `move_prs.py` script with the access token set in the environment variable `GITHUB_AUTH_TOKEN`.
1. Pass the full repo name (`<user>/<repo>` or `<organization>/<repo>`) as a positional argument.
1. Optionally, specify the `--from_branch` and/or `--to_branch`.

To move PRs on this repo from `master` to `main`, for instance:

```
$ GITHUB_AUTH_TOKEN=abcdef01234567890 python move_prs.py njvrzm/move_pull_requests
```

To move them from `blue` to `yellow` instead:

```shell
$ GITHUB_AUTH_TOKEN=abcdef01234567890 python move_prs.py njvrzm/move_pull_requests --from_branch=blue --to_branch=yellow
```

