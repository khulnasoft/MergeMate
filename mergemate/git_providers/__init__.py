from mergemate.config_loader import get_settings
from mergemate.git_providers.bitbucket_provider import BitbucketProvider
from mergemate.git_providers.bitbucket_server_provider import BitbucketServerProvider
from mergemate.git_providers.codecommit_provider import CodeCommitProvider
from mergemate.git_providers.github_provider import GithubProvider
from mergemate.git_providers.gitlab_provider import GitLabProvider
from mergemate.git_providers.local_git_provider import LocalGitProvider
from mergemate.git_providers.azuredevops_provider import AzureDevopsProvider
from mergemate.git_providers.gerrit_provider import GerritProvider


_GIT_PROVIDERS = {
    'github': GithubProvider,
    'gitlab': GitLabProvider,
    'bitbucket': BitbucketProvider,
    'bitbucket_server': BitbucketServerProvider,
    'azure': AzureDevopsProvider,
    'codecommit': CodeCommitProvider,
    'local' : LocalGitProvider,
    'gerrit': GerritProvider,
}

def get_git_provider():
    try:
        provider_id = get_settings().config.git_provider
    except AttributeError as e:
        raise ValueError("git_provider is a required attribute in the configuration file") from e
    if provider_id not in _GIT_PROVIDERS:
        raise ValueError(f"Unknown git provider: {provider_id}")
    return _GIT_PROVIDERS[provider_id]
