from TwitterAPI import TwitterAPI
import json

class TwitterBot:
    def __init__(self, credentials, account, stalker_account):
        self.api = TwitterAPI(credentials['api_key'], 
                    credentials['api_key_secret'],
                    credentials['access_token'],
                    credentials['access_token_secret'])
        
        self.account = account
        self.stalker_account = stalker_account
        self.stalker_account_id = self.__get_stalker_account_id()
    
    def block_followersOf_replying(self):
        stream = self.api.request('statuses/filter', { 'follow': self.account })
        for tweet in stream:
            # print(tweet)
            if self.__user_follows_stalker(tweet):
                user = tweet['user']['id']
                username = tweet['user']['screen_name']
                self.api.request('blocks/create', { 'user_id' : user })
                print(f'User @{username} blocked!')
            # if is_following_stalker():


    def __get_stalker_account_id(self):
        response = self.api.request('users/show', {'screen_name':self.stalker_account})

        if response.status_code == 200:
            return  json.loads(response.text)['id_str']
        else:
            print('PROBLEM: ' + response.text)
            exit()

    def __user_follows_stalker(self, tweet):
        if 'user' in tweet:
            user = tweet['user']['screen_name']
            relation = self.api.request('friendships/show', { 'source_screen_name': user, 'target_screen_name': self.stalker_account })

            content = json.loads(relation.response._content)

            # print(content['relationship']['target']['followed_by'])
            return content['relationship']['target']['followed_by']

        else:
            return False

    def __tweeted_by_stalked_account(self, tweet):
        return (tweet['text'][0:4] == 'RT @')
