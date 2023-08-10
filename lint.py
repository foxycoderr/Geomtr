"""
Pylint Action Configuration File

Controls how the PyLint action that automatically runs upon a commit functions. The action itself
can be found in Geomtr/.github/workflows/pylint.yml. This configuration file allows different
fail thresholds, the default is 7, but the threshold is controlled in the YML file. It is currently
set to 8.

"""

# Thanks to doedotdev for this code; you can read his article containing this code at:
# https://medium.com/analytics-vidhya/
# pylint-static-code-analysis-github-
# action-to-fail-below-a-score-threshold-58a124aafaa0


import argparse
from pylint.lint import Run

parser = argparse.ArgumentParser(prog="LINT")

parser.add_argument('-p',
                    '--path',
                    help='path to directory you want to run pylint | '
                         'Default: %(default)s | '
                         'Type: %(type)s ',
                    default='./src',
                    type=str)

parser.add_argument('-t',
                    '--threshold',
                    help='score threshold to fail pylint runner | '
                         'Default: %(default)s | '
                         'Type: %(type)s ',
                    default=7,
                    type=float)

args = parser.parse_args()
path = str(args.path)
threshold = float(args.threshold)

results = Run([path], do_exit=False)

final_score = results.linter.stats.global_note

if final_score < threshold:

    message = ('PyLint Failed | '
               'Score: {} | '
               'Threshold: {} '.format(final_score, threshold))

    logging.error(message)
    raise Exception(message)

else:
    message = ('PyLint Passed | '
               'Score: {} | '
               'Threshold: {} '.format(final_score, threshold))



    exit(0)
