# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.

import argparse
import utils

argp = argparse.ArgumentParser()
argp.add_argument('--eval_corpus_path',
                  help="Path of the corpus to evaluate on", default=None)
args = argp.parse_args()

assert args.eval_corpus_path is not None

length = len([l for l  in open(args.eval_corpus_path, encoding='utf8')])
predections = ['London']*length
total, correct = utils.evaluate_places(args.eval_corpus_path, predections)
print('Correct: {} out of {}: {}%'.format(correct, total, correct/total*100))