from dotenv import load_dotenv
import argparse
from datetime import date
from clip_stitch import ClipStitch

load_dotenv()


def main():
    parser = argparse.ArgumentParser(description="Download clips from Twitch and stitch them together.")
    parser.add_argument("-username", help="Username of the Twitch account.  [REQUIRED]", type=str)
    parser.add_argument("-begin", help="The start of the date range for clips. MM/dd/YYYY  [REQUIRED]", type=str)
    parser.add_argument("-end", help="The end of the date range for clips, defaults to today.", type=str)
    parser.add_argument("-limit", help="The maximum number of clips to recieve", type=int)
    parser.add_argument("-popular", help="Get the most popular clips in the specified date window. DEFAULT=True",
                        type=bool, default=True)

    current_date = date.today()

    args = parser.parse_args()

    if args.username is None:
        print("Error no twitch username provided.\n")
        exit(1)

    if args.begin is None:
        begin_month = current_date.strftime('%m')
        begin_day = current_date.strftime('%d')
        begin_year = current_date.year
    else:
        start_split = args.begin.split("/")
        begin_month = start_split[0]
        begin_day = start_split[1]
        begin_year = start_split[2]

    if args.end is None:
        end_month = current_date.strftime('%m')
        end_day = current_date.strftime('%d')
        end_year = current_date.year
    else:
        end_split = args.begin.split("/")
        end_month = end_split[0]
        end_day = end_split[1]
        end_year = end_split[2]

    if args.limit is None:
        clip_limit = 5
    else:
        clip_limit = args.limit

    app = ClipStitch()
    app.run(args.username, clip_limit, begin_year, begin_month, begin_day, end_year, end_month, end_day)


if __name__ == "__main__":
    main()
