[Documentation](./README.md)  | Simple Docs
<div align="center">
<h1 align="center">Genshin Impact Auto Login</h1>

[![CodeFactor](https://www.codefactor.io/repository/github/viole403/genshin-auto-login/badge/main)](https://www.codefactor.io/repository/github/viole403/genshin-auto-login/overview/main)
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/Viole403/genshin-auto-login/blob/main/LICENSE)
[![Docker Automated build](https://img.shields.io/docker/automated/jrottenberg/ffmpeg)](https://github.com/Viole403/genshin-auto-login/blob/main/Dockerfile)

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
</div>

## Table of contents
* [About](#about)
* [Deploy](#deploy)
* [User ️Agreement](#user-agreement)

## 💭About

Genshin Impact is the only game I have seen where the game itself is separated from the check-in benefits. Players need to download the MiHoYo App to check-in.

In fact, you can choose to ignore the sign-in, and there is no big loss if you don't sign in; or you can choose to sign-in manually, but in this case, it will be a headache to forget to check in.

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


</details>


## :warning:User ️Agreement

Using Genshin Impact Auto Login means that you know and agree to:

- This code uses cookies to log in to the Miyoushe webpage through a simulated browser, and click the page to complete the sign-in to realize the sign-in. The function is implemented through the official public API, not a game plug-in
- The user's cookie is stored on the Github server and is only used for this project. If the Github server is compromised, your cookies are at risk of being leaked. In addition, the developer has no right to obtain your cookie; even the user, once created Secrets, cannot view the cookie from it again
- Genshin Impact Auto Login will not be responsible for any of your losses, including but not limited to reward recovery, abnormal account, cutting off, mining of minerals, nuclear bomb explosion, World War III, etc.
