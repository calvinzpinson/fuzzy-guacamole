import optparse
import csv


def main():
    ''' Takes a csv of tweets downloaded from the
        political twitter archive https://github.com/bpb27/political_twitter_archive
        and converts the tweet text into a text file for later training with an RNN
    '''
    parser = optparse.OptionParser('usage %prog ' + \
        '-i <tweet csv> -d <destination file>')

    parser.add_option('-d', dest='destFile', type='string', \
        help='specify destination file')
    parser.add_option('-i', dest='inputFile', type='string', \
        help='specify the input csv')

    (options, args) = parser.parse_args()
    dest_file = options.destFile
    csv_file = options.inputFile

    if dest_file is None or csv_file is None:
        print parser.usage
        exit(0)

    tweets = []
    with open(csv_file) as tweet_csv:
        tweet_reader = csv.DictReader(tweet_csv)
        for row in tweet_reader:
            tweets.append(row['text'])

    with open(dest_file, 'w') as txt_file:
        for tweet in tweets:
            txt_file.write(tweet)
            txt_file.write('\n\n')

if __name__ == '__main__':
    main()
