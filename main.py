import time
import logging
import parsing


def main():
    start_time = time.time()
    try:
        parsing_off_or_on = int(input('Enter "on" = 1 or "off" = 0 for parsing: '))
        format = ('%(asctime)s - [%(levelname)s] - %(message)s')
        logging.basicConfig(level=logging.INFO, format=format, filename="hbr.log")
        if parsing_off_or_on == 1:
            print('!!! [+++] Start parsing !!!')
            parsing.download_html()
        parsing.save_json()
        finish_time = time.time() - start_time
        print(finish_time)
        print('!!! [+++] Parsing complete !!!')
    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    main()
