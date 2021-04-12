![logo](/design/logo/svg/logo-type-dark.svg)

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

Of course! You need to:

1. Fork this repository.
1. For each repository like `https://github.com/jafar/my-repo`, add a [yaml](https://en.wikipedia.org/wiki/YAML) file to `first/repos` \
  (i.e. `first/repos/jafar/my-repo.yaml`):
  ```yaml
  # first/repos/jafar/my-repo.yaml
  
  name: My Cool Repository
  description: I am particularly cool here
  languages:
    - JavaScript
    - Hashemi
    - ...
  ```
1. Make a pull request.

👉 You can see examples in the [repos](/first/repos) directory.

👉 You can add a list of maintainers (with whom hackathon participants can be in contact) as well:
```yaml
# first/repos/jafar/my-repo.yaml

name: My Cool Repository
description: I am particularly cool here
languages:
  - JavaScript
  - Hashemi
#
# 👉 for user `https://github.com/asghar`, add `asghar` to this list
# 👉 also don't forget the repo owner if they are going to be a maintainer as well
#
maintainers:
  - jafar
  - asghar
  - nooshin
  - maliheh
```

👉 If your repo belongs to a company, you **MUST** specify maintainers independently.

<br>

## Repositories

<!-- Repos Table -->
 | Name | Description | Owner | Maintainer(s) | Languages | 
 | --- | --- | --- | --- | --- | 
 | [TyFON](https://github.com/loreanvictor/tyfon) | Typed Functions Over Network | [loreanvictor](https://github.com/loreanvictor) | [loreanvictor](https://github.com/loreanvictor) | typescript, javascript | 
 | [Callbag JSX](https://github.com/loreanvictor/callbag-jsx) | callbags + JSX: fast and tiny interactive web apps | [loreanvictor](https://github.com/loreanvictor) | [loreanvictor](https://github.com/loreanvictor) | typescript | 
 | [Anbar](https://github.com/mehdy/anbar) | A basic S3 compatible storage server in Rust. | [mehdy](https://github.com/mehdy) | [mehdy](https://github.com/mehdy) | rust | 
 | [Pyeez](https://github.com/mehdy/pyeez) | A simple framework to create console applications (like htop). | [mehdy](https://github.com/mehdy) | [mehdy](https://github.com/mehdy) | python | 
 | [Keepalived Exporter](https://github.com/cafebazaar/keepalived-exporter) | Prometheus exporter for Keepalived metrics. | [cafebazaar](https://github.com/cafebazaar) | [mehdy](https://github.com/mehdy) | go | 
 | [text-to-commit-history](https://github.com/erfaniaa/text-to-commit-history) | Write a large text on your Github profile, with your commits history (contribution graph). | [erfaniaa](https://github.com/erfaniaa) | [erfaniaa](https://github.com/erfaniaa) | Python | 
 | [thatcher-effect-dataset-generator](https://github.com/erfaniaa/thatcher-effect-dataset-generator) | Using OpenCV to apply Thatcher effect on a set of face images | [erfaniaa](https://github.com/erfaniaa) | [erfaniaa](https://github.com/erfaniaa) | Python | 
 | [gRPC Go Contracts](https://github.com/shayanh/grpc-go-contracts) | Verify the communication of your microservices by writing contracts for your RPCs | [shayanh](https://github.com/shayanh) | [shayanh](https://github.com/shayanh) | go | 
<!-- /Repos Table -->

> _To be completed_

<br>

## Duration

Beginning | تیر ۱۵        | 06 July
----------|:-------------------|:-------------------
Ending    | شهریور ۱۵  | 06 September 

۱۴۰۰ / 2021

<br>

### 👉 For Participants

Your pull requests **MUST** be submitted after beginning of the hackathon period and be merged before the end of the hackathon.

<br>

### 👉 For Maintainers

Ideally, submit your repositories before the start of the hackathon, though you can (⚠️) submit it during the duration of the hackathon as well.

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
