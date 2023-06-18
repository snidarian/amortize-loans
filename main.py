import argparse
import logging
import traceback
import sys
logger = logging.getLogger(__name__)


def main(loan_principal: float, loan_term: int, interest_rate: float) -> int:

    # todo: calculate
    ...

    # todo: graph
    ...

    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-lp", "--loan-principal", type=float, required=True)
    parser.add_argument("-lt", "--loan-term", type=int, required=True)
    parser.add_argument("-ir", "--interest-rate", type=float, required=True)
    argv = parser.parse_args()

    exit_code = 0
    try:
        exit_code = main(**vars(argv))
    except Exception as be:
        exit_code = 1
        logger.exception(f"{traceback.format_exc()}")

    sys.exit(exit_code)
