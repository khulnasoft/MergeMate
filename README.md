<div align="center">

<div align="center">


<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://khulnasoft.com/images/mergemate/logo-dark.png" width="330">
  <source media="(prefers-color-scheme: light)" srcset="https://khulnasoft.com/images/mergemate/logo-light.png" width="330">
  <img alt="logo">
</picture>
<br/>
Making pull requests less painful with an AI agent
</div>

[![GitHub license](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://github.com/khulnasoft/mergemate/blob/main/LICENSE)
[![Discord](https://badgen.net/badge/icon/discord?icon=discord&label&color=purple)](https://discord.com/channels/1057273017547378788/1126104260430528613)
[![Twitter](https://img.shields.io/twitter/follow/khulnasoft)](https://twitter.com/khulnasoft)
    <a href="https://github.com/khulnasoft/mergemate/commits/main">
    <img alt="GitHub" src="https://img.shields.io/github/last-commit/khulnasoft/mergemate/main?style=for-the-badge" height="20">
    </a>
</div>

## Table of Contents
- [News and Updates](#news-and-updates)
- [Overview](#overview)
- [Example results](#example-results)
- [Try it now](#try-it-now)
- [Installation](#installation)
- [MergeMate Pro 💎](#mergemate-pro-)
- [How it works](#how-it-works)
- [Why use MergeMate?](#why-use-mergemate)
  
## News and Updates
### Feb 11, 2024
The `review` tool has been revamped, aiming to make the feedback clearer and more relevant, and better compliment the `improve` tool.

<kbd>

<img src="https://www.khulnasoft.com/images/mergemate/review_reworked.png" width="512">

</kbd>

### Feb 6, 2024
A new feature was added to the `review` tool - [Auto-approve PRs](./docs/REVIEW.md#auto-approval-1). If enabled, this feature enables to automatically approve PRs that meet specific criteria, by commenting on a PR: `/review auto_approve`.

### Feb 2, 2024
We are excited to introduce "PR Actions" 💎:

<kbd>

[<img src="https://www.khulnasoft.com/images/mergemate/pr_actions.png" width="512"/>](https://www.khulnasoft.com/images/mergemate/pr-actions.mp4)

</kbd>

(click on the image to see a video demonstration)

### Jan 28, 2024
- 💎 Test - A new tool, [`/test component_name`](https://github.com/khulnasoft/mergemate/blob/main/docs/TEST.md), was added to MergeMate Pro. The tool will generate tests for a selected component, based on the PR code changes.
- 💎 Analyze - The [`/analyze`](https://github.com/khulnasoft/mergemate/blob/main/docs/Analyze.md) tool was updated and simplified. It now presents a summary of the code components that were changed in the PR.
### Jan 21, 2024
- 💎 Custom suggestions - A new tool, `/custom_suggestions`, was added to MergeMate Pro. The tool will propose only suggestions that follow specific guidelines defined by the user. 
See [here](https://github.com/khulnasoft/mergemate/blob/main/docs/CUSTOM_SUGGESTIONS.md) for more details.


## Overview
<div style="text-align:left;">

CodiumAI MergeMate is an open-source tool to help efficiently review and handle pull requests. It automatically analyzes the pull request and can provide several types of commands:

|       |                                                                                                                                          | GitHub | Gitlab | Bitbucket |
|-------|------------------------------------------------------------------------------------------------------------------------------------------|:------:|:------:|:---------:|
| TOOLS | Review                                                                                                                                   |   :white_check_mark:    |   :white_check_mark:    |   :white_check_mark:       |
|       | ⮑ Incremental                                                                                                                            |   :white_check_mark:    |                         |                            |
|       | ⮑ [SOC2 Compliance](https://github.com/khulnasoft/mergemate/blob/main/docs/REVIEW.md#soc2-ticket-compliance-) 💎                           |   :white_check_mark:    |   :white_check_mark:    |   :white_check_mark:        |
|       | Describe                                                                                                                                 |   :white_check_mark:    |   :white_check_mark:    |   :white_check_mark:        |
|       | ⮑ [Inline File Summary](https://github.com/khulnasoft/mergemate/blob/main/docs/DESCRIBE.md#inline-file-summary-) 💎                        |   :white_check_mark:    |       |          |
|       | Improve                                                                                                                                  |   :white_check_mark:    |   :white_check_mark:    |   :white_check_mark:        |
|       | ⮑ Extended                                                                                                                               |   :white_check_mark:    |   :white_check_mark:    |   :white_check_mark:        |
|       | Ask                                                                                                                                      |   :white_check_mark:    |   :white_check_mark:    |   :white_check_mark:        |
|       | [Custom Suggestions](https://github.com/khulnasoft/mergemate/blob/main/docs/CUSTOM_SUGGESTIONS.md) 💎                                      |   :white_check_mark:    |   :white_check_mark:    |   :white_check_mark:        |
|       | [Test](https://github.com/khulnasoft/mergemate/blob/main/docs/TEST.md) 💎                                                                  |   :white_check_mark:    |   :white_check_mark:    |   :white_check_mark:        |
|       | Reflect and Review                                                                                                                       |   :white_check_mark:    |   :white_check_mark:    |   :white_check_mark:        |
|       | Update CHANGELOG.md                                                                                                                      |   :white_check_mark:    |   :white_check_mark:    |   :white_check_mark:        |
|       | Find Similar Issue                                                                                                                       |   :white_check_mark:    |                         |                             |
|       | [Add PR Documentation](https://github.com/khulnasoft/mergemate/blob/main/docs/ADD_DOCUMENTATION.md) 💎                                     |   :white_check_mark:    |   :white_check_mark:    |   :white_check_mark:        |
|       | [Custom Labels](https://github.com/khulnasoft/mergemate/blob/main/docs/DESCRIBE.md#handle-custom-labels-from-the-repos-labels-page-gem) 💎 |   :white_check_mark:    |   :white_check_mark:    |         |
|       | [Analyze](https://github.com/khulnasoft/mergemate/blob/main/docs/Analyze.md) 💎                                                            |   :white_check_mark:    |   :white_check_mark:    |        |
|       |                                                                                                                                          |        |        |      |
| USAGE | CLI                                                                                                                                      |   :white_check_mark:    |   :white_check_mark:    |   :white_check_mark:       |
|       | App / webhook                                                                                                                            |   :white_check_mark:    |   :white_check_mark:    |  :white_check_mark:     |
|       | Tagging bot                                                                                                                              |   :white_check_mark:    |        |           | 
|       | Actions                                                                                                                                  |   :white_check_mark:    |        |  :white_check_mark:         | 
|       |                                                                                                                                          |        |        |      |
| CORE  | PR compression                                                                                                                           |   :white_check_mark:    |   :white_check_mark:    |   :white_check_mark:       |
|       | Repo language prioritization                                                                                                             |   :white_check_mark:    |   :white_check_mark:    |   :white_check_mark:       |
|       | Adaptive and token-aware<br />file patch fitting                                                                                         |   :white_check_mark:    |   :white_check_mark:    |   :white_check_mark:     |
|       | Multiple models support                                                                                                                  |   :white_check_mark:    |   :white_check_mark:    |   :white_check_mark:       | :white_check_mark: |
|       | [Static code analysis](https://github.com/khulnasoft/mergemate/blob/main/docs/Analyze.md) 💎                                               |   :white_check_mark:    |   :white_check_mark:     |    :white_check_mark:    |
|       | [Global configuration](https://github.com/khulnasoft/mergemate/blob/main/Usage.md#global-configuration-file-) 💎                           |   :white_check_mark:    |   :white_check_mark:     |    :white_check_mark:    |
|       | [PR Actions](https://www.khulnasoft.com/images/mergemate/pr-actions.mp4) 💎                                     |   :white_check_mark:    |        |        |

- 💎 means this feature is available only in [MergeMate Pro](https://www.khulnasoft.com/pricing/)
- Support for additional git providers is described in [here](./docs/Full_environments.md)
___

‣ **Auto Description ([`/describe`](./docs/DESCRIBE.md))**: Automatically generating PR description - title, type, summary, code walkthrough and labels.
\
‣ **Auto Review ([`/review`](./docs/REVIEW.md))**: Adjustable feedback about the PR main theme, type, relevant tests, security issues, score, and various suggestions for the PR content.
\
‣ **Question Answering ([`/ask ...`](./docs/ASK.md))**: Answering free-text questions about the PR.
\
‣ **Code Suggestions ([`/improve`](./docs/IMPROVE.md))**: Committable code suggestions for improving the PR.
\
‣ **Update Changelog ([`/update_changelog`](./docs/UPDATE_CHANGELOG.md))**: Automatically updating the CHANGELOG.md file with the PR changes.
\
‣ **Find Similar Issue ([`/similar_issue`](./docs/SIMILAR_ISSUE.md))**: Automatically retrieves and presents similar issues.
\
‣ **Add Documentation 💎  ([`/add_docs`](./docs/ADD_DOCUMENTATION.md))**: Automatically adds documentation to methods/functions/classes that changed in the PR.
\
‣ **Generate Custom Labels 💎 ([`/generate_labels`](./docs/GENERATE_CUSTOM_LABELS.md))**: Automatically suggests custom labels based on the PR code changes.
\
‣ **Analyze 💎 ([`/analyze`](./docs/Analyze.md))**: Automatically analyzes the PR, and presents changes walkthrough for each component.
\
‣ **Custom Suggestions 💎 ([`/custom_suggestions`](./docs/CUSTOM_SUGGESTIONS.md))**: Automatically generates custom suggestions for improving the PR code, based on specific guidelines defined by the user.
\
‣ **Generate Tests 💎 ([`/test component_name`](./docs/TEST.md))**: Automatically generates unit tests for a selected component, based on the PR code changes.

See the [Installation Guide](./INSTALL.md) for instructions on installing and running the tool on different git platforms.

See the [Usage Guide](./Usage.md) for running the MergeMate commands via different interfaces, including _CLI_, _online usage_, or by _automatically triggering_ them when a new PR is opened.

See the [Tools Guide](./docs/TOOLS_GUIDE.md) for a detailed description of the different tools (tools are run via the commands).


## Example results
</div>
<h4><a href="https://github.com/khulnasoft/mergemate/pull/530">/describe</a></h4>
<div align="center">
<p float="center">
<img src="https://www.khulnasoft.com/images/mergemate/describe_new_short_main.png" width="800">
</p>
</div>
<hr>
<h4><a href="https://github.com/khulnasoft/mergemate/pull/472#discussion_r1435819374">/improve</a></h4>

<div align="center">
<p float="center">
<kbd>
<img src="https://www.khulnasoft.com/images/mergemate/improve_short_main.png" width="768">
</kbd>
</p>

</div>
<hr>
<h4><a href="https://github.com/khulnasoft/mergemate/pull/530">/generate_labels</a></h4>
<div align="center">
<p float="center">
<kbd><img src="https://www.khulnasoft.com/images/mergemate/geneare_custom_labels_main_short.png" width="300"></kbd>
</p>
</div>

[//]: # (<h4><a href="https://github.com/khulnasoft/mergemate/pull/78#issuecomment-1639739496">/reflect_and_review:</a></h4>)

[//]: # (<div align="center">)

[//]: # (<p float="center">)

[//]: # (<img src="https://www.khulnasoft.com/images/reflect_and_review.gif" width="800">)

[//]: # (</p>)

[//]: # (</div>)

[//]: # (<h4><a href="https://github.com/khulnasoft/mergemate/pull/229#issuecomment-1695020538">/ask:</a></h4>)

[//]: # (<div align="center">)

[//]: # (<p float="center">)

[//]: # (<img src="https://www.khulnasoft.com/images/ask-2.gif" width="800">)

[//]: # (</p>)

[//]: # (</div>)

[//]: # (<h4><a href="https://github.com/khulnasoft/mergemate/pull/229#issuecomment-1695024952">/improve:</a></h4>)

[//]: # (<div align="center">)

[//]: # (<p float="center">)

[//]: # (<img src="https://www.khulnasoft.com/images/improve-2.gif" width="800">)

[//]: # (</p>)

[//]: # (</div>)
<div align="left">


</div>
<hr>


## Try it now

Try the GPT-4 powered MergeMate instantly on _your public GitHub repository_. Just mention `@CodiumAI-Agent` and add the desired command in any PR comment. The agent will generate a response based on your command.
For example, add a comment to any pull request with the following text:
```
@CodiumAI-Agent /review
```
and the agent will respond with a review of your PR

![Review generation process](https://www.khulnasoft.com/images/demo-2.gif)


To set up your own MergeMate, see the [Installation](#installation) section below.
Note that when you set your own MergeMate or use CodiumAI hosted MergeMate, there is no need to mention `@CodiumAI-Agent ...`. Instead, directly start with the command, e.g., `/ask ...`.

---

## Installation
To use your own version of MergeMate, you first need to acquire two tokens:

1. An OpenAI key from [here](https://platform.openai.com/), with access to GPT-4.
2. A GitHub personal access token (classic) with the repo scope.

There are several ways to use MergeMate:

**Locally**
- [Use Docker image (no installation required)](./INSTALL.md#use-docker-image-no-installation-required)
- [Run from source](./INSTALL.md#run-from-source)

**GitHub specific methods**
- [Run as a GitHub Action](./INSTALL.md#run-as-a-github-action)
- [Run as a GitHub App](./INSTALL.md#run-as-a-github-app)

**GitLab specific methods**
- [Run a GitLab webhook server](./INSTALL.md#run-a-gitlab-webhook-server)

**BitBucket specific methods**
- [Run as a Bitbucket Pipeline](./INSTALL.md#run-as-a-bitbucket-pipeline)

## MergeMate Pro 💎
[MergeMate Pro](https://www.khulnasoft.com/pricing/) is a hosted version of MergeMate, provided by CodiumAI. It is available for a monthly fee, and provides the following benefits:
1. **Fully managed** - We take care of everything for you - hosting, models, regular updates, and more. Installation is as simple as signing up and adding the MergeMate app to your GitHub\BitBucket repo.
2. **Improved privacy** - No data will be stored or used to train models. MergeMate Pro will employ zero data retention, and will use an OpenAI account with zero data retention.
3. **Improved support** - MergeMate Pro users will receive priority support, and will be able to request new features and capabilities.
4. **Extra features** -In addition to the benefits listed above, MergeMate Pro will emphasize more customization, and the usage of static code analysis, in addition to LLM logic, to improve results. It has the following additional tools and features:
    - [**Analyze PR components**](https://github.com/khulnasoft/mergemate/blob/main/docs/Analyze.md)
    - [**Custom Code Suggestions**](https://github.com/khulnasoft/mergemate/blob/main/docs/CUSTOM_SUGGESTIONS.md)
    - [**Tests**](https://github.com/khulnasoft/mergemate/blob/main/docs/TEST.md)
    - [**PR documentation**](https://github.com/khulnasoft/mergemate/blob/main/docs/ADD_DOCUMENTATION.md)
    - [**SOC2 compliance check**](https://github.com/khulnasoft/mergemate/blob/main/docs/REVIEW.md#soc2-ticket-compliance-)
    - [**Custom labels**](https://github.com/khulnasoft/mergemate/blob/main/docs/DESCRIBE.md#handle-custom-labels-from-the-repos-labels-page-gem)
    - [**Global configuration**](https://github.com/khulnasoft/mergemate/blob/main/Usage.md#global-configuration-file-)



## How it works

The following diagram illustrates MergeMate tools and their flow:

![MergeMate Tools](https://khulnasoft.com/images/mergemate/diagram-v0.9.png)

Check out the [PR Compression strategy](./PR_COMPRESSION.md) page for more details on how we convert a code diff to a manageable LLM prompt

## Why use MergeMate?

A reasonable question that can be asked is: `"Why use MergeMate? What makes it stand out from existing tools?"`

Here are some advantages of MergeMate:

- We emphasize **real-life practical usage**. Each tool (review, improve, ask, ...) has a single GPT-4 call, no more. We feel that this is critical for realistic team usage - obtaining an answer quickly (~30 seconds) and affordably.
- Our [PR Compression strategy](./PR_COMPRESSION.md)  is a core ability that enables to effectively tackle both short and long PRs.
- Our JSON prompting strategy enables to have **modular, customizable tools**. For example, the '/review' tool categories can be controlled via the [configuration](mergemate/settings/configuration.toml) file. Adding additional categories is easy and accessible.
- We support **multiple git providers** (GitHub, Gitlab, Bitbucket), **multiple ways** to use the tool (CLI, GitHub Action, GitHub App, Docker, ...), and **multiple models** (GPT-4, GPT-3.5, Anthropic, Cohere, Llama2).


## Data privacy

If you host MergeMate with your OpenAI API key, it is between you and OpenAI. You can read their API data privacy policy here:
https://openai.com/enterprise-privacy

When using MergeMate Pro 💎, hosted by CodiumAI, we will not store any of your data, nor will we use it for training.
You will also benefit from an OpenAI account with zero data retention.

## Links

[![Join our Discord community](https://raw.githubusercontent.com/khulnasoft/khulnasoft-vscode-release/main/media/docs/Joincommunity.png)](https://discord.gg/kG35uSHDBc)

- Discord community: https://discord.gg/kG35uSHDBc
- CodiumAI site: https://khulnasoft.com
- Blog: https://www.khulnasoft.com/blog/
- Troubleshooting: https://www.khulnasoft.com/blog/technical-faq-and-troubleshooting/
- Support: support@khulnasoft.com
