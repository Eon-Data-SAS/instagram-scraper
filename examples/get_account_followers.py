from context import Instagram # pylint: disable=no-name-in-module
from time import sleep

instagram = Instagram()
instagram.with_credentials('username', 'password', 'sessions')
instagram.login(force=False,two_step_verificator=True)

sleep(2) # Delay to mimic user

username = 'kevin'
followers = []
account = instagram.get_account(username)
sleep(1)

for follower in instagram.get_followers(account.identifier, 150, 100, delayed=True):
    print(follower)
