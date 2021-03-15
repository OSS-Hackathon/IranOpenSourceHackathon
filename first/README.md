![logo](/logo/svg/logo-type-dark.svg)

_Iran Open Source Hackathon_ is an open-source hackathon (duh) with the aim of encouraging participation in open-source contribution amongst Iranian developers.
There is a [curated list of repositories][REPOS] whose maintainers volunteered to be part of the hackathon. Contribute to any of these repositories [during the hackathon][DURATION], and at the end [top contributors will be acknowledged here][TOP-CONTS] (so yes in the end its just about bragging rights).

In this readme and in [the code of conduct][COC], keywords **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **MAY**, and **OPTIONAL**, when appearing in caps lock and in bold, are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119). This is not a software spec document, but still the extra clarity helps avoiding confusion.

👉 If you are a maintainer and want to enter some of your repositories in the hackathon so our participants will contribute to them, check [this section][MAINTS].

> ⚠️⚠️ **NOTICE**
>
> This is work in progress. As long as this notice is up here, any rule, date, information, etc is subject to sudden change without
> any prior notice.
>
> If a piece of information is followed by `⚠️`, then there is a good chance we will change it in near future and current
> information is mostly a placeholder.

<br>

## How Can I Participate?

Contribute to one of [these repositories][REPOS] during the [time of the hackathon][DURATION]:

- Make a pull request, include #iosh⚠️ in its title⚠️.
- The pull request **MUST** be accepted to the repository before [the end of the hackathon][DURATION].
- Each pull request will count towards your total score (depends on how many lines of code it is ⚠️).
- At the end, top 5⚠️ contributors (highest scores ⚠️) will be acknowledged [here][TOP-CONTS]. We might update the list during the hackathon as well.

If you are unfamiliar with open-source contribution, git or github, take a look at [these resources][TUTS].

Also carefully read our [code of conduct][COC] before you start contributing. Administrative action (including bans from current hackathon
or even from all subsequent hackathons) might be taken in response to violations of the [code of conduct][COC].

<br>

### Why Should I Participate?

- You will help improve software that people like you use (apes together strong).
- You will learn a lot (like seriously, a TON).
- You will earn street-cred (which also helps with employability).

<br>

## I Am A Maintainer. Can I Add My Repos To This Hackathon?

Of course! You need to ⚠️:

1. Fork this repo
1. Create a directory in sub-directory `first/repos` with your username, i.e. `/first/repos/jafar`
1. For each repository you want to enter, make a [yaml](https://yaml.org) file inside that directory with the same name as your repository that looks like this:
   ```yaml
   name: <name of your repo>
   description: <a short description of your repo>
   repository: <address of the repository>
   owner: <name of the owner of the repository>
   languages:
     - <language 1 used in the repo>
     - <language 2 used in the repo>
     - ...
   ```
1. Make a pull request.

👉 You can see examples in the [repos](/first/repos) directory.

<br>

## Repositories

| Name | Owner | Description | Languages |
| --- | --- | --- | --- |
| [TyFON](https://github.com/loreanvictor/tyfon) | [loreanvictor](https://github.com/loreanvictor) | Typed Functions Over Network | typescript, javascript| --- | --- | --- | --- |
| [Callbag JSX](https://github.com/loreanvictor/callbag-jsx) | [loreanvictor](https://github.com/loreanvictor) | callbags + JSX: fast and tiny interactive web apps | typescript| --- | --- | --- | --- |
| [Pyeez](https://github.com/mehdy/pyeez) | [mehdy](https://github.com/mehdy) | A simple framework to create console applications (like htop). | python

> _To be completed_

<br>

## Duration

> _To be Announced_

<br>

## Top Contributors

> _To be determined_

<br>

[COC]: /CODE_OF_CONDUCT.md
[TUTS]: /TUTORIALS.md
[REPOS]: #repositories
[DURATION]: #duration
[TOP-CONTS]: #top-contributors
[MAINTS]: #i-am-a-maintainer-can-i-add-my-repos-to-this-hackathon
