# Buildbot Matrix Plugin
[![PyPI version](https://badge.fury.io/py/buildbot-matrix.svg)](https://badge.fury.io/py/buildbot-matrix)

This Plugin for buildbot adds a reporter which sends notifications to a specified matrix room.

Inspired by [buildbot-gitea](https://github.com/lab132/buildbot-gitea) by lab132.

# Installation
```
pip install buildbot_matrix
```

This installs itself into buildbot, no extra imports required.

# Setup

## Matrix Bot
* Create a new Matrix user which will be used to send notifications.
* Set a meaningful display name for the user. For Example `Buildbot Notifications`
* Get an access token for this user.
* Add the user to the room you want the notifications to be in.

## Buildbot
* Add this to the buildbot configuration:

```py

c['services'] = [
	reporters.MatrixStatusPush(
		'https://homeserver.example.com',
		'ROOM_ID:example.com',
		'BOT_ACCESS_TOKEN',
		verbose=True
	)
]
```

* Change the URL of the homeserver to the homeserver you want to use.
* Replace `BOT_ACCESS_TOKEN` with the acces token of the matrix user, this can be a buildbot secret.
* Replace `ROOM_ID` with the id of the matrix room the bot should send the notifications to. Replace the `!` at the beginning with `%21`. 

# Personalizing

You can modify the notifications by changing the following parameters:

| Parameter | Description | Default |
| --- | --- | --- |
| `startDescription` | Short description when a build started | `Build started.` |
| `endDescription` | Short description when a build ended | `Build done.` |
| `context` | Identifier to give messages a context | `Interpolate('buildbot/%(prop:buildername)s')` |
| `context_pr` | Identifier to give messages a context, used on pull requests | `Interpolate('buildbot/pull_request/%(prop:buildername)s')` |
| `warningAsSuccess` | Treat warnings as build success | `False` |
| `onlyEndState` | Only send a message if a build has ended | `False` |
