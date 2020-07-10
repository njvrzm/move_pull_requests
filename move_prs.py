from github import Github
import fire
import logging
import os
import sys

logging.basicConfig(stream=sys.stderr,
	                style='{',
	                format='{asctime} {levelname} {message}')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def move_prs(repo_name, from_branch='master', to_branch='main'):
    gh = Github(os.environ['GITHUB_AUTH_TOKEN'])
    repo = gh.get_repo(repo_name)
    pulls = list(repo.get_pulls(base=from_branch))
    if not pulls:
    	logger.info("No pull requests to move.")
    	sys.exit(0)
    for pr in pulls:
        logger.info("Updating #{} ({})...".format(pr.number, pr.title))
        pr.edit(base=to_branch)
    logger.info("Moved {} pull request(s) from {} to {}".format(len(pulls),
    	                                                        from_branch,
    	                                                        to_branch))

if __name__ == '__main__':
    fire.Fire(move_prs)
