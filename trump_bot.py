import ConfigParser
import tweepy
import subprocess
import os


def get_config():
    config_parser = ConfigParser.ConfigParser()
    config_path = "./config"
    config_parser.read(config_path)

    return config_parser

def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])

    return tweepy.API(auth)

def tweet(message):
    config = get_config()
    cfg = {
        'consumer_key'          : config.get('Twitter', 'consumer_key'),
        'consumer_secret'       : config.get('Twitter', 'consumer_secret'),
        'access_token'          : config.get('Twitter', 'access_token'),
        'access_token_secret'   : config.get('Twitter', 'access_token_secret')
    }

    api = get_api(cfg)
    api.update_status(status=message)

def build_status():
    status = ''

    while True:
        sentence = ''

        while '.' not in sentence:
            sentence = query_rnn(120).replace('\n', ' ')

        if len(sentence) + len(status) > 140:
            break
        else:
            status += sentence.split('.')[0] + "."

    return status

def query_rnn(num_characters):
    '''Syscall to get text from RNN'''

    command = ['th', 'sample.lua', '-checkpoint', 'cv/checkpoint_10000.t7', '-length', str(num_characters), ' -gpu', '-1']
    p = subprocess.Popen(command, cwd=os.getcwd(), stdout=subprocess.PIPE)
    output, err = p.communicate()

    return output
    #return 'Hello World!.'

def main():

    status = build_status()
    print status
    #tweet(status)

if __name__ == '__main__':
    main()