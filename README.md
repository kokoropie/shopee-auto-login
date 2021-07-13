Documentation  | [Simple Docs](./README.simple.md)
<div align="center">
<h1 align="center">Genshin Impact Auto Login</h1>

[![CodeFactor](https://www.codefactor.io/repository/github/viole403/genshin-auto-login/badge/main)](https://www.codefactor.io/repository/github/viole403/genshin-auto-login/overview/main)
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/Viole403/genshin-auto-login/blob/main/LICENSE)
[![Docker Automated build](https://img.shields.io/docker/automated/jrottenberg/ffmpeg)](https://github.com/Viole403/genshin-auto-login/blob/main/Dockerfile)

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
</div>

## Table of contents
* [About](#about)
* [Characteristic](#characteristic)
* [Deploy](#deploy)
* [Result](#result)
* [Notification](#notification)
* [Parameter](#parameter)
* [Development](#development)
* [User ️Agreement](#user-agreement)

## 💭About

Genshin Impact is the only game I have seen where the game itself is separated from the check-in benefits. Players need to download the MiHoYo App to check-in.

In fact, you can choose to ignore the sign-in, and there is no big loss if you don't sign in; or you can choose to sign-in manually, but in this case, it will be a headache to forget to check in.
##  💡Characteristic

- [x] **Automatic sign-in**  The program will automatically execute the sign-in process every morning, or you can go through the deployment tutorial at any time`Step 4`Manual trigger, refer to specific time [Here](.github/workflows/main-os.yml)
- [x] **Support synchronization**  Automatic synchronization of upstream warehouses, closed by default
- [x] **Support notification**   Multiple notification methods can be selected, which can be turned on by configuring different parameters, and the check-in results will be pushed to subscribers every day
- [x] **Support multiple accounts**  Different accounts`Cookie`Use between values`#`Separated, such as:`Cookie1#Cookie2#Cookie3`
- [x] **Supports multiple roles**  Supports MiHoYo accounts that bind official service and channel service roles

## 📐Deploy

- Fork Project
- Get Cookie
- Add Cookie to Secrets
- Enable Actions
- Multiple Accounts

<details>
<summary>View tutorial</summary>

### 1. Fork Project

- Click on the upper right corner `Fork` to go to your account

![fork](https://i.loli.net/2020/10/28/qpXowZmIWeEUyrJ.png)

### 2. Get Cookie

Open [Here](https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481) in the browser and log in to the account
#### 2.1 Method 1

- Press `F12`，open `Developer tools`，find`Network` and click
- Press `F5` refresh the page, copy as shown in the figure below`Cookie`

![cookie](https://i.loli.net/2021/04/28/8u5oJIDh9szaMlk.jpg)

-  When triggered `Debugger`, you can try to press `Ctrl + F8` close, then refresh the page again, and finally copy `Cookie`

#### 2.2 Method 2

- Copy the following code

```
var cookie = document.cookie;
var ask = confirm('Cookie: ' + cookie + '\n\nWant copy your Cookie to clipboard？');
if (ask == true) {
    copy(cookie);
    msg = cookie;
} else {
    msg = 'Cancel';
}
```

- Press `F12`, open `Developer tools`, find `Console` and click
- Paste the code on the command line and run it to get similar `Cookie:xxxxxx` output information
- `xxxxxx` The part is what needs to be copied Cookie, click OK to copy

### 3. Add Cookie to Secrets

- Back to your repository page, Click `Settings`-->`Secrets`-->`New secret`.

![new-secret.png](https://i.loli.net/2020/10/28/sxTuBFtRvzSgUaA.png)

- Add a new secret named `OS_COOKIE` and the value is what you obtained in the previous step. Warning: THE NAME MUST BE `OS_COOKIE`
- Account_id, Cookie_token, Ltoken are required fields in the secret

![add-secret](https://i.imgur.com/187niY1.png)
![add-secret](https://i.imgur.com/5rZwtK6.png)

- Select `Genshin Impact Auto Login Global` on the Actions page.
- Click the `Run workflow` button.
- When the build is complete, click the `Genshin Impact Auto Login Global`-->`build`-->`Run sign` to view logs.
### 4. Enable Actions

> Actions are disabled by default. After the Fork, it needs to be executed manually, and it will be activated if it runs successfully.

Return to the main page of the project, click on the top `Actions`, then click on the left `Genshin Impact Auto Login`, and then click `Run workflow`

![run](https://i.loli.net/2020/10/28/5ylvgdYf9BDMqAH.png)

At this point, the deployment is complete.But if you have more than 1 account, then continue with the next step

## 5. Multiple Accounts

- Multiple account cookies need to be separated by "#" symbol

![multiple-accounts](https://i.imgur.com/MFXsKbC.png)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FViole403%2Fgenshin-auto-login.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FViole403%2Fgenshin-auto-login?ref=badge_shield)


</details>

## 🔍Result

When you complete the above process，Allowable `Actions` Page click `Genshin Impact Auto Login`-->`build`-->`Run sign`Check the running log, pay attention`Check-in result`Tips.
<details>
<summary>View result</summary>

### Sign in successfully

If successful, a similar check-in result: `Success: 2 | Failure: 0` message will be output:

```
Check-in result: Success: 2 | Failure: 0

No.1 account:
    #########2021-01-13#########
    🔅[YourUID]
    Today's reward: Mora × 8000
    Sign this month: 13 days
    Check-in result: OK
    ###########################
No.2 account:
    #########2021-01-13########
    🔅[YourUID]
    Today's Reward: Good Ore for Fine Forging × 3
    Sign this month: 2 days
    Check-in result: 👀 Traveler, you've already checked in today
    ###########################
```

### Sign in failed

If it fails, a similar check-in result: `Success: 0 | Failure: 1` message will be output:
```
Check-in result: Success: 0 | Failure: 1

    No.1 account:
        Login invalid, please log in again
```

At the same time, you will receive an email from GitHub with the title `Run failed: Genshin Impact Auto Login - master`.

</details>

## 🔔Notification

If you turn on Notification push, you will receive push notifications regardless of success or failure.

Support Telegram Bot, Discord Webhook and custom push single or multiple pushes, configure the corresponding parameters to open the corresponding push method , The parameter list is detailed in the `parameters` section below.
#### Custom push

Create a secret named `PUSH_CONFIG`, and fill in the following json template according to the custom push document you use
<details>
<summary>View data</summary>

```json
{
     "method": "post",
     "url": "",
     "data": {},
     "text": "",
     "code": 200,
     "data_type": "data",
     "show_title_and_desp": false,
     "set_data_title": "",
     "set_data_sub_title": "",
     "set_data_desp": ""
}
```
```
Description:
    method: required, request method. Default: post.
    url: required, complete custom push link.
    data: Optional, sent data. The default is empty, you can add additional parameters.
    text: required, the key of the status code returned by the response body. For example: the server sauce is errno.
    code: Required, the value of the status code returned by the response body. For example, the value of the server sauce is 0.
    data_type: Optional, the method of sending data, optional params|json|data, default: data.
    show_title_and_desp: Optional, whether to merge the title (application name + running status) with the running result. Default: false.
    set_data_title: Required, fill in the key of the message title in the push method data. For example: server sauce is text.
    set_data_sub_title: Optional, fill in the key of the message body in the push method data. Some push methods have a secondary structure in the body key, and need to cooperate with set_data_title to construct a child, which is mutually exclusive with set_data_desp. For example: In enterprise WeChat, set_data_title fills in text, set_data_sub_title Fill in content.
    set_data_desp: Optional, fill in the key of the message body in the push method data. For example, the server sauce is desp. It is mutually exclusive with set_data_sub_title. If both are filled, this item will not take effect.
```

For other push methods, please refer to the corresponding official documents to obtain parameters such as KEY or TOKEN, and then add them to `Secrets`
</details>

## 🧬Parameter

For parameters added in `Settings`-->`Secrets`, `Name` must be one of the following parameter names, and `Value` fills in the corresponding obtained value

|   Parameter name         |   Required   |   Defaults           |   Description                                                          |
|---                |---          |---                 |---                                                              |
|   COOKIE          | ❌         |                    |   Yuanshen (CN Only) COOKIE                                                 |
|   OS_COOKIE       | ✅         |                    |   HoYoLAB COOKIE                                                 |
|   TG_BOT_API      | ❌         | api.telegram.org   |   Telegram API address (can be customized as a reverse proxy server)                       |
|   TG_BOT_TOKEN    | ❌         |                    |   Telegram Bot token. Generated when applying for bot from bot father                    |
|   TG_USER_ID      | ❌         |                    |   The user ID of the Telegram push object                                         |
|   PUSH_CONFIG     | ❌         |                    |   Custom push configuration in JSON format. For details, please refer to the description of Subscription-Custom Push                |
|   CRON_SIGNIN     | ❌         | 30 9 * * *         |   Automatic check-in scheduled task of DOCKER script                                        |

## ⛏️Development

If you need to refactor or add additional functions, please refer to the following data:
<details>
<summary>View data</summary>

```python
# Role information
roles = Roles(cookie).get_roles()
roles = {
    'retcode': 0,
    'message': 'OK',
    'data': {
        'list': [
            {
                'game_biz': 'hk4e_global',
                'region': 'cn_gf01',
                'game_uid': '111111111',
                'nickname': 'Paimon',
                'level': 48,
                'is_chosen': False,
                'region_name': 'Sky island',
                'is_official': True
            }
        ]
    }
}
```
```python
# Sign-in information
infos = Sign(cookie).get_info()
infos = [
    {
        'retcode': 0,
        'message': 'OK',
        'data': {
            'total_sign_day': 5,
            'today': '2021-01-05',
            'is_sign': True,
            'first_bind': False,
            'is_sub': False,
            'month_first': False
        }
    }
]
```

</details>

## :warning:User ️Agreement

Using Genshin Impact Auto Login means that you know and agree to:

- This code uses cookies to log in to the Miyoushe webpage through a simulated browser, and click the page to complete the sign-in to realize the sign-in. The function is implemented through the official public API, not a game plug-in
- The user's cookie is stored on the Github server and is only used for this project. If the Github server is compromised, your cookies are at risk of being leaked. In addition, the developer has no right to obtain your cookie; even the user, once created Secrets, cannot view the cookie from it again
- Genshin Impact Auto Login will not be responsible for any of your losses, including but not limited to reward recovery, abnormal account, cutting off, mining of minerals, nuclear bomb explosion, World War III, etc.

## ✨Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FViole403%2Fgenshin-auto-login.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FViole403%2Fgenshin-auto-login?ref=badge_large)