![logo](/design/logo/svg/logo-type-dark.svg)

[![Join the chat at https://gitter.im/Iran-Open-Source-Hackathon/community](https://badges.gitter.im/Iran-Open-Source-Hackathon/community.svg)](https://gitter.im/Iran-Open-Source-Hackathon/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

_Iran Open Source Hackathon_ is an open-source hackathon (duh) with the aim of encouraging participation in open-source contribution amongst Iranian developers.
There is a [curated list of repositories][REPOS] whose maintainers volunteered to be part of the hackathon. Contribute to any of these repositories [during the hackathon][DURATION], and at the end [top contributors will be acknowledged here][TOP-CONTS] (so yes in the end its just about bragging rights).

👉 If you are a maintainer and want to enter some of your repositories in the hackathon so our participants will contribute to them, check [this section][MAINTS].

<br>

<details>

<summary>A Note on Terminology</summary>

<br>

> In these documents, keywords **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**,
> **RECOMMENDED**, **MAY**, and **OPTIONAL**, when appearing in caps lock and in bold, are to be interpreted as described in
> [RFC 2119](https://tools.ietf.org/html/rfc2119). This is not a software spec document, but still the extra clarity helps avoiding confusion.

<br>

</details>

<details>
  
<summary>
⚠️⚠️ WORK IN PROGRESS NOTICE
</summary>

<br>

> This is work in progress. As long as this notice is up here, any rule, date, information, etc is subject to sudden change without
> any prior notice.
>
> If a piece of information is followed by `⚠️`, then there is a good chance we will change it in near future and current
> information is mostly a placeholder.

<br>

</details>

<br>

## How Can I Participate?

Contribute to one of [these repositories][REPOS] during the [time of the hackathon][DURATION]:

- Make a pull request, include #iosh⚠️ in its title⚠️.
- The pull request **MUST** be accepted to the repository before [the end of the hackathon][DURATION].
- Each pull request will count towards your total score (depends on how many lines of code it is ⚠️).
- At the end, top 5⚠️ contributors (highest scores ⚠️) will be acknowledged [here][TOP-CONTS]. We might update the list during the hackathon as well.

👉 If you are unfamiliar with open-source contribution, git or github, take a look at [these resources][TUTS]. You could also join us at [gitter](https://gitter.im/Iran-Open-Source-Hackathon/community) to seek help and pointers.

**NOTE**: Please carefully read our [code of conduct][COC] before you start contributing.

<br>

### Why Should I Participate?

- You will help improve software that people like you use (apes together strong).
- You will learn a lot (like seriously, a TON).
- You will earn street-cred (which also helps with employability).

<br>

## I Am A Maintainer. Can I Add My Repos To This Hackathon?

Of course! You need to:

1. Fork this repository.
2. For each repository like `https://github.com/jafar/my-repo`, add a [yaml](https://en.wikipedia.org/wiki/YAML) file to `first/repos` \
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

3. Make a pull request.

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

👉 If your repo belongs to a company or organization, you **MUST** specify maintainers independently.

**NOTE**: Please carefully read our [code of conduct][COC] before you submit your repositories.

<br>

## Repositories

<!-- Repos Table -->
 | Name | Description | Owner | Maintainer(s) | Languages |
 | --- | --- | --- | --- | --- |
 | [BarnameKon](https://github.com/anvaari/BarnameKon) | Telegram bot which create "Add to Google Calendar" link for your events. | [anvaari](https://github.com/anvaari) | [anvaari](https://github.com/anvaari) | python |
 | [text-style-editor](https://github.com/mehdizarepour/text-style-editor) | Text style editor widget for flutter. | [mehdizarepour](https://github.com/mehdizarepour) | [mehdizarepour](https://github.com/mehdizarepour) | Dart |
 | [flutter-global-configs](https://github.com/mehdizarepour/flutter-global-configs) | A flutter package to manage application configurations via singleton pattern. | [mehdizarepour](https://github.com/mehdizarepour) | [mehdizarepour](https://github.com/mehdizarepour) | Dart |
 | [gato](https://github.com/mehdizarepour/gato) | A dart utility library inspired by javascript lodash library. | [mehdizarepour](https://github.com/mehdizarepour) | [mehdizarepour](https://github.com/mehdizarepour) | Dart |
 | [instagram-text-editor](https://github.com/mehdizarepour/instagram-text-editor) | An Instagram like text editor Flutter widget that helps you to change your text style. | [mehdizarepour](https://github.com/mehdizarepour) | [mehdizarepour](https://github.com/mehdizarepour) | Dart |
 | [paperify](https://github.com/alisinabh/paperify) | Backup files on paper using QRCodes. | [alisinabh](https://github.com/alisinabh) | [alisinabh](https://github.com/alisinabh) | shell |
 | [Microsoft Windows 7 Preview on Web](https://github.com/nainemom/win7) | Yet another OS preview via web technologies focused on Microsoft Windows 7. | [nainemom](https://github.com/nainemom) | [nainemom](https://github.com/nainemom) | javascript |
 | [Laravel Toman](https://github.com/evryn/laravel-toman) | Elegant Zarinpal and IDPay payment gateways for Laravel | [evryn](https://github.com/evryn) | [AmirrezaNasiri](https://github.com/AmirrezaNasiri) | PHP |
 | [Keepalived Exporter](https://github.com/cafebazaar/keepalived-exporter) | Prometheus exporter for Keepalived metrics. | [cafebazaar](https://github.com/cafebazaar) | [mehdy](https://github.com/mehdy) | go |
 | [gRPC Go Contracts](https://github.com/shayanh/grpc-go-contracts) | Verify the communication of your microservices by writing contracts for your RPCs | [shayanh](https://github.com/shayanh) | [shayanh](https://github.com/shayanh) | go |
 | [Iconbox](https://github.com/iconsbox/icons) | A world of famous icon packs with easy to use interface | [iconsbox](https://github.com/iconsbox) | [sayjeyhi](https://github.com/sayjeyhi) | javascript, typescript |
 | [gogit](https://github.com/ajangi/gogit) | A simple Github Toolkit written in Golang | [ajangi](https://github.com/ajangi) | [ajangi](https://github.com/ajangi) | golang |
 | [PHP Rest Response](https://github.com/ajangi/php-rest-response) | A PHP standard response structure to unify responses between microservices. | [ajangi](https://github.com/ajangi) | [ajangi](https://github.com/ajangi) | php |
 | [Laravel Crypt Model](https://github.com/ajangi/laravel-crypt-model) | Encoding and Decoding laravel model attributes made easy. | [ajangi](https://github.com/ajangi) | [ajangi](https://github.com/ajangi) | php |
 | [React.js persian interview questions](https://github.com/Mariotek/reactjs-persian-interview-questions) | A book with more than 300 react.js questions | [Mariotek](https://github.com/Mariotek) | [sayjeyhi](https://github.com/sayjeyhi) | javascript, markdown |
 | [Javascript persian interview questions](https://github.com/Mariotek/javascript-persian-interview-questions) | A book with more than 1000 js questions | [Mariotek](https://github.com/Mariotek) | [sayjeyhi](https://github.com/sayjeyhi) | javascript, markdown |
 | [Peanar](https://github.com/martianboy/peanar) | A background job scheduler for Node.js based on RabbitMQ | [martianboy](https://github.com/martianboy) | [martianboy](https://github.com/martianboy) | typescript |
 | [Zarb project](https://github.com/zarbchain/zarb-go) | Zarb blockchain | [zarbchain](https://github.com/zarbchain) | [b00f](https://github.com/b00f) | Go, Rust, Javascript |
 | [divar-starter-kit](https://github.com/divar-ir/divar-starter-kit) | React.js SSR-ready boilerplate using Razzle. | [divar-ir](https://github.com/divar-ir) | [iMohammadReza](https://github.com/iMohammadReza) | javascript |
 | [thatcher-effect-dataset-generator](https://github.com/erfaniaa/thatcher-effect-dataset-generator) | Using OpenCV to apply Thatcher effect on a set of face images | [erfaniaa](https://github.com/erfaniaa) | [erfaniaa](https://github.com/erfaniaa) | Python |
 | [text-to-commit-history](https://github.com/erfaniaa/text-to-commit-history) | Write a large text on your Github profile, with your commits history (contribution graph). | [erfaniaa](https://github.com/erfaniaa) | [erfaniaa](https://github.com/erfaniaa) | Python |
 | [Lightweight Message Queue (LMQ)](https://github.com/justmisam/lmq) | A lightweight message queue to work with short messages or content references as messages. | [justmisam](https://github.com/justmisam) | [justmisam](https://github.com/justmisam) | Go |
 | [PyLMQ](https://github.com/justmisam/PyLMQ) | Python Library for LMQ | [justmisam](https://github.com/justmisam) | [justmisam](https://github.com/justmisam) | Python |
 | [Letiner](https://github.com/justmisam/leitner) | An intelligent Leitner to memorize information, especially words, without needing to maintain boxes manually. It can be synced with Dropbox. | [justmisam](https://github.com/justmisam) | [justmisam](https://github.com/justmisam) | Javascript, HTML, CSS |
 | [TyFON](https://github.com/loreanvictor/tyfon) | Typed Functions Over Network | [loreanvictor](https://github.com/loreanvictor) | [loreanvictor](https://github.com/loreanvictor) | typescript, javascript |
 | [Callbag JSX](https://github.com/loreanvictor/callbag-jsx) | callbags + JSX: fast and tiny interactive web apps | [loreanvictor](https://github.com/loreanvictor) | [loreanvictor](https://github.com/loreanvictor) | typescript |
 | [FL Chart](https://github.com/imaNNeoFighT/fl_chart) | A powerful Flutter chart library, currently supporting Line Chart, Bar Chart, Pie Chart, Scatter Chart and Radar Chart. | [imaNNeoFighT](https://github.com/imaNNeoFighT) | [imaNNeoFighT](https://github.com/imaNNeoFighT) | dart |
 | [Anbar](https://github.com/mehdy/anbar) | A basic S3 compatible storage server in Rust. | [mehdy](https://github.com/mehdy) | [mehdy](https://github.com/mehdy) | rust |
 | [Pyeez](https://github.com/mehdy/pyeez) | A simple framework to create console applications (like htop). | [mehdy](https://github.com/mehdy) | [mehdy](https://github.com/mehdy) | python |
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

<!-- CONTRIBUTORS_STATS TABLE -->
 | Contributor | Total PRs | Repos |
 | --- | --- | --- |

<!-- /CONTRIBUTORS_STATS TABLE -->

<br>

## Top Repos

> _To be determined_

<!-- REPOS_STATS TABLE -->
 | Repo | Total PRs | Contributors |
 | --- | --- | --- |

<!-- /REPOS_STATS TABLE -->

<br>

[COC]: /CODE_OF_CONDUCT.md
[TUTS]: /TUTORIALS.md
[REPOS]: #repositories
[DURATION]: #duration
[TOP-CONTS]: #top-contributors
[MAINTS]: #i-am-a-maintainer-can-i-add-my-repos-to-this-hackathon
