import logging


def main():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename='runner_tests.log',
        filemode='w',
        encoding='utf-8'
    )

    logger.debug('Logging debug!')
    logger.info('Logging info!')
    logger.warning('Logging warning!')
    logger.error('Logging error!')
    logger.critical('Logging critical!')
    logger.exception('Logging exception!')


if __name__ == '__main__':
    main()
